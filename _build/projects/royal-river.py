from urllib.parse import quote

PROJECT_NAME = "Royal River"
PRICE_FROM = "Vanaf € 698.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "royal-river",
    "TITLE": f"{PROJECT_NAME} MARBELLA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Royal River Marbella: 16 luxe residenties in Golf Río Real met spa, wellness, solarium en ruime terrassen. Appartementen en penthouses vanaf € 698.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe residenties in Golf Río Real, Marbella",
    "OG_DESCRIPTION": "16 exclusieve woningen met spa, zwembad en zonneterras in de prestigieuze Golf Río Real urbanisatie in Marbella.",
    "OG_IMAGE": "https://projects.investinspain.be/images/royal-river/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/royal-river/hero.webp",
    "HERO_BG_ALT": "Royal River — luchtfoto van het luxeresidentieproject in Golf Río Real, Marbella",
    "HERO_NAME": "Royal River",
    "HERO_LOCATION": "MARBELLA",
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
    "META_DESCRIPTION": "Royal River Marbella: 16 luxury residences in Golf Río Real with spa, wellness, solarium and spacious terraces. Apartments and penthouses from € 698,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury residences in Golf Río Real, Marbella",
    "OG_DESCRIPTION": "16 exclusive homes with spa, pool and sun terrace in the prestigious Golf Río Real urbanisation in Marbella.",
    "HERO_BG_ALT": "Royal River — aerial view of the luxury residence project in Golf Río Real, Marbella",
}
# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
