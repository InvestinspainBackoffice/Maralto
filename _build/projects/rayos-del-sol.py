from urllib.parse import quote

PROJECT_NAME = "Rayos del Sol"
PRICE_FROM = "Vanaf € 520.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "rayos-del-sol",
    "TITLE": f"{PROJECT_NAME} Las Lagunas de Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Rayos del Sol: moderne appartementen met zeezicht in Las Lagunas de Mijas. Communaal zwembad, ruime terrassen en topligging nabij strand, golf en Fuengirola. Vanaf € 520.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen met zeezicht, Las Lagunas de Mijas",
    "OG_DESCRIPTION": "Rayos del Sol in Las Lagunas de Mijas: eigentijdse appartementen met zeezicht, ruime terrassen en communale faciliteiten nabij strand en golf. Vanaf € 520.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/rayos-del-sol/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/rayos-del-sol/hero.webp",
    "HERO_BG_ALT": "Rayos del Sol Las Lagunas de Mijas exterieur met zeezicht",
    "HERO_NAME": "Rayos del Sol",
    "HERO_LOCATION": "LAS LAGUNAS DE MIJAS, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Rayos del Sol: modern apartments with sea views in Las Lagunas de Mijas. Communal pool, generous terraces and a prime location near the beach, golf and Fuengirola. From € 520,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments with sea views, Las Lagunas de Mijas",
    "OG_DESCRIPTION": "Rayos del Sol in Las Lagunas de Mijas: contemporary apartments with sea views, spacious terraces and communal amenities near the beach and golf. From € 520,000.",
    "HERO_BG_ALT": "Rayos del Sol Las Lagunas de Mijas exterior with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Las Lagunas de Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/rayos-del-sol/hero.webp",
    "LAT": 36.51184,
    "LNG": -4.65339,
    "HREF": "/rayos-del-sol/",
}
