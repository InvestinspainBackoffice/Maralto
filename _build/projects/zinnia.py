from urllib.parse import quote

PROJECT_NAME = "Zinnia"
PRICE_FROM = "Vanaf € 320.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "zinnia",
    "TITLE": f"{PROJECT_NAME} Nerja — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Zinnia: Moderne wonen aan de Costa del Sol. Luxe appartementen en villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Nerja",
    "OG_DESCRIPTION": "Zinnia: Moderne appartementen en villas in Nerja. Vanaf € 320.000",
    "OG_IMAGE": "https://projects.investinspain.be/images/zinnia/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/zinnia/hero.webp",
    "HERO_BG_ALT": "Zinnia — moderne appartementen in Nerja",
    "HERO_NAME": "Zinnia",
    "HERO_LOCATION": "SAN PEDRO DE ALCÁNTARA",
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
    "META_DESCRIPTION": "Zinnia: Modern living on the Costa del Sol. Luxury apartments and villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Nerja",
    "OG_DESCRIPTION": "Zinnia: Modern apartments and villas in Nerja. Vanaf € 320.000",
    "HERO_BG_ALT": "Zinnia — modern apartments in Nerja",
}

HUB = {
    "NAME": "Zinnia",
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": "Vanaf € 320.000",
    "THUMB": "https://projects.investinspain.be/images/zinnia/hero.webp",
    "LAT": 36.485825,
    "LNG": -4.984455,
    "HREF": "/zinnia/",
}
