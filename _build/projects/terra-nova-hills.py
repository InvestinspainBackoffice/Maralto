from urllib.parse import quote

PROJECT_NAME = "Terra Nova Hills"
PRICE_FROM = "Vanaf € 395.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "terra-nova-hills",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Terra Nova Hills: Moderne wonen aan de Costa del Sol. Luxe appartementen en villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "Terra Nova Hills: Moderne appartementen en villas in Estepona. Vanaf € 395.000",
    "OG_IMAGE": "https://projects.investinspain.be/images/terra-nova-hills/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/terra-nova-hills/hero.webp",
    "HERO_BG_ALT": "Terra Nova Hills — moderne appartementen in Estepona",
    "HERO_NAME": "Terra Nova Hills",
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
    "META_DESCRIPTION": "Terra Nova Hills: Modern living on the Costa del Sol. Luxury apartments and villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "Terra Nova Hills: Modern apartments and villas in Estepona. Vanaf € 395.000",
    "HERO_BG_ALT": "Terra Nova Hills — modern apartments in Estepona",
}

HUB = {
    "NAME": "Terra Nova Hills",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 395.000",
    "THUMB": "https://projects.investinspain.be/images/terra-nova-hills/hero.webp",
    "LAT": 36.4452,
    "LNG": -5.1502,
    "HREF": "/terra-nova-hills/",
}
