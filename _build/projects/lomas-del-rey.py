from urllib.parse import quote

PROJECT_NAME = "Lomas del Rey"
PRICE_FROM = "Vanaf € 1.395.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "lomas-del-rey",
    "TITLE": f"{PROJECT_NAME} Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Lomas del Rey: exclusieve appartementen in traditionele Andalusische stijl met zeezicht in Marbella. 25.000 m² aangelegde tuinen, zwembaden en 24/7 beveiliging. Vanaf € 1.395.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Andalusische appartementen met zeezicht in Marbella",
    "OG_DESCRIPTION": "Lomas del Rey in Marbella: luxe appartementen in Andalusische stijl met panoramisch zeezicht, 25.000 m² tuinen, zwembaden en 24/7 beveiliging in een exclusief complex. Vanaf € 1.395.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/lomas-del-rey/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/lomas-del-rey/hero.webp",
    "HERO_BG_ALT": "Lomas del Rey Marbella exterieur Andalusische stijl appartementencomplex",
    "HERO_NAME": "Lomas del Rey",
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
}

DATA_EN = {
    "META_DESCRIPTION": "Lomas del Rey: exclusive apartments in traditional Andalusian style with sea views in Marbella. 25,000 m² landscaped gardens, pools and 24/7 security. From € 1,395,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Andalusian apartments with sea views in Marbella",
    "OG_DESCRIPTION": "Lomas del Rey in Marbella: luxury apartments in Andalusian style with panoramic sea views, 25,000 m² gardens, pools and 24/7 security within an exclusive complex. From € 1,395,000.",
    "HERO_BG_ALT": "Lomas del Rey Marbella exterior Andalusian style apartment complex",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/lomas-del-rey/hero.webp",
    "LAT": 36.510343,
    "LNG": -4.929954,
    "HREF": "/lomas-del-rey/",
}
