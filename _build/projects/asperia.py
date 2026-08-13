from urllib.parse import quote

PROJECT_NAME = "Asperia"
PRICE_FROM = "Vanaf € 530.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "asperia",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Asperia: 43 appartementen in Estepona met 1-3 slaapkamers. Zwembad, fitness, parkeergarage. Vanaf € 530.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "Asperia: Moderne appartementen in het centrum van Estepona met zwembad, fitness en luxe voorzieningen. Vanaf € 530.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/asperia/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/asperia/hero.webp",
    "HERO_BG_ALT": "Asperia — moderne appartementen in het centrum van Estepona",
    "HERO_NAME": "Asperia",
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
    "META_DESCRIPTION": "Asperia: 43 apartments in Estepona with 1-3 bedrooms. Pool, fitness, parking garage. From € 530,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "Asperia: Modern apartments in the center of Estepona with pool, fitness and luxury amenities. From € 530,000.",
    "HERO_BG_ALT": "Asperia — modern apartments in the center of Estepona",
}

HUB = {
    "NAME": "Asperia",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 530.000",
    "THUMB": "https://projects.investinspain.be/images/asperia/hero.webp",
    "LAT": 36.4304,
    "LNG": -5.1355,
    "HREF": "/asperia/",
}
