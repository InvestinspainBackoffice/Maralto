from urllib.parse import quote

PROJECT_NAME = "Marina Golden Bay"
PRICE_FROM = "Vanaf € 1.038.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "marina-golden-bay",
    "TITLE": f"{PROJECT_NAME} BENALMÁDENA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Marina Golden Bay Benalmádena: 33 appartementen en penthouses vlakbij de haven, met gemeenschappelijk zwembad en privéterras. Vanaf € 1.038.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen bij de haven van Benalmádena",
    "OG_DESCRIPTION": "Marina Golden Bay combineert stadsleven met luxe aan zee: 33 appartementen en penthouses met zwembad en terras, vlakbij de haven van Benalmádena.",
    "OG_IMAGE": "https://projects.investinspain.be/images/marina-golden-bay/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/marina-golden-bay/hero.webp",
    "HERO_BG_ALT": "Marina Golden Bay — modern appartementencomplex bij de haven van Benalmádena",
    "HERO_NAME": "Marina Golden Bay",
    "HERO_LOCATION": "BENALMÁDENA",
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
    "META_DESCRIPTION": "Marina Golden Bay Benalmádena: 33 apartments and penthouses near the marina, with communal pool and private terrace. From € 1,038,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments near Benalmádena marina",
    "OG_DESCRIPTION": "Marina Golden Bay combines city living with seaside luxury: 33 apartments and penthouses with pool and terrace, near Benalmádena's marina.",
    "HERO_BG_ALT": "Marina Golden Bay — modern apartment complex near Benalmádena marina",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benalmádena",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/marina-golden-bay/hero.webp",
    "LAT": 36.587585,
    "LNG": -4.645059,
    "HREF": "/marina-golden-bay/",
}
