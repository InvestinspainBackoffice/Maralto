from urllib.parse import quote

PROJECT_NAME = "Calanova Homes"
PRICE_FROM = "Vanaf € 1.035.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "calanova-homes",
    "TITLE": f"{PROJECT_NAME} Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Calanova Homes: luxueuze villa's op de golfbaan van Calanova in Mijas Costa. Privézwembad, zeezicht en directe toegang tot de fairway. Vanaf €1.035.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Golfvilla's in Mijas Costa",
    "OG_DESCRIPTION": "Ontdek Calanova Homes: stijlvolle villa's op de Calanova golfbaan in Mijas Costa met privézwembad, zeezicht en directe toegang tot de fairway. Luxe en natuur in harmonie. Vanaf €1.035.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/calanova-homes/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/calanova-homes/hero.webp",
    "HERO_BG_ALT": "Calanova Homes — luxueuze golfvilla met zeezicht in Mijas Costa",
    "HERO_NAME": "CALANOVA HOMES",
    "HERO_LOCATION": "MIJAS COSTA",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "WA_TEXT_ENCODED": quote(WA_MESSAGE),
    "PROJECT_NAME": PROJECT_NAME,
    "AGENT_NAME": "Gunther De Vleeschouwer",
    "AGENT_PHOTO": "https://investinspain.be/wp-content/uploads/2020/01/Gunther-De-Vleeschouwer-INVESTINSPAIN.jpg",
    "AGENT_PHONE_TEL": "+32496571397",
    "AGENT_PHONE_DISPLAY": "+32 496 57 13 97",
    "AGENT_EMAIL": "gunther@investinspain.be",
    "WA_NUMBER": "32496571397",
}

DATA_EN = {
    "META_DESCRIPTION": "Calanova Homes: luxury villas on the Calanova golf course in Mijas Costa. Private pool, sea views and direct access to the fairway. From €1,035,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Golf Villas in Mijas Costa",
    "OG_DESCRIPTION": "Discover Calanova Homes: stylish villas on the Calanova golf course in Mijas Costa with private pool, sea views and direct fairway access. Luxury and nature in harmony. From €1,035,000.",
    "HERO_BG_ALT": "Calanova Homes — luxury golf villa with sea views in Mijas Costa",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas Costa",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/calanova-homes/hero.webp",
    "LAT": 36.513634,
    "LNG": -4.718017,
    "HREF": "/calanova-homes/",
}
