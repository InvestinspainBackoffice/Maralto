from urllib.parse import quote

PROJECT_NAME = "Privilege By Marein"
PRICE_FROM = "€ 10.000.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "privilege-by-marein",
    "TITLE": f"{PROJECT_NAME} SAN PEDRO — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Privilege By Marein: uniek turnkey beachfront villa-project aan de promenade van San Pedro, op 1,5 km van Puerto Banús. Ontworpen door architect Ismael Mérida. € 10.000.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe beachfront villa in San Pedro, Marbella",
    "OG_DESCRIPTION": "Privilege By Marein is een exclusieve, volledig gemeubileerde beachfront villa in Cortijo Blanco, San Pedro, met privélift, infinity zwembad en rooftop solarium met tweede zwembad.",
    "OG_IMAGE": "https://projects.investinspain.be/images/privilege-by-marein/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/privilege-by-marein/hero.webp",
    "HERO_BG_ALT": "Privilege By Marein — luxe beachfront villa in San Pedro, Marbella",
    "HERO_NAME": "Privilege By Marein",
    "HERO_LOCATION": "SAN PEDRO, MARBELLA",
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
    "META_DESCRIPTION": "Privilege By Marein: unique turnkey beachfront villa on the San Pedro promenade, 1.5 km from Puerto Banús. Designed by architect Ismael Mérida. € 10,000,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury beachfront villa in San Pedro, Marbella",
    "OG_DESCRIPTION": "Privilege By Marein is an exclusive, fully furnished beachfront villa in Cortijo Blanco, San Pedro, with private lift, infinity pool and rooftop solarium with a second pool.",
    "HERO_BG_ALT": "Privilege By Marein — luxury beachfront villa in San Pedro, Marbella",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/privilege-by-marein/hero.webp",
    "LAT": 36.478828,
    "LNG": -4.974943,
    "HREF": "/privilege-by-marein/",
}
