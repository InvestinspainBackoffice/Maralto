from urllib.parse import quote

PROJECT_NAME = "Breeze Marbella"
PRICE_FROM = "Vanaf € 870.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "breeze-marbella",
    "TITLE": f"{PROJECT_NAME} San Pedro de Alcántara — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Breeze Marbella: 34 appartementen en penthouses 2-3-4 slaapkamers boven Guadalmina Golf, San Pedro de Alcántara. Co-working, fitness, golfzicht, zeezicht. Vanaf € 870.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 34 woningen boven Guadalmina Golf San Pedro",
    "OG_DESCRIPTION": "34 appartementen en penthouses 2-3-4 slaapkamers boven Guadalmina Golf in San Pedro de Alcántara. Co-working, fitness, panoramisch golf- en zeezicht. Vanaf € 870.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/breeze-marbella/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/breeze-marbella/hero.webp",
    "HERO_BG_ALT": "Breeze Marbella appartementen golfzicht San Pedro de Alcántara",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "SAN PEDRO DE ALCÁNTARA, MARBELLA",
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
    "MAP_LAT": "36.479392344408",
    "MAP_LNG": "-4.999166808621",
}

DATA_EN = {
    "META_DESCRIPTION": "Breeze Marbella: 34 apartments and penthouses 2-3-4 bedrooms above Guadalmina Golf, San Pedro de Alcántara. Co-working, fitness, golf and sea views. From € 870,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 34 homes above Guadalmina Golf San Pedro",
    "OG_DESCRIPTION": "34 apartments and penthouses 2-3-4 bedrooms above Guadalmina Golf in San Pedro de Alcántara. Co-working, fitness, panoramic golf and sea views. From € 870,000.",
    "HERO_BG_ALT": "Breeze Marbella apartments golf views San Pedro de Alcántara",
}
