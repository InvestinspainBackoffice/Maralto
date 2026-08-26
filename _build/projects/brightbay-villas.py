from urllib.parse import quote

PROJECT_NAME = "Brightbay Villas"
PRICE_FROM = "Vanaf € 1.950.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "brightbay-villas",
    "TITLE": f"{PROJECT_NAME} La Herradura — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Brightbay: 14 exclusieve luxevilla's met 3 slaapkamers en privé-infinity zwembad aan de baai van La Herradura, Costa Tropical. Vanaf €1.950.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxevilla's aan de Baai van La Herradura",
    "OG_DESCRIPTION": "Ontdek Brightbay: 14 frontline-strand villa's met panoramisch bayzicht, privé-infinity zwembad en dubbelhoge leefruimte in La Herradura, Costa Tropical. Vanaf €1.950.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/brightbay-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/brightbay-villas/hero.webp",
    "HERO_BG_ALT": "Brightbay Villas — luchtfoto van de villa's aan de baai van La Herradura",
    "HERO_NAME": "BRIGHTBAY VILLAS",
    "HERO_LOCATION": "LA HERRADURA",
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
    "META_DESCRIPTION": "Brightbay: 14 exclusive luxury villas with 3 bedrooms and a private infinity pool on the bay of La Herradura, Costa Tropical. From €1,950,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Villas on the Bay of La Herradura",
    "OG_DESCRIPTION": "Discover Brightbay: 14 frontline-beach villas with panoramic bay views, a private infinity pool and a double-height living space in La Herradura, Costa Tropical. From €1,950,000.",
    "HERO_BG_ALT": "Brightbay Villas — aerial view of the villas on the bay of La Herradura",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Herradura",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/brightbay-villas/hero.webp",
    "LAT": 36.728,
    "LNG": -3.733,
    "HREF": "/brightbay-villas/",
}
