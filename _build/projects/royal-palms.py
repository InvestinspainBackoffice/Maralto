from urllib.parse import quote

PROJECT_NAME = "Royal Palms"
PRICE_FROM = "Vanaf € 659.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "royal-palms",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Royal Palms Mijas: resort-stijl project met 1-3 slaapkamer appartementen en penthouses in La Cala de Mijas. Zeezicht, zwembad met strandzone, fitness, speelzone. Vanaf € 659.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Resort-stijl 1-3 slpk La Cala de Mijas",
    "OG_DESCRIPTION": "Resort-stijl project met ruime appartementen en penthouses in La Cala de Mijas. Zeezicht, zwembad met strandzone, fitness, golfbanen in de buurt. Vanaf € 659.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/royal-palms/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/royal-palms/hero.webp",
    "HERO_BG_ALT": "Royal Palms Mijas zwembad strandzone zeezicht La Cala de Mijas",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "LA CALA DE MIJAS",
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
    "MAP_LAT": "36.505482147585",
    "MAP_LNG": "-4.6918103932198",
}

DATA_EN = {
    "META_DESCRIPTION": "Royal Palms Mijas: resort-style project with 1-3 bedroom apartments and penthouses in La Cala de Mijas. Sea views, beach-style pool, fitness, play area. From € 659,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Resort-style 1-3 bed La Cala de Mijas",
    "OG_DESCRIPTION": "Resort-style project with spacious apartments and penthouses in La Cala de Mijas. Sea views, beach-style pool, fitness, golf courses nearby. From € 659,000.",
    "HERO_BG_ALT": "Royal Palms Mijas pool beach zone sea views La Cala de Mijas",
}
