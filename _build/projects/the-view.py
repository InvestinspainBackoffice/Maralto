from urllib.parse import quote

PROJECT_NAME = "The View Marbella"
PRICE_FROM = "Vanaf € 899.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-view",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The View Marbella Fase II & III: 58 luxe appartementen en penthouses met 2, 3 of 4 slaapkamers in Las Colinas de Marbella, tussen Marbella en Benahavís. Vanaf €899.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Fase II & III: Luxe Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Fase II & III van The View Marbella: privézwembaden, wellness club, business center met golfsimulator en panoramisch zee- en golfzicht. Vanaf €899.000.",
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
    "META_DESCRIPTION": "The View Marbella Phase II & III: 58 luxury apartments and penthouses with 2, 3 or 4 bedrooms in Las Colinas de Marbella, between Marbella and Benahavís. From €899,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Phase II & III: Luxury Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Phase II & III of The View Marbella: private pools, a wellness club, a business centre with golf simulator and panoramic sea and golf views. From €899,000.",
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
