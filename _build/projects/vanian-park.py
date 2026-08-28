from urllib.parse import quote

PROJECT_NAME = "Vanian Park"
PRICE_FROM = "Vanaf € 469.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vanian-park",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vanian Park: exclusieve residentie van 50 hoogwaardige woningen in Estepona, ontworpen voor comfort, design en natuur. Vanaf €469.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne Woningen",
    "OG_DESCRIPTION": "Ontdek Vanian Park: moderne architectuur te midden van natuur, met waterbesparende tuinen, zwembad en fitnessruimte in Estepona. Vanaf €469.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/08/Entry-scaled.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/08/Entry-scaled.jpg",
    "HERO_BG_ALT": "Vanian Park — moderne gebouwen tussen groene tuinen",
    "HERO_NAME": "VANIAN PARK",
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
    "META_DESCRIPTION": "Vanian Park: an exclusive residence of 50 high-quality homes in Estepona, designed for comfort, design and nature. From €469,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Homes",
    "OG_DESCRIPTION": "Discover Vanian Park: modern architecture amid nature, with water-saving gardens, pool and fitness room in Estepona. From €469,000.",
    "HERO_BG_ALT": "Vanian Park — modern buildings amid green gardens",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/vanian-park/thumb.webp",
    "LAT": 36.461727,
    "LNG": -5.084428,
    "HREF": "/vanian-park/",
}
