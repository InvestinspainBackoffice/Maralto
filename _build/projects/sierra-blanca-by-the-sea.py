from urllib.parse import quote

PROJECT_NAME = "Sierra Blanca by the Sea"
PRICE_FROM = "Vanaf € 2.950.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "sierra-blanca-by-the-sea",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Sierra Blanca by the Sea: exclusieve frontline residenties op de New Golden Mile in Estepona. 6 villa's en 42 appartementen & penthouses met panoramisch zeezicht. Vanaf €2.950.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline Villa's, Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Sierra Blanca by the Sea: een van de laatste frontline percelen aan de Costa del Sol, met spa, binnenzwembad, padelveld en 24/7 conciërgeservice. Vanaf €2.950.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/04/Sierra-Blanca-by-the-Sea.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/04/Sierra-Blanca-by-the-Sea.jpg",
    "HERO_BG_ALT": "Sierra Blanca by the Sea — residentie met tuinen en zwembaden aan zee",
    "HERO_NAME": "SIERRA BLANCA",
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

DATA_EN = {
    "META_DESCRIPTION": "Sierra Blanca by the Sea: exclusive frontline residences on the New Golden Mile in Estepona. 6 villas and 42 apartments & penthouses with panoramic sea views. From €2,950,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline Villas, Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Sierra Blanca by the Sea: one of the last frontline plots on the Costa del Sol, with spa, indoor pool, padel court and 24/7 concierge service. From €2,950,000.",
    "HERO_BG_ALT": "Sierra Blanca by the Sea — residence with gardens and pools by the sea",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/sierra-blanca-by-the-sea/thumb.webp",
    "LAT": 36.430101,
    "LNG": -5.123605,
    "HREF": "/sierra-blanca-by-the-sea/",
}
