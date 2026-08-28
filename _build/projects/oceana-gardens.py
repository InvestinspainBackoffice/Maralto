from urllib.parse import quote

PROJECT_NAME = "Oceana Gardens"
PRICE_FROM = "Vanaf € 480.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "oceana-gardens",
    "TITLE": f"{PROJECT_NAME} Cancelada — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Oceana Gardens: gelijkvloers appartement 3 slaapkamers op de New Golden Mile in Cancelada. Privéterras, gemeenschapszwembad en parking. Vanaf €480.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Appartement op de New Golden Mile",
    "OG_DESCRIPTION": "Ontdek Oceana Gardens: eigentijds gelijkvloers appartement in Cancelada (New Golden Mile) met 3 slaapkamers, privéterras, gedeeld zwembad en parking. Nabij golf en strand. Vanaf €480.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/oceana-gardens/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/oceana-gardens/hero.webp",
    "HERO_BG_ALT": "Oceana Gardens — modern appartement op de New Golden Mile in Cancelada",
    "HERO_NAME": "OCEANA GARDENS",
    "HERO_LOCATION": "CANCELADA",
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
    "META_DESCRIPTION": "Oceana Gardens: ground-floor apartment 3 bedrooms on the New Golden Mile in Cancelada. Private terrace, communal pool and parking. From €480,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Apartment on the New Golden Mile",
    "OG_DESCRIPTION": "Discover Oceana Gardens: contemporary ground-floor apartment in Cancelada (New Golden Mile) with 3 bedrooms, private terrace, shared pool and parking. Near golf and beach. From €480,000.",
    "HERO_BG_ALT": "Oceana Gardens — modern apartment on the New Golden Mile in Cancelada",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Cancelada",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/oceana-gardens/hero.webp",
    "LAT": 36.467831,
    "LNG": -5.060954,
    "HREF": "/oceana-gardens/",
}
