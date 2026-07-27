from urllib.parse import quote

PROJECT_NAME = "The View Marbella"
PRICE_FROM = "Vanaf € 899.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-view",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The View Marbella: luxe appartementen tussen Marbella en Benahavís met panoramisch zee- en golfzicht. Vanaf €899.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Appartementen",
    "OG_DESCRIPTION": "Ontdek The View Marbella: boutique complex met 24u beveiliging, conciërgedienst, spa en binnen- en buitenzwembaden. Vanaf €899.000.",
    "OG_IMAGE": "https://homeinspain.be/wp-content/uploads/2026/07/Block-7-scaled.jpg",
    "HERO_BG": "https://homeinspain.be/wp-content/uploads/2026/07/Block-7-scaled.jpg",
    "HERO_BG_ALT": "The View Marbella — gebogen architectuur tegen de heuvel",
    "HERO_NAME": "THE VIEW",
    "HERO_LOCATION": "BENAHAVÍS",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "WA_TEXT_ENCODED": quote(WA_MESSAGE),
    "PROJECT_NAME": PROJECT_NAME,
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benahavís",
    "PRICE": PRICE_FROM,
    "THUMB": "https://homeinspain.be/wp-content/uploads/2026/07/Block-7-scaled.jpg",
    "LAT": 36.4666272,
    "LNG": -5.0836161,
    "HREF": "/the-view/",
}
