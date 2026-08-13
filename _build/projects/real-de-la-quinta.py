from urllib.parse import quote

PROJECT_NAME = "Real de la Quinta"
PRICE_FROM = "Vanaf € 890.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "real-de-la-quinta",
    "TITLE": f"{PROJECT_NAME} Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Real de la Quinta: Moderne wonen aan de Costa del Sol. Luxe appartementen en villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Marbella",
    "OG_DESCRIPTION": "Real de la Quinta: Moderne appartementen en villas in Marbella. Vanaf € 890.000",
    "OG_IMAGE": "https://projects.investinspain.be/images/real-de-la-quinta/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/real-de-la-quinta/hero.webp",
    "HERO_BG_ALT": "Real de la Quinta — moderne appartementen in Marbella",
    "HERO_NAME": "Real de la Quinta",
    "HERO_LOCATION": "MARBELLA",
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
    "META_DESCRIPTION": "Real de la Quinta: Modern living on the Costa del Sol. Luxury apartments and villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Marbella",
    "OG_DESCRIPTION": "Real de la Quinta: Modern apartments and villas in Marbella. Vanaf € 890.000",
    "HERO_BG_ALT": "Real de la Quinta — modern apartments in Marbella",
}

HUB = {
    "NAME": "Real de la Quinta",
    "LOCATION": "Marbella",
    "PRICE": "Vanaf € 890.000",
    "THUMB": "https://projects.investinspain.be/images/real-de-la-quinta/hero.webp",
    "LAT": 36.5105,
    "LNG": -4.9211,
    "HREF": "/real-de-la-quinta/",
}
