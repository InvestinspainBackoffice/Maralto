from urllib.parse import quote

PROJECT_NAME = "Golden View I & II"
PRICE_FROM = "Vanaf € 673.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "golden-view-i-en-ii",
    "TITLE": f"{PROJECT_NAME} Manilva — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Golden View I & II – luxe appartementen met privézwembad, solarium en zeezicht in Manilva, Costa del Sol. Rustige ligging dicht bij strand en golf. Vanaf € 673.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxe appartementen Manilva · INVESTINSPAIN.BE",
    "OG_DESCRIPTION": "Exclusieve appartementen met privézwembad en panoramisch zeezicht in Manilva. Rust en luxe aan de Costa del Sol. Vraag brochure aan bij INVESTINSPAIN.",
    "OG_IMAGE": "https://projects.investinspain.be/images/golden-view-i-en-ii/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/golden-view-i-en-ii/hero.webp",
    "HERO_BG_ALT": "Golden View I II exterieur luxe appartementen Manilva Costa del Sol zeezicht",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "MANILVA, COSTA DEL SOL",
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
    "MAP_LAT": "36.324234746951",
    "MAP_LNG": "-5.2544102612462",
}

DATA_EN = {
    "META_DESCRIPTION": "Golden View I & II – luxury apartments with private pool, solarium and sea views in Manilva, Costa del Sol. Peaceful location close to beach and golf. From € 673,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxury apartments Manilva · INVESTINSPAIN.BE",
    "OG_DESCRIPTION": "Exclusive apartments with private pool and panoramic sea views in Manilva. Tranquillity and luxury on the Costa del Sol. Request the brochure at INVESTINSPAIN.",
    "HERO_BG_ALT": "Golden View I II exterior luxury apartments Manilva Costa del Sol sea views",
}
