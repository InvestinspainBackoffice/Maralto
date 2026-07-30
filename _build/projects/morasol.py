from urllib.parse import quote

PROJECT_NAME = "Morasol"
PRICE_FROM = "Vanaf € 351.520"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "morasol",
    "TITLE": f"{PROJECT_NAME} Manilva — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Morasol: 151 woningen met 2 of 3 slaapkamers in Manilva, op wandelafstand van het strand. Gemeenschappelijk zwembad en mediterrane tuinen. Vanaf €351.520.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Morasol: comfort, privacy en levenskwaliteit in een exclusief nieuwbouwcomplex in Manilva, met privéterrassen en zeezicht. Vanaf €351.520.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/10/Morasol-Manilva-INVESTINSPAIN-2.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/10/Morasol-Manilva-INVESTINSPAIN-2.jpg",
    "HERO_BG_ALT": "Morasol — gemeenschappelijk zwembad bij schemering met zicht op zee",
    "HERO_NAME": "MORASOL",
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
    "META_DESCRIPTION": "Morasol: 151 homes with 2 or 3 bedrooms in Manilva, within walking distance of the beach. Communal pool and Mediterranean gardens. From €351.520.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Morasol: comfort, privacy and quality of life in an exclusive new-build complex in Manilva, with private terraces and sea views. From €351.520.",
    "HERO_BG_ALT": "Morasol — communal swimming pool at dusk with sea view",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Manilva",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2025/10/Morasol-Manilva-INVESTINSPAIN-2.jpg",
    "LAT": 36.321681748191,
    "LNG": -5.2482868359576,
    "HREF": "/morasol/",
}
