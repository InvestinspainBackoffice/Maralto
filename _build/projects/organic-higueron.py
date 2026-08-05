from urllib.parse import quote

PROJECT_NAME = "Organic"
PRICE_FROM = "Vanaf € 747.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "organic-higueron",
    "TITLE": f"{PROJECT_NAME} El Higuerón — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Organic: boutiqueproject van 25 woningen met 3 en 4 slaapkamers en privézwembad in El Higuerón, Fuengirola. Vanaf €747.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Wonen in Harmonie met Natuur en Zeezicht",
    "OG_DESCRIPTION": "Ontdek Organic: 25 exclusieve woningen met privézwembad, coworkingruimte en yoga-zones, geïnspireerd op het reliëf van de heuvel in El Higuerón. Vanaf €747.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/organic-higueron/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/organic-higueron/hero.webp",
    "HERO_BG_ALT": "Organic — infinity zwembad met zicht op zee bij zonsondergang",
    "HERO_NAME": "ORGANIC",
    "HERO_LOCATION": "FUENGIROLA",
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
    "META_DESCRIPTION": "Organic: boutique project of 25 homes with 3 and 4 bedrooms and a private pool in El Higuerón, Fuengirola. From €747,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Living in Harmony with Nature and Sea Views",
    "OG_DESCRIPTION": "Discover Organic: 25 exclusive homes with a private pool, coworking space and yoga zones, inspired by the contours of the hillside in El Higuerón. From €747,000.",
    "HERO_BG_ALT": "Organic — infinity pool with sea views at sunset",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
