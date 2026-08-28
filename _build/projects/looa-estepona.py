from urllib.parse import quote

PROJECT_NAME = "Looa Estepona"
PRICE_FROM = "Vanaf € 489.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "looa-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Looa Estepona: boutique nieuwbouwproject van 22 exclusieve woningen met 3 slaapkamers, op wandelafstand van de Middellandse Zee. Vanaf €489.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutique Project met 3 Slaapkamers",
    "OG_DESCRIPTION": "Ontdek Looa Estepona: slechts 22 exclusieve woningen met hedendaagse architectuur, grote terrassen en solarium, op wandelafstand van zee. Vanaf €489.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/looa-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/looa-estepona/hero.webp",
    "HERO_BG_ALT": "Looa Estepona — luchtfoto van het gebouw met zicht op zee",
    "HERO_NAME": "LOOA ESTEPONA",
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
    "META_DESCRIPTION": "Looa Estepona: boutique new-build project of 22 exclusive homes with 3 bedrooms, within walking distance of the Mediterranean. From €489,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutique Project with 3 Bedrooms",
    "OG_DESCRIPTION": "Discover Looa Estepona: just 22 exclusive homes with contemporary architecture, large terraces and a solarium, within walking distance of the sea. From €489,000.",
    "HERO_BG_ALT": "Looa Estepona — aerial view of the building with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/looa-estepona/hero.webp",
    "LAT": 36.427255,
    "LNG": -5.160471,
    "HREF": "/looa-estepona/",
}
