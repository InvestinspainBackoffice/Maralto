from urllib.parse import quote

PROJECT_NAME = "Las Mesas Blue Horizon"
PRICE_FROM = "Vanaf € 705.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "las-mesas-blue-horizon",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Las Mesas Blue Horizon: 36 appartementen met panoramisch zeezicht in Estepona. Vanaf €705.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met zeezicht",
    "OG_DESCRIPTION": "Ontdek Las Mesas Blue Horizon: spa, fitnessruimte, co-workingruimte en bioscoop in het hart van Estepona. Vanaf €705.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2024/09/4_Las-Mesas-Blue-Horizon_Estepona.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2024/09/4_Las-Mesas-Blue-Horizon_Estepona.jpg",
    "HERO_BG_ALT": "Las Mesas Blue Horizon — moderne architectuur met zwembad",
    "HERO_NAME": "BLUE HORIZON",
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
    "META_DESCRIPTION": "Las Mesas Blue Horizon: 36 apartments with panoramic sea views in Estepona. From €705.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with Sea Views",
    "OG_DESCRIPTION": "Discover Las Mesas Blue Horizon: spa, fitness room, coworking space and cinema in the heart of Estepona. From €705.000.",
    "HERO_BG_ALT": "Las Mesas Blue Horizon — modern architecture with swimming pool",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2024/09/4_Las-Mesas-Blue-Horizon_Estepona.jpg",
    "LAT": 36.4262544,
    "LNG": -5.1578951,
    "HREF": "/las-mesas-blue-horizon/",
}
