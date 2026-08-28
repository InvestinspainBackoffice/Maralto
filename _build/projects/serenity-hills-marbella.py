from urllib.parse import quote

PROJECT_NAME = "Serenity Hills Marbella"
PRICE_FROM = "Vanaf € 850.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "serenity-hills-marbella",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Serenity Hills Marbella: luxueuze villa's en appartementen op de heuvels van Marbella. Privézwembad, panoramisch zeezicht en moderne architectuur. Vanaf €850.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Villa's op de Heuvels van Marbella",
    "OG_DESCRIPTION": "Ontdek Serenity Hills Marbella: stijlvolle woningen op de groene heuvels van Marbella met panoramisch zeezicht, privézwembad en eigentijdse architectuur. Vanaf €850.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/serenity-hills-marbella/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/serenity-hills-marbella/hero.webp",
    "HERO_BG_ALT": "Serenity Hills Marbella — luxueuze woning met zeezicht op de heuvels van Marbella",
    "HERO_NAME": "SERENITY HILLS MARBELLA",
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
    "META_DESCRIPTION": "Serenity Hills Marbella: luxury villas and apartments on the hills of Marbella. Private pool, panoramic sea views and modern architecture. From €850,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Homes on the Hills of Marbella",
    "OG_DESCRIPTION": "Discover Serenity Hills Marbella: stylish homes on the green hills of Marbella with panoramic sea views, private pool and contemporary architecture. From €850,000.",
    "HERO_BG_ALT": "Serenity Hills Marbella — luxury home with sea views on the hills of Marbella",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/serenity-hills-marbella/hero.webp",
    "LAT": 36.51029,
    "LNG": -4.784994,
    "HREF": "/serenity-hills-marbella/",
}
