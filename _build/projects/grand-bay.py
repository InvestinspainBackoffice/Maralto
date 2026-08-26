from urllib.parse import quote

PROJECT_NAME = "Grand Bay"
PRICE_FROM = "Vanaf € 390.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "grand-bay",
    "TITLE": f"{PROJECT_NAME} Manilva — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Grand Bay: appartementen en penthouses met 2 en 3 slaapkamers en panoramisch uitzicht in Bahía de las Rocas, Manilva. Vanaf €390.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Wonen met Panoramisch Uitzicht",
    "OG_DESCRIPTION": "Ontdek Grand Bay: appartementen en penthouses met zeezicht, gemeenschappelijke zwembaden en fitness, tussen Punta Paloma en Sotogrande. Vanaf €390.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/grand-bay/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/grand-bay/hero.webp",
    "HERO_BG_ALT": "Grand Bay — luchtfoto van het complex met zicht op zee en Gibraltar",
    "HERO_NAME": "GRAND BAY",
    "HERO_LOCATION": "MANILVA",
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
    "META_DESCRIPTION": "Grand Bay: apartments and penthouses with 2 and 3 bedrooms and panoramic views in Bahía de las Rocas, Manilva. From €390,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Living with Panoramic Views",
    "OG_DESCRIPTION": "Discover Grand Bay: apartments and penthouses with sea views, communal pools and a gym, between Punta Paloma and Sotogrande. From €390,000.",
    "HERO_BG_ALT": "Grand Bay — aerial view of the complex with sea and Gibraltar views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Manilva",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/grand-bay/hero.webp",
    "LAT": 36.347712,
    "LNG": -5.239791,
    "HREF": "/grand-bay/",
}
