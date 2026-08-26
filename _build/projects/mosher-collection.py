from urllib.parse import quote

PROJECT_NAME = "Mosher Collection"
PRICE_FROM = "Vanaf € 820.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "mosher-collection",
    "TITLE": f"{PROJECT_NAME} Benalmádena — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Mosher Collection: 44 exclusieve residenties met 1 tot 3 slaapkamers en panoramisch zeezicht in Rancho Domingo, Benalmádena. Vanaf €820.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve Residenties met Panoramisch Zeezicht",
    "OG_DESCRIPTION": "Ontdek Mosher Collection: 44 gelijkvloerse appartementen en penthouses geïnspireerd op de architectuur van Robert Mosher, met gemeenschappelijk zoutwaterzwembad in Rancho Domingo, Benalmádena. Vanaf €820.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/mosher-collection/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/mosher-collection/hero.webp",
    "HERO_BG_ALT": "Mosher Collection — residenties tegen de heuvel van Rancho Domingo",
    "HERO_NAME": "MOSHER COLLECTION",
    "HERO_LOCATION": "BENALMÁDENA",
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
    "META_DESCRIPTION": "Mosher Collection: 44 exclusive residences with 1 to 3 bedrooms and panoramic sea views in Rancho Domingo, Benalmádena. From €820,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive Residences with Panoramic Sea Views",
    "OG_DESCRIPTION": "Discover Mosher Collection: 44 ground-floor apartments and penthouses inspired by the architecture of Robert Mosher, with a communal saltwater pool in Rancho Domingo, Benalmádena. From €820,000.",
    "HERO_BG_ALT": "Mosher Collection — residences set into the Rancho Domingo hillside",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benalmádena",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/mosher-collection/hero.webp",
    "LAT": 36.587585,
    "LNG": -4.645059,
    "HREF": "/mosher-collection/",
}
