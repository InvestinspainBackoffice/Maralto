from urllib.parse import quote

PROJECT_NAME = "Alonia Manilva"
PRICE_FROM = "Vanaf € 301.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "alonia-manilva",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Alonia Manilva: 60 moderne appartementen, duplexen en penthouses met golf- en bergzicht in Manilva. Vanaf € 301.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses met golfzicht",
    "OG_DESCRIPTION": "Alonia Manilva: 2 en 3-slaapkamer woningen met ruime terrassen, gedeeld zwembad en gastroteca, vlak bij La Duquesa Marina. Vanaf € 301.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/alonia-manilva/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/alonia-manilva/hero.webp",
    "HERO_BG_ALT": "Alonia Manilva — moderne appartementen met golfzicht in Manilva",
    "HERO_NAME": "Alonia Manilva",
    "HERO_LOCATION": "MANILVA",
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
    "META_DESCRIPTION": "Alonia Manilva: 60 modern apartments, duplexes and penthouses with golf and mountain views in Manilva. From € 301,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses with golf views",
    "OG_DESCRIPTION": "Alonia Manilva: 2 and 3-bedroom homes with spacious terraces, shared pool and gastro lounge, close to La Duquesa Marina. From € 301,000.",
    "HERO_BG_ALT": "Alonia Manilva — modern apartments with golf views in Manilva",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Manilva",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/alonia-manilva/hero.webp",
    "LAT": 36.360999,
    "LNG": -5.238665,
    "HREF": "/alonia-manilva/",
}
