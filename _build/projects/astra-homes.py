from urllib.parse import quote

PROJECT_NAME = "Astra Homes"
PRICE_FROM = "Vanaf € 343.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "astra-homes",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Astra Homes: 126 appartementen met 1, 2 en 3 slaapkamers en panoramisch uitzicht in Fuengirola. Sky infinity pool, spa en cinema room. Vanaf €343.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met Panoramisch Uitzicht",
    "OG_DESCRIPTION": "Ontdek Astra Homes: 126 appartementen met een privéresort-gevoel — sky infinity pool, spa, sauna, coworking en privébioscoop, in het hart van Fuengirola. Vanaf €343.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/astra-homes/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/astra-homes/hero.webp",
    "HERO_BG_ALT": "Astra Homes — gevelaanzicht van het gebouw in Fuengirola",
    "HERO_NAME": "ASTRA HOMES",
    "HERO_LOCATION": "FUENGIROLA",
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
    "META_DESCRIPTION": "Astra Homes: 126 apartments with 1, 2 and 3 bedrooms and panoramic views in Fuengirola. Sky infinity pool, spa and cinema room. From €343,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with Panoramic Views",
    "OG_DESCRIPTION": "Discover Astra Homes: 126 apartments with a private-resort feel — a sky infinity pool, spa, sauna, coworking space and private cinema, in the heart of Fuengirola. From €343,000.",
    "HERO_BG_ALT": "Astra Homes — facade view of the building in Fuengirola",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Fuengirola",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/astra-homes/hero.webp",
    "LAT": 36.570048,
    "LNG": -4.609375,
    "HREF": "/astra-homes/",
}
