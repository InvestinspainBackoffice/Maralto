from urllib.parse import quote

PROJECT_NAME = "Marbella Design Hills"
PRICE_FROM = "Prijs op aanvraag"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "marbella-design-hills",
    "TITLE": f"{PROJECT_NAME} — Dolce & Gabbana — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Marbella Design Hills: 92 villa-appartementen en een shoppingcenter in samenwerking met Dolce & Gabbana, op de Golden Mile van Marbella. Prijs op aanvraag.",
    "OG_TITLE": f"{PROJECT_NAME} — In samenwerking met Dolce & Gabbana",
    "OG_DESCRIPTION": "Ontdek Marbella Design Hills: een landmark project van 80.000 m² op de Golden Mile, met beachclub, wandelpromenade en de grootste openlucht kunsttentoonstelling van Spanje. Prijs op aanvraag.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2023/09/Marbella-design-hills-scaled.jpeg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2023/09/Marbella-design-hills-scaled.jpeg",
    "HERO_BG_ALT": "Marbella Design Hills — doorsnede van het gebouw met zeezicht",
    "HERO_NAME": "MARBELLA DESIGN HILLS",
    "HERO_LOCATION": "GOLDEN MILE, MARBELLA",
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
    "META_DESCRIPTION": "Marbella Design Hills: 92 villa-apartments and a shopping center in collaboration with Dolce & Gabbana, on the Golden Mile of Marbella. Price on request.",
    "OG_TITLE": f"{PROJECT_NAME} — In Collaboration with Dolce & Gabbana",
    "OG_DESCRIPTION": "Discover Marbella Design Hills: an 80,000 m² landmark project on the Golden Mile, with beach club, promenade and Spain's largest open-air art exhibition. Price on request.",
    "HERO_BG_ALT": "Marbella Design Hills — cross-section of the building with sea view",
    "PRICE_FROM": "Price on request",
    "HERO_PRICE": "Price on request",
    "PRICE_LABEL": "Price",
    "PRICE_AMOUNT": "on request",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/marbella-design-hills/thumb.webp",
    "LAT": 36.510751,
    "LNG": -4.944059,
    "HREF": "/marbella-design-hills/",
}
