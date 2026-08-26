from urllib.parse import quote

PROJECT_NAME = "UNELMA Estepona"
PRICE_FROM = "Vanaf € 525.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "unelma-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "UNELMA Estepona: moderne appartementen met gemeenschappelijk zwembad en mediterrane tuinen in Estepona. Rustige ligging nabij strand en golf. Vanaf € 525.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen in Estepona",
    "OG_DESCRIPTION": "Stijlvol appartementenproject met ruime terrassen, gemeenschappelijk zwembad en mediterrane tuinen in Estepona, Costa del Sol.",
    "OG_IMAGE": "https://projects.investinspain.be/images/unelma-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/unelma-estepona/hero.webp",
    "HERO_BG_ALT": "UNELMA Estepona — luchtfoto van het appartementencomplex met zwembad",
    "HERO_NAME": "UNELMA Estepona",
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
    "META_DESCRIPTION": "UNELMA Estepona: modern apartments with communal pool and Mediterranean gardens in Estepona. Peaceful setting near beach and golf. From € 525,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments in Estepona",
    "OG_DESCRIPTION": "Stylish apartment project with spacious terraces, communal pool and Mediterranean gardens in Estepona, Costa del Sol.",
    "HERO_BG_ALT": "UNELMA Estepona — aerial view of the apartment complex with pool",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/unelma-estepona/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/unelma-estepona/",
}
