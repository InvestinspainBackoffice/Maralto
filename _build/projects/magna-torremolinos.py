from urllib.parse import quote

PROJECT_NAME = "Magna Torremolinos"
PRICE_FROM = "Vanaf € 412.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "magna-torremolinos",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Magna Torremolinos: 353 appartementen en penthouses met 1 tot 4 slaapkamers, 5 min van Playa de la Carihuela. Binnen- en buitenzwembad, bioscoopzaal, daktuin. Vanaf € 412.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Appartementen & Penthouses",
    "OG_DESCRIPTION": "Exclusief nieuwbouwproject van 353 woningen aan de Avenida Carlota Alessandri, op wandelafstand van Playa de la Carihuela. Vanaf € 412.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/magna-torremolinos/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/magna-torremolinos/hero.webp",
    "HERO_BG_ALT": "Magna Torremolinos — gevel aan de Avenida Carlota Alessandri bij schemering",
    "HERO_NAME": "MAGNA TORREMOLINOS",
    "HERO_LOCATION": "TORREMOLINOS",
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
    "MAP_LAT": "36.6085855",
    "MAP_LNG": "-4.508366",
}

DATA_EN = {
    "META_DESCRIPTION": "Magna Torremolinos: 353 apartments and penthouses with 1 to 4 bedrooms, 5 min from Playa de la Carihuela. Indoor and outdoor pool, cinema room, roof garden. From € 412,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Apartments & Penthouses",
    "OG_DESCRIPTION": "Exclusive new-build development of 353 homes on Avenida Carlota Alessandri, within walking distance of Playa de la Carihuela. From € 412,000.",
    "HERO_BG_ALT": "Magna Torremolinos — facade on Avenida Carlota Alessandri at dusk",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Torremolinos",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/magna-torremolinos/hero.webp",
    "LAT": 36.6085855,
    "LNG": -4.508366,
    "HREF": "/magna-torremolinos/",
}
