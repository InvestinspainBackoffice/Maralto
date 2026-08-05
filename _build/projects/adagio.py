from urllib.parse import quote

PROJECT_NAME = "Adagio"
PRICE_FROM = "Vanaf € 512.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "adagio",
    "TITLE": f"{PROJECT_NAME} Cancelada — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Adagio: appartementen en penthouses met ruime terrassen in Cancelada, New Golden Mile. Vanaf €512.000.",
    "OG_TITLE": f"{PROJECT_NAME} Cancelada — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Adagio: 80 woningen omgeven door golfterreinen op de New Golden Mile, met zwembad, gym en Zen-zone. Vanaf €512.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/04/Adagio-Cancelada-6.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/04/Adagio-Cancelada-6.jpg",
    "HERO_BG_ALT": "Adagio Cancelada — appartementen rond een zwembad met palmbomen",
    "HERO_NAME": "ADAGIO",
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
    "META_DESCRIPTION": "Adagio: apartments and penthouses with spacious terraces in Cancelada, New Golden Mile. From €512,000.",
    "OG_TITLE": f"{PROJECT_NAME} Cancelada — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Adagio: 80 homes surrounded by golf courses on the New Golden Mile, with swimming pool, gym and Zen zone. From €512,000.",
    "HERO_BG_ALT": "Adagio Cancelada — apartments around a swimming pool with palm trees",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Cancelada",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/adagio/thumb.webp",
    "LAT": 36.4651772,
    "LNG": -5.0599806,
    "HREF": "/adagio/",
}
