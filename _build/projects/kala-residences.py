from urllib.parse import quote

PROJECT_NAME = "Kala Residences"
PRICE_FROM = "Vanaf € 995.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "kala-residences",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Kala Residences: stijlvolle townhouses met 2 en 3 slaapkamers nabij zee en voorzieningen in El Higuerón, Fuengirola. Vanaf €995.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses in een Toplocatie nabij Zee",
    "OG_DESCRIPTION": "Ontdek Kala Residences: townhouses met grote raampartijen, gemeenschappelijk zwembad en groene zones, op wandelafstand van het strand in El Higuerón. Vanaf €995.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/kala-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/kala-residences/hero.webp",
    "HERO_BG_ALT": "Kala Residences — luchtfoto van het complex tegen de bergen",
    "HERO_NAME": "KALA RESIDENCES",
    "HERO_LOCATION": "FUENGIROLA",
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
    "META_DESCRIPTION": "Kala Residences: stylish townhouses with 2 and 3 bedrooms close to the sea and amenities in El Higuerón, Fuengirola. From €995,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses in a Prime Location near the Sea",
    "OG_DESCRIPTION": "Discover Kala Residences: townhouses with large windows, a communal pool and green zones, within walking distance of the beach in El Higuerón. From €995,000.",
    "HERO_BG_ALT": "Kala Residences — aerial view of the complex against the mountains",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Fuengirola",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/kala-residences/hero.webp",
    "LAT": 36.584146,
    "LNG": -4.601868,
    "HREF": "/kala-residences/",
}
