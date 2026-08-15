from urllib.parse import quote

PROJECT_NAME = "WaveView"
PRICE_FROM = "Vanaf € 1.750.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "waveview",
    "TITLE": f"{PROJECT_NAME} Frontline Beach Villa's Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "WaveView: 3 moderne frontline beach villa's met spectaculair zeezicht in Las Farolas, Mijas Costa. Direct aan strand, nabij Chaparral Golf Club. Vanaf € 1.750.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 3 frontline beach villa's Mijas Costa",
    "OG_DESCRIPTION": "3 exclusieve villa's frontline beach in Las Farolas, Mijas Costa. Spectaculair zeezicht, privézwembad, terras, nabij Chaparral Golf Club. Vanaf € 1.750.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/waveview/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/waveview/hero.webp",
    "HERO_BG_ALT": "WaveView frontline beach villa zwembad zeezicht Mijas Costa",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "LAS FAROLAS, MIJAS COSTA",
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
    "MAP_LAT": "36.507475002013",
    "MAP_LNG": "-4.6558799024638",
}

DATA_EN = {
    "META_DESCRIPTION": "WaveView: 3 modern frontline beach villas with spectacular sea views in Las Farolas, Mijas Costa. Direct beach access, near Chaparral Golf Club. From € 1,750,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 3 frontline beach villas Mijas Costa",
    "OG_DESCRIPTION": "3 exclusive frontline beach villas in Las Farolas, Mijas Costa. Spectacular sea views, private pool, terrace, near Chaparral Golf Club. From € 1,750,000.",
    "HERO_BG_ALT": "WaveView frontline beach villa pool sea views Mijas Costa",
}
