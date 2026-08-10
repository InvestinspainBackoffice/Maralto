from urllib.parse import quote

PROJECT_NAME = "Belvedere Collection"
PRICE_FROM = "Vanaf € 430.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "belvedere-collection",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Belvedere Collection: exclusief wooncomplex met infinity pool, fitness en sauna in Fuengirola. Vanaf € 430.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Fuengirola",
    "OG_DESCRIPTION": "Belvedere Collection: ruime lichte interieurs, keramische vloeren, infinity pool en laadpunten voor elektrische auto's in Fuengirola. Vanaf € 430.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/belvedere-collection/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/belvedere-collection/hero.webp",
    "HERO_BG_ALT": "Belvedere Collection — exclusief wooncomplex in Fuengirola",
    "HERO_NAME": "Belvedere Collection",
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
    "META_DESCRIPTION": "Belvedere Collection: exclusive residential complex with infinity pool, gym and sauna in Fuengirola. From € 430,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Fuengirola",
    "OG_DESCRIPTION": "Belvedere Collection: spacious bright interiors, ceramic floors, infinity pool and EV charging points in Fuengirola. From € 430,000.",
    "HERO_BG_ALT": "Belvedere Collection — exclusive residential complex in Fuengirola",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
