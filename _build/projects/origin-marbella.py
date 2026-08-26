from urllib.parse import quote

PROJECT_NAME = "Origin Marbella"
PRICE_FROM = "Vanaf € 545.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "origin-marbella",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Origin Marbella: moderne appartementen met zwembad, gym en coworking nabij Marbella. Uitstekende faciliteiten en topligging in de heuvels boven de stad. Vanaf € 545.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen met zwembad en gym, Marbella",
    "OG_DESCRIPTION": "Origin Marbella: eigentijdse appartementen met communaal zwembad, gym, coworking en ruime terrassen in de heuvels nabij Marbella. Uitstekende prijs-kwaliteit. Vanaf € 545.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/origin-marbella/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/origin-marbella/hero.webp",
    "HERO_BG_ALT": "Origin Marbella communaal zwembad en terras",
    "HERO_NAME": "Origin Marbella",
    "HERO_LOCATION": "MARBELLA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Origin Marbella: modern apartments with pool, gym and coworking space near Marbella. Excellent amenities and a great location in the hills above the city. From € 545,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments with pool and gym, Marbella",
    "OG_DESCRIPTION": "Origin Marbella: contemporary apartments with communal pool, gym, coworking and spacious terraces in the hills near Marbella. Outstanding value for money. From € 545,000.",
    "HERO_BG_ALT": "Origin Marbella communal pool and terrace",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/origin-marbella/hero.webp",
    "LAT": 36.502843,
    "LNG": -4.913942,
    "HREF": "/origin-marbella/",
}
