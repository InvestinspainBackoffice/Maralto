from urllib.parse import quote

PROJECT_NAME = "La Quinta de Cerrado"
PRICE_FROM = "Vanaf € 975.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "la-quinta-de-cerrado",
    "TITLE": f"{PROJECT_NAME} La Cala de Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "La Quinta de Cerrado – luxe nieuwbouwvilla's op een gated domein in La Cala de Mijas, Costa del Sol. Privézwembad, zeezicht, golfbanen nabij. Vanaf € 975.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxe villa's La Cala de Mijas · INVESTINSPAIN.BE",
    "OG_DESCRIPTION": "Exclusieve villa's op een beveiligd domein in La Cala de Mijas, Costa del Sol. Privézwembad en uitzicht op zee en golf. Vraag brochure aan bij INVESTINSPAIN.",
    "OG_IMAGE": "https://projects.investinspain.be/images/la-quinta-de-cerrado/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/la-quinta-de-cerrado/hero.webp",
    "HERO_BG_ALT": "La Quinta de Cerrado luxe nieuwbouwvilla exterieur La Cala de Mijas Costa del Sol",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "LA CALA DE MIJAS, COSTA DEL SOL",
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
    "MAP_LAT": "36.526841485455",
    "MAP_LNG": "-4.6634318305033",
}

DATA_EN = {
    "META_DESCRIPTION": "La Quinta de Cerrado – luxury new-build villas on a gated estate in La Cala de Mijas, Costa del Sol. Private pool, sea views, golf courses nearby. From € 975,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxury villas La Cala de Mijas · INVESTINSPAIN.BE",
    "OG_DESCRIPTION": "Exclusive villas on a gated estate in La Cala de Mijas, Costa del Sol. Private pool and views of the sea and golf. Request the brochure at INVESTINSPAIN.",
    "HERO_BG_ALT": "La Quinta de Cerrado luxury new-build villa exterior La Cala de Mijas Costa del Sol",
}
