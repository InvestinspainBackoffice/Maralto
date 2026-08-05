from urllib.parse import quote

PROJECT_NAME = "ISEA Estepona"
PRICE_FROM = "€ 525.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "isea-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "ISEA Estepona: gelijkvloers appartement met 3 slaapkamers, ruim terras en tuin, in een urbanisatie met zeezicht. €525.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Gelijkvloers Drie-slaapkamerappartement",
    "OG_DESCRIPTION": "Ontdek ISEA Estepona: een gelijkvloers appartement met tuin, ruim terras, gemeenschappelijk zwembad, fitness en sauna. €525.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/isea-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/isea-estepona/hero.webp",
    "HERO_BG_ALT": "ISEA Estepona — terras van het gelijkvloers appartement",
    "HERO_NAME": "ISEA ESTEPONA",
    "HERO_LOCATION": "ESTEPONA",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "PRICE_LABEL": "",
    "PRICE_AMOUNT": PRICE_FROM,
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
    "META_DESCRIPTION": "ISEA Estepona: ground-floor apartment with 3 bedrooms, a spacious terrace and garden, in a development with sea views. €525,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ground-floor Three-bedroom Apartment",
    "OG_DESCRIPTION": "Discover ISEA Estepona: a ground-floor apartment with a garden, spacious terrace, communal pool, gym and sauna. €525,000.",
    "HERO_BG_ALT": "ISEA Estepona — terrace of the ground-floor apartment",
    "PRICE_FROM": "€ 525,000",
    "HERO_PRICE": "€ 525,000",
    "PRICE_AMOUNT": "€ 525,000",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
