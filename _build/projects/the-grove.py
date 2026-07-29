from urllib.parse import quote

PROJECT_NAME = "The Grove"
PRICE_FROM = "Vanaf € 390.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-grove",
    "TITLE": f"{PROJECT_NAME} San Pedro — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Grove: appartementen met 1-4 slaapkamers in San Pedro de Alcántara, met skypool en spa. Vanaf €390.000.",
    "OG_TITLE": f"{PROJECT_NAME} San Pedro — Appartementen",
    "OG_DESCRIPTION": "Ontdek The Grove: rooftop lounge met skypool, verwarmd binnenzwembad, gym en spa in San Pedro de Alcántara. Vanaf €390.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/01/06-The-Grove.png",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/01/06-The-Grove.png",
    "HERO_BG_ALT": "The Grove — appartementencomplex met zwembad en weelderige tuinen",
    "HERO_NAME": "THE GROVE",
    "HERO_LOCATION": "SAN PEDRO",
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
    "META_DESCRIPTION": "The Grove: 1-4 bedroom apartments in San Pedro de Alcántara, with skypool and spa. From €390,000.",
    "OG_TITLE": f"{PROJECT_NAME} San Pedro — Apartments",
    "OG_DESCRIPTION": "Discover The Grove: rooftop lounge with skypool, heated indoor pool, gym and spa in San Pedro de Alcántara. From €390,000.",
    "HERO_BG_ALT": "The Grove — apartment complex with pool and lush gardens",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2026/01/06-The-Grove.png",
    "LAT": 36.4873997,
    "LNG": -4.9843947,
    "HREF": "/the-grove/",
}
