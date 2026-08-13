from urllib.parse import quote

PROJECT_NAME = "Sunway Residence"
PRICE_FROM = "Vanaf € 480.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "sunway-residence",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Sunway Residence: 48 appartementen met 3 slaapkamers, terrassen en gated community in Estepona. Vanaf € 480.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "48 moderne appartementen met 3 slaapkamers en gated community in Estepona.",
    "OG_IMAGE": "https://projects.investinspain.be/images/sunway-residence/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/sunway-residence/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Appartementen in Estepona",
    "HERO_NAME": "Sunway Residence",
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
    "META_DESCRIPTION": "Sunway Residence: 48 apartments with 3 bedrooms, terraces and gated community in Estepona. From € 480,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "48 modern apartments with 3 bedrooms and gated community in Estepona.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Apartments in Estepona",
}

HUB = {
    "NAME": "Sunway Residence",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 480.000",
    "THUMB": "https://projects.investinspain.be/images/sunway-residence/hero.webp",
    "LAT": 36.411673,
    "LNG": -5.193465,
    "HREF": "/sunway-residence/",
}
