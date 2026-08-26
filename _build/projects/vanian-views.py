from urllib.parse import quote

PROJECT_NAME = "Vanian Views"
PRICE_FROM = "Vanaf € 419.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vanian-views",
    "TITLE": f"{PROJECT_NAME} Selwo Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vanian Views: 61 stijlvolle appartementen en penthouses met 2 en 3 slaapkamers in Selwo, Estepona. Semi-ovale architectuur, eigen garage en berging. Vanaf € 419.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Appartementen & penthouses Selwo Estepona",
    "OG_DESCRIPTION": "61 appartementen en penthouses in het exclusieve Selwo, Estepona. Opvallende architectuur, top-materialen, eigen garage. Vanaf € 419.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/vanian-views/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/vanian-views/hero.webp",
    "HERO_BG_ALT": "Vanian Views terras appartement Selwo Estepona",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "SELWO, ESTEPONA",
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
    "MAP_LAT": "36.464248619149",
    "MAP_LNG": "-5.0829374137959",
}

DATA_EN = {
    "META_DESCRIPTION": "Vanian Views: 61 stylish apartments and penthouses with 2 and 3 bedrooms in Selwo, Estepona. Semi-oval architecture, private garage and storage. From € 419,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Apartments & penthouses Selwo Estepona",
    "OG_DESCRIPTION": "61 apartments and penthouses in exclusive Selwo, Estepona. Striking architecture, premium materials, private garage. From € 419,000.",
    "HERO_BG_ALT": "Vanian Views terrace apartment Selwo Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Selwo, Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/vanian-views/hero.webp",
    "LAT": 36.442,
    "LNG": -5.038,
    "HREF": "/vanian-views/",
}
