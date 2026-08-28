from urllib.parse import quote

PROJECT_NAME = "Azulea"
PRICE_FROM = "Vanaf € 875.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "azulea",
    "TITLE": f"{PROJECT_NAME} Chapparal Golf — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Azulea: stijlvolle townhouses met 2 en 3 slaapkamers en panoramisch zeezicht bij Chapparal Golf in Mijas Costa. Vanaf €875.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses met Panoramisch Zeezicht",
    "OG_DESCRIPTION": "Ontdek Azulea: elegante townhouses met privézwembad, solarium en open zicht op de Middellandse Zee, bij Chapparal Golf in Mijas Costa. Vanaf €875.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/azulea/img2.webp",
    "HERO_BG": "https://projects.investinspain.be/images/azulea/img2.webp",
    "HERO_BG_ALT": "Azulea — luchtfoto van de townhouses met zicht op zee",
    "HERO_NAME": "AZULEA",
    "HERO_LOCATION": "MIJAS",
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
    "META_DESCRIPTION": "Azulea: stylish townhouses with 2 and 3 bedrooms and panoramic sea views near Chapparal Golf in Mijas Costa. From €875,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses with Panoramic Sea Views",
    "OG_DESCRIPTION": "Discover Azulea: elegant townhouses with a private pool, solarium and open views over the Mediterranean, near Chapparal Golf in Mijas Costa. From €875,000.",
    "HERO_BG_ALT": "Azulea — aerial view of the townhouses with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/azulea/hero.webp",
    "LAT": 36.511887,
    "LNG": -4.659334,
    "HREF": "/azulea/",
}
