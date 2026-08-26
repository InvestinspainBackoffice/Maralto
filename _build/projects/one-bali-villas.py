from urllib.parse import quote

PROJECT_NAME = "One Bali Villas"
PRICE_FROM = "Vanaf € 1.860.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "one-bali-villas",
    "TITLE": f"{PROJECT_NAME} La Cala de Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "One Bali Villas: 19 exclusieve villa's in een gated community in La Cala de Mijas. Bioscoop, spa, privézwembad. Prijzen vanaf € 1.860.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Villa's in La Cala de Mijas",
    "OG_DESCRIPTION": "19 villa's in een bewaakt domein in La Cala de Mijas. Bioscoop, spa en privézwembad. Ontdek dit exclusieve project via INVESTINSPAIN.BE.",
    "OG_IMAGE": "https://projects.investinspain.be/images/one-bali-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/one-bali-villas/hero.webp",
    "HERO_BG_ALT": "One Bali Villas La Cala de Mijas villa exterieur",
    "HERO_NAME": "One Bali Villas",
    "HERO_LOCATION": "LA CALA DE MIJAS, COSTA DEL SOL",
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
    "META_DESCRIPTION": "One Bali Villas: 19 exclusive villas in a gated community in La Cala de Mijas. Cinema room, spa, private pool. Prices from € 1,860,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Villas in La Cala de Mijas",
    "OG_DESCRIPTION": "19 villas in a secured estate in La Cala de Mijas. Cinema room, spa and private pool. Discover this exclusive project via INVESTINSPAIN.BE.",
    "HERO_BG_ALT": "One Bali Villas La Cala de Mijas villa exterior",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Cala de Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/one-bali-villas/hero.webp",
    "LAT": 36.5561,
    "LNG": -4.8159,
    "HREF": "/one-bali-villas/",
}
