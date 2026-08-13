from urllib.parse import quote

PROJECT_NAME = "Vista Linda"
PRICE_FROM = "Vanaf € 1.460.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vista-linda",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vista Linda: 4 villa's met 3 slaapkamers, privé lift en panoramisch zeezicht in Torreblanca, Fuengirola. Vanaf € 1.460.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's in Fuengirola",
    "OG_DESCRIPTION": "4 villa's met 3 slaapkamers, privé lift en panoramisch zeezicht in Fuengirola.",
    "OG_IMAGE": "https://projects.investinspain.be/images/vista-linda/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/vista-linda/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villa's in Fuengirola",
    "HERO_NAME": "Vista Linda",
    "HERO_LOCATION": "FUENGIROLA",
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
    "META_DESCRIPTION": "Vista Linda: 4 villas with 3 bedrooms, private elevator and panoramic sea views in Torreblanca, Fuengirola. From € 1,460,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas in Fuengirola",
    "OG_DESCRIPTION": "4 villas with 3 bedrooms, private elevator and panoramic sea views in Fuengirola.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villas in Fuengirola",
}

HUB = {
    "NAME": "Vista Linda",
    "LOCATION": "Fuengirola",
    "PRICE": "Vanaf € 1.460.000",
    "THUMB": "https://projects.investinspain.be/images/vista-linda/hero.webp",
    "LAT": 36.564259,
    "LNG": -4.611357,
    "HREF": "/vista-linda/",
}
