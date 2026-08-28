from urllib.parse import quote

PROJECT_NAME = "Almina Residences"
PRICE_FROM = "Vanaf € 669.465"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "almina-residences",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Almina Residences: 60 appartementen en penthouses in Estepona met spa, gym, zwembaden, cinema en coworking. Resortachtig gated complex. Vanaf €669.465.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Wonen met Resortgevoel",
    "OG_DESCRIPTION": "Ontdek Almina Residences: 60 stijlvolle appartementen in Estepona met uitgebreide wellness, cinema, coworking en sociale beleving. Gated community met volledige lifestyle. Vanaf €669.465.",
    "OG_IMAGE": "https://projects.investinspain.be/images/almina-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/almina-residences/hero.webp",
    "HERO_BG_ALT": "Almina Residences — gevelaanzicht bij zonsondergang",
    "HERO_NAME": "ALMINA RESIDENCES",
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
    "META_DESCRIPTION": "Almina Residences: 60 apartments and penthouses in Estepona with spa, gym, pools, cinema and coworking. Resort-like gated complex. From €669,465.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Living with Resort Feel",
    "OG_DESCRIPTION": "Discover Almina Residences: 60 stylish apartments in Estepona with extensive wellness, cinema, coworking and social life. Gated community with complete lifestyle. From €669,465.",
    "HERO_BG_ALT": "Almina Residences — facade view at sunset",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/almina-residences/hero.webp",
    "LAT": 36.436422,
    "LNG": -5.111313,
    "HREF": "/almina-residences/",
}
