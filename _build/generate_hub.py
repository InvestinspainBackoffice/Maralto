"""
Bouwt projecten/index.html: een overzichtspagina met kaart + kaartjes voor
elk project dat een HUB-dict definieert in _build/projects/*.py. Wordt
automatisch bijgewerkt zodra een nieuw project-bestand een HUB toevoegt -
geen handmatige HTML-bewerking nodig.

Gebruik: python3 _build/generate_hub.py
"""
import html
import importlib.util
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "_build", "templates")
PROJECTS_DIR = os.path.join(ROOT, "_build", "projects")

# Maralto eerst (vlaggenschip), daarna alfabetisch. Nieuwe projecten die hier
# niet in staan, komen automatisch achteraan (alfabetisch) terecht.
ORDER = ["maralto"]

# Volgorde waarin projecten zijn toegevoegd (oudste eerst) - bepaalt welke 5
# in de roterende hero komen. Voeg een nieuwe slug toe aan het EINDE zodra
# er een project bijkomt; vergeten mag ook, die komen dan automatisch
# (alfabetisch) achteraan terecht en tellen dus als "oudst".
CHRONOLOGICAL = [
    "maralto", "adagio", "the-view", "zew-elviria",
    "marine-hills", "the-sky-marbella", "the-grove",
    "dunique", "zenity-azure", "the-kove",
    "essence-residence", "altezza-suites", "las-mesas-blue-horizon", "vesta-mare",
    "romero", "360", "santa-clara-homes", "ikkil-bay", "nubay", "solenne",
    "birdie-hills", "australy-aures", "vivace-villas", "ocean-view-marbella",
]
HERO_ROTATION_COUNT = 5

# Prijsbanden voor de filter op /projecten/. Grenzen in euro; de bovengrens
# van elke band is exclusief (net als de "max" hieronder aangeeft).
PRICE_BANDS = [
    ("tot-500k", "Tot € 500.000", None, 500_000),
    ("500k-1m", "€ 500.000 – € 1.000.000", 500_000, 1_000_000),
    ("1m-2m", "€ 1.000.000 – € 2.000.000", 1_000_000, 2_000_000),
    ("2m-plus", "€ 2.000.000 en meer", 2_000_000, None),
]


def parse_price_number(price_str):
    """Haalt het eerste bedrag uit een prijstekst zoals 'Vanaf € 990.000' of
    '€ 995.000 (Excl. meubels)' en geeft het terug als geheel getal in euro."""
    match = re.search(r"([\d.,]+)", price_str)
    if not match:
        return None
    digits = re.sub(r"[.,]", "", match.group(1))
    return int(digits) if digits else None


def price_band_id(price_num):
    if price_num is None:
        return ""
    for band_id, _label, lo, hi in PRICE_BANDS:
        if (lo is None or price_num >= lo) and (hi is None or price_num < hi):
            return band_id
    return ""


def load_hub_entries_by_slug():
    entries = {}
    for fname in sorted(os.listdir(PROJECTS_DIR)):
        if not fname.endswith(".py"):
            continue
        slug = fname[:-3]
        spec = importlib.util.spec_from_file_location(slug, os.path.join(PROJECTS_DIR, fname))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "HUB"):
            entry = dict(mod.HUB)
            entry["SLUG"] = slug
            entries[slug] = entry
    return entries


def display_order(entries):
    ordered_slugs = [s for s in ORDER if s in entries]
    ordered_slugs += sorted(s for s in entries if s not in ORDER)
    return [entries[s] for s in ordered_slugs]


def last_n_chronological(entries, n):
    slugs = [s for s in CHRONOLOGICAL if s in entries]
    slugs += sorted(s for s in entries if s not in CHRONOLOGICAL)
    last = slugs[-n:]
    last.reverse()  # nieuwste eerst in de rotatie
    return [entries[s] for s in last]


def render_card(entry):
    price_num = parse_price_number(entry["PRICE"])
    band_id = price_band_id(price_num)
    return f"""    <a class="project-card" href="{entry['HREF']}" data-location="{html.escape(entry['LOCATION'])}" data-price-band="{band_id}">
      <div class="project-card__img-wrap">
        <img class="project-card__img" src="{entry['THUMB']}" alt="{html.escape(entry['NAME'])}" loading="lazy">
      </div>
      <div class="project-card__body">
        <div class="project-card__name">{html.escape(entry['NAME'])}</div>
        <div class="project-card__location">{html.escape(entry['LOCATION'])}</div>
        <div class="project-card__price">{html.escape(entry['PRICE'])}</div>
      </div>
    </a>"""


def render_location_options(entries):
    locations = sorted({e["LOCATION"] for e in entries})
    return "\n".join(
        f'        <option value="{html.escape(loc)}">{html.escape(loc)}</option>'
        for loc in locations
    )


def render_price_options():
    return "\n".join(
        f'        <option value="{band_id}">{html.escape(label)}</option>'
        for band_id, label, _lo, _hi in PRICE_BANDS
    )


def main():
    by_slug = load_hub_entries_by_slug()
    if not by_slug:
        raise SystemExit("Geen enkel project-bestand met een HUB-dict gevonden.")

    entries = display_order(by_slug)
    hero_entries = last_n_chronological(by_slug, HERO_ROTATION_COUNT)

    cards_html = "\n".join(render_card(e) for e in entries)
    markers = [
        {
            "name": e["NAME"],
            "location": e["LOCATION"],
            "price": e["PRICE"],
            "href": e["HREF"],
            "lat": e["LAT"],
            "lng": e["LNG"],
        }
        for e in entries
    ]
    hero_rotation = [
        {"name": e["NAME"], "thumb": e["THUMB"], "href": e["HREF"]}
        for e in hero_entries
    ]

    with open(os.path.join(TEMPLATES, "hub.html"), encoding="utf-8") as f:
        page = f.read()

    page = page.replace("__PROJECT_CARDS__", cards_html)
    page = page.replace("__LOCATION_OPTIONS__", render_location_options(entries))
    page = page.replace("__PRICE_OPTIONS__", render_price_options())
    page = page.replace("__MAP_MARKERS_JSON__", json.dumps(markers, ensure_ascii=False))
    page = page.replace("__HERO_ROTATION_JSON__", json.dumps(hero_rotation, ensure_ascii=False))

    out_dir = os.path.join(ROOT, "projecten")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"projecten/index.html -> {len(entries)} projecten ({len(page)} chars)")


if __name__ == "__main__":
    main()
