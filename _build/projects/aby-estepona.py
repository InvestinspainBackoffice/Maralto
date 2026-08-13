from urllib.parse import quote

PROJECT_NAME = "Aby Estepona"
PRICE_FROM = "Prijs op aanvraag"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "aby-estepona",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Aby Estepona: Moderne wonen aan de Costa del Sol. Luxe appartementen en villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "Aby Estepona: Moderne appartementen en villas in Estepona. Prijs op aanvraag",
    "OG_IMAGE": "https://projects.investinspain.be/images/aby-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/aby-estepona/hero.webp",
    "HERO_BG_ALT": "Aby Estepona — moderne appartementen in Estepona",
    "HERO_NAME": "Aby Estepona",
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
    "META_DESCRIPTION": "Aby Estepona: Modern living on the Costa del Sol. Luxury apartments and villas.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "Aby Estepona: Modern apartments and villas in Estepona. Prijs op aanvraag",
    "HERO_BG_ALT": "Aby Estepona — modern apartments in Estepona",
}

HUB = {
    "NAME": "Aby Estepona",
    "LOCATION": "Estepona",
    "PRICE": "Prijs op aanvraag",
    "THUMB": "https://projects.investinspain.be/images/aby-estepona/hero.webp",
    "LAT": 36.4304,
    "LNG": -5.1355,
    "HREF": "/aby-estepona/",
}
