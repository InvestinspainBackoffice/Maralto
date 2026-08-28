from urllib.parse import quote

PROJECT_NAME = "Birdie Hills"
PRICE_FROM = "Vanaf € 320.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "birdie-hills",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Birdie Hills: 68 nieuwe woningen met 1 tot 3 slaapkamers, in de golfenclave van Estepona. Buitenzwembad, solariumzwembad en social club. Vanaf €320.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Birdie Hills: modern wonen met panoramisch golfzicht, ruime terrassen en een social club, aan de golfbaan van Estepona. Vanaf €320.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/06/Birdie-Hills-Estepona_208_INFOGRAFIAS-ANTEPROYECTO-2-5-1.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/06/Birdie-Hills-Estepona_208_INFOGRAFIAS-ANTEPROYECTO-2-5-1.jpg",
    "HERO_BG_ALT": "Birdie Hills — modern wooncomplex aan de golfbaan van Estepona",
    "HERO_NAME": "BIRDIE HILLS",
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
    "META_DESCRIPTION": "Birdie Hills: 68 new homes with 1 to 3 bedrooms, in the golf enclave of Estepona. Outdoor swimming pool, solarium pool and social club. From €320,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Birdie Hills: modern living with panoramic golf views, spacious terraces and a social club, on Estepona's golf course. From €320,000.",
    "HERO_BG_ALT": "Birdie Hills — modern residential complex on Estepona's golf course",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/birdie-hills/thumb.webp",
    "LAT": 36.408796,
    "LNG": -5.210714,
    "HREF": "/birdie-hills/",
}
