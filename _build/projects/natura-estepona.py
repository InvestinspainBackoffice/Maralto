from urllib.parse import quote

PROJECT_NAME = "Natura Estepona"
PRICE_FROM = "Vanaf € 525.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "natura-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Natura Estepona: moderne appartementen omgeven door natuur in Estepona. Gedeeld zwembad, tuinen en uitstekende ligging nabij strand en golf. Vanaf €525.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Natuur & Comfort in Estepona",
    "OG_DESCRIPTION": "Ontdek Natura Estepona: eigentijdse appartementen in een groene, rustige omgeving in Estepona. Gedeeld zwembad, aangelegde tuinen en nabijheid van strand en golf. Vanaf €525.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/natura-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/natura-estepona/hero.webp",
    "HERO_BG_ALT": "Natura Estepona — moderne appartementen in groene omgeving in Estepona",
    "HERO_NAME": "NATURA ESTEPONA",
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
    "META_DESCRIPTION": "Natura Estepona: modern apartments surrounded by nature in Estepona. Shared pool, gardens and excellent location near beach and golf. From €525,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Nature & Comfort in Estepona",
    "OG_DESCRIPTION": "Discover Natura Estepona: contemporary apartments in a green, peaceful setting in Estepona. Shared pool, landscaped gardens and proximity to beach and golf. From €525,000.",
    "HERO_BG_ALT": "Natura Estepona — modern apartments in green surroundings in Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/natura-estepona/hero.webp",
    "LAT": 36.407649,
    "LNG": -5.190943,
    "HREF": "/natura-estepona/",
}
