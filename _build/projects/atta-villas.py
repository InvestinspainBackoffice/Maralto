from urllib.parse import quote

PROJECT_NAME = "ATTA Villas"
PRICE_FROM = "Vanaf € 830.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "atta-villas",
    "TITLE": f"{PROJECT_NAME} San Pedro de Alcántara — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "ATTA Villas: exclusieve villa's met privézwembad en moderne architectuur in San Pedro de Alcántara. Ruime leefruimtes, hoogwaardige afwerking en uitstekende ligging. Vanaf € 830.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve villa's met privézwembad, San Pedro de Alcántara",
    "OG_DESCRIPTION": "ATTA Villas in San Pedro de Alcántara: moderne villa's met privézwembad, ruime terrassen en luxueuze afwerking op een toplocatie nabij Marbella. Vanaf € 830.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/atta-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/atta-villas/hero.webp",
    "HERO_BG_ALT": "ATTA Villas San Pedro de Alcántara exterieur",
    "HERO_NAME": "ATTA Villas",
    "HERO_LOCATION": "SAN PEDRO DE ALCÁNTARA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "ATTA Villas: exclusive villas with private pool and modern architecture in San Pedro de Alcántara. Spacious living areas, premium finishes and an excellent location. From € 830,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive villas with private pool, San Pedro de Alcántara",
    "OG_DESCRIPTION": "ATTA Villas in San Pedro de Alcántara: modern villas with private pool, generous terraces and luxury finishes in a prime location near Marbella. From € 830,000.",
    "HERO_BG_ALT": "ATTA Villas San Pedro de Alcántara exterior",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/atta-villas/hero.webp",
    "LAT": 36.479952,
    "LNG": -5.027157,
    "HREF": "/atta-villas/",
}
