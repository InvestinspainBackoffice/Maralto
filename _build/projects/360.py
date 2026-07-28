from urllib.parse import quote

PROJECT_NAME = "360°"
PRICE_FROM = "Vanaf € 400.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "360",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "360°: 71 stijlvolle appartementen op een heuveltop in Mijas, naast Cerrado del Águila Golf. Vanaf €400.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek 360°: wellnesszone met sauna en hammam, gastrobar, gamingruimte en panoramisch zeezicht in Mijas. Vanaf €400.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/08/360-20.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/08/360-20.jpg",
    "HERO_BG_ALT": "360° — wooncomplex met zwembad bij avondlicht",
    "HERO_NAME": "360°",
    "HERO_LOCATION": "MIJAS",
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

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2025/08/360-20.jpg",
    "LAT": 36.5269758,
    "LNG": -4.6646297,
    "HREF": "/360/",
}
