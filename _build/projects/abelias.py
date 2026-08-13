from urllib.parse import quote

PROJECT_NAME = "Abelias"
PRICE_FROM = "Vanaf € 415.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "abelias",
    "TITLE": f"{PROJECT_NAME} Benalmádena — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Abelias: Moderne residences in Benalmádena met golf- en zeezicht. Duplex penthouses en 2-slaapkamer appartementen. Vanaf € 415.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Benalmádena",
    "OG_DESCRIPTION": "Abelias: Moderne residences met Andalusisch charme, overflow pool, fitness en co-working ruimte. Vanaf € 415.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/abelias/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/abelias/hero.webp",
    "HERO_BG_ALT": "Abelias — moderne residences met golf- en zeezicht in Benalmádena",
    "HERO_NAME": "Abelias",
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
    "META_DESCRIPTION": "Abelias: Modern residences in Benalmádena with golf and sea views. Duplex penthouses and 2-bedroom apartments. From € 415,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Benalmádena",
    "OG_DESCRIPTION": "Abelias: Modern residences with Andalusian charm, overflow pool, fitness and co-working space. From € 415,000.",
    "HERO_BG_ALT": "Abelias — modern residences with golf and sea views in Benalmádena",
}

HUB = {
    "NAME": "Abelias",
    "LOCATION": "Benalmádena",
    "PRICE": "Vanaf € 415.000",
    "THUMB": "https://projects.investinspain.be/images/abelias/hero.webp",
    "LAT": 36.5942,
    "LNG": -4.7195,
    "HREF": "/abelias/",
}
