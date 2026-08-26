from urllib.parse import quote

PROJECT_NAME = "Greenity"
PRICE_FROM = "Vanaf € 332.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "greenity",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Greenity: modern wonen in een groene omgeving nabij zee en golf in Mijas. Gedeeld zwembad, fitness, co-working en beveiliging. Vanaf €332.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Groen Wonen in Mijas",
    "OG_DESCRIPTION": "Ontdek Greenity: eigentijdse appartementen in Mijas omringd door groen, nabij stranden en golf. Gemeenschappelijke faciliteiten, ondergrondse parking en co-working zone. Vanaf €332.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/greenity/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/greenity/hero.webp",
    "HERO_BG_ALT": "Greenity — modern appartementencomplex in groen Mijas",
    "HERO_NAME": "GREENITY",
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

DATA_EN = {
    "META_DESCRIPTION": "Greenity: modern living in a green setting near the sea and golf in Mijas. Shared pool, fitness, co-working and security. From €332,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Green Living in Mijas",
    "OG_DESCRIPTION": "Discover Greenity: contemporary apartments in Mijas surrounded by greenery, near beaches and golf. Communal facilities, underground parking and co-working zone. From €332,000.",
    "HERO_BG_ALT": "Greenity — modern apartment complex in green Mijas",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/greenity/hero.webp",
    "LAT": 36.530481,
    "LNG": -4.652558,
    "HREF": "/greenity/",
}
