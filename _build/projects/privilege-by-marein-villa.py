from urllib.parse import quote

PROJECT_NAME = "Privilege By Marein"
PRICE_FROM = "€ 10.000.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "privilege-by-marein-villa",
    "TITLE": f"{PROJECT_NAME} Cortijo Blanco San Pedro — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Privilege By Marein: unieke turnkey frontline beach villa in Cortijo Blanco, San Pedro de Alcántara. 4 niveaus, infinity zwembad, privé bioscoopzaal en rooftop solarium. € 10.000.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Frontline beach villa San Pedro",
    "OG_DESCRIPTION": "Turnkey villa direct aan het strand in Cortijo Blanco, op 1,5 km van Puerto Banús. 4 niveaus, binnenzwembad, bioscoopzaal, rooftop solarium. Ontworpen door Ismael Mérida.",
    "OG_IMAGE": "https://projects.investinspain.be/images/privilege-by-marein-villa/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/privilege-by-marein-villa/hero.webp",
    "HERO_BG_ALT": "Privilege By Marein frontline beach villa San Pedro Cortijo Blanco",
    "HERO_NAME": "Privilege By Marein",
    "HERO_LOCATION": "CORTIJO BLANCO, SAN PEDRO DE ALCÁNTARA",
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
    "META_DESCRIPTION": "Privilege By Marein: unique turnkey frontline beach villa in Cortijo Blanco, San Pedro de Alcántara. 4 levels, infinity pool, private cinema and rooftop solarium. € 10,000,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Frontline beach villa San Pedro",
    "OG_DESCRIPTION": "Turnkey villa directly on the beach in Cortijo Blanco, 1.5 km from Puerto Banús. 4 levels, indoor pool, cinema room, rooftop solarium. Designed by Ismael Mérida.",
    "HERO_BG_ALT": "Privilege By Marein frontline beach villa San Pedro Cortijo Blanco",
}
