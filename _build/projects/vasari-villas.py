from urllib.parse import quote

PROJECT_NAME = "Vasari Villas"
PRICE_FROM = "Vanaf € 1.950.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vasari-villas",
    "TITLE": f"{PROJECT_NAME} Nueva Andalucía — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vasari Villas: 14 luxe villa's met 4 en 5 slaapkamers in El Campanario, Nueva Andalucía. Privézwembad, golfclublidmaatschap inclusief. Vanaf € 1.950.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Villa's in Nueva Andalucía",
    "OG_DESCRIPTION": "Vasari Villas: eigentijdse villa's met privézwembad en automatisch lidmaatschap El Campanario Golf Club. Vlakbij Puerto Banús. Vanaf € 1.950.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/vasari-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/vasari-villas/hero.webp",
    "HERO_BG_ALT": "Vasari Villas — luxe villa met zwembad in Nueva Andalucía",
    "HERO_NAME": "Vasari Villas",
    "HERO_LOCATION": "NUEVA ANDALUCÍA, MARBELLA",
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
    "META_DESCRIPTION": "Vasari Villas: 14 luxury villas with 4 and 5 bedrooms in El Campanario, Nueva Andalucía. Private pool, golf club membership included. From € 1,950,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Villas in Nueva Andalucía",
    "OG_DESCRIPTION": "Vasari Villas: contemporary villas with private pool and automatic El Campanario Golf Club membership. Close to Puerto Banús. From € 1,950,000.",
    "HERO_BG_ALT": "Vasari Villas — luxury villa with pool in Nueva Andalucía",
}

HUB = {
    "NAME": "Vasari Villas",
    "LOCATION": "Nueva Andalucía",
    "PRICE": "Vanaf € 1.950.000",
    "THUMB": "https://projects.investinspain.be/images/vasari-villas/hero.webp",
    "LAT": 36.4756,
    "LNG": -5.0218,
    "HREF": "/vasari-villas/",
}
