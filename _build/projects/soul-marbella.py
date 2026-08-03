from urllib.parse import quote

PROJECT_NAME = "Soul Marbella"
PRICE_FROM = "Vanaf € 1.500.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "soul-marbella",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Soul Marbella: appartementen, penthouses en villa's met 2 tot 5 slaapkamers vlakbij Santa Clara Golf, Oost-Marbella. Vanaf €1.500.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen, Penthouses & Villa's",
    "OG_DESCRIPTION": "Ontdek Soul Marbella: zorgvuldig ontworpen woningen vol natuurlijk licht, met gedeeld zwembad, gym, sauna en social club vlakbij Santa Clara Golf. Vanaf €1.500.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2020/03/V3_day.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2020/03/V3_day.jpg",
    "HERO_BG_ALT": "Soul Marbella — gedeeld zwembad met cabana's en palmbomen",
    "HERO_NAME": "SOUL MARBELLA",
    "HERO_LOCATION": "OOST-MARBELLA",
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
    "META_DESCRIPTION": "Soul Marbella: apartments, penthouses and villas with 2 to 5 bedrooms near Santa Clara Golf, East Marbella. From €1,500,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments, Penthouses & Villas",
    "OG_DESCRIPTION": "Discover Soul Marbella: carefully designed homes full of natural light, with a shared pool, gym, sauna and social club near Santa Clara Golf. From €1,500,000.",
    "HERO_BG_ALT": "Soul Marbella — shared pool with cabanas and palm trees",
    "HERO_LOCATION": "EAST MARBELLA",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2020/03/V3_day.jpg",
    "LAT": 36.5124,
    "LNG": -4.8300,
    "HREF": "/soul-marbella/",
}
