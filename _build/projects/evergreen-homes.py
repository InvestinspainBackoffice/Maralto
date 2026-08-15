from urllib.parse import quote

PROJECT_NAME = "Evergreen Homes"
PRICE_FROM = "Vanaf € 747.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "evergreen-homes",
    "TITLE": f"{PROJECT_NAME} La Cala de Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Evergreen Homes: 80 townhouses met 3 en 4 slaapkamers vlakbij El Chaparral, La Cala de Mijas. Omheind complex, gym, gemeenschappelijk buitenzwembad, prachtige natuur. Vanaf € 747.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 80 townhouses 3-4 slpk El Chaparral La Cala",
    "OG_DESCRIPTION": "80 townhouses 3-4 slaapkamers in een omheind complex vlakbij El Chaparral, La Cala de Mijas. Gym, buitenzwembad, groene zones. Vanaf € 747.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/evergreen-homes/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/evergreen-homes/hero.webp",
    "HERO_BG_ALT": "Evergreen Homes townhouses gemeenschappelijke tuin zwembad La Cala de Mijas",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "EL CHAPARRAL, LA CALA DE MIJAS",
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
    "MAP_LAT": "36.510101870132",
    "MAP_LNG": "-4.6612954168841",
}

DATA_EN = {
    "META_DESCRIPTION": "Evergreen Homes: 80 townhouses with 3 and 4 bedrooms near El Chaparral, La Cala de Mijas. Gated complex, gym, communal outdoor pool, beautiful nature. From € 747,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 80 townhouses 3-4 bed El Chaparral La Cala",
    "OG_DESCRIPTION": "80 townhouses 3-4 bedrooms in a gated complex near El Chaparral, La Cala de Mijas. Gym, outdoor pool, green areas. From € 747,000.",
    "HERO_BG_ALT": "Evergreen Homes townhouses communal garden pool La Cala de Mijas",
}
