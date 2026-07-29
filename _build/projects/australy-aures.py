from urllib.parse import quote

PROJECT_NAME = "Australy Aures"
PRICE_FROM = "Vanaf € 688.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "australy-aures",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Australy Aures: appartementen en penthouses met 2, 3 of 4 slaapkamers in Estepona. Gemeenschappelijk zwembad, spa, sauna en social club. Vanaf €688.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Australy Aures: ruime woningen met tuin of terras, omringd door natuur, vlakbij Estepona. Vanaf €688.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2023/08/AURES-EXTERIOR-3-min.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2023/08/AURES-EXTERIOR-3-min.jpg",
    "HERO_BG_ALT": "Australy Aures — luchtfoto van het complex met zicht op zee",
    "HERO_NAME": "AUSTRALY AURES",
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
    "META_DESCRIPTION": "Australy Aures: apartments and penthouses with 2, 3 or 4 bedrooms in Estepona. Communal swimming pool, spa, sauna and social club. From €688,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Australy Aures: spacious homes with garden or terrace, surrounded by nature, close to Estepona. From €688,000.",
    "HERO_BG_ALT": "Australy Aures — aerial view of the complex with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2023/08/AURES-EXTERIOR-3-min.jpg",
    "LAT": 36.46162316773,
    "LNG": -5.0828572014322,
    "HREF": "/australy-aures/",
}
