from urllib.parse import quote

PROJECT_NAME = "Quintessence"
PRICE_FROM = "Vanaf € 570.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "quintessence",
    "TITLE": f"{PROJECT_NAME} Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Quintessence Marbella: boutique appartementen met spa, gym, panoramisch zeezicht en golfbanen in de buurt. Energie-efficiënt, exclusief wonen in Marbella. Vanaf € 570.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Boutique appartementen Marbella spa gym",
    "OG_DESCRIPTION": "Boutique appartementen in Marbella met spa, gym, panoramisch zeezicht en nabijheid van de beste golfbanen. Energie-efficiënt en exclusief. Vanaf € 570.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/quintessence/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/quintessence/hero.webp",
    "HERO_BG_ALT": "Quintessence boutique appartementen panoramisch uitzicht Marbella",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "MARBELLA, COSTA DEL SOL",
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
    "MAP_LAT": "36.525632057634",
    "MAP_LNG": "-4.8338818244324",
}

DATA_EN = {
    "META_DESCRIPTION": "Quintessence Marbella: boutique apartments with spa, gym, panoramic sea views and nearby golf courses. Energy-efficient, exclusive living in Marbella. From € 570,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Boutique apartments Marbella spa gym",
    "OG_DESCRIPTION": "Boutique apartments in Marbella with spa, gym, panoramic sea views and proximity to the best golf courses. Energy-efficient and exclusive. From € 570,000.",
    "HERO_BG_ALT": "Quintessence boutique apartments panoramic views Marbella",
}
