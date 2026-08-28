from urllib.parse import quote

PROJECT_NAME = "Santa Clara Homes"
PRICE_FROM = "Vanaf € 1.345.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "santa-clara-homes",
    "TITLE": f"{PROJECT_NAME} Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Santa Clara Homes: 104 luxueuze appartementen en penthouses met privézwembad, naast een golfbaan en op wandelafstand van het strand in Marbella. Vanaf €1.345.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Santa Clara Homes: low density wonen met privézwembad, gym & spa, naast de golfbaan en vlakbij het strand van Los Monteros in Marbella. Vanaf €1.345.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2023/05/santa-clara-galeria-7-min.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2023/05/santa-clara-galeria-7-min.jpg",
    "HERO_BG_ALT": "Santa Clara Homes — zwembad tussen de gebouwen met bergzicht",
    "HERO_NAME": "SANTA CLARA HOMES",
    "HERO_LOCATION": "MARBELLA",
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
    "META_DESCRIPTION": "Santa Clara Homes: 104 luxurious apartments and penthouses with private pool, next to a golf course and within walking distance of the beach in Marbella. From €1.345.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Santa Clara Homes: low-density living with private pool, gym & spa, next to the golf course and close to Los Monteros beach in Marbella. From €1.345.000.",
    "HERO_BG_ALT": "Santa Clara Homes — swimming pool between the buildings with mountain views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/santa-clara-homes/thumb.webp",
    "LAT": 36.510965,
    "LNG": -4.832622,
    "HREF": "/santa-clara-homes/",
}
