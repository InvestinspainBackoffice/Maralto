from urllib.parse import quote

PROJECT_NAME = "Serene Atalaya"
PRICE_FROM = "Vanaf € 850.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "serene-atalaya",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Serene Atalaya – luxe appartementen met terrassen, gemeenschappelijk zwembad en tuin in Atalaya, Estepona. Modern design, rustige ligging aan de Costa del Sol. Vanaf € 850.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxe appartementen Atalaya Estepona · INVESTINSPAIN.BE",
    "OG_DESCRIPTION": "Exclusieve nieuwbouwappartementen in Atalaya, Estepona. Gemeenschappelijk zwembad, terrassen en tuin. Vraag brochure aan bij INVESTINSPAIN.",
    "OG_IMAGE": "https://projects.investinspain.be/images/serene-atalaya/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/serene-atalaya/hero.webp",
    "HERO_BG_ALT": "Serene Atalaya terras zeezicht luxe appartementen Atalaya Estepona",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "ATALAYA, ESTEPONA",
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
    "MAP_LAT": "36.464740556221",
    "MAP_LNG": "-5.0183158035744",
}

DATA_EN = {
    "META_DESCRIPTION": "Serene Atalaya – luxury apartments with terraces, communal pool and garden in Atalaya, Estepona. Modern design, peaceful location on the Costa del Sol. From € 850,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxury apartments Atalaya Estepona · INVESTINSPAIN.BE",
    "OG_DESCRIPTION": "Exclusive new-build apartments in Atalaya, Estepona. Communal pool, terraces and garden. Request the brochure at INVESTINSPAIN.",
    "HERO_BG_ALT": "Serene Atalaya terrace sea views luxury apartments Atalaya Estepona",
}
