from urllib.parse import quote

PROJECT_NAME = "Nyra Residences"
PRICE_FROM = "Vanaf € 668.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "nyra-residences",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Nyra Residences: moderne appartementen in de Golden Triangle van Estepona. Gedeeld zwembad, yoga-zone en stijlvolle architectuur. Vanaf €668.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne Appartementen in Estepona",
    "OG_DESCRIPTION": "Ontdek Nyra Residences: eigentijdse appartementen in de Golden Triangle van Estepona met gedeeld zwembad, yoga-zone en verfijnde architectuur. Ideaal gelegen tussen strand en golf. Vanaf €668.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/nyra-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/nyra-residences/hero.webp",
    "HERO_BG_ALT": "Nyra Residences — moderne appartementen in de Golden Triangle Estepona",
    "HERO_NAME": "NYRA RESIDENCES",
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
    "META_DESCRIPTION": "Nyra Residences: modern apartments in the Golden Triangle of Estepona. Shared pool, yoga zone and stylish architecture. From €668,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Apartments in Estepona",
    "OG_DESCRIPTION": "Discover Nyra Residences: contemporary apartments in Estepona's Golden Triangle with shared pool, yoga zone and refined architecture. Ideally situated between beach and golf. From €668,000.",
    "HERO_BG_ALT": "Nyra Residences — modern apartments in the Golden Triangle Estepona",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
