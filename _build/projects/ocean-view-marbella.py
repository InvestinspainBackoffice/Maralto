from urllib.parse import quote

PROJECT_NAME = "Ocean View Marbella"
PRICE_FROM = "Vanaf € 960.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "ocean-view-marbella",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Ocean View Marbella: 44 exclusieve woningen met 2 of 3 slaapkamers en 10 penthouses met privézwembad, in de heuvels van Marbella. Vanaf €960.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Ocean View Marbella: een afgesloten community in de heuvels, grenzend aan een beschermd natuurgebied, met panoramisch zeezicht. Vanaf €960.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2022/03/Leisure-club-front.INVESTINSPAIN-Ocean-View-Marbella.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2022/03/Leisure-club-front.INVESTINSPAIN-Ocean-View-Marbella.jpg",
    "HERO_BG_ALT": "Ocean View Marbella — leisure club met zwembad en panoramisch zeezicht",
    "HERO_NAME": "OCEAN VIEW MARBELLA",
    "HERO_LOCATION": "MARBELLA",
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

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2022/03/Leisure-club-front.INVESTINSPAIN-Ocean-View-Marbella.jpg",
    "LAT": 36.522046516712,
    "LNG": -4.7387156894166,
    "HREF": "/ocean-view-marbella/",
}
