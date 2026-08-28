from urllib.parse import quote

PROJECT_NAME = "Atria"
PRICE_FROM = "Vanaf € 550.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "atria",
    "TITLE": f"{PROJECT_NAME} Torremolinos — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Atria: Moderne wonen aan de Costa del Sol. Luxe appartementen en villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Torremolinos",
    "OG_DESCRIPTION": "Atria: Moderne appartementen en villas in Torremolinos. Vanaf € 550.000",
    "OG_IMAGE": "https://projects.investinspain.be/images/atria/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/atria/hero.webp",
    "HERO_BG_ALT": "Atria — moderne appartementen in Torremolinos",
    "HERO_NAME": "Atria",
    "HERO_LOCATION": "LA ALCAIDESA",
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
    "META_DESCRIPTION": "Atria: Modern living on the Costa del Sol. Luxury apartments and villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Torremolinos",
    "OG_DESCRIPTION": "Atria: Modern apartments and villas in Torremolinos. Vanaf € 550.000",
    "HERO_BG_ALT": "Atria — modern apartments in Torremolinos",
}

HUB = {
    "NAME": "Atria",
    "LOCATION": "La Alcaidesa",
    "PRICE": "Vanaf € 550.000",
    "THUMB": "https://projects.investinspain.be/images/atria/hero.webp",
    "LAT": 36.237538,
    "LNG": -5.331402,
    "HREF": "/atria/",
}
