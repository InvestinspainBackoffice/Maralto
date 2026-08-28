from urllib.parse import quote

PROJECT_NAME = "Equilibrio"
PRICE_FROM = "Vanaf € 620.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "equilibrio",
    "TITLE": f"{PROJECT_NAME} ESTEPONA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Equilibrio Estepona: boutique project van 15 elegante appartementen op 220m van het strand, met zeezicht, gemeenschappelijk zwembad en mediterrane tuinen. Vanaf € 620.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutique appartementen op 220m van het strand in Estepona",
    "OG_DESCRIPTION": "15 elegante appartementen verdeeld over 3 lage blokken, op slechts 220m van het strand in Estepona, met zeezicht en gedeeld zwembad.",
    "OG_IMAGE": "https://projects.investinspain.be/images/equilibrio/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/equilibrio/hero.webp",
    "HERO_BG_ALT": "Equilibrio — stijlvol interieur van een boutique appartement in Estepona",
    "HERO_NAME": "Equilibrio",
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
    "META_DESCRIPTION": "Equilibrio Estepona: boutique project of 15 elegant apartments 220m from the beach, with sea views, communal pool and Mediterranean gardens. From € 620,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutique apartments 220m from the beach in Estepona",
    "OG_DESCRIPTION": "15 elegant apartments across 3 low-rise blocks, just 220m from the beach in Estepona, with sea views and shared pool.",
    "HERO_BG_ALT": "Equilibrio — stylish interior of a boutique apartment in Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/equilibrio/hero.webp",
    "LAT": 36.392567,
    "LNG": -5.204194,
    "HREF": "/equilibrio/",
}
