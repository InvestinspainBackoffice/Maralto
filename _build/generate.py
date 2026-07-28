"""
Bouwt <slug>/index.html voor elk project in _build/projects/*.py, door
head.html + hero.html + het handgeschreven body-fragment + tail.html samen
te voegen en de __TOKEN__-placeholders in te vullen.

Gebruik:  python3 _build/generate.py            (alle projecten)
          python3 _build/generate.py adagio      (één project)
"""
import importlib.util
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "_build", "templates")
PROJECTS_DIR = os.path.join(ROOT, "_build", "projects")

# Budgetcategorieën voor de Zapier-lead ("budget"-veld in de master sheet /
# CRM). We vragen dit nooit rechtstreeks aan de bezoeker - elke projectpagina
# kent zijn eigen vanaf-prijs, dus die zetten we automatisch om naar dezelfde
# categorieën die daar voor andere leadbronnen (Facebook, survey's) al in
# gebruik zijn. Op de /projecten/ overzichtspagina is er geen vast project,
# dus blijft dit veld daar leeg.
BUDGET_BUCKETS = [
    ("<200k", None, 200_000),
    ("200k-400k", 200_000, 400_000),
    ("400k-600k", 400_000, 600_000),
    ("600k-800k", 600_000, 800_000),
    ("800k-1m", 800_000, 1_000_000),
    ("1m - 3m", 1_000_000, 3_000_000),
    ("3m+", 3_000_000, None),
]


def parse_price_number(price_str):
    match = re.search(r"([\d.,]+)", price_str)
    if not match:
        return None
    digits = re.sub(r"[.,]", "", match.group(1))
    return int(digits) if digits else None


def budget_bucket(price_num):
    if price_num is None:
        return ""
    for label, lo, hi in BUDGET_BUCKETS:
        if (lo is None or price_num >= lo) and (hi is None or price_num < hi):
            return label
    return ""


def load_module(path):
    spec = importlib.util.spec_from_file_location("project", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fill(template, data):
    out = template
    for key, value in data.items():
        out = out.replace(f"__{key}__", value)
    return out


def build_one(project_file):
    mod = load_module(project_file)
    if not hasattr(mod, "DATA"):
        return  # projectbestand zonder eigen pagina (alleen een HUB-vermelding)
    data = dict(mod.DATA)
    slug = data["SLUG"]
    # De sticky-cta bar heeft alleen het bedrag nodig (zonder "Vanaf "-prefix).
    # Projecten zonder vaste prijs ("Prijs op aanvraag") zetten PRICE_LABEL
    # en PRICE_AMOUNT expliciet in hun eigen DATA-dict, zodat de tekst er
    # klopt in plaats van de standaard "Vanaf "-prefix te forceren.
    data.setdefault("PRICE_AMOUNT", data["PRICE_FROM"].replace("Vanaf ", ""))
    data.setdefault("PRICE_LABEL", "Vanaf")
    data.setdefault("BUDGET_BUCKET", budget_bucket(parse_price_number(data["PRICE_FROM"])))

    with open(os.path.join(TEMPLATES, "head.html"), encoding="utf-8") as f:
        head = f.read()
    with open(os.path.join(TEMPLATES, "hero.html"), encoding="utf-8") as f:
        hero = f.read()
    with open(os.path.join(TEMPLATES, "tail.html"), encoding="utf-8") as f:
        tail = f.read()

    body_path = os.path.join(PROJECTS_DIR, f"{slug}_body.html")
    with open(body_path, encoding="utf-8") as f:
        body = f.read()

    page = fill(head, data) + fill(hero, data) + body + fill(tail, data)

    remaining = [tok for tok in page.split("__") if tok.isupper() and "_" in tok]
    # Grove check: als er nog __IETS_MET_HOOFDLETTERS__ overblijft, is er een token vergeten
    import re
    leftovers = set(re.findall(r"__[A-Z_]+__", page))
    if leftovers:
        raise SystemExit(f"[{slug}] Niet-ingevulde tokens: {sorted(leftovers)}")

    # De projectenpagina (hub) leeft op de root van de site ("/"); elk
    # project, inclusief Maralto, krijgt zijn eigen submap.
    out_dir = os.path.join(ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"[{slug}] -> {out_path} ({len(page)} chars)")


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    files = sorted(f for f in os.listdir(PROJECTS_DIR) if f.endswith(".py"))
    if only:
        files = [f for f in files if f == f"{only}.py"]
        if not files:
            raise SystemExit(f"Geen project-databestand gevonden voor '{only}'")
    for f in files:
        build_one(os.path.join(PROJECTS_DIR, f))


if __name__ == "__main__":
    main()
