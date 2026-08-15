from urllib.parse import quote

PROJECT_NAME = "Blue View Heights"
PRICE_FROM = "Vanaf € 474.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "blue-view-heights",
    "TITLE": f"{PROJECT_NAME} Manilva — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Blue View Heights: 46 exclusieve appartementen met 2, 3 en 4 slaapkamers en spectaculair zeezicht in Manilva. Gedeeld zwembad, privéterrassen, berging, garage. Vanaf € 474.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 46 appartementen zeezicht Manilva",
    "OG_DESCRIPTION": "46 eigentijdse appartementen 2-4 slaapkamers met spectaculair zee- en bergzicht in Manilva. Gedeeld zwembad, privéterrassen, garage, berging. Vanaf € 474.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/blue-view-heights/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/blue-view-heights/hero.webp",
    "HERO_BG_ALT": "Blue View Heights appartementen zeezicht zwembad terras Manilva",
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
    "MAP_LAT": "36.317432700995",
    "MAP_LNG": "-5.2522178153175",
}

DATA_EN = {
    "META_DESCRIPTION": "Blue View Heights: 46 exclusive apartments with 2, 3 and 4 bedrooms and spectacular sea views in Manilva. Communal pool, private terraces, storage, garage. From € 474,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 46 apartments sea views Manilva",
    "OG_DESCRIPTION": "46 contemporary apartments 2-4 bedrooms with spectacular sea and mountain views in Manilva. Communal pool, private terraces, garage, storage. From € 474,000.",
    "HERO_BG_ALT": "Blue View Heights apartments sea views pool terrace Manilva",
}
