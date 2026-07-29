from urllib.parse import quote

PROJECT_NAME = "Dunique"
PRICE_FROM = "Vanaf € 3.350.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "dunique",
    "TITLE": f"{PROJECT_NAME} Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Dunique: appartementen en townhouses aan het strand in Las Chapas, Marbella. Vanaf €3.350.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Townhouses",
    "OG_DESCRIPTION": "Ontdek Dunique: privézwembad in elke woning, Social Club met spa, gym en 40 meter overdekt zwembad. Vanaf €3.350.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2022/02/DUNIQUE-VISTA-DESDE-PISCINA-VOLADA-min-scaled.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2022/02/DUNIQUE-VISTA-DESDE-PISCINA-VOLADA-min-scaled.jpg",
    "HERO_BG_ALT": "Dunique — zwembad met panoramisch zeezicht bij zonsondergang",
    "HERO_NAME": "DUNIQUE",
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

DATA_EN = {
    "META_DESCRIPTION": "Dunique: apartments and townhouses on the beach in Las Chapas, Marbella. From €3,350,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Townhouses",
    "OG_DESCRIPTION": "Discover Dunique: a private pool in every home, a Social Club with spa, gym and a 40-metre indoor pool. From €3,350,000.",
    "HERO_BG_ALT": "Dunique — swimming pool with panoramic sea view at sunset",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2022/02/DUNIQUE-VISTA-DESDE-PISCINA-VOLADA-min-scaled.jpg",
    "LAT": 36.5006105,
    "LNG": -4.8113747,
    "HREF": "/dunique/",
}
