from urllib.parse import quote

PROJECT_NAME = "Lomas Unique"
PRICE_FROM = "Vanaf € 620.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "lomas-unique",
    "TITLE": f"{PROJECT_NAME} El Higuerón Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Lomas Unique: Garden Villas, appartementen en Sky Penthouses in het El Higuerón resort in Fuengirola. Luxe met zeezicht, zwembad en privégarage. Vanaf € 620.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Garden Villas & Sky Penthouses El Higuerón",
    "OG_DESCRIPTION": "Exclusief woonconcept in El Higuerón, Fuengirola: Garden Villas, Unique Apartments en Sky Solarium Penthouses. Zwembad, groen, garage, zeezicht. Vanaf € 620.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/lomas-unique/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/lomas-unique/hero.webp",
    "HERO_BG_ALT": "Lomas Unique El Higuerón resort Fuengirola gemeenschappelijke zones",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "EL HIGUERÓN, FUENGIROLA",
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
    "MAP_LAT": "36.570289904719",
    "MAP_LNG": "-4.5981712330243",
}

DATA_EN = {
    "META_DESCRIPTION": "Lomas Unique: Garden Villas, apartments and Sky Penthouses in the El Higuerón resort in Fuengirola. Luxury with sea views, pool and private garage. From € 620,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Garden Villas & Sky Penthouses El Higuerón",
    "OG_DESCRIPTION": "Exclusive residential concept at El Higuerón, Fuengirola: Garden Villas, Unique Apartments and Sky Solarium Penthouses. Pool, gardens, garage, sea views. From € 620,000.",
    "HERO_BG_ALT": "Lomas Unique El Higuerón resort Fuengirola communal areas",
}
