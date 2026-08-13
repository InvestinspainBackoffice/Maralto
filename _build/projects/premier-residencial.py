from urllib.parse import quote

PROJECT_NAME = "Premier Residencial"
PRICE_FROM = "Vanaf € 465.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "premier-residencial",
    "TITLE": f"{PROJECT_NAME} Benalmádena — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Premier Residencial: Moderne wonen aan de Costa del Sol. Luxe appartementen en villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Benalmádena",
    "OG_DESCRIPTION": "Premier Residencial: Moderne appartementen en villas in Benalmádena. Vanaf € 465.000",
    "OG_IMAGE": "https://projects.investinspain.be/images/premier-residencial/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/premier-residencial/hero.webp",
    "HERO_BG_ALT": "Premier Residencial — moderne appartementen in Benalmádena",
    "HERO_NAME": "Premier Residencial",
    "HERO_LOCATION": "BENALMÁDENA",
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
    "META_DESCRIPTION": "Premier Residencial: Modern living on the Costa del Sol. Luxury apartments and villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Benalmádena",
    "OG_DESCRIPTION": "Premier Residencial: Modern apartments and villas in Benalmádena. Vanaf € 465.000",
    "HERO_BG_ALT": "Premier Residencial — modern apartments in Benalmádena",
}

HUB = {
    "NAME": "Premier Residencial",
    "LOCATION": "Benalmádena",
    "PRICE": "Vanaf € 465.000",
    "THUMB": "https://projects.investinspain.be/images/premier-residencial/hero.webp",
    "LAT": 36.5942,
    "LNG": -4.7195,
    "HREF": "/premier-residencial/",
}
