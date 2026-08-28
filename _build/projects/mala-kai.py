from urllib.parse import quote

PROJECT_NAME = "Mãla Kai"
PRICE_FROM = "Vanaf € 725.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "mala-kai",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Mãla Kai: 'Tuinen aan zee' — appartementen en penthouses met zeezicht, gym, yoga, zwembaden en gastrobar in Estepona. Ecologisch design, gated community. Vanaf € 725.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen en penthouses met zeezicht in Estepona",
    "OG_DESCRIPTION": "Mãla Kai in Estepona: luxe appartementen en penthouses met Middellandse Zeezicht, fitness, yogaruimte, communale zwembaden, gastrobar en chilloutzone. Op wandelafstand van het strand. Vanaf € 725.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/mala-kai/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/mala-kai/hero.webp",
    "HERO_BG_ALT": "Mãla Kai Estepona exterieur appartementen en penthouses overdag",
    "HERO_NAME": "Mãla Kai",
    "HERO_LOCATION": "ESTEPONA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Mãla Kai: 'Gardens by the Sea' — apartments and penthouses with sea views, gym, yoga, pools and gastrobar in Estepona. Ecological design, gated community. From € 725,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments and penthouses with sea views in Estepona",
    "OG_DESCRIPTION": "Mãla Kai in Estepona: luxury apartments and penthouses with Mediterranean sea views, fitness, yoga room, communal pools, gastrobar and chill-out zone. Walking distance to the beach. From € 725,000.",
    "HERO_BG_ALT": "Mãla Kai Estepona exterior apartments and penthouses daytime",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/mala-kai/hero.webp",
    "LAT": 36.406676,
    "LNG": -5.191147,
    "HREF": "/mala-kai/",
}
