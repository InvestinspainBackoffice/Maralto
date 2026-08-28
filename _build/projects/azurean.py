from urllib.parse import quote

PROJECT_NAME = "Azurean"
PRICE_FROM = "Vanaf € 901.992"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "azurean",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Azurean: eigentijdse penthouse-appartementen op de New Golden Mile in Estepona. Daktuin, privézwembad en panoramisch zeezicht. Vanaf €901.992.",
    "OG_TITLE": f"{PROJECT_NAME} — Penthouse met Zeezicht in Estepona",
    "OG_DESCRIPTION": "Ontdek Azurean: exclusieve penthouse-appartementen op de New Golden Mile in Estepona. Privédaktuin, zwembad en spectaculair zeezicht. Nieuw project. Vanaf €901.992.",
    "OG_IMAGE": "https://projects.investinspain.be/images/azurean/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/azurean/hero.webp",
    "HERO_BG_ALT": "Azurean — penthouse-appartement met zeezicht op de New Golden Mile Estepona",
    "HERO_NAME": "AZUREAN",
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
    "META_DESCRIPTION": "Azurean: contemporary penthouse apartments on the New Golden Mile in Estepona. Private rooftop terrace, pool and panoramic sea views. From €901,992.",
    "OG_TITLE": f"{PROJECT_NAME} — Penthouse with Sea Views in Estepona",
    "OG_DESCRIPTION": "Discover Azurean: exclusive penthouse apartments on the New Golden Mile in Estepona. Private rooftop terrace, pool and spectacular sea views. New project. From €901,992.",
    "HERO_BG_ALT": "Azurean — penthouse apartment with sea views on the New Golden Mile Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/azurean/hero.webp",
    "LAT": 36.520234,
    "LNG": -5.00609,
    "HREF": "/azurean/",
}
