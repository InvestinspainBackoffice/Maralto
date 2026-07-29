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
    "AGENT_NAME": "Gunther De Vleeschouwer",
    "AGENT_PHOTO": "https://investinspain.be/wp-content/uploads/2020/01/Gunther-De-Vleeschouwer-INVESTINSPAIN.jpg",
    "AGENT_PHONE_TEL": "+32496571397",
    "AGENT_PHONE_DISPLAY": "+32 496 57 13 97",
    "AGENT_EMAIL": "gunther@investinspain.be",
    "WA_NUMBER": "32496571397",
}

DATA_EN = {
    "META_DESCRIPTION": "The View Marbella: luxury apartments between Marbella and Benahavís with panoramic sea and golf views. From €899,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Apartments",
    "OG_DESCRIPTION": "Discover The View Marbella: boutique complex with 24-hour security, concierge service, spa and indoor and outdoor swimming pools. From €899,000.",
    "HERO_BG_ALT": "The View Marbella — curved architecture set against the hillside",
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
