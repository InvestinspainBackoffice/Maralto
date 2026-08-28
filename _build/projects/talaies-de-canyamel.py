from urllib.parse import quote

PROJECT_NAME = "Talaies de Canyamel"
PRICE_FROM = "Vanaf € 436.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "talaies-de-canyamel",
    "TITLE": f"{PROJECT_NAME} Mallorca — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Talaies de Canyamel: stijlvolle appartementen en penthouses aan de ongerepte kust van Canyamel, Mallorca. Vanaf € 436.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Wonen aan het strand van Canyamel, Mallorca",
    "OG_DESCRIPTION": "Talaies de Canyamel: moderne architectuur omringd door pijnbomen, op wandelafstand van het strand, met vier golfbanen in de buurt. Vanaf € 436.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/talaies-de-canyamel/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/talaies-de-canyamel/hero.webp",
    "HERO_BG_ALT": "Talaies de Canyamel — appartementen aan de kust van Mallorca",
    "HERO_NAME": "Talaies de Canyamel",
    "HERO_LOCATION": "CANYAMEL, MALLORCA",
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
    "META_DESCRIPTION": "Talaies de Canyamel: stylish apartments and penthouses on the unspoiled coast of Canyamel, Mallorca. From € 436,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Living by the beach of Canyamel, Mallorca",
    "OG_DESCRIPTION": "Talaies de Canyamel: modern architecture surrounded by pine trees, within walking distance of the beach, with four golf courses nearby. From € 436,000.",
    "HERO_BG_ALT": "Talaies de Canyamel — apartments on the coast of Mallorca",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Canyamel, Mallorca",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/talaies-de-canyamel/hero.webp",
    "LAT": 39.655679,
    "LNG": 3.437994,
    "HREF": "/talaies-de-canyamel/",
}
