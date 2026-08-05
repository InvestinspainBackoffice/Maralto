from urllib.parse import quote

PROJECT_NAME = "Salvia"
PRICE_FROM = "Vanaf € 880.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "salvia",
    "TITLE": f"{PROJECT_NAME} San Pedro de Alcántara — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Salvia: exclusief appartementencomplex met 2 tot 4 slaapkamers in San Pedro de Alcántara, op wandelafstand van de boulevard. Vanaf €880.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Salvia: ruime terrassen met zuidelijk zeezicht en noordelijk bergzicht, verwarmd binnenzwembad en co-working, in San Pedro de Alcántara. Vanaf €880.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2023/09/05-SALVIA-Marbella-ABU-NVOGA-Penthouse-min-min.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2023/09/05-SALVIA-Marbella-ABU-NVOGA-Penthouse-min-min.jpg",
    "HERO_BG_ALT": "Salvia — penthouse terras met uitzicht op zee",
    "HERO_NAME": "SALVIA",
    "HERO_LOCATION": "SAN PEDRO DE ALCÁNTARA",
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
    "META_DESCRIPTION": "Salvia: exclusive apartment complex with 2 to 4 bedrooms in San Pedro de Alcántara, within walking distance of the boulevard. From €880.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Salvia: spacious terraces with southern sea views and northern mountain views, a heated indoor pool and co-working, in San Pedro de Alcántara. From €880.000.",
    "HERO_BG_ALT": "Salvia — penthouse terrace with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/salvia/thumb.webp",
    "LAT": 36.480207272882,
    "LNG": -4.9903263749755,
    "HREF": "/salvia/",
}
