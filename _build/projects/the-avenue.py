from urllib.parse import quote

PROJECT_NAME = "The Avenue"
PRICE_FROM = "Vanaf € 4.450.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-avenue",
    "TITLE": f"{PROJECT_NAME} Nueva Andalucía — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Avenue: 26 luxe villa's in 3 typologieën met privézwembad, domotica en panoramisch berg- en zeezicht in Nueva Andalucía. Vanaf € 4.450.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's in Nueva Andalucía",
    "OG_DESCRIPTION": "26 luxe villa's met privézwembad, domotica en panoramisch uitzicht in Nueva Andalucía.",
    "OG_IMAGE": "https://projects.investinspain.be/images/the-avenue/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/the-avenue/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villa's in Nueva Andalucía",
    "HERO_NAME": "The Avenue",
    "HERO_LOCATION": "NUEVA ANDALUCÍA",
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
    "META_DESCRIPTION": "The Avenue: 26 luxury villas in 3 typologies with private pool, home automation and panoramic mountain & sea views in Nueva Andalucía. From € 4,450,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas in Nueva Andalucía",
    "OG_DESCRIPTION": "26 luxury villas with private pool, home automation and panoramic views in Nueva Andalucía.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villas in Nueva Andalucía",
}

HUB = {
    "NAME": "The Avenue",
    "LOCATION": "Nueva Andalucía",
    "PRICE": "Vanaf € 4.450.000",
    "THUMB": "https://projects.investinspain.be/images/the-avenue/hero.webp",
    "LAT": 36.498734,
    "LNG": -4.968133,
    "HREF": "/the-avenue/",
}
