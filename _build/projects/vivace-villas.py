from urllib.parse import quote

PROJECT_NAME = "Vivace Villas"
PRICE_FROM = "Prijs op aanvraag"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vivace-villas",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vivace Villas: collectie van 30 exclusieve villa's met 3 of 4 slaapkamers in Valle Romano, Estepona. Drie typologieën, passieve architectuur, privé tuin en zwembad.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve Villa's",
    "OG_DESCRIPTION": "Ontdek Vivace Villas: moderne elegantie en de rust van een golfbaan in Valle Romano, met privé tuin, zwembad en berg- en zeezicht.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/06/vivace-villas-T2-1.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/06/vivace-villas-T2-1.jpg",
    "HERO_BG_ALT": "Vivace Villas — villa met zwembad bij avondlicht",
    "HERO_NAME": "VIVACE VILLAS",
    "HERO_LOCATION": "ESTEPONA",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "PRICE_LABEL": "Prijs",
    "PRICE_AMOUNT": "op aanvraag",
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
    "META_DESCRIPTION": "Vivace Villas: a collection of 30 exclusive villas with 3 or 4 bedrooms in Valle Romano, Estepona. Three typologies, passive architecture, private garden and pool.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive Villas",
    "OG_DESCRIPTION": "Discover Vivace Villas: modern elegance and the tranquillity of a golf course in Valle Romano, with private garden, pool and mountain and sea views.",
    "HERO_BG_ALT": "Vivace Villas — villa with swimming pool at dusk",
    "PRICE_FROM": "Price on request",
    "HERO_PRICE": "Price on request",
    "PRICE_LABEL": "Price",
    "PRICE_AMOUNT": "on request",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2025/06/vivace-villas-T2-1.jpg",
    "LAT": 36.423702016702,
    "LNG": -5.19424670248,
    "HREF": "/vivace-villas/",
}
