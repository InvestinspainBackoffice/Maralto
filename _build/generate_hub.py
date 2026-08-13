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
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "_build", "templates")
PROJECTS_DIR = os.path.join(ROOT, "_build", "projects")

LANGUAGES = ["nl", "en"]

HUB_OG_IMAGE = "https://investinspain.be/wp-content/uploads/2026/07/SOLENNE-001-scaled.jpg"

HUB_TEXT = {
    "nl": {
        "TITLE": "Onze projecten — INVESTINSPAIN.BE",
        "META_DESCRIPTION": "Ontdek de actuele nieuwbouwprojecten van INVESTINSPAIN.BE aan de Costa del Sol, op kaart en op naam.",
        "OG_DESCRIPTION": "Ontdek de actuele nieuwbouwprojecten van INVESTINSPAIN.BE aan de Costa del Sol.",
    },
    "en": {
        "TITLE": "Our projects — INVESTINSPAIN.BE",
        "META_DESCRIPTION": "Discover INVESTINSPAIN.BE's current new-build projects on the Costa del Sol, by map and by name.",
        "OG_DESCRIPTION": "Discover INVESTINSPAIN.BE's current new-build projects on the Costa del Sol.",
    },
}

# Projecten die NIET in de hub moeten verschijnen (offline houden)
EXCLUDE = [
    "kosmos",                      # Batch 28 - offline
    "kristina-views",              # Batch 28 - offline
    "octavia",                     # Batch 28 - offline
    "the-list-rio-real",           # Batch 29 - offline
    "el-bosque-en-alcuzcuz",       # Batch 29 - offline
    "alura-living",                # Batch 29 - offline
    "las-mesas-infinity-homes",    # Batch 29 - offline
    "vasari-villas",               # Batch 30 - offline
    "balance-mijas",               # Batch 30 - offline
    "noura",                       # Batch 30 - offline
    "imagine-by-marein",           # Batch 30 - offline
    "aura-cabopino",               # Batch 30 - offline
    "aura-higueron",               # Batch 30 - offline
    "the-line-superior-villas",    # Batch 30 - offline
    "the-place-by-alcazaba",       # Batch 30 - offline
    "lomas-unique",                # Batch 30 - offline
    "higueron-south-residences",   # Batch 31 - offline
    "balcon-del-mediterraneo",     # Batch 31 - offline
    "the-oak-48",                  # Batch 31 - offline
    "waveview",                    # Batch 31 - offline
    "astrid-torremuelle",          # Batch 31 part 2 - offline
    "abelias",                     # Batch 31 part 2 - offline
    "zenith-estepona",             # Batch 31 part 2 - offline
    "asperia",                     # Batch 31 part 2 - offline
    "lakun",                       # Batch 31 part 2 - offline
    "la-finca-de-jasmine-the-sky-villas",  # Batch 32 - offline
    "torre-biznaga",               # Batch 32 - offline
    "real-de-la-quinta",           # Batch 32 - offline
    "mimosas-real-de-la-quinta",   # Batch 32 - offline
    "terra-nova-hills",            # Batch 32 - offline
    "los-hidalgos-de-la-duquesa-villas",  # Batch 32 - offline
    "atria",                       # Batch 32 - offline
    "premier-residencial",         # Batch 32 - offline
    "sira-homes",                  # Batch 32 - offline
    "aby-estepona",                # Batch 32 - offline
    "zinnia",                      # Batch 32 - offline
    "one-seven-villas-estepona",   # Batch 32 - offline
    "the-meadows-la-cala-golf",    # Batch 32 - offline
    "idyllic",                     # Batch 32 - offline
    "camarate-hills",              # Batch 32 - offline
    "terra-homes",                 # Batch 33 - offline
    "nalu-suites",                 # Batch 33 - offline
    "termica-beach",               # Batch 33 - offline
    "savia",                       # Batch 33 - offline
    "unika",                       # Batch 33 - offline
    "celestia-homes",              # Batch 33 - offline
    "4our-villas",                 # Batch 33 - offline
    "aruna-cabopino-golf",         # Batch 33 - offline
    "idris-6-view",                # Batch 33 - offline
    "taray",                       # Batch 33 - offline
    "horizonte-village",           # Batch 33 - offline
    "sancha-view-32",              # Batch 33 - offline
    "vista-linda",                 # Batch 33 - offline
    "la-loma-de-cortesin",         # Batch 33 - offline
    "pinares-hills",               # Batch 33 - offline
    "seven-diamonds",              # Batch 33 - offline
    "ava-villas",                  # Batch 33 - offline
    "sunway-residence",            # Batch 33 - offline
    "armonia",                     # Batch 33 - offline
    "bougainvillea",               # Batch 33 - offline
    "the-avenue",                  # Batch 33 - offline
    "waterfall-residences",        # Batch 33 - offline
]

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
    "etherna-homes", "riviera-hill", "nacare", "vanian-park", "skye",
    "casatalaya", "salvia", "beyond-homes", "australy-thera", "tyrian",
    "haiku-estepona", "morasol",
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
        if slug in EXCLUDE:
            continue
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
    # Sommige thumbnails hebben een storende watermerktekst onderaan de
    # bronfoto; die projecten zetten een SLUG-scoped regel in
    # __CARD_EXTRA_CSS__ (zie main()) om net dat stukje uit de crop te
    # croppen zonder de gedeelde kaart-CSS voor alle projecten te raken.
    slug_class = f" project-card--{entry['SLUG']}" if entry.get("THUMB_EXTRA_CSS") else ""
    return f"""    <a class="project-card{slug_class}" href="{entry['HREF']}" data-location="{html.escape(entry['LOCATION'])}" data-price-band="{band_id}">
      <div class="project-card__img-wrap">
        <img class="project-card__img" src="{entry['THUMB']}" alt="{html.escape(entry['NAME'])}" loading="lazy" decoding="async">
      </div>
      <div class="project-card__body">
        <div class="project-card__name">{html.escape(entry['NAME'])}</div>
        <div class="project-card__location">{html.escape(entry['LOCATION'])}</div>
        <div class="project-card__price">{html.escape(entry['PRICE'])}</div>
      </div>
    </a>"""


def entry_for_lang(entry, lang):
    """Geeft een kopie van een HUB-entry terug met de prijs vertaald en de
    HREF naar de juiste taalversie - enkel relevant zolang niet elk project
    al een Engelse pagina heeft."""
    if lang != "en":
        return entry
    out = dict(entry)
    price_translations = {
        "Prijs op aanvraag": "Price on request",
        "Binnenkort beschikbaar": "Coming soon",
        "Uitverkocht": "Sold out",
    }
    out["PRICE"] = price_translations.get(
        out["PRICE"], out["PRICE"].replace("Vanaf €", "From €")
    )
    out["HREF"] = f"/en{out['HREF']}"
    return out


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


def build(lang):
    by_slug = load_hub_entries_by_slug()
    if not by_slug:
        raise SystemExit("Geen enkel project-bestand met een HUB-dict gevonden.")

    if lang == "en":
        # Zolang niet elk project een Engelse pagina heeft, toont de Engelse
        # hub enkel kaartjes voor projecten die er al één hebben - anders
        # linkt hij naar pagina's die niet bestaan.
        by_slug = {
            slug: e for slug, e in by_slug.items()
            if os.path.exists(os.path.join(ROOT, "en", slug, "index.html"))
        }
        if not by_slug:
            print("index.html (en) overgeslagen: nog geen enkel project heeft een Engelse pagina")
            return

    entries = [entry_for_lang(e, lang) for e in display_order(by_slug)]
    hero_entries = [entry_for_lang(e, lang) for e in last_n_chronological(by_slug, HERO_ROTATION_COUNT)]

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
    card_extra_css_parts = []
    for e in entries:
        if e.get("THUMB_EXTRA_CSS"):
            card_extra_css_parts.append(
                f".project-card--{e['SLUG']} .project-card__img {{ {e['THUMB_EXTRA_CSS']} }}"
            )
        if e.get("THUMB_HOVER_EXTRA_CSS"):
            card_extra_css_parts.append(
                f".project-card--{e['SLUG']}:hover .project-card__img {{ {e['THUMB_HOVER_EXTRA_CSS']} }}"
            )
    card_extra_css = "\n".join(card_extra_css_parts)

    with open(os.path.join(TEMPLATES, "hub.html"), encoding="utf-8") as f:
        page = f.read()

    page = page.replace("__PROJECT_CARDS__", cards_html)
    page = page.replace("__LOCATION_OPTIONS__", render_location_options(entries))
    page = page.replace("__PRICE_OPTIONS__", render_price_options())
    page = page.replace("__MAP_MARKERS_JSON__", json.dumps(markers, ensure_ascii=False))
    page = page.replace("__HERO_ROTATION_JSON__", json.dumps(hero_rotation, ensure_ascii=False))
    page = page.replace("__CARD_EXTRA_CSS__", card_extra_css)

    text = HUB_TEXT[lang]
    page = page.replace("__HUB_TITLE__", text["TITLE"])
    page = page.replace("__HUB_META_DESCRIPTION__", text["META_DESCRIPTION"])
    page = page.replace("__HUB_OG_DESCRIPTION__", text["OG_DESCRIPTION"])
    page = page.replace("__HUB_OG_IMAGE__", HUB_OG_IMAGE)
    for key, value in i18n.strings_for(lang).items():
        page = page.replace(f"__I_{key}__", value)
    page = page.replace("__LANG_SWITCH_HREF__", "/" if lang == "en" else "/en/")
    page = page.replace("__THANKS_HREF__", "/en/thank-you/" if lang == "en" else "/bedankt/")

    leftovers = set(re.findall(r"__[A-Z0-9_]+__", page))
    if leftovers:
        raise SystemExit(f"index.html ({lang}) Niet-ingevulde tokens: {sorted(leftovers)}")

    # De projectenpagina is nu de hoofdpagina van de site ("/") - dezelfde
    # content stond al op het hoofddomein investinspain.be, dus deze
    # subdomeinpagina's blijven voorlopig op noindex staan. De Engelse
    # versie spiegelt dezelfde structuur onder /en/.
    out_dir = os.path.join(ROOT, "en") if lang == "en" else ROOT
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"index.html ({lang}) -> {len(entries)} projecten ({len(page)} chars)")


def main():
    for lang in LANGUAGES:
        build(lang)


if __name__ == "__main__":
    main()
