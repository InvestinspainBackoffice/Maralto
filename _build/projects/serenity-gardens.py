from urllib.parse import quote

PROJECT_NAME = "Serenity Gardens"
PRICE_FROM = "Vanaf € 405.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "serenity-gardens",
    "TITLE": f"{PROJECT_NAME} ESTEPONA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Serenity Gardens Estepona: rustige appartementen met ruime terrassen en groene omgeving. Op korte afstand van het strand en Estepona centrum. Vanaf € 405.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Rustige appartementen met terras in Estepona",
    "OG_DESCRIPTION": "Serenity Gardens combineert rust en groen met moderne appartementen en ruime terrassen, op korte afstand van het strand in Estepona.",
    "OG_IMAGE": "https://projects.investinspain.be/images/serenity-gardens/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/serenity-gardens/hero.webp",
    "HERO_BG_ALT": "Serenity Gardens — modern appartementencomplex in Estepona",
    "HERO_NAME": "Serenity Gardens",
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
    "META_DESCRIPTION": "Serenity Gardens Estepona: peaceful apartments with spacious terraces and green surroundings. Short distance to the beach and Estepona centre. From € 405,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Peaceful apartments with terrace in Estepona",
    "OG_DESCRIPTION": "Serenity Gardens combines tranquility and greenery with modern apartments and spacious terraces, a short distance from the beach in Estepona.",
    "HERO_BG_ALT": "Serenity Gardens — modern apartment complex in Estepona",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/serenity-gardens/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/serenity-gardens/",
}
