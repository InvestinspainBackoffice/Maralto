from urllib.parse import quote

PROJECT_NAME = "Seven Diamonds"
PRICE_FROM = "Vanaf € 1.530.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "seven-diamonds",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Seven Diamonds: 7 unieke villa's met 3-4 slaapkamers en eigen overloopzwembad in Atalaya, Estepona. Vanaf € 1.530.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's in Estepona",
    "OG_DESCRIPTION": "7 unieke villa's met eigen overloopzwembad en panoramisch uitzicht in Atalaya, Estepona.",
    "OG_IMAGE": "https://projects.investinspain.be/images/seven-diamonds/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/seven-diamonds/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villa's in Estepona",
    "HERO_NAME": "Seven Diamonds",
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
    "META_DESCRIPTION": "Seven Diamonds: 7 unique villas with 3-4 bedrooms and private infinity pool in Atalaya, Estepona. From € 1,530,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas in Estepona",
    "OG_DESCRIPTION": "7 unique villas with private infinity pool and panoramic views in Atalaya, Estepona.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villas in Estepona",
}

HUB = {
    "NAME": "Seven Diamonds",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 1.530.000",
    "THUMB": "https://projects.investinspain.be/images/seven-diamonds/hero.webp",
    "LAT": 36.476567,
    "LNG": -5.017319,
    "HREF": "/seven-diamonds/",
}
