from urllib.parse import quote

PROJECT_NAME = "Epic Marbella"
PRICE_FROM = "Vanaf € 3.750.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "epic-marbella",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Epic Marbella: tijdloze ultra-luxe appartementen op 5 minuten van het strand in Marbella. Privézwembad, eigen lift en spectaculaire zeezichten. Vanaf €3.750.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-Luxe Appartementen in Marbella",
    "OG_DESCRIPTION": "Ontdek Epic Marbella: tijdloze ultra-luxe appartementen met privézwembad, eigen lift en panoramisch zeezicht. Op 5 minuten van het strand in Marbella. Vanaf €3.750.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/epic-marbella/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/epic-marbella/hero.webp",
    "HERO_BG_ALT": "Epic Marbella — ultra-luxe appartementencomplex vlak bij het strand in Marbella",
    "HERO_NAME": "EPIC MARBELLA",
    "HERO_LOCATION": "MARBELLA",
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
    "META_DESCRIPTION": "Epic Marbella: timeless ultra-luxury apartments 5 minutes from the beach in Marbella. Private pool, private lift and spectacular sea views. From €3,750,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-Luxury Apartments in Marbella",
    "OG_DESCRIPTION": "Discover Epic Marbella: timeless ultra-luxury apartments with private pool, private lift and panoramic sea views. Just 5 minutes from the beach in Marbella. From €3,750,000.",
    "HERO_BG_ALT": "Epic Marbella — ultra-luxury apartment complex near the beach in Marbella",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/epic-marbella/hero.webp",
    "LAT": 36.502843,
    "LNG": -4.913942,
    "HREF": "/epic-marbella/",
}
