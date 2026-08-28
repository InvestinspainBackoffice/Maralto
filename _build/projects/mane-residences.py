from urllib.parse import quote

PROJECT_NAME = "Mane Residences"
PRICE_FROM = "Vanaf € 614.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "mane-residences",
    "TITLE": f"{PROJECT_NAME} Benalmádena — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Mane Residences: nieuwbouwappartementen met 2-3 slaapkamers en panoramisch zeezicht in Benalmádena. Prijzen vanaf € 614.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met Zeezicht in Benalmádena",
    "OG_DESCRIPTION": "Nieuwbouwappartementen met 2-3 slaapkamers en panoramisch zeezicht in Benalmádena. Ontdek Mane Residences via INVESTINSPAIN.BE.",
    "OG_IMAGE": "https://projects.investinspain.be/images/mane-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/mane-residences/hero.webp",
    "HERO_BG_ALT": "Mane Residences Benalmádena exterieur zeezicht",
    "HERO_NAME": "Mane Residences",
    "HERO_LOCATION": "BENALMÁDENA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Mane Residences: new build apartments with 2-3 bedrooms and panoramic sea views in Benalmádena. Prices from € 614,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with Sea Views in Benalmádena",
    "OG_DESCRIPTION": "New build apartments with 2-3 bedrooms and panoramic sea views in Benalmádena. Discover Mane Residences via INVESTINSPAIN.BE.",
    "HERO_BG_ALT": "Mane Residences Benalmádena exterior sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benalmádena",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/mane-residences/hero.webp",
    "LAT": 36.602349,
    "LNG": -4.562922,
    "HREF": "/mane-residences/",
}
