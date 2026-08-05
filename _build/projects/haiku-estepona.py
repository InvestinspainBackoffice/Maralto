from urllib.parse import quote

PROJECT_NAME = "Haiku Estepona"
PRICE_FROM = "Vanaf € 500.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "haiku-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Haiku Estepona: 36 appartementen (Haiku Suites) en 15 townhouses (Haiku Residences) in Cancelada, New Golden Mile. Panoramisch zeezicht. Vanaf €500.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Townhouses",
    "OG_DESCRIPTION": "Ontdek Haiku Estepona: gemeenschappelijk zwembad, gedeelde tuinen, lounge, spa en fitness in de exclusieve wijk Cancelada, New Golden Mile. Vanaf €500.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/04/Haiku-Estepona-Image-2025-08-11-at-16.24.34-1.jpeg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/04/Haiku-Estepona-Image-2025-08-11-at-16.24.34-1.jpeg",
    "HERO_BG_ALT": "Haiku Estepona — zwembad tussen de gebouwen",
    "HERO_NAME": "HAIKU ESTEPONA",
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
    "META_DESCRIPTION": "Haiku Estepona: 36 apartments (Haiku Suites) and 15 townhouses (Haiku Residences) in Cancelada, New Golden Mile. Panoramic sea views. From €500,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Townhouses",
    "OG_DESCRIPTION": "Discover Haiku Estepona: communal swimming pool, shared gardens, lounge, spa and fitness in the exclusive Cancelada neighbourhood, New Golden Mile. From €500,000.",
    "HERO_BG_ALT": "Haiku Estepona — swimming pool between the buildings",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/haiku-estepona/thumb.webp",
    "LAT": 36.466856444687,
    "LNG": -5.0597456901361,
    "HREF": "/haiku-estepona/",
}
