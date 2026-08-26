from urllib.parse import quote

PROJECT_NAME = "Ocean View Marbella"
PRICE_FROM = "Vanaf € 960.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "ocean-view-marbella-2",
    "TITLE": f"{PROJECT_NAME} MARBELLA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Ocean View Marbella: 44 exclusieve residenties met 2-3 slaapkamers en 10 penthouses met privézwembad, nabij natuurreservaat. Vanaf € 960.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve residenties met zeezicht in Marbella",
    "OG_DESCRIPTION": "44 residenties met verwarmd zwembad, conciergeservice en 24u beveiliging in de heuvels van Marbella nabij een beschermd natuurreservaat.",
    "OG_IMAGE": "https://projects.investinspain.be/images/ocean-view-marbella-2/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/ocean-view-marbella-2/hero.webp",
    "HERO_BG_ALT": "Ocean View Marbella — leisure club met verwarmd zwembad en zeezicht",
    "HERO_NAME": "Ocean View Marbella",
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
    "META_DESCRIPTION": "Ocean View Marbella: 44 exclusive residences with 2-3 bedrooms and 10 penthouses with private pool, near nature reserve. From € 960,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive residences with sea views in Marbella",
    "OG_DESCRIPTION": "44 residences with heated pool, concierge service and 24h security in the hills of Marbella near a protected nature reserve.",
    "HERO_BG_ALT": "Ocean View Marbella — leisure club with heated pool and sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/ocean-view-marbella-2/hero.webp",
    "LAT": 36.502843,
    "LNG": -4.913942,
    "HREF": "/ocean-view-marbella-2/",
}
