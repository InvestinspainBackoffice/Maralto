from urllib.parse import quote

PROJECT_NAME = "Bougainvillea"
PRICE_FROM = "Vanaf € 549.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "bougainvillea",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Bougainvillea: 25 exclusieve appartementen in Estepona met gym, sauna, spa, jacuzzi en zeezicht. Ontworpen door Europese architecten. Vanaf € 549.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "25 exclusieve appartementen in Estepona met gym, sauna, spa en zeezicht — Europees design.",
    "OG_IMAGE": "https://projects.investinspain.be/images/bougainvillea/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/bougainvillea/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Appartementen in Estepona",
    "HERO_NAME": "Bougainvillea",
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
    "META_DESCRIPTION": "Bougainvillea: 25 exclusive apartments in Estepona with gym, sauna, spa, jacuzzi and sea views. Designed by European architects. From € 549,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "25 exclusive apartments in Estepona with gym, sauna, spa and sea views — European design.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Apartments in Estepona",
}

HUB = {
    "NAME": "Bougainvillea",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 549.000",
    "THUMB": "https://projects.investinspain.be/images/bougainvillea/hero.webp",
    "LAT": 36.43808,
    "LNG": -5.113512,
    "HREF": "/bougainvillea/",
}
