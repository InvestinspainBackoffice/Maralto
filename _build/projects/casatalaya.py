from urllib.parse import quote

PROJECT_NAME = "Casatalaya"
PRICE_FROM = "Vanaf € 900.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "casatalaya",
    "TITLE": f"{PROJECT_NAME} Benalmádena — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Casatalaya: exclusief boetiekcomplex met 28 appartementen en penthouses in Torremuelle, Benalmádena. Vrij zeezicht voor elke woning. Vanaf €900.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Casatalaya: een boetiekcomplex met directe toegang tot het strand, buiten- en binnenzwembaden en een sociale lounge in Torremuelle. Vanaf €900.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/06/Casatalaya-03.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/06/Casatalaya-03.jpg",
    "HERO_BG_ALT": "Casatalaya — infinity zwembad met zicht op zee",
    "HERO_NAME": "CASATALAYA",
    "HERO_LOCATION": "BENALMÁDENA",
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
    "META_DESCRIPTION": "Casatalaya: an exclusive boutique complex with 28 apartments and penthouses in Torremuelle, Benalmádena. Unobstructed sea views from every home. From €900,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Casatalaya: a boutique complex with direct beach access, indoor and outdoor swimming pools, and a social lounge in Torremuelle. From €900,000.",
    "HERO_BG_ALT": "Casatalaya — infinity pool with sea view",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benalmádena",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2025/06/Casatalaya-03.jpg",
    "LAT": 36.580969929598,
    "LNG": -4.5706188754204,
    "HREF": "/casatalaya/",
}
