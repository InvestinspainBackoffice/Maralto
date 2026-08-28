from urllib.parse import quote

PROJECT_NAME = "Solaia"
PRICE_FROM = "Vanaf € 890.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "solaia-cancelada",
    "TITLE": f"{PROJECT_NAME} Cancelada — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Solaia: 22 exclusieve boutique appartementen en penthouses met 2 tot 4 slaapkamers aan de New Golden Mile in Cancelada. Vanaf € 890.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutique appartementen aan de New Golden Mile",
    "OG_DESCRIPTION": "Solaia: kleinschalig, eco-bewust project met spa, sauna, fitness/yoga-studio en co-working-ruimte in Cancelada, tussen Estepona en Marbella. Vanaf € 890.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/solaia-cancelada/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/solaia-cancelada/hero.webp",
    "HERO_BG_ALT": "Solaia — boutique appartementen aan de New Golden Mile in Cancelada",
    "HERO_NAME": "Solaia",
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
    "META_DESCRIPTION": "Solaia: 22 exclusive boutique apartments and penthouses with 2 to 4 bedrooms on the New Golden Mile in Cancelada. From € 890,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutique apartments on the New Golden Mile",
    "OG_DESCRIPTION": "Solaia: a small-scale, eco-conscious project with spa, sauna, gym/yoga studio and co-working space in Cancelada, between Estepona and Marbella. From € 890,000.",
    "HERO_BG_ALT": "Solaia — boutique apartments on the New Golden Mile in Cancelada",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Cancelada",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/solaia-cancelada/hero.webp",
    "LAT": 36.465627,
    "LNG": -5.048604,
    "HREF": "/solaia-cancelada/",
}
