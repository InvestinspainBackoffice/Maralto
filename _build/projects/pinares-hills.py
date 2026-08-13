from urllib.parse import quote

PROJECT_NAME = "Pinares Hills"
PRICE_FROM = "Vanaf € 2.400.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "pinares-hills",
    "TITLE": f"{PROJECT_NAME} Málaga — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Pinares Hills: moderne villa's met 4-5 slaapkamers, privézwembad en zeezicht in Pinares de San Antón, Málaga. Vanaf € 2.400.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's in Málaga",
    "OG_DESCRIPTION": "Moderne villa's met 4-5 slaapkamers en zeezicht in een gated community in Málaga.",
    "OG_IMAGE": "https://projects.investinspain.be/images/pinares-hills/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/pinares-hills/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villa's in Málaga",
    "HERO_NAME": "Pinares Hills",
    "HERO_LOCATION": "MÁLAGA",
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
    "META_DESCRIPTION": "Pinares Hills: modern villas with 4-5 bedrooms, private pool and sea views in Pinares de San Antón, Málaga. From € 2,400,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas in Málaga",
    "OG_DESCRIPTION": "Modern villas with 4-5 bedrooms and sea views in a gated community in Málaga.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villas in Málaga",
}

HUB = {
    "NAME": "Pinares Hills",
    "LOCATION": "Málaga",
    "PRICE": "Vanaf € 2.400.000",
    "THUMB": "https://projects.investinspain.be/images/pinares-hills/hero.webp",
    "LAT": 36.73908,
    "LNG": -4.355106,
    "HREF": "/pinares-hills/",
}
