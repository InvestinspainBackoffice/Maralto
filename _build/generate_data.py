"""
Schrijft api/_projects.json - de kennisbasis waarmee de AI-chatwidget praat.

Waarom in api/ en niet in _build/: .vercelignore sluit _build/ uit van de
deploy, dus een bestand daar is op Vercel onbereikbaar voor de functie.
Bestandsnamen die met _ beginnen worden door Vercel niet als route
behandeld, dus api/_projects.json is data, geen endpoint.

De inhoud komt volledig uit bestaande bronnen - de DATA-dicts in
_build/projects/*.py en de handgeschreven body-fragmenten - zodat er geen
tweede plek ontstaat waar projectteksten onderhouden moeten worden.

Gebruik:  python3 _build/generate_data.py
"""
import html
import json
import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate  # noqa: E402  (hergebruikt load_module, budget_bucket, ...)

ROOT = generate.ROOT
PROJECTS_DIR = generate.PROJECTS_DIR
OUT_PATH = os.path.join(ROOT, "api", "_projects.json")
BASE_URL = "https://projects.investinspain.be"


def strip_tags(fragment):
    """HTML-fragment -> platte tekst, met <br> als spatie."""
    text = re.sub(r"<br\s*/?>", " ", fragment)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def find_all(pattern, source):
    return [strip_tags(m) for m in re.findall(pattern, source, re.S)]


def parse_body(body):
    """Haalt de inhoudelijke tekst uit een body-fragment.

    De fragmenten zijn door onszelf gegenereerd en volgen allemaal dezelfde
    structuur, dus regex volstaat hier - een HTML-parser als dependency
    toevoegen zou niet in verhouding staan.
    """
    headings = find_all(r'<h2 class="heading">(.*?)</h2>', body)
    paragraphs = find_all(r'<p class="body-text">(.*?)</p>', body)

    sections = []
    for i, text in enumerate(paragraphs):
        sections.append({
            "heading": headings[i] if i < len(headings) else "",
            "text": text,
        })

    stats = []
    for value, label in re.findall(
        r'<div class="stat__value">(.*?)</div>\s*'
        r'<div class="stat__label">(.*?)</div>',
        body, re.S,
    ):
        stats.append(f"{strip_tags(value)} {strip_tags(label)}")

    facts = []
    for dist, name in re.findall(
        r'<span class="location-fact__dist">(.*?)</span>\s*'
        r'<span class="location-fact__name">(.*?)</span>',
        body, re.S,
    ):
        facts.append(f"{strip_tags(name)}: {strip_tags(dist)}")

    amenities = find_all(
        r'<div class="amenity-item">.*?<span>(.*?)</span>', body
    )

    coords = ""
    coord_match = re.search(r"maps\?q=(-?[\d.]+,-?[\d.]+)", body)
    if coord_match:
        coords = coord_match.group(1)

    return {
        "sections": sections,
        "stats": stats,
        "amenities": amenities,
        "location_facts": facts,
        "coords": coords,
    }


def data_for_lang(mod, lang):
    """Reproduceert de taalafhankelijke DATA-samenstelling uit generate.py."""
    data = dict(mod.DATA)
    if lang == "en":
        for key, value in list(data.items()):
            if isinstance(value, str) and "Vanaf €" in value:
                data[key] = value.replace("Vanaf €", "From €")
        if hasattr(mod, "DATA_EN"):
            data.update(mod.DATA_EN)
    return data


def build_project(project_file):
    mod = generate.load_module(project_file)
    if not hasattr(mod, "DATA"):
        return None  # alleen een HUB-vermelding, geen eigen pagina
    if not hasattr(mod, "HUB"):
        return None  # niet zichtbaar op de hub — chatbot toont enkel hub-projecten

    slug = mod.DATA["SLUG"]
    price_num = generate.parse_price_number(mod.DATA["PRICE_FROM"])

    nl_data = data_for_lang(mod, "nl")
    entry = {
        "slug": slug,
        "price_num": price_num,
        "budget": generate.budget_bucket(price_num),
        # Voor de projectkaartjes op /selectie/ (zie api/match.js).
        # THUMB (uit het optionele HUB-dict) eerst: dat is bij de oudere
        # projecten de enige zelf-gehoste (WebP) variant - hun OG_IMAGE/
        # HERO_BG linkt daar nog rechtstreeks naar investinspain.be, wat we
        # juist nooit willen (zie CLAUDE.md). Met deze volgorde heeft elk
        # van de 128 projecten een zelf-gehoste foto.
        "image": getattr(mod, "HUB", {}).get("THUMB")
        or nl_data.get("HERO_BG")
        or nl_data.get("OG_IMAGE", ""),
    }

    for lang in ("nl", "en"):
        suffix = "_body.html" if lang == "nl" else "_body_en.html"
        body_path = os.path.join(PROJECTS_DIR, f"{slug}{suffix}")
        if not os.path.exists(body_path):
            continue
        with open(body_path, encoding="utf-8") as f:
            parsed = parse_body(f.read())

        data = data_for_lang(mod, lang)
        entry[lang] = {
            "name": data.get("HERO_NAME", data.get("PROJECT_NAME", "")),
            "location": data.get("HERO_LOCATION", ""),
            "price": data.get("PRICE_FROM", ""),
            "summary": data.get("META_DESCRIPTION", ""),
            "url": f"{BASE_URL}/{slug}/" if lang == "nl" else f"{BASE_URL}/en/{slug}/",
            **parsed,
        }
        entry.setdefault("coords", parsed["coords"])

    # De coördinaten komen normaal uit de Google-Maps-link in het body-fragment.
    # Een enkel project heeft die kaart niet; daar valt het terug op LAT/LNG
    # uit het HUB-dict. /selectie/ leidt de regio (Málaga/Marbella/Estepona/
    # Sotogrande) af uit de lengtegraad, dus zonder coördinaten valt een
    # project uit elke regiofilter.
    hub = getattr(mod, "HUB", {})
    if not entry.get("coords") and hub.get("LAT") is not None:
        entry["coords"] = f"{hub['LAT']},{hub['LNG']}"

    return entry if "nl" in entry else None


def main():
    files = sorted(f for f in os.listdir(PROJECTS_DIR) if f.endswith(".py"))
    projects = {}
    for f in files:
        entry = build_project(os.path.join(PROJECTS_DIR, f))
        if entry:
            projects[entry["slug"]] = entry

    payload = {
        "generated": date.today().isoformat(),
        "projects": projects,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))

    size_kb = os.path.getsize(OUT_PATH) / 1024
    with_en = sum(1 for p in projects.values() if "en" in p)
    print(f"api/_projects.json -> {len(projects)} projecten "
          f"({with_en} met EN) - {size_kb:.0f} kB")


if __name__ == "__main__":
    main()
