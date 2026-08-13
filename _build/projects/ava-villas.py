from urllib.parse import quote

PROJECT_NAME = "AVA Villas"
PRICE_FROM = "Uitverkocht"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "ava-villas",
    "TITLE": f"{PROJECT_NAME} San Pedro de Alcántara — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "AVA Villas: 5 exclusieve villa's met 5 slaapkamers en zoutwaterzwembad in Altavista, San Pedro de Alcántara. Uitverkocht.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's in San Pedro de Alcántara",
    "OG_DESCRIPTION": "5 exclusieve villa's met 5 slaapkamers en zoutwaterzwembad in Altavista, San Pedro.",
    "OG_IMAGE": "https://projects.investinspain.be/images/ava-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/ava-villas/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villa's in San Pedro de Alcántara",
    "HERO_NAME": "AVA Villas",
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
    "META_DESCRIPTION": "AVA Villas: 5 exclusive villas with 5 bedrooms and saltwater pool in Altavista, San Pedro de Alcántara. Sold out.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas in San Pedro de Alcántara",
    "OG_DESCRIPTION": "5 exclusive villas with 5 bedrooms and saltwater pool in Altavista, San Pedro.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villas in San Pedro de Alcántara",
}

HUB = {
    "NAME": "AVA Villas",
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": "Uitverkocht",
    "THUMB": "https://projects.investinspain.be/images/ava-villas/hero.webp",
    "LAT": 36.486999,
    "LNG": -4.998686,
    "HREF": "/ava-villas/",
}
