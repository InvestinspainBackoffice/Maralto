from urllib.parse import quote

PROJECT_NAME = "Altezza Suites"
PRICE_FROM = "Vanaf € 795.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "altezza-suites",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Altezza Suites: moderne appartementen met zeezicht op de New Golden Mile, Estepona. Vanaf €795.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met zeezicht",
    "OG_DESCRIPTION": "Ontdek Altezza Suites: 72 eenheden met Modulnova-keukens, spa, fitnessruimte en binnen- en buitenzwembaden. Vanaf €795.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2024/10/02-Altezza-Suites-Estepona.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2024/10/02-Altezza-Suites-Estepona.jpg",
    "HERO_BG_ALT": "Altezza Suites — zwembad omgeven door palmbomen en moderne architectuur",
    "HERO_NAME": "ALTEZZA SUITES",
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
    "META_DESCRIPTION": "Altezza Suites: modern apartments with sea views on the New Golden Mile, Estepona. From €795,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with sea views",
    "OG_DESCRIPTION": "Discover Altezza Suites: 72 units with Modulnova kitchens, spa, fitness room and indoor and outdoor swimming pools. From €795,000.",
    "HERO_BG_ALT": "Altezza Suites — swimming pool surrounded by palm trees and modern architecture",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2024/10/02-Altezza-Suites-Estepona.jpg",
    "LAT": 36.4770737,
    "LNG": -5.0765539,
    "HREF": "/altezza-suites/",
}
