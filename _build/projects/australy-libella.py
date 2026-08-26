from urllib.parse import quote

PROJECT_NAME = "Australy Libella"
PRICE_FROM = "Vanaf € 665.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "australy-libella",
    "TITLE": f"{PROJECT_NAME} Selwo Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Australy Libella: 67 moderne appartementen en penthouses met 2 en 3 slaapkamers vlakbij Selwo Estepona. Ruime terrassen, solariums en privézwembaden. Vanaf € 665.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Appartementen & penthouses Selwo Estepona",
    "OG_DESCRIPTION": "67 woningen met 2 en 3 slaapkamers in Selwo, Estepona. Penthouses met solarium, gelijkvloerse appartementen met tuin, ruime terrassen met zeezicht. Vanaf € 665.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/australy-libella/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/australy-libella/hero.webp",
    "HERO_BG_ALT": "Australy Libella terras met zeezicht Estepona",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "SELWO, ESTEPONA",
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
    "MAP_LAT": "36.466529143538",
    "MAP_LNG": "-5.0878205530823",
}

DATA_EN = {
    "META_DESCRIPTION": "Australy Libella: 67 modern apartments and penthouses with 2 and 3 bedrooms near Selwo Estepona. Generous terraces, solariums and private pools. From € 665,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Apartments & penthouses Selwo Estepona",
    "OG_DESCRIPTION": "67 homes with 2 and 3 bedrooms in Selwo, Estepona. Penthouses with solarium, ground-floor apartments with garden, generous terraces with sea views. From € 665,000.",
    "HERO_BG_ALT": "Australy Libella terrace with sea views Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Selwo, Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/australy-libella/hero.webp",
    "LAT": 36.442,
    "LNG": -5.038,
    "HREF": "/australy-libella/",
}
