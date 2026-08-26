from urllib.parse import quote

PROJECT_NAME = "Bahía"
PRICE_FROM = "Vanaf € 443.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "bahia",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Bahía Mijas: 108 nieuwbouwappartementen met 2-3 slaapkamers in 6 gebouwen. Gated community met zwembad. Prijzen vanaf € 443.000.",
    "OG_TITLE": f"{PROJECT_NAME} — 108 Appartementen in Mijas",
    "OG_DESCRIPTION": "108 nieuwbouwappartementen met 2-3 slaapkamers in Mijas. 6 gebouwen, gated community, communaal zwembad. Ontdek Bahía via INVESTINSPAIN.BE.",
    "OG_IMAGE": "https://projects.investinspain.be/images/bahia/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/bahia/hero.webp",
    "HERO_BG_ALT": "Bahía Mijas exterieur appartementen",
    "HERO_NAME": "Bahía",
    "HERO_LOCATION": "MIJAS, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Bahía Mijas: 108 new build apartments with 2-3 bedrooms in 6 buildings. Gated community with pool. Prices from € 443,000.",
    "OG_TITLE": f"{PROJECT_NAME} — 108 Apartments in Mijas",
    "OG_DESCRIPTION": "108 new build apartments with 2-3 bedrooms in Mijas. 6 buildings, gated community, communal pool. Discover Bahía via INVESTINSPAIN.BE.",
    "HERO_BG_ALT": "Bahía Mijas exterior apartments",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/bahia/hero.webp",
    "LAT": 36.530481,
    "LNG": -4.652558,
    "HREF": "/bahia/",
}
