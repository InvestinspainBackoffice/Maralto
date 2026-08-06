from urllib.parse import quote

PROJECT_NAME = "Valle Romano"
PRICE_FROM = "Vanaf € 385.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "valle-romano",
    "TITLE": f"{PROJECT_NAME} ESTEPONA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Valle Romano Estepona: exclusieve privé urbanisatie met communaal zwembad en groene omgeving, aan de golfbaan van Valle Romano. Vanaf € 385.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve privé urbanisatie in Estepona",
    "OG_DESCRIPTION": "Valle Romano biedt moderne appartementen in een exclusieve privé urbanisatie aan de golfbaan van Valle Romano, in Estepona.",
    "OG_IMAGE": "https://projects.investinspain.be/images/valle-romano/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/valle-romano/hero.webp",
    "HERO_BG_ALT": "Valle Romano — moderne appartementen aan de golfbaan in Estepona",
    "HERO_NAME": "Valle Romano",
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
    "META_DESCRIPTION": "Valle Romano Estepona: exclusive private urbanisation with communal pool and green surroundings, on the Valle Romano golf course. From € 385,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive private urbanisation in Estepona",
    "OG_DESCRIPTION": "Valle Romano offers modern apartments in an exclusive private urbanisation on the Valle Romano golf course, in Estepona.",
    "HERO_BG_ALT": "Valle Romano — modern apartments on the golf course in Estepona",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
