from urllib.parse import quote

PROJECT_NAME = "Villa Playa San Pedro"
PRICE_FROM = "Prijs op aanvraag"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "villa-playa-san-pedro",
    "TITLE": f"{PROJECT_NAME} Puerto Banús — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Villa Playa San Pedro: exclusieve frontline beach villa in San Pedro de Alcántara, naast Puerto Banús. Directe strandbelijning, gym, meerdere slaapkamers. Prijs op aanvraag.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline Beach Villa bij Puerto Banús",
    "OG_DESCRIPTION": "Exclusieve frontline beach villa in San Pedro de Alcántara, op wandelafstand van Puerto Banús. Direct aan het strand. Ontdek dit uniek aanbod via INVESTINSPAIN.BE.",
    "OG_IMAGE": "https://projects.investinspain.be/images/villa-playa-san-pedro/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/villa-playa-san-pedro/hero.webp",
    "HERO_BG_ALT": "Villa Playa San Pedro frontline beach villa hoofdingang nacht",
    "HERO_NAME": "Villa Playa San Pedro",
    "HERO_LOCATION": "SAN PEDRO DE ALCÁNTARA, MARBELLA",
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
    "META_DESCRIPTION": "Villa Playa San Pedro: exclusive frontline beach villa in San Pedro de Alcántara, next to Puerto Banús. Direct beach access, gym, multiple bedrooms. Price on request.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline Beach Villa near Puerto Banús",
    "OG_DESCRIPTION": "Exclusive frontline beach villa in San Pedro de Alcántara, within walking distance of Puerto Banús. Direct beach access. Discover this unique property via INVESTINSPAIN.BE.",
    "HERO_BG_ALT": "Villa Playa San Pedro frontline beach villa main entrance night",
}
