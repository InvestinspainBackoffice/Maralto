from urllib.parse import quote

PROJECT_NAME = "Spinto Hills"
PRICE_FROM = "Vanaf € 2.150.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "spinto-hills",
    "TITLE": f"{PROJECT_NAME} ESTEPONA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Spinto Hills Estepona: exclusieve villa's met premium afwerking en panoramisch uitzicht in de heuvels van Estepona. Vanaf € 2.150.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve villa's in de heuvels van Estepona",
    "OG_DESCRIPTION": "Spinto Hills biedt exclusieve villa's met premium afwerking en panoramisch uitzicht in de heuvels van Estepona.",
    "OG_IMAGE": "https://projects.investinspain.be/images/spinto-hills/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/spinto-hills/hero.webp",
    "HERO_BG_ALT": "Spinto Hills — exclusieve villa's met panoramisch uitzicht in Estepona",
    "HERO_NAME": "Spinto Hills",
    "HERO_LOCATION": "ESTEPONA",
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
    "META_DESCRIPTION": "Spinto Hills Estepona: exclusive villas with premium finishes and panoramic views in the hills of Estepona. From € 2,150,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive villas in the hills of Estepona",
    "OG_DESCRIPTION": "Spinto Hills offers exclusive villas with premium finishes and panoramic views in the hills of Estepona.",
    "HERO_BG_ALT": "Spinto Hills — exclusive villas with panoramic views in Estepona",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/spinto-hills/hero.webp",
    "LAT": 36.396847,
    "LNG": -5.21533,
    "HREF": "/spinto-hills/",
}
