from urllib.parse import quote

PROJECT_NAME = "Almare"
PRICE_FROM = "Vanaf € 582.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "almare",
    "TITLE": f"{PROJECT_NAME} La Cala de Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Almare: 48 appartementen en penthouses met 2, 3 en 4 slaapkamers en panoramisch zeezicht in La Cala de Mijas. Vanaf €582.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met Panoramisch Zeezicht",
    "OG_DESCRIPTION": "Ontdek Almare: 48 hedendaagse appartementen en penthouses met ruime terrassen, gemeenschappelijk zwembad en fitness in La Cala de Mijas. Vanaf €582.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/almare/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/almare/hero.webp",
    "HERO_BG_ALT": "Almare — gebouw met panoramisch zicht op zee",
    "HERO_NAME": "ALMARE",
    "HERO_LOCATION": "LA CALA DE MIJAS",
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
    "META_DESCRIPTION": "Almare: 48 apartments and penthouses with 2, 3 and 4 bedrooms and panoramic sea views in La Cala de Mijas. From €582,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with Panoramic Sea Views",
    "OG_DESCRIPTION": "Discover Almare: 48 contemporary apartments and penthouses with spacious terraces, a communal pool and a gym in La Cala de Mijas. From €582,000.",
    "HERO_BG_ALT": "Almare — building with panoramic sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Cala de Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/almare/hero.webp",
    "LAT": 36.511869,
    "LNG": -4.679016,
    "HREF": "/almare/",
}
