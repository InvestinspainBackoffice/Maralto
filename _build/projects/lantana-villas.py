from urllib.parse import quote

PROJECT_NAME = "Lantana Villa's"
PRICE_FROM = "Vanaf € 1.650.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "lantana-villas",
    "TITLE": f"{PROJECT_NAME} Calahonda — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Lantana Villa's: 7 exclusieve villa's met 4 tot 6 slaapkamers, privézwembad en solarium in Calahonda, vlakbij zee. Vanaf € 1.650.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxevilla's aan de kust van Calahonda",
    "OG_DESCRIPTION": "Lantana Villa's: ruime percelen, privézwembaden, sanitair van Roca en Cisal en twee parkeerplaatsen per villa in Calahonda. Vanaf € 1.650.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/lantana-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/lantana-villas/hero.webp",
    "HERO_BG_ALT": "Lantana Villa's — luxevilla's met privézwembad in Calahonda",
    "HERO_NAME": "Lantana Villa's",
    "HERO_LOCATION": "CALAHONDA",
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
    "META_DESCRIPTION": "Lantana Villas: 7 exclusive villas with 4 to 6 bedrooms, private pool and solarium in Calahonda, close to the sea. From € 1,650,000.",
    "OG_TITLE": "Lantana Villas — Luxury villas on the Calahonda coast",
    "OG_DESCRIPTION": "Lantana Villas: spacious plots, private pools, Roca and Cisal bathroom fittings and two parking spaces per villa in Calahonda. From € 1,650,000.",
    "HERO_BG_ALT": "Lantana Villas — luxury villas with private pool in Calahonda",
    "HERO_NAME": "Lantana Villas",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Calahonda",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/lantana-villas/hero.webp",
    "LAT": 36.489656,
    "LNG": -4.722085,
    "HREF": "/lantana-villas/",
}
