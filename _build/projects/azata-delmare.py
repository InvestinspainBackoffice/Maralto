from urllib.parse import quote

PROJECT_NAME = "Azata Delmare"
PRICE_FROM = "Vanaf € 430.250"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "azata-delmare",
    "TITLE": f"{PROJECT_NAME} Casares Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Azata Delmare: 74 appartementen met 2 en 3 slaapkamers op 250 m van het strand in Casares Costa. Zeezicht, overloopzwembad, gesloten woonwijk. Vanaf € 430.250.",
    "OG_TITLE": f"{PROJECT_NAME} · Appartementen met zeezicht Casares Costa",
    "OG_DESCRIPTION": "74 appartementen en penthouses op 250 m van het strand in Casares Costa. Overloopzwembad, zeezicht, gesloten gemeenschap. Vanaf € 430.250.",
    "OG_IMAGE": "https://projects.investinspain.be/images/azata-delmare/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/azata-delmare/hero.webp",
    "HERO_BG_ALT": "Azata Delmare appartementen met zeezicht Casares Costa",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "CASARES COSTA",
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
    "MAP_LAT": "36.388761890696",
    "MAP_LNG": "-5.2100140626062",
}

DATA_EN = {
    "META_DESCRIPTION": "Azata Delmare: 74 apartments with 2 and 3 bedrooms, 250 m from the beach in Casares Costa. Sea views, infinity pool, gated community. From € 430,250.",
    "OG_TITLE": f"{PROJECT_NAME} · Apartments with sea views Casares Costa",
    "OG_DESCRIPTION": "74 apartments and penthouses 250 m from the beach in Casares Costa. Infinity pool, sea views, gated community. From € 430,250.",
    "HERO_BG_ALT": "Azata Delmare apartments with sea views Casares Costa",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Casares Costa",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/azata-delmare/hero.webp",
    "LAT": 36.388762,
    "LNG": -5.210014,
    "HREF": "/azata-delmare/",
}
