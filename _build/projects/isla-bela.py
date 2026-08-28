from urllib.parse import quote

PROJECT_NAME = "Isla Bela"
PRICE_FROM = "Vanaf € 820.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "isla-bela",
    "TITLE": f"{PROJECT_NAME} MARBELLA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Isla Bela Marbella: exclusieve appartementen met spa, gym en infinity-pool. Uniek resort-gevoel in het hart van de Costa del Sol. Vanaf € 820.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve residenties met spa & infinity-pool in Marbella",
    "OG_DESCRIPTION": "Isla Bela combineert resort-luxe met residentieel wooncomfort: spa, gym, infinity-pool en stijlvolle interieurs in Marbella. Tijdloze elegantie aan de Costa del Sol.",
    "OG_IMAGE": "https://projects.investinspain.be/images/isla-bela/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/isla-bela/hero.webp",
    "HERO_BG_ALT": "Isla Bela — exclusief appartementencomplex met infinity-pool en spa in Marbella",
    "HERO_NAME": "Isla Bela",
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
    "META_DESCRIPTION": "Isla Bela Marbella: exclusive apartments with spa, gym and infinity pool. Unique resort feeling in the heart of the Costa del Sol. From € 820,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive residences with spa & infinity pool in Marbella",
    "OG_DESCRIPTION": "Isla Bela combines resort luxury with residential comfort: spa, gym, infinity pool and stylish interiors in Marbella. Timeless elegance on the Costa del Sol.",
    "HERO_BG_ALT": "Isla Bela — exclusive apartment complex with infinity pool and spa in Marbella",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/isla-bela/hero.webp",
    "LAT": 36.496995,
    "LNG": -4.966135,
    "HREF": "/isla-bela/",
}
