#!/usr/bin/env python3
"""
_build/sync_prices.py
Leest de actuele prijslijsten uit Dropbox en werkt api/_projects.json bij.
Draait automatisch via GitHub Actions, of handmatig:

  DROPBOX_TOKEN=xxx python3 _build/sync_prices.py
  DROPBOX_TOKEN=xxx python3 _build/sync_prices.py --dry-run

Vereisten:
  pip install dropbox pdfplumber

GitHub Actions secret: DROPBOX_TOKEN
  → maak een Dropbox App-token aan op https://www.dropbox.com/developers/apps
    met scopes: files.metadata.read, files.content.read
"""

import os
import re
import sys
import json
import tempfile
import unicodedata
from pathlib import Path

try:
    import dropbox
    from dropbox.exceptions import ApiError
    from dropbox.files import FolderMetadata, FileMetadata
except ImportError:
    sys.exit("pip install dropbox")

try:
    import pdfplumber
except ImportError:
    sys.exit("pip install pdfplumber")

# ── configuratie ────────────────────────────────────────────────────────────

DROPBOX_TOKEN = os.environ.get("DROPBOX_TOKEN", "")
DRY_RUN = "--dry-run" in sys.argv

ROOT = Path(__file__).parent.parent
PROJECTS_JSON = ROOT / "api" / "_projects.json"

# Regio-mappen in Dropbox (bewaar de exacte display-paden)
REGION_PATHS = [
    "/Gunther De Vleeschouwer/IIS Projects/01 Costa del Sol",
    "/Gunther De Vleeschouwer/IIS Projects/02 Costa Blanca",
    "/Gunther De Vleeschouwer/IIS Projects/03 Costa Almeria",
    "/Gunther De Vleeschouwer/IIS Projects/04 Mallorca",
]

# Mapnamen die we overslaan (geen projectmappen)
SKIP_FOLDERS = {
    "00 admin", "01 existing property", "02 verhuur",
    "collaboration", "kycprev", "kyc", "0) reservation",
    "1) pbc", "s4lesagents",
}

# ── hulpfuncties ─────────────────────────────────────────────────────────────

def normalize(name: str) -> str:
    """Verwijder accenten, lowercase, spaties → koppeltekens."""
    nfkd = unicodedata.normalize("NFKD", name)
    ascii_str = nfkd.encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_str.lower()).strip("-")


def extract_lowest_price(text: str) -> int | None:
    """
    Extraheer de laagste beschikbare prijs uit de PDF-tekst.
    Regels met RESERVADO of Sold worden overgeslagen.
    Zoekt naar patronen als '500.000 €' of '€ 500.000'.
    """
    PRICE_RE = re.compile(r"(\d{1,3}(?:[.,]\d{3})+)\s*€")
    prices = []
    for line in text.splitlines():
        upper = line.upper()
        if "RESERVADO" in upper or "SOLD" in upper or "VENDIDO" in upper:
            continue
        for match in PRICE_RE.finditer(line):
            raw = match.group(1).replace(".", "").replace(",", "")
            num = int(raw)
            if 50_000 < num < 50_000_000:
                prices.append(num)
    return min(prices) if prices else None


def find_pricelist_pdf(dbx: dropbox.Dropbox, project_path: str) -> str | None:
    """
    Zoek de actuele prijslijst PDF in een projectmap.
    Kijkt in: Prices/, Pricelist/, Prijslijst/ (niet in dated/-submappen).
    Geeft het path_display terug van de meest recente PDF.
    """
    candidate_folders = ["Prices", "Pricelist", "Prijslijst", "Price list"]
    for folder_name in candidate_folders:
        folder_path = f"{project_path}/{folder_name}"
        try:
            result = dbx.files_list_folder(folder_path)
        except ApiError:
            continue
        pdfs: list[tuple[str, str]] = []
        for entry in result.entries:
            if isinstance(entry, FileMetadata) and entry.name.lower().endswith(".pdf"):
                if "dated" not in entry.path_lower:
                    pdfs.append((entry.server_modified, entry.path_display))
        if pdfs:
            pdfs.sort(reverse=True)
            return pdfs[0][1]
    return None


def pdf_to_text(dbx: dropbox.Dropbox, path: str) -> str | None:
    """Download PDF van Dropbox en extraheer tekst met pdfplumber."""
    try:
        _, response = dbx.files_download(path)
    except ApiError as e:
        print(f"    ⚠ Download mislukt: {e}")
        return None
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(response.content)
        tmp_path = tmp.name
    try:
        text_parts = []
        with pdfplumber.open(tmp_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text_parts.append(t)
        return "\n".join(text_parts)
    except Exception as e:
        print(f"    ⚠ PDF-parsing mislukt: {e}")
        return None
    finally:
        os.unlink(tmp_path)


def format_price_nl(price: int) -> str:
    return f"Vanaf € {price:,.0f}".replace(",", ".")


def format_price_en(price: int) -> str:
    return f"From € {price:,}"


def budget_bucket(price: int) -> str:
    if price < 200_000:   return "under-200k"
    if price < 400_000:   return "200k-400k"
    if price < 600_000:   return "400k-600k"
    if price < 800_000:   return "600k-800k"
    if price < 1_200_000: return "800k-1.2m"
    if price < 2_000_000: return "1.2m-2m"
    return "2m-plus"


# ── hoofdlogica ──────────────────────────────────────────────────────────────

def list_subfolders(dbx: dropbox.Dropbox, path: str) -> list[tuple[str, str]]:
    folders = []
    try:
        result = dbx.files_list_folder(path)
        while True:
            for entry in result.entries:
                if isinstance(entry, FolderMetadata):
                    folders.append((entry.name, entry.path_display))
            if not result.has_more:
                break
            result = dbx.files_list_folder_continue(result.cursor)
    except ApiError as e:
        print(f"  ⚠ Kan map niet lezen ({path}): {e}")
    return folders


def sync(dbx: dropbox.Dropbox, projects: dict) -> dict:
    slug_by_norm: dict[str, str] = {}
    for slug in projects:
        try:
            nl_name = projects[slug]["nl"]["name"]
            slug_by_norm[normalize(nl_name)] = slug
        except (KeyError, TypeError):
            pass
        slug_by_norm[slug] = slug

    changes: dict[str, int] = {}

    for region_path in REGION_PATHS:
        print(f"\n📍 Regio: {region_path.split('/')[-1]}")
        developers = list_subfolders(dbx, region_path)

        for dev_name, dev_path in sorted(developers):
            if normalize(dev_name) in SKIP_FOLDERS:
                continue

            project_folders = list_subfolders(dbx, dev_path)
            if not project_folders:
                project_folders = [(dev_name, dev_path)]

            for proj_name, proj_path in project_folders:
                norm = normalize(proj_name)
                if norm in SKIP_FOLDERS:
                    continue

                slug = slug_by_norm.get(norm)
                if not slug:
                    short = re.sub(r"-(residences|homes|properties|villas|suites|living|views|golf|beach|park|hills|bay|gardens)$", "", norm)
                    slug = slug_by_norm.get(short)

                if not slug:
                    continue

                print(f"  🔍 {proj_name} → {slug}")

                pdf_path = find_pricelist_pdf(dbx, proj_path)
                if not pdf_path:
                    print(f"     ⚠ Geen prijslijst gevonden")
                    continue

                text = pdf_to_text(dbx, pdf_path)
                if not text:
                    continue

                lowest = extract_lowest_price(text)
                if not lowest:
                    print(f"     ⚠ Geen prijs gevonden in {pdf_path.split('/')[-1]}")
                    continue

                current = projects[slug].get("price_num")
                if current == lowest:
                    print(f"     ✓ Prijs ongewijzigd: {format_price_nl(lowest)}")
                else:
                    print(f"     💰 {format_price_nl(current or 0)} → {format_price_nl(lowest)}")
                    changes[slug] = lowest

    return changes


def apply_changes(projects: dict, changes: dict[str, int]) -> dict:
    for slug, price in changes.items():
        projects[slug]["price_num"] = price
        projects[slug]["budget"] = budget_bucket(price)
        if "nl" in projects[slug]:
            projects[slug]["nl"]["price"] = format_price_nl(price)
        if "en" in projects[slug]:
            projects[slug]["en"]["price"] = format_price_en(price)
    return projects


def main():
    if not DROPBOX_TOKEN:
        sys.exit("❌ Stel DROPBOX_TOKEN in als omgevingsvariabele.")

    print("🔗 Verbinden met Dropbox...")
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    try:
        account = dbx.users_get_current_account()
        print(f"✓ Ingelogd als {account.email}")
    except Exception as e:
        sys.exit(f"❌ Dropbox-authenticatie mislukt: {e}")

    print(f"\n📂 Laden: {PROJECTS_JSON}")
    with open(PROJECTS_JSON) as f:
        data = json.load(f)
    projects = data["projects"]
    print(f"   {len(projects)} projecten geladen")

    changes = sync(dbx, projects)

    print(f"\n{'─' * 50}")
    if not changes:
        print("✅ Geen prijswijzigingen gevonden.")
        return

    print(f"🔄 {len(changes)} prijswijziging(en):")
    for slug, price in changes.items():
        print(f"   {slug}: {format_price_nl(price)}")

    if DRY_RUN:
        print("\n⚠ DRY RUN – geen bestanden gewijzigd.")
        return

    data["projects"] = apply_changes(projects, changes)
    with open(PROJECTS_JSON, "w") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    print(f"\n✅ {PROJECTS_JSON.name} bijgewerkt.")

    print("\n🔨 HTML regenereren...")
    import subprocess
    for script in ["generate.py", "generate_hub.py"]:
        result = subprocess.run(
            ["python3", str(ROOT / "_build" / script)],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"   ⚠ {script}: {result.stderr[:200]}")
        else:
            print(f"   ✓ {script}")


if __name__ == "__main__":
    main()
