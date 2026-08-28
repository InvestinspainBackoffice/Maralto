from urllib.parse import quote

PROJECT_NAME = "Aires del Mar"
PRICE_FROM = "Vanaf € 611.751"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "aires-del-mar",
    "TITLE": f"{PROJECT_NAME} ESTEPONA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Aires del Mar Estepona: 28 exclusieve residenties met 1-4 slaapkamers, ruime terrassen en aerothermische installatie in een afgesloten community. Vanaf € 611.751.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve residenties in Estepona",
    "OG_DESCRIPTION": "28 stijlvolle residenties met ruime terrassen, hoogwaardige materialen en energiezuinige aerothermische installatie in een afgesloten community in Estepona.",
    "OG_IMAGE": "https://projects.investinspain.be/images/aires-del-mar/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/aires-del-mar/hero.webp",
    "HERO_BG_ALT": "Aires del Mar — modern appartementencomplex in Estepona",
    "HERO_NAME": "Aires del Mar",
    "HERO_LOCATION": "ESTEPONA",
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
    "META_DESCRIPTION": "Aires del Mar Estepona: 28 exclusive residences with 1-4 bedrooms, spacious terraces and aerothermal system in a gated community. From € 611,751.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive residences in Estepona",
    "OG_DESCRIPTION": "28 stylish residences with spacious terraces, high-quality materials and energy-efficient aerothermal system in a gated community in Estepona.",
    "HERO_BG_ALT": "Aires del Mar — modern apartment complex in Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/aires-del-mar/hero.webp",
    "LAT": 36.434135,
    "LNG": -5.145979,
    "HREF": "/aires-del-mar/",
}
