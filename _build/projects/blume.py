from urllib.parse import quote

PROJECT_NAME = "Blume"
PRICE_FROM = "Vanaf € 4.290.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "blume",
    "TITLE": f"{PROJECT_NAME} San Pedro — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Blume: exclusieve luxevilla's met 4 slaapkamers en 5 badkamers in Cortijo Blanco, San Pedro de Alcántara. Vanaf €4.290.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxevilla's in Cortijo Blanco",
    "OG_DESCRIPTION": "Ontdek Blume: hoogwaardige villa's met privézwembad, domotica en vloerverwarming, op wandelafstand van het strand en vlak bij Puerto Banús. Vanaf €4.290.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/blume/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/blume/hero.webp",
    "HERO_BG_ALT": "Blume — moderne villa met privézwembad en tuin",
    "HERO_NAME": "BLUME",
    "HERO_LOCATION": "SAN PEDRO",
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
    "META_DESCRIPTION": "Blume: exclusive luxury villas with 4 bedrooms and 5 bathrooms in Cortijo Blanco, San Pedro de Alcántara. From €4,290,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Villas in Cortijo Blanco",
    "OG_DESCRIPTION": "Discover Blume: premium villas with a private pool, home automation and underfloor heating, within walking distance of the beach and close to Puerto Banús. From €4,290,000.",
    "HERO_BG_ALT": "Blume — modern villa with private pool and garden",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/blume/hero.webp",
    "LAT": 36.486461,
    "LNG": -4.991505,
    "HREF": "/blume/",
}
