from urllib.parse import quote

PROJECT_NAME = "Capri"
PRICE_FROM = "€ 490.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "capri-estepona",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Capri: gelijkvloers twee-slaapkamerappartement in Estepona met ruime tuin van 110 m², terras en parking. €490.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Gelijkvloers Twee-slaapkamerappartement",
    "OG_DESCRIPTION": "Ontdek Capri: een gelijkvloers appartement met open lay-out, ruime tuin, twee buitenzwembaden, verwarmd binnenzwembad en fitness. €490.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/capri-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/capri-estepona/hero.webp",
    "HERO_BG_ALT": "Capri — overdekt terras met zicht op zee",
    "HERO_NAME": "CAPRI",
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
    "META_DESCRIPTION": "Capri: ground-floor two-bedroom apartment in Estepona with a spacious 110 m² garden, terrace and parking. €490,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ground-floor Two-bedroom Apartment",
    "OG_DESCRIPTION": "Discover Capri: a ground-floor apartment with an open layout, a spacious garden, two outdoor pools, a heated indoor pool and a gym. €490,000.",
    "HERO_BG_ALT": "Capri — covered terrace with sea views",
    "PRICE_FROM": "€ 490,000",
    "HERO_PRICE": "€ 490,000",
    "PRICE_AMOUNT": "€ 490,000",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
