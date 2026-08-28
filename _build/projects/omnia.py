from urllib.parse import quote

PROJECT_NAME = "Omnia"
PRICE_FROM = "Vanaf € 469.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "omnia",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Omnia Estepona: 84 hoogwaardige appartementen met 1 tot 3 slaapkamers in El Campanario, tussen zee, golf en natuur. Vanaf € 469.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in El Campanario",
    "OG_DESCRIPTION": "Omnia Estepona: lichte, hedendaagse appartementen met ruime terrassen, meerdere zwembaden en beveiligd complex in El Campanario, Estepona. Vanaf € 469.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/omnia/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/omnia/hero.webp",
    "HERO_BG_ALT": "Omnia — moderne appartementen in El Campanario, Estepona",
    "HERO_NAME": "Omnia",
    "HERO_LOCATION": "EL CAMPANARIO, ESTEPONA",
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
    "META_DESCRIPTION": "Omnia Estepona: 84 high-quality apartments with 1 to 3 bedrooms in El Campanario, between sea, golf and nature. From € 469,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in El Campanario",
    "OG_DESCRIPTION": "Omnia Estepona: bright, contemporary apartments with spacious terraces, multiple pools and a gated complex in El Campanario, Estepona. From € 469,000.",
    "HERO_BG_ALT": "Omnia — modern apartments in El Campanario, Estepona",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "El Campanario, Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/omnia/hero.webp",
    "LAT": 36.476467,
    "LNG": -5.021157,
    "HREF": "/omnia/",
}
