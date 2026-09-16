from urllib.parse import quote

PROJECT_NAME = "Atelier 4"
PRICE_FROM = "Vanaf € 3.003.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "atelier-4",
    "TITLE": f"{PROJECT_NAME} by Ikkil Bay — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Atelier 4 by Ikkil Bay: 4 exclusieve strandappartementen met 2 tot 4 slaapkamers in Estepona. Panoramisch zeezicht, verwarmd binnenzwembad, spa. Vanaf € 3.003.000.",
    "OG_TITLE": f"{PROJECT_NAME} by Ikkil Bay · Exclusieve Strandresidenties",
    "OG_DESCRIPTION": "Slechts 4 unieke villa-achtige residenties — Mare, Natura, Stella en Ventu — direct aan het strand in Estepona. Vanaf € 3.003.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/atelier-4/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/atelier-4/hero.webp",
    "HERO_BG_ALT": "Atelier 4 — dakterras bij schemering met panoramisch zeezicht in Estepona",
    "HERO_NAME": "ATELIER 4",
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
    "MAP_LAT": "36.417126",
    "MAP_LNG": "-5.165255",
}

DATA_EN = {
    "META_DESCRIPTION": "Atelier 4 by Ikkil Bay: 4 exclusive beachfront apartments with 2 to 4 bedrooms in Estepona. Panoramic sea views, heated indoor pool, spa. From € 3,003,000.",
    "OG_TITLE": f"{PROJECT_NAME} by Ikkil Bay · Exclusive Beachfront Residences",
    "OG_DESCRIPTION": "Just 4 unique villa-like residences — Mare, Natura, Stella and Ventu — directly on the beach in Estepona. From € 3,003,000.",
    "HERO_BG_ALT": "Atelier 4 — rooftop terrace at dusk with panoramic sea view in Estepona",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/atelier-4/hero.webp",
    "LAT": 36.417126,
    "LNG": -5.165255,
    "HREF": "/atelier-4/",
}
