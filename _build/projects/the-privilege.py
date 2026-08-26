from urllib.parse import quote

PROJECT_NAME = "The Privilege"
PRICE_FROM = "Vanaf € 678.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-privilege",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Privilege: exclusief avant-garde woonproject in Estepona met 32 units, spa, gym, gedeeld zwembad en co-working. Private tuinen en solariums. Vanaf €678.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Avant-Garde Wonen in Estepona",
    "OG_DESCRIPTION": "Ontdek The Privilege: 32 luxe appartementen en penthouses in Estepona met moderne architectuur, spa, fitness en groene zones. Exclusief gated complex met privéfaciliteiten. Vanaf €678.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/the-privilege/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/the-privilege/hero.webp",
    "HERO_BG_ALT": "The Privilege — moderne gevel van het exclusieve complex in Estepona",
    "HERO_NAME": "THE PRIVILEGE",
    "HERO_LOCATION": "ESTEPONA",
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
    "META_DESCRIPTION": "The Privilege: exclusive avant-garde residential project in Estepona with 32 units, spa, gym, shared pool and co-working. Private gardens and solariums. From €678,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Avant-Garde Living in Estepona",
    "OG_DESCRIPTION": "Discover The Privilege: 32 luxury apartments and penthouses in Estepona with modern architecture, spa, fitness and green zones. Exclusive gated complex with private facilities. From €678,000.",
    "HERO_BG_ALT": "The Privilege — modern facade of the exclusive complex in Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/the-privilege/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/the-privilege/",
}
