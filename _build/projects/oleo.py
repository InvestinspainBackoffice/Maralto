from urllib.parse import quote

PROJECT_NAME = "Oleo"
PRICE_FROM = "Vanaf € 725.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "oleo",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Oleo: moderne villa's in Mijas met privézwembad en zeezicht. Ruime terrassen, hoogwaardige afwerking en ideale ligging aan de Costa del Sol. Vanaf €725.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's in Mijas",
    "OG_DESCRIPTION": "Ontdek Oleo: stijlvolle villa's in Mijas met privézwembad, ruime terrassen en zeezicht. Hoogwaardige afwerking en uitstekende ligging aan de Costa del Sol. Vanaf €725.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/oleo/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/oleo/hero.webp",
    "HERO_BG_ALT": "Oleo — moderne villa met zeezicht in Mijas",
    "HERO_NAME": "OLEO",
    "HERO_LOCATION": "MIJAS",
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
    "META_DESCRIPTION": "Oleo: modern villas in Mijas with private pool and sea views. Spacious terraces, high-quality finishes and ideal location on the Costa del Sol. From €725,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas in Mijas",
    "OG_DESCRIPTION": "Discover Oleo: stylish villas in Mijas with private pool, spacious terraces and sea views. High-quality finishes and excellent location on the Costa del Sol. From €725,000.",
    "HERO_BG_ALT": "Oleo — modern villa with sea views in Mijas",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
