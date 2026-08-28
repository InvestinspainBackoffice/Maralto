from urllib.parse import quote

PROJECT_NAME = "Upper101"
PRICE_FROM = "Vanaf € 320.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "upper101",
    "TITLE": f"{PROJECT_NAME} San Pedro — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Upper101: 101 woningen van studio's tot 4 slaapkamers, met infinity pools en penthouses met privézwembad in San Pedro, Marbella. Vanaf € 320.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in San Pedro",
    "OG_DESCRIPTION": "Upper101: gated community met coworkingruimtes, gym met spa, panoramische daktuinen en 24-uurs beveiliging in San Pedro. Vanaf € 320.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/upper101/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/upper101/hero.webp",
    "HERO_BG_ALT": "Upper101 — modern residentieel project in San Pedro",
    "HERO_NAME": "Upper101",
    "HERO_LOCATION": "SAN PEDRO, MARBELLA",
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
    "META_DESCRIPTION": "Upper101: 101 homes from studios to 4 bedrooms, with infinity pools and penthouses with private pool in San Pedro, Marbella. From € 320,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in San Pedro",
    "OG_DESCRIPTION": "Upper101: gated community with coworking spaces, gym with spa, panoramic roof gardens and 24-hour security in San Pedro. From € 320,000.",
    "HERO_BG_ALT": "Upper101 — modern residential project in San Pedro",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/upper101/hero.webp",
    "LAT": 36.488832,
    "LNG": -4.985757,
    "HREF": "/upper101/",
}
