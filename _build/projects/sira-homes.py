from urllib.parse import quote

PROJECT_NAME = "Sira Homes"
PRICE_FROM = "Vanaf € 425.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "sira-homes",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Sira Homes: Moderne wonen aan de Costa del Sol. Luxe appartementen en villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "Sira Homes: Moderne appartementen en villas in Estepona. Vanaf € 425.000",
    "OG_IMAGE": "https://projects.investinspain.be/images/sira-homes/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/sira-homes/hero.webp",
    "HERO_BG_ALT": "Sira Homes — moderne appartementen in Estepona",
    "HERO_NAME": "Sira Homes",
    "HERO_LOCATION": "ELVIRIA, MARBELLA",
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
    "META_DESCRIPTION": "Sira Homes: Modern living on the Costa del Sol. Luxury apartments and villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "Sira Homes: Modern apartments and villas in Estepona. Vanaf € 425.000",
    "HERO_BG_ALT": "Sira Homes — modern apartments in Estepona",
}

HUB = {
    "NAME": "Sira Homes",
    "LOCATION": "Elviria",
    "PRICE": "Vanaf € 425.000",
    "THUMB": "https://projects.investinspain.be/images/sira-homes/hero.webp",
    "LAT": 36.510711,
    "LNG": -4.776275,
    "HREF": "/sira-homes/",
}
