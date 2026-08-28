from urllib.parse import quote

PROJECT_NAME = "Emare"
PRICE_FROM = "Uitverkocht"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "emare",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Emare: 28 villa-appartementen frontline aan het strand op de New Golden Mile, Estepona. 4 of 5 slaapkamers, verwarmd infinity zwembad van 37x9m. Uitverkocht.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa-appartementen Frontline Strand",
    "OG_DESCRIPTION": "Ontdek Emare: exclusief frontline strandcomplex met 24u beveiliging, privélift per woning en panoramisch zeezicht op de New Golden Mile. Uitverkocht.",
    "OG_IMAGE": "https://emare.immo/wp-content/uploads/2021/10/084A5415x.jpg",
    "HERO_BG": "https://emare.immo/wp-content/uploads/2021/10/084A5415x.jpg",
    "HERO_BG_ALT": "Emare — verwarmd infinity zwembad rechtstreeks aan het strand",
    "HERO_NAME": "EMARE",
    "HERO_LOCATION": "ESTEPONA",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "PRICE_LABEL": "",
    "PRICE_AMOUNT": "Uitverkocht",
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
    "META_DESCRIPTION": "Emare: 28 frontline beach villa-apartments on the New Golden Mile, Estepona. 4 or 5 bedrooms, heated 37x9m infinity pool. Sold out.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline Beach Villa-Apartments",
    "OG_DESCRIPTION": "Discover Emare: an exclusive frontline beach complex with 24h security, a private lift per home and panoramic sea views on the New Golden Mile. Sold out.",
    "HERO_BG_ALT": "Emare — heated infinity pool right on the beach",
    "PRICE_FROM": "Sold out",
    "HERO_PRICE": "Sold out",
    "PRICE_LABEL": "",
    "PRICE_AMOUNT": "Sold out",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/emare/thumb.webp",
    "LAT": 36.448648,
    "LNG": -5.086878,
    "HREF": "/emare/",
}
