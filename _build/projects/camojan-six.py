from urllib.parse import quote

PROJECT_NAME = "Camojan Six"
PRICE_FROM = "Vanaf € 5.650.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "camojan-six",
    "TITLE": f"{PROJECT_NAME} Golden Mile Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Camojan Six: zes exclusieve villa's op het hoogste punt van Cascada de Camojan, in het hart van de Golden Mile. Berg- en zeezicht, gated community, 24/7 beveiliging. Vanaf € 5.650.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Zes exclusieve villa's in Cascada de Camojan, Golden Mile Marbella",
    "OG_DESCRIPTION": "Camojan Six in Marbella: zes luxueuze villa's op het hoogste punt van de gated community Cascada de Camojan. Panoramisch berg- en zeezicht, privézwembad, gym, 24/7 bewaking en volledig omgeven door natuur. Vanaf € 5.650.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/camojan-six/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/camojan-six/hero.webp",
    "HERO_BG_ALT": "Camojan Six Marbella villa solarium Golden Mile",
    "HERO_NAME": "Camojan Six",
    "HERO_LOCATION": "GOLDEN MILE, MARBELLA",
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
    "META_DESCRIPTION": "Camojan Six: six exclusive villas at the highest point of Cascada de Camojan, in the heart of the Golden Mile. Mountain and sea views, gated community, 24/7 security. From € 5,650,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Six exclusive villas in Cascada de Camojan, Golden Mile Marbella",
    "OG_DESCRIPTION": "Camojan Six in Marbella: six luxurious villas at the highest point of the gated community Cascada de Camojan. Panoramic mountain and sea views, private pool, gym, 24/7 security and fully surrounded by nature. From € 5,650,000.",
    "HERO_BG_ALT": "Camojan Six Marbella villa solarium Golden Mile",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Golden Mile, Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/camojan-six/hero.webp",
    "LAT": 36.529306,
    "LNG": -4.906508,
    "HREF": "/camojan-six/",
}
