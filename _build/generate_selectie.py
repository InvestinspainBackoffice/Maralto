"""
Bouwt /selectie/index.html (NL) en /en/selection/index.html (EN): de eigen
vervanger voor de Typeform-vragenlijst.

Verschil met de Typeform: het formulier eindigt niet met "we sturen u een
lijstje", maar toont meteen de best passende projecten uit onze eigen
portefeuille als klikbare kaartjes. Het matchen gebeurt in api/match.js -
de browser stuurt alleen de antwoorden door, nooit projectdata.

De vragen en antwoordopties staan hieronder in QUESTIONS en niet in
_build/i18n.py: dat bestand is bewust beperkt tot vaste UI-tekst die in
meerdere templates terugkomt (knoppen, labels, foutmeldingen). Deze vragen
zijn inhoud van deze ene pagina.

Gebruik:  python3 _build/generate_selectie.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate  # noqa: E402
import i18n  # noqa: E402

ROOT = generate.ROOT
TEMPLATES = generate.TEMPLATES
IMG = "https://projects.investinspain.be/images"

# Waar de pagina terechtkomt, per taal. /selectie/ spiegelt het pad van de
# Typeform (/selection), zodat bestaande advertenties met hun UTM-parameters
# vrijwel één-op-één om te leggen zijn.
PATHS = {"nl": "selectie", "en": os.path.join("en", "selection")}
HREFS = {"nl": "/selectie/", "en": "/en/selection/"}

# Infinity pool met de zee op de achtergrond - de meest herkenbare "Costa
# del Sol"-belofte uit heel de beeldbank, en zonder watermerk (in
# tegenstelling tot enkele andere kandidaten, zoals ocean-view-marbella-2).
HERO_IMAGE = f"{IMG}/veridian/pool.webp"

# Antwoordopties met een foto gebruiken bestaande, zelf-gehoste projectfoto's
# (zie CLAUDE.md: nooit hotlinken). Ze illustreren de categorie; ze zijn geen
# uitspraak over welk project je krijgt.
TYPE_IMAGES = {
    "apartment": f"{IMG}/oceana-views/hero.webp",
    "penthouse": f"{IMG}/royal-river/img3.webp",
    "villa": f"{IMG}/las-villas-sotogrande/hero.webp",
    "townhouse": f"{IMG}/the-valley/exterior.webp",
    "turnkey": f"{IMG}/oceana-views/living-1.webp",
}

# ── De tien vragen ───────────────────────────────────────────────────────
#
# `param` is de naam waarmee het antwoord naar /api/match gaat; is die leeg,
# dan telt de vraag niet mee in de matching en gaat het antwoord alleen mee
# met de lead. Dat geldt bewust voor "reden van aankoop" en "wanneer wilt u
# verhuizen": daar staat niets over in onze projectdata, dus zouden we op die
# antwoorden alleen maar kunnen doen alsof we filteren.
#
# `multi` maakt er een meerkeuzevraag van, `required` blokkeert doorgaan
# zonder antwoord (net als in de Typeform).
QUESTIONS = [
    {
        "id": "region",
        "param": "regions",
        "multi": True,
        "required": True,
        "region_cards": True,
        "nl": {"q": "In welke regio bent u het meest ge&iuml;nteresseerd?"},
        "en": {"q": "Which area are you most interested in?"},
        "options": [
            {"value": "A", "nl": "M&aacute;laga &ndash; Marbella", "en": "M&aacute;laga &ndash; Marbella"},
            {"value": "B", "nl": "Marbella &ndash; Estepona", "en": "Marbella &ndash; Estepona"},
            {"value": "C", "nl": "Estepona &ndash; Sotogrande", "en": "Estepona &ndash; Sotogrande"},
        ],
    },
    {
        "id": "type",
        "param": "type",
        "required": True,
        "photos": True,
        "nl": {"q": "Welk type woning zoekt u?"},
        "en": {"q": "What type of property are you interested in?"},
        "options": [
            {"value": "apartment", "nl": "Nieuw appartement", "en": "New apartment"},
            {"value": "penthouse", "nl": "Nieuw penthouse", "en": "New penthouse"},
            {"value": "villa", "nl": "Nieuwe villa", "en": "New villa"},
            {"value": "townhouse", "nl": "Nieuwe townhouse", "en": "New townhouse"},
            {"value": "turnkey", "nl": "Sleutelklare moderne woning", "en": "Turnkey modern property"},
        ],
    },
    {
        "id": "reason",
        "param": "",
        "required": True,
        "nl": {"q": "Wat is uw belangrijkste reden om te kopen?"},
        "en": {"q": "What's your main reason for buying?"},
        "options": [
            {"value": "investment", "nl": "Investering", "en": "Investment"},
            {"value": "personal", "nl": "Eigen gebruik", "en": "Personal use"},
            {"value": "both", "nl": "Zowel investering als eigen gebruik", "en": "Both investment & personal"},
            {"value": "move", "nl": "Permanente verhuis", "en": "Permanent move"},
        ],
    },
    {
        "id": "budget",
        "param": "budget",
        "required": True,
        # De waarden zijn de URL-veilige codes uit api/match.js; die endpoint
        # vertaalt ze naar de Salesforce-codes ('<200k', '3m+', ...) die
        # ongewijzigd mee moeten met de lead.
        "nl": {"q": "Wat is uw budget?"},
        "en": {"q": "What is your budget?"},
        "options": [
            {"value": "lt200k", "nl": "Tot &euro; 200.000", "en": "Up to &euro; 200,000"},
            {"value": "200-400", "nl": "&euro; 200.000 &ndash; 400.000", "en": "&euro; 200,000 &ndash; 400,000"},
            {"value": "400-600", "nl": "&euro; 400.000 &ndash; 600.000", "en": "&euro; 400,000 &ndash; 600,000"},
            {"value": "600-1m", "nl": "&euro; 600.000 &ndash; 1 miljoen", "en": "&euro; 600,000 &ndash; 1 million"},
            {"value": "1m-3m", "nl": "&euro; 1 &ndash; 3 miljoen", "en": "&euro; 1 &ndash; 3 million"},
            {"value": "3m-plus", "nl": "Meer dan &euro; 3 miljoen", "en": "More than &euro; 3 million"},
        ],
    },
    {
        "id": "timing",
        "param": "",
        "multi": True,
        "required": True,
        "nl": {"q": "Wanneer wilt u er intrekken?"},
        "en": {"q": "When would you like to move in?"},
        "options": [
            {"value": "2026", "nl": "2026", "en": "2026"},
            {"value": "2027", "nl": "2027", "en": "2027"},
            {"value": "2028", "nl": "2028 of later", "en": "2028 or later"},
        ],
    },
    {
        "id": "bedrooms",
        "param": "bedrooms",
        "nl": {"q": "Hoeveel slaapkamers heeft u het liefst?"},
        "en": {"q": "Preferred number of bedrooms"},
        "options": [
            {"value": "1", "nl": "1", "en": "1"},
            {"value": "2", "nl": "2", "en": "2"},
            {"value": "3", "nl": "3", "en": "3"},
            {"value": "4plus", "nl": "4 of meer", "en": "4 or more"},
        ],
    },
    {
        "id": "location",
        "param": "location",
        "nl": {"q": "Wat voor ligging zoekt u?"},
        "en": {"q": "Preferred location type"},
        "options": [
            {"value": "quiet", "nl": "Rustig gelegen", "en": "Quiet"},
            {"value": "city", "nl": "In het centrum", "en": "City center"},
            {"value": "golf", "nl": "Aan een golfbaan", "en": "Golf area"},
            {"value": "beach", "nl": "Aan het strand", "en": "Beach"},
            {"value": "countryside", "nl": "In het groen", "en": "Countryside"},
        ],
    },
    {
        "id": "view",
        "param": "view",
        "nl": {"q": "Welk uitzicht heeft uw voorkeur?"},
        "en": {"q": "Preferred view"},
        "options": [
            {"value": "sea", "nl": "Zeezicht", "en": "Sea"},
            {"value": "mountain", "nl": "Bergzicht", "en": "Mountain"},
            {"value": "none", "nl": "Geen voorkeur", "en": "No preference"},
        ],
    },
    {
        "id": "indoor",
        "param": "indoor",
        "required": True,
        "nl": {"q": "Hoeveel woonoppervlak zoekt u? (m&sup2;)"},
        "en": {"q": "Desired indoor space (m&sup2;)"},
        "options": [
            {"value": "lt100", "nl": "Minder dan 100", "en": "Less than 100"},
            {"value": "100-150", "nl": "100 &ndash; 150", "en": "100 &ndash; 150"},
            {"value": "150plus", "nl": "150 of meer", "en": "150 or more"},
        ],
    },
    {
        "id": "outdoor",
        # Geen `param`: buitenruimte in m² staat in geen enkel projectbestand,
        # dus hierop matchen zou schijnprecisie zijn. De vraag blijft wel
        # staan - het antwoord is nuttige informatie voor de opvolging en gaat
        # mee met de lead.
        "param": "",
        "required": True,
        "nl": {"q": "Hoeveel buitenruimte zoekt u? (m&sup2;)"},
        "en": {"q": "Desired outdoor area (m&sup2;)"},
        "options": [
            {"value": "0-25", "nl": "0 &ndash; 25", "en": "0 &ndash; 25"},
            {"value": "25-100", "nl": "25 &ndash; 100", "en": "25 &ndash; 100"},
            {"value": "100plus", "nl": "100 of meer", "en": "100 or more"},
        ],
    },
]

LETTERS = "ABCDEFGH"


def region_prices():
    """Vanaf-prijzen per regio, berekend uit onze eigen projectdata.

    De Typeform toont hier vaste getallen die met de hand zijn ingetypt en
    dus verouderen zodra de portefeuille verandert. Deze komen bij elke
    regeneratie opnieuw uit api/_projects.json, zodat wat de bezoeker op de
    kaart ziet altijd klopt met wat hij daarna te zien krijgt.
    """
    data_path = os.path.join(ROOT, "api", "_projects.json")
    with open(data_path, encoding="utf-8") as f:
        projects = json.load(f)["projects"]

    bands = {"A": (-4.92, -3.70), "B": (-5.18, -4.85), "C": (-5.42, -5.10)}
    found = {r: {"apartment": [], "villa": []} for r in bands}

    for entry in projects.values():
        if not entry.get("price_num") or not entry.get("coords"):
            continue
        lon = float(entry["coords"].split(",")[1])
        nl = entry["nl"]
        text = " ".join(
            [nl.get("summary", "")]
            + [s["heading"] + " " + s["text"] for s in nl.get("sections", [])]
        ).lower()
        for region, (lo, hi) in bands.items():
            if not lo <= lon <= hi:
                continue
            if "appartement" in text:
                found[region]["apartment"].append(entry["price_num"])
            if "villa" in text:
                found[region]["villa"].append(entry["price_num"])

    def fmt(values):
        if not values:
            return "&mdash;"
        # De laagste vanaf-prijs, afgerond naar beneden op tienduizendtallen:
        # "v.a. € 250.000" leest als een richtprijs, "v.a. € 248.000" wekt de
        # indruk dat het om één specifiek project gaat.
        low = (min(values) // 10000) * 10000
        return "&euro; " + f"{low:,}".replace(",", ".")

    return {
        region: {"apartment": fmt(v["apartment"]), "villa": fmt(v["villa"])}
        for region, v in found.items()
    }


def phone_optgroups():
    """Hergebruikt de landcode-lijst uit tail.html i.p.v. een vierde kopie.

    Die lijst staat daar al drie keer (hoofdformulier, zijpaneel, pop-up).
    Hem hier overtypen zou een vierde plek maken waar een nieuw land
    toegevoegd moet worden; door hem uit te lezen blijft tail.html de bron.
    """
    with open(os.path.join(TEMPLATES, "tail.html"), encoding="utf-8") as f:
        tail = f.read()
    match = re.search(r"(<optgroup label=\"__I_PHONE_POPULAR__\".*?</optgroup>\s*"
                      r"<optgroup label=\"__I_PHONE_ALL_COUNTRIES__\".*?</optgroup>)",
                      tail, re.S)
    if not match:
        raise SystemExit(
            "Landcode-lijst niet gevonden in tail.html - is de structuur van "
            "de .phone-prefix-select daar gewijzigd?"
        )
    return match.group(1)


def render_options(question, lang):
    """Antwoordopties als knoppen. Elke knop draagt zijn eigen waarde, zodat
    de JS niets over de vragen hoeft te weten."""
    parts = []
    photos = question.get("photos")
    for i, opt in enumerate(question["options"]):
        letter = LETTERS[i]
        classes = "sel-option" + (" sel-option--photo" if photos else "")
        image = ""
        if photos:
            image = (
                f'<span class="sel-option__img" role="presentation" '
                f'style="background-image:url(\'{TYPE_IMAGES[opt["value"]]}\')"></span>'
            )
        parts.append(
            f'<button type="button" class="{classes}" data-value="{opt["value"]}" '
            f'role="{"checkbox" if question.get("multi") else "radio"}" aria-checked="false">'
            f"{image}"
            f'<span class="sel-option__letter" aria-hidden="true">{letter}</span>'
            f'<span class="sel-option__label">{opt[lang]}</span>'
            f'<span class="sel-option__tick" aria-hidden="true"></span>'
            f"</button>"
        )
    return "\n          ".join(parts)


def render_region_options(question, lang, strings, prices):
    """Vraag 1: de drie regio's als klikbare kaarten - geen aparte kaart mét
    losse antwoordknoppen eronder. Die twee stonden eerst na elkaar en zeiden
    hetzelfde tweemaal; dit is de ene set knoppen die je ook echt aanklikt.

    HTML-knoppen in plaats van SVG-rects: een <rect> is geen focusbaar,
    klikbaar element zonder een hoop extra werk (foreignObject, click-mapping
    op coördinaten). Drie <button>'s met dezelfde look kosten dat niet en
    werken meteen met dezelfde toetsenbordbediening als de andere vragen.
    """
    coast = f"""<div class="sel-coast" aria-hidden="true">
    <svg viewBox="0 0 544 34" preserveAspectRatio="none">
      <path d="M4 14 C 120 6, 180 22, 272 12 S 430 2, 540 10"/>
    </svg>
    <span class="sel-coast__label">{strings['SEL_MAP_SEA']}</span>
  </div>"""

    labels = [
        ("A", "M&Aacute;LAGA", "MARBELLA"),
        ("B", "MARBELLA", "ESTEPONA"),
        ("C", "ESTEPONA", "SOTOGRANDE"),
    ]
    role = "checkbox" if question.get("multi") else "radio"
    cards = []
    for code, left, right in labels:
        cards.append(f"""
      <button type="button" class="sel-option sel-option--region" data-value="{code}"
              role="{role}" aria-checked="false">
        <span class="sel-option__region-code" aria-hidden="true">{code}</span>
        <span class="sel-option__places">
          <span>{left}</span><span class="sel-option__dash" aria-hidden="true">&mdash;</span><span>{right}</span>
        </span>
        <span class="sel-option__prices">
          <span>{strings['SEL_MAP_APT']} {prices[code]['apartment']}</span>
          <span>{strings['SEL_MAP_VILLA']} {prices[code]['villa']}</span>
        </span>
        <span class="sel-option__tick" aria-hidden="true"></span>
      </button>""")

    options = (
        f'<div class="sel-options sel-options--region" '
        f'role="{"group" if question.get("multi") else "radiogroup"}" '
        f'aria-label="{question[lang]["q"]}">{"".join(cards)}\n      </div>'
    )
    return coast + "\n      " + options


def build(lang, prices, project_total):
    strings = i18n.strings_for(lang)
    data = {f"I_{k}": v for k, v in strings.items()}
    data["I_SEL_HERO_PROJECTS"] = data["I_SEL_HERO_PROJECTS"].replace(
        "__PROJECT_TOTAL__", str(project_total)
    )

    steps = []
    for index, question in enumerate(QUESTIONS):
        number = index + 1
        hint = (
            f'<p class="sel-step__hint">{strings["SEL_MULTI_HINT"]}</p>'
            if question.get("multi")
            else ""
        )
        if question.get("region_cards"):
            options_html = render_region_options(question, lang, strings, prices)
        else:
            grid_class = "sel-options"
            if question.get("photos"):
                grid_class += " sel-options--photo"
            options_html = (
                f'<div class="{grid_class}" role="{"group" if question.get("multi") else "radiogroup"}" '
                f'aria-label="{question[lang]["q"]}">\n          {render_options(question, lang)}\n        </div>'
            )
        steps.append(f"""
      <section class="sel-step" data-step="{number}" data-id="{question['id']}"
               data-param="{question.get('param', '')}"
               data-multi="{'1' if question.get('multi') else ''}"
               data-required="{'1' if question.get('required') else ''}"
               hidden>
        <p class="sel-step__count">{strings['SEL_STEP']} {number:02d} <span>{strings['SEL_OF']} {len(QUESTIONS)}</span></p>
        <h2 class="sel-step__q" tabindex="-1">{question[lang]['q']}</h2>
        {hint}
        {options_html}
        <p class="sel-step__error" role="alert" hidden>{strings['SEL_REQUIRED']}</p>
      </section>""")

    data["STEPS"] = "\n".join(steps)
    data["STEP_TOTAL"] = str(len(QUESTIONS))
    data["HERO_IMAGE"] = HERO_IMAGE
    data["PHONE_OPTGROUPS"] = phone_optgroups()
    data["LANG_SWITCH_HREF"] = HREFS["en" if lang == "nl" else "nl"]
    data["SELF_HREF"] = HREFS[lang]
    data["HUB_HREF"] = "/en/" if lang == "en" else "/"
    data["OG_IMAGE"] = HERO_IMAGE

    with open(os.path.join(TEMPLATES, "selectie.html"), encoding="utf-8") as f:
        page = generate.fill(f.read(), data)
    # Tweede pas: sommige i18n-waarden bevatten zelf nog een token.
    page = generate.fill(page, data)

    leftovers = set(re.findall(r"__[A-Z0-9_]+__", page))
    if leftovers:
        raise SystemExit(f"[selectie] ({lang}) Niet-ingevulde tokens: {sorted(leftovers)}")

    out_dir = os.path.join(ROOT, PATHS[lang])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"[selectie] ({lang}) -> {out_path} ({len(page)} chars)")


def main():
    data_path = os.path.join(ROOT, "api", "_projects.json")
    if not os.path.exists(data_path):
        raise SystemExit(
            "api/_projects.json ontbreekt - draai eerst python3 _build/generate_data.py"
        )
    with open(data_path, encoding="utf-8") as f:
        projects = json.load(f)["projects"]
    # Alleen projecten met een vanaf-prijs; api/match.js laat de andere ook
    # weg, dus het getal op het welkomstscherm moet daarbij aansluiten.
    total = sum(1 for p in projects.values() if p.get("price_num"))

    prices = region_prices()
    for lang in ("nl", "en"):
        build(lang, prices, total)


if __name__ == "__main__":
    main()
