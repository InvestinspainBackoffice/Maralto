from urllib.parse import quote

PROJECT_NAME = "Absolute Estepona"
PRICE_FROM = "Vanaf € 645.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "absolute-estepona",
    "TITLE": f"{PROJECT_NAME} ESTEPONA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Absolute Estepona: moderne residenties met communaal zwembad, zeezicht en premium afwerking in Estepona. Op korte afstand van strand en haven. Vanaf € 645.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne residenties met zeezicht in Estepona",
    "OG_DESCRIPTION": "Absolute Estepona biedt stijlvolle appartementen met zeezicht, communaal zwembad en kwalitatieve afwerking in één van de mooiste kustgemeenten van de Costa del Sol.",
    "OG_IMAGE": "https://projects.investinspain.be/images/absolute-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/absolute-estepona/hero.webp",
    "HERO_BG_ALT": "Absolute Estepona — modern appartementencomplex met zeezicht in Estepona",
    "HERO_NAME": "Absolute Estepona",
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
    "META_DESCRIPTION": "Absolute Estepona: modern residences with communal pool, sea views and premium finishes in Estepona. Short distance to beach and marina. From € 645,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern residences with sea views in Estepona",
    "OG_DESCRIPTION": "Absolute Estepona offers stylish apartments with sea views, communal pool and quality finishes in one of the finest coastal municipalities on the Costa del Sol.",
    "HERO_BG_ALT": "Absolute Estepona — modern apartment complex with sea views in Estepona",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/absolute-estepona/hero.webp",
    "LAT": 36.394165,
    "LNG": -5.205772,
    "HREF": "/absolute-estepona/",
}
