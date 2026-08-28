from urllib.parse import quote

PROJECT_NAME = "Lagumare41"
PRICE_FROM = "Vanaf € 478.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "lagumare41",
    "TITLE": f"{PROJECT_NAME} ESTEPONA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Lagumare41 Estepona: moderne appartementen en penthouses met tuinen, privézwembad-optie en solarium. Op 5 min van Estepona centrum. Vanaf € 478.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen en penthouses met tuin in Estepona",
    "OG_DESCRIPTION": "Lagumare41 biedt gelijkvloerse appartementen met tuin en privézwembad-optie en penthouses met solarium van 108m² op wandelafstand van Estepona.",
    "OG_IMAGE": "https://projects.investinspain.be/images/lagumare41/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/lagumare41/hero.webp",
    "HERO_BG_ALT": "Lagumare41 — modern appartementencomplex met tuinen in Estepona",
    "HERO_NAME": "Lagumare41",
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
    "META_DESCRIPTION": "Lagumare41 Estepona: modern apartments and penthouses with gardens, private pool option and solarium. 5 min from Estepona centre. From € 478,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments and penthouses with garden in Estepona",
    "OG_DESCRIPTION": "Lagumare41 offers ground-floor apartments with garden and private pool option, and penthouses with 108m² solarium, within walking distance of Estepona.",
    "HERO_BG_ALT": "Lagumare41 — modern apartment complex with gardens in Estepona",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/lagumare41/hero.webp",
    "LAT": 36.436986,
    "LNG": -5.110333,
    "HREF": "/lagumare41/",
}
