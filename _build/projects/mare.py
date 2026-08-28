from urllib.parse import quote

PROJECT_NAME = "MARE"
PRICE_FROM = "Vanaf € 720.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "mare",
    "TITLE": f"{PROJECT_NAME} San Pedro de Alcántara — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "MARE: moderne appartementen met zeezicht nabij Puerto Banús en San Pedro de Alcántara. Ruime terrassen, communale zwembaden en topligging aan de Costa del Sol. Vanaf € 720.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen met zeezicht, San Pedro de Alcántara",
    "OG_DESCRIPTION": "MARE nabij Puerto Banús: eigentijdse appartementen met zeezicht, ruime terrassen en communale faciliteiten. Topligging aan de Costa del Sol. Vanaf € 720.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/mare/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/mare/hero.webp",
    "HERO_BG_ALT": "Appartementen MARE met zeezicht San Pedro de Alcántara",
    "HERO_NAME": "MARE",
    "HERO_LOCATION": "SAN PEDRO DE ALCÁNTARA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "MARE: modern apartments with sea views near Puerto Banús and San Pedro de Alcántara. Spacious terraces, communal pools and a prime location on the Costa del Sol. From € 720,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments with sea views, San Pedro de Alcántara",
    "OG_DESCRIPTION": "MARE near Puerto Banús: contemporary apartments with sea views, spacious terraces and communal amenities. Prime Costa del Sol location. From € 720,000.",
    "HERO_BG_ALT": "MARE apartments with sea views San Pedro de Alcántara",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/mare/hero.webp",
    "LAT": 36.480234,
    "LNG": -4.989064,
    "HREF": "/mare/",
}
