from urllib.parse import quote

PROJECT_NAME = "Solenne"
PRICE_FROM = "Vanaf € 990.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "solenne",
    "TITLE": f"{PROJECT_NAME} Benahavís — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Solenne: elegant boutique-project met 21 woningen, 2 of 3 slaapkamers, in het prestigieuze Benahavís. Golfsimulator, overdekt verwarmd zwembad en spa. Vanaf €990.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutique-appartementen",
    "OG_DESCRIPTION": "Ontdek Solenne: stijlvolle appartementen met ruime terrassen, uitzicht op heuvels en de Middellandse Zee, in het prestigieuze Benahavís. Vanaf €990.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/01/SOLENNE-004.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/01/SOLENNE-004.jpg",
    "HERO_BG_ALT": "Solenne — infinity pool bij zonsondergang met zicht over de kust",
    "HERO_NAME": "SOLENNE",
    "HERO_LOCATION": "BENAHAVÍS",
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
    "LOCATION": "Benahavís",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2026/01/SOLENNE-004.jpg",
    "LAT": 36.505856521457,
    "LNG": -5.0096572906735,
    "HREF": "/solenne/",
}
