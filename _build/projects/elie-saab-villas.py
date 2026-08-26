from urllib.parse import quote

PROJECT_NAME = "Elie Saab Villas"
PRICE_FROM = "Vanaf € 8.300.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "elie-saab-villas",
    "TITLE": f"{PROJECT_NAME} Sierra Blanca Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Elie Saab Villas: 5 prestigieuze villa's in Sierra Blanca, Marbella. ±1.000 m² op percelen van ±2.200 m², 4 slaapkamers, infinity zwembad, jacuzzi, lift en domotica. Vanaf € 8.300.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Sierra Blanca Marbella",
    "OG_DESCRIPTION": "Slechts 5 ultra-luxe villa's in Sierra Blanca, Marbella. Ontworpen in samenwerking met Elie Saab: ±1.000 m², prachtig zeezicht, privézwembad, jacuzzi, sauna en lift.",
    "OG_IMAGE": "https://projects.investinspain.be/images/elie-saab-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/elie-saab-villas/hero.webp",
    "HERO_BG_ALT": "Elie Saab Villas Sierra Blanca Marbella infinity pool zeezicht",
    "HERO_NAME": "Elie Saab Villas",
    "HERO_LOCATION": "SIERRA BLANCA, MARBELLA",
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
    "META_DESCRIPTION": "Elie Saab Villas: 5 prestigious villas in Sierra Blanca, Marbella. ±1,000 m² on plots of ±2,200 m², 4 bedrooms, infinity pool, jacuzzi, elevator and smart home. From € 8,300,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Sierra Blanca Marbella",
    "OG_DESCRIPTION": "Just 5 ultra-luxury villas in Sierra Blanca, Marbella. Designed in collaboration with Elie Saab: ±1,000 m², stunning sea views, private pool, jacuzzi, sauna and elevator.",
    "HERO_BG_ALT": "Elie Saab Villas Sierra Blanca Marbella infinity pool sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Sierra Blanca, Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/elie-saab-villas/hero.webp",
    "LAT": 36.517,
    "LNG": -4.916,
    "HREF": "/elie-saab-villas/",
}
