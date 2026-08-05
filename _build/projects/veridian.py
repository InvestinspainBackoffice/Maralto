from urllib.parse import quote

PROJECT_NAME = "Veridian"
PRICE_FROM = "Vanaf € 797.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "veridian",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Veridian: duurzame townhouses met 3 slaapkamers en zeezicht in El Higuerón, Fuengirola. Vanaf €797.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Duurzame Townhouses met Zeezicht",
    "OG_DESCRIPTION": "Ontdek Veridian: eco-townhouses met zonnepanelen, private tuinen en panoramisch zicht op de Middellandse Zee, in het groene El Higuerón, Fuengirola. Vanaf €797.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/veridian/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/veridian/hero.webp",
    "HERO_BG_ALT": "Veridian — townhouses tegen de heuvel met zicht op zee",
    "HERO_NAME": "VERIDIAN",
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
    "META_DESCRIPTION": "Veridian: sustainable townhouses with 3 bedrooms and sea views in El Higuerón, Fuengirola. From €797,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Sustainable Townhouses with Sea Views",
    "OG_DESCRIPTION": "Discover Veridian: eco-townhouses with solar panels, private gardens and panoramic Mediterranean views, in green El Higuerón, Fuengirola. From €797,000.",
    "HERO_BG_ALT": "Veridian — townhouses set into the hillside with sea views",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
