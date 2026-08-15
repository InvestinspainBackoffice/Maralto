from urllib.parse import quote

PROJECT_NAME = "Lomas del Higuerón"
PRICE_FROM = "Vanaf € 520.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "lomas-del-higueron",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Lomas del Higuerón: luxueus nieuwbouwproject met zeezicht in Fuengirola. Gated community, spa, gym, concierge, co-working zone, meerdere zwembaden. Vanaf € 520.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxe gated community zeezicht Fuengirola",
    "OG_DESCRIPTION": "Luxueus woonproject in Fuengirola met zeezicht, gated community, spa, gym, concierge en meerdere zwembaden. Apartementen en penthouses. Vanaf € 520.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/lomas-del-higueron/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/lomas-del-higueron/hero.webp",
    "HERO_BG_ALT": "Lomas del Higuerón gated community zwembad zeezicht Fuengirola",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "HIGUERÓN, FUENGIROLA",
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
    "MAP_LAT": "36.577400810435",
    "MAP_LNG": "-4.5993069390576",
}

DATA_EN = {
    "META_DESCRIPTION": "Lomas del Higuerón: luxury new-build project with sea views in Fuengirola. Gated community, spa, gym, concierge, co-working zone, multiple pools. From € 520,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxury gated community sea views Fuengirola",
    "OG_DESCRIPTION": "Luxury residential project in Fuengirola with sea views, gated community, spa, gym, concierge and multiple pools. Apartments and penthouses. From € 520,000.",
    "HERO_BG_ALT": "Lomas del Higuerón gated community pool sea views Fuengirola",
}
