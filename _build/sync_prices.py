#!/usr/bin/env python3
"""
_build/sync_prices.py
Leest de actuele prijslijsten uit Dropbox en werkt api/_projects.json bij.
Draait automatisch via GitHub Actions, of handmatig:

  DROPBOX_TOKEN=xxx python3 _build/sync_prices.py
  DROPBOX_TOKEN=xxx python3 _build/sync_prices.py --dry-run

Vereisten:
  pip install requests pdfplumber

GitHub Actions secret: DROPBOX_TOKEN
"""

import os
import re
import sys
import json
import tempfile
import unicodedata
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

try:
    import pdfplumber
except ImportError:
    sys.exit("pip install pdfplumber")

# ── configuratie ─────────────────────────────────────────────────────────────

DROPBOX_TOKEN    = os.environ.get("DROPBOX_TOKEN", "")
DRY_RUN          = "--dry-run" in sys.argv

ROOT             = Path(__file__).parent.parent
PROJECTS_JSON    = ROOT / "api" / "_projects.json"

# Namespace-ID van de gedeelde "IIS Projects" Dropbox-map
IIS_NAMESPACE_ID = "7492713440"

# Regio-submappen relatief aan de IIS Projects namespace root
REGION_SUBPATHS  = [
    "/01 Costa del Sol",
    "/02 Costa Blanca",
    "/03 Costa Almeria",
    "/04 Mallorca",
]

# Dropbox API endpoints
LIST_FOLDER_URL     = "https://api.dropboxapi.com/2/files/list_folder"
LIST_CONTINUE_URL   = "https://api.dropboxapi.com/2/files/list_folder/continue"
DOWNLOAD_URL        = "https://content.dropboxapi.com/2/files/download"

# Mapnamen die we overslaan
SKIP_FOLDERS = {
    "00 admin", "01 existing property", "02 verhuur",
    "collaboration", "kycprev", "kyc", "0) reservation",
    "1) pbc", "s4lesagents",
}

# ── Dropbox API helpers ───────────────────────────────────────────────────────

def _headers(extra: dict | None = None) -> dict:
    h = {
        "Authorization": f"Bearer {DROPBOX_TOKEN}",
        "Content-Type": "application/json",
        # Gebruik de namespace als pad-root
        "Dropbox-API-Path-Root": json.dumps({
            ".tag": "namespace_id",
            "namespace_id": IIS_NAMESPACE_ID
        }),
    }
    if extra:
        h.update(extra)
    return h


def list_folder(path: str) -> list[dict]:
    """Geeft alle entries terug in een Dropbox-map (paginering inbegrepen)."""
    resp = requests.post(
        LIST_FOLDER_URL,
        headers=_headers(),
        json={"path": path, "recursive": False},
    )
    if not resp.ok:
        raise RuntimeError(f"list_folder({path}): {resp.status_code} {resp.text[:200]}")
    data = resp.json()
    entries = data.get("entries", [])
    while data.get("has_more"):
        resp = requests.post(LIST_CONTINUE_URL, headers=_headers(),
                             json={"cursor": data["cursor"]})
        data = resp.json()
        entries.extend(data.get("entries", []))
    return entries


def download_file(path: str) -> bytes | None:
    """Download een bestand vanuit de IIS namespace."""
    resp = requests.post(
        DOWNLOAD_URL,
        headers={
            "Authorization": f"Bearer {DROPBOX_TOKEN}",
            "Dropbox-API-Arg": json.dumps({
                "path": path,
            }),
            "Dropbox-API-Path-Root": json.dumps({
                ".tag": "namespace_id",
                "namespace_id": IIS_NAMESPACE_ID,
            }),
        },
    )
    if not resp.ok:
        print(f"    ⚠ Download mislukt ({path}): {resp.status_code}")
        return None
    return resp.content


def subfolders(path: str) -> list[tuple[str, str]]:
    """Geeft [(name, path)] terug voor alle submappen van path."""
    try:
        entries = list_folder(path)
    except RuntimeError as e:
        print(f"  ⚠ {e}")
        return []
    return [
        (e["name"], e["path_display"])
        for e in entries
        if e[".tag"] == "folder"
    ]

# ── prijsextractie ────────────────────────────────────────────────────────────

def normalize(name: str) -> str:
    nfkd = unicodedata.normalize("NFKD", name)
    ascii_str = nfkd.encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_str.lower()).strip("-")


def find_pricelist_pdf(project_path: str) -> str | None:
    """Zoek de actuele prijslijst PDF (niet in dated/-submap)."""
    for folder_name in ["Prices", "Pricelist", "Prijslijst", "Price list"]:
        folder_path = f"{project_path}/{folder_name}"
        try:
            entries = list_folder(folder_path)
        except RuntimeError:
            continue
        pdfs = [
            (e["server_modified"], e["path_display"])
            for e in entries
            if e[".tag"] == "file"
            and e["name"].lower().endswith(".pdf")
            and "dated" not in e["path_display"].lower()
        ]
        if pdfs:
            pdfs.sort(reverse=True)
            return pdfs[0][1]
    return None


def pdf_to_text(path: str) -> str | None:
    content = download_file(path)
    if not content:
        return None
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    try:
        parts = []
        with pdfplumber.open(tmp_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    parts.append(t)
        return "\n".join(parts)
    except Exception as e:
        print(f"    ⚠ PDF-parsing mislukt: {e}")
        return None
    finally:
        os.unlink(tmp_path)


def extract_lowest_price(text: str) -> int | None:
    PRICE_RE = re.compile(r"(\d{1,3}(?:[.,]\d{3})+)\s*€")
    prices = []
    for line in text.splitlines():
        upper = line.upper()
        if any(w in upper for w in ("RESERVADO", "SOLD", "VENDIDO")):
            continue
        for m in PRICE_RE.finditer(line):
            num = int(m.group(1).replace(".", "").replace(",", ""))
            if 50_000 < num < 50_000_000:
                prices.append(num)
    return min(prices) if prices else None

# ── prijsformattering ─────────────────────────────────────────────────────────

def fmt_nl(p: int) -> str:
    return f"Vanaf € {p:,.0f}".replace(",", ".")

def fmt_en(p: int) -> str:
    return f"From € {p:,}"

def budget_bucket(p: int) -> str:
    if p < 200_000:   return "under-200k"
    if p < 400_000:   return "200k-400k"
    if p < 600_000:   return "400k-600k"
    if p < 800_000:   return "600k-800k"
    if p < 1_200_000: return "800k-1.2m"
    if p < 2_000_000: return "1.2m-2m"
    return "2m-plus"

# ── hoofd-synchronisatie ──────────────────────────────────────────────────────

def sync(projects: dict) -> dict[str, int]:
    slug_by_norm: dict[str, str] = {}
    for slug in projects:
        try:
            slug_by_norm[normalize(projects[slug]["nl"]["name"])] = slug
        except (KeyError, TypeError):
            pass
        slug_by_norm[slug] = slug

    changes: dict[str, int] = {}

    for region_path in REGION_SUBPATHS:
        print(f"\n📍 Regio: {region_path.strip('/')}")
        developers = subfolders(region_path)

        for dev_name, dev_path in sorted(developers):
            if normalize(dev_name) in SKIP_FOLDERS:
                continue
            project_list = subfolders(dev_path) or [(dev_name, dev_path)]

            for proj_name, proj_path in project_list:
                norm = normalize(proj_name)
                if norm in SKIP_FOLDERS:
                    continue

                slug = slug_by_norm.get(norm)
                if not slug:
                    short = re.sub(
                        r"-(residences|homes|properties|villas|suites|living|"
                        r"views|golf|beach|park|hills|bay|gardens)$", "", norm)
                    slug = slug_by_norm.get(short)
                if not slug:
                    continue

                print(f"  🔍 {proj_name} → {slug}")
                pdf_path = find_pricelist_pdf(proj_path)
                if not pdf_path:
                    print("     ⚠ Geen prijslijst gevonden")
                    continue

                text = pdf_to_text(pdf_path)
                if not text:
                    continue

                lowest = extract_lowest_price(text)
                if not lowest:
                    print(f"     ⚠ Geen prijs gevonden in {pdf_path.split('/')[-1]}")
                    continue

                current = projects[slug].get("price_num")
                if current == lowest:
                    print(f"     ✓ Ongewijzigd: {fmt_nl(lowest)}")
                else:
                    print(f"     💰 {fmt_nl(current or 0)} → {fmt_nl(lowest)}")
                    changes[slug] = lowest

    return changes


def apply_changes(projects: dict, changes: dict[str, int]) -> dict:
    for slug, price in changes.items():
        projects[slug]["price_num"] = price
        projects[slug]["budget"]    = budget_bucket(price)
        if "nl" in projects[slug]:
            projects[slug]["nl"]["price"] = fmt_nl(price)
        if "en" in projects[slug]:
            projects[slug]["en"]["price"] = fmt_en(price)
    return projects


def main():
    if not DROPBOX_TOKEN:
        sys.exit("❌ Stel DROPBOX_TOKEN in als omgevingsvariabele.")

    # Verbindingstest
    resp = requests.post(
        "https://api.dropboxapi.com/2/users/get_current_account",
        headers={"Authorization": f"Bearer {DROPBOX_TOKEN}"},
    )
    if not resp.ok:
        sys.exit(f"❌ Dropbox-authenticatie mislukt: {resp.text}")
    print(f"✓ Ingelogd als {resp.json().get('email')}")

    print(f"\n📂 Laden: {PROJECTS_JSON}")
    with open(PROJECTS_JSON) as f:
        data = json.load(f)
    projects = data["projects"]
    print(f"   {len(projects)} projecten geladen")

    changes = sync(projects)

    print(f"\n{'─' * 50}")
    if not changes:
        print("✅ Geen prijswijzigingen gevonden.")
        return

    print(f"🔄 {len(changes)} prijswijziging(en):")
    for slug, price in changes.items():
        print(f"   {slug}: {fmt_nl(price)}")

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
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"   ⚠ {script}: {result.stderr[:200]}")
        else:
            print(f"   ✓ {script}")


if __name__ == "__main__":
    main()
