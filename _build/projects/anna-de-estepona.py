from urllib.parse import quote

PROJECT_NAME = "Anna de Estepona"
PRICE_FROM = "Vanaf € 380.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "anna-de-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Anna de Estepona: moderne appartementen met gemeenschappelijk zwembad en tuinen in Estepona. Ideale ligging nabij strand, golf en het centrum. Vanaf €380.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne Appartementen in Estepona",
    "OG_DESCRIPTION": "Ontdek Anna de Estepona: eigentijdse appartementen met gemeenschappelijk zwembad en groene tuinen in Estepona. Strand, golf en het centrum op korte afstand. Vanaf €380.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/anna-de-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/anna-de-estepona/hero.webp",
    "HERO_BG_ALT": "Anna de Estepona — moderne appartementen met zwembad in Estepona",
    "HERO_NAME": "ANNA DE ESTEPONA",
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
    "META_DESCRIPTION": "Anna de Estepona: modern apartments with communal pool and gardens in Estepona. Ideal location near beach, golf and the town centre. From €380,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Apartments in Estepona",
    "OG_DESCRIPTION": "Discover Anna de Estepona: contemporary apartments with communal pool and green gardens in Estepona. Beach, golf and the town centre within easy reach. From €380,000.",
    "HERO_BG_ALT": "Anna de Estepona — modern apartments with pool in Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/anna-de-estepona/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/anna-de-estepona/",
}
