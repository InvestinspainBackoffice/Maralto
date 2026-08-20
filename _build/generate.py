"""
Bouwt <slug>/index.html (NL) en en/<slug>/index.html (EN) voor elk project
in _build/projects/*.py, door head.html + hero.html + het handgeschreven
body-fragment + tail.html samen te voegen en de __TOKEN__-placeholders in
te vullen.

Gebruik:  python3 _build/generate.py            (alle projecten, beide talen)
          python3 _build/generate.py adagio      (één project, beide talen)
"""
import importlib.util
import json
import os
import re
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "_build", "templates")
PROJECTS_DIR = os.path.join(ROOT, "_build", "projects")

LANGUAGES = ["nl", "en"]

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
    ("600k-1m", 600_000, 1_000_000),
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


def build_one(project_file, lang):
    mod = load_module(project_file)
    if not hasattr(mod, "DATA"):
        return  # projectbestand zonder eigen pagina (alleen een HUB-vermelding)
    data = dict(mod.DATA)
    slug = data["SLUG"]

    if lang == "en":
        # Automatische vertaling van de vanaf-prijs (komt in meerdere velden
        # voor: PRICE_FROM, HERO_PRICE, vaak ook in de meta/OG-omschrijving).
        # Projecten met een echte Engelse tekst per veld (DATA_EN) overriden
        # dit hieronder gewoon weer.
        for key, value in list(data.items()):
            if isinstance(value, str) and "Vanaf €" in value:
                data[key] = value.replace("Vanaf €", "From €")
        # Bijna elk project gebruikt exact hetzelfde WA-bericht-sjabloon;
        # dat vertalen we automatisch zodat niet elk project apart een
        # DATA_EN["WA_MESSAGE"] nodig heeft. Projecten met een afwijkend
        # bericht (bv. Maralto) zetten dat gewoon zelf in DATA_EN.
        wa_match = re.match(
            r"^Hallo, ik heb interesse in (.+)\. Kan ik meer informatie ontvangen\?$",
            data.get("WA_MESSAGE", ""),
        )
        if wa_match:
            data["WA_MESSAGE"] = f"Hello, I'm interested in {wa_match.group(1)}. Could I receive more information?"
        if hasattr(mod, "DATA_EN"):
            data.update(mod.DATA_EN)
        if "WA_MESSAGE" in data:
            data["WA_TEXT_ENCODED"] = quote(data["WA_MESSAGE"])

    # De sticky-cta bar heeft alleen het bedrag nodig (zonder "Vanaf "-prefix).
    # Projecten zonder vaste prijs ("Prijs op aanvraag") zetten PRICE_LABEL
    # en PRICE_AMOUNT expliciet in hun eigen DATA-dict, zodat de tekst er
    # klopt in plaats van de standaard "Vanaf "-prefix te forceren.
    price_prefix = "Vanaf " if lang == "nl" else "From "
    data.setdefault("PRICE_AMOUNT", data["PRICE_FROM"].replace(price_prefix, ""))
    data.setdefault("PRICE_LABEL", "Vanaf" if lang == "nl" else "From")
    data.setdefault("BUDGET_BUCKET", budget_bucket(parse_price_number(data["PRICE_FROM"])))
    # Verticale ankerpositie van de hero-achtergrond (CSS background-position).
    # Projecten met een storende watermerk-tekst onderaan hun herofoto zetten
    # dit expliciet naar "top" om die tekst buiten beeld te croppen.
    data.setdefault("HERO_BG_POSITION", "60%")
    # Kleine per-project CSS-overrides (bv. watermerk uit een herofoto croppen)
    # die niet elk project aangaan, dus niet in de gedeelde stylesheet horen.
    data.setdefault("EXTRA_HEAD_CSS", "")

    # fill() is een kale str.replace() zonder enig besef van HTML- vs.
    # JS-context. __PROJECT_NAME__ wordt in tail.html ook rechtstreeks in een
    # JS-stringliteral geplakt (project_name: '__PROJECT_NAME__') - een
    # projectnaam met een apostrof (Lantana Villa's, Alexandra's Dream, ...)
    # sluit die string dan vroegtijdig af en breekt het hele scriptblok
    # (formulier, scroll-animaties, alles). json.dumps() escaped dat correct;
    # het token in tail.html gebruikt deze WEL-gequote variant, dus zonder
    # eigen '...' eromheen.
    data["PROJECT_NAME_JS"] = json.dumps(data["PROJECT_NAME"])

    # Vaste UI-teksten (labels, knoppen, foutmeldingen) per taal - één
    # aanpassing in _build/i18n.py of in de gedeelde templates geldt
    # automatisch voor zowel de NL- als de EN-versie van elke pagina.
    for key, value in i18n.strings_for(lang).items():
        data[f"I_{key}"] = value

    # Taalwissel-link: verwijst naar dezelfde pagina in de andere taal.
    data["LANG_SWITCH_HREF"] = f"/{slug}/" if lang == "en" else f"/en/{slug}/"
    # Waar het leadformulier na een geslaagde inzending naartoe stuurt.
    data["THANKS_HREF"] = "/en/thank-you/" if lang == "en" else "/bedankt/"

    with open(os.path.join(TEMPLATES, "head.html"), encoding="utf-8") as f:
        head = f.read()
    # Gebruik hero_video.html als HERO_VIDEO_ID is opgegeven, anders hero.html.
    hero_tpl = "hero_video.html" if data.get("HERO_VIDEO_ID") else "hero.html"
    with open(os.path.join(TEMPLATES, hero_tpl), encoding="utf-8") as f:
        hero = f.read()
    with open(os.path.join(TEMPLATES, "tail.html"), encoding="utf-8") as f:
        tail = f.read()

    body_suffix = "_body.html" if lang == "nl" else "_body_en.html"
    body_path = os.path.join(PROJECTS_DIR, f"{slug}{body_suffix}")
    if lang == "en" and not os.path.exists(body_path):
        print(f"[{slug}] (en) overgeslagen: {slug}_body_en.html bestaat nog niet")
        return
    with open(body_path, encoding="utf-8") as f:
        body = f.read()

    page = fill(head, data) + fill(hero, data) + body + fill(tail, data)
    # Tweede pas: sommige data-waarden (bv. I_MODAL_INTRO) bevatten zelf nog
    # een __TOKEN__ (__PROJECT_NAME__) - die is pas na de eerste pas ontstaan.
    page = fill(page, data)

    leftovers = set(re.findall(r"__[A-Z0-9_]+__", page))
    if leftovers:
        raise SystemExit(f"[{slug}] ({lang}) Niet-ingevulde tokens: {sorted(leftovers)}")

    # De projectenpagina (hub) leeft op de root van de site ("/"); elk
    # project, inclusief Maralto, krijgt zijn eigen submap. De Engelse
    # versie spiegelt dezelfde structuur onder /en/.
    out_dir = os.path.join(ROOT, "en", slug) if lang == "en" else os.path.join(ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"[{slug}] ({lang}) -> {out_path} ({len(page)} chars)")


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    files = sorted(f for f in os.listdir(PROJECTS_DIR) if f.endswith(".py"))
    if only:
        files = [f for f in files if f == f"{only}.py"]
        if not files:
            raise SystemExit(f"Geen project-databestand gevonden voor '{only}'")
    for f in files:
        for lang in LANGUAGES:
            build_one(os.path.join(PROJECTS_DIR, f), lang)


if __name__ == "__main__":
    main()
