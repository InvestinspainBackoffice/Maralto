from urllib.parse import quote

PROJECT_NAME = "Aire"
PRICE_FROM = "Vanaf € 472.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "aire",
    "TITLE": f"{PROJECT_NAME} Cancelada — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Aire: luchtige moderne appartementen in Cancelada op de New Golden Mile. Gedeeld zwembad, zeezicht en ideale ligging tussen Estepona en Marbella. Vanaf €472.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne Appartementen in Cancelada",
    "OG_DESCRIPTION": "Ontdek Aire: eigentijdse appartementen in Cancelada met gedeeld zwembad, zeezicht en een sfeervolle avondatmosfeer. Op de New Golden Mile tussen Estepona en Marbella. Vanaf €472.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/aire/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/aire/hero.webp",
    "HERO_BG_ALT": "Aire — moderne appartementen met zeezicht in Cancelada",
    "HERO_NAME": "AIRE",
    "HERO_LOCATION": "CANCELADA",
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
    "META_DESCRIPTION": "Aire: airy modern apartments in Cancelada on the New Golden Mile. Shared pool, sea views and ideal location between Estepona and Marbella. From €472,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Apartments in Cancelada",
    "OG_DESCRIPTION": "Discover Aire: contemporary apartments in Cancelada with shared pool, sea views and a beautiful sunset atmosphere. On the New Golden Mile between Estepona and Marbella. From €472,000.",
    "HERO_BG_ALT": "Aire — modern apartments with sea views in Cancelada",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Cancelada",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/aire/hero.webp",
    "LAT": 36.4643,
    "LNG": -5.06031,
    "HREF": "/aire/",
}
