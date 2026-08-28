from urllib.parse import quote

PROJECT_NAME = "Amaris Villas"
PRICE_FROM = "Vanaf € 1.520.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "amaris-villas",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Amaris Villas: moderne designvilla's met zeezicht en golfomgeving in Estepona. Privé zwembad, solarium, en-suite badkamers en privé tuin. Vanaf €1.520.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Designvilla's met Zeezicht in Estepona",
    "OG_DESCRIPTION": "Ontdek Amaris Villas: exclusieve villa's in Estepona met panoramisch zeezicht, privé zwembad, solarium en hoogwaardige afwerking. Nabij golf en stranden. Vanaf €1.520.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/amaris-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/amaris-villas/hero.webp",
    "HERO_BG_ALT": "Amaris Villas — moderne designvilla met zeezicht in Estepona",
    "HERO_NAME": "AMARIS VILLAS",
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
    "META_DESCRIPTION": "Amaris Villas: modern design villas with sea views and golf surroundings in Estepona. Private pool, solarium, en-suite bathrooms and private garden. From €1,520,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Design Villas with Sea Views in Estepona",
    "OG_DESCRIPTION": "Discover Amaris Villas: exclusive villas in Estepona with panoramic sea views, private pool, solarium and high-end finishes. Near golf and beaches. From €1,520,000.",
    "HERO_BG_ALT": "Amaris Villas — modern design villa with sea views in Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/amaris-villas/hero.webp",
    "LAT": 36.421852,
    "LNG": -5.200932,
    "HREF": "/amaris-villas/",
}
