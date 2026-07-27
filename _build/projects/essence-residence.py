from urllib.parse import quote

PROJECT_NAME = "Essence Residence"
PRICE_FROM = "Vanaf € 754.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "essence-residence",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Essence Residence: ruime, moderne appartementen vlakbij Villa Padierna resort in Estepona. Vanaf €754.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Essence Residence: ontworpen door architect Pablo Villarroel, met spa, fitness, co-working en zwembaden. Vanaf €754.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/02/Essence-Residence-Estepona_31_post-topaz-denoise-1110x623.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/02/Essence-Residence-Estepona_31_post-topaz-denoise-1110x623.jpg",
    "HERO_BG_ALT": "Essence Residence — gebouw met zwembad en palmbomen",
    "HERO_NAME": "ESSENCE RESIDENCE",
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

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2025/02/Essence-Residence-Estepona_31_post-topaz-denoise-1110x623.jpg",
    "LAT": 36.4680914,
    "LNG": -5.0495274,
    "HREF": "/essence-residence/",
}
