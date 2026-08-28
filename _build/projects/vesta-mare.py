from urllib.parse import quote

PROJECT_NAME = "Vesta Mare"
PRICE_FROM = "Vanaf € 435.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vesta-mare",
    "TITLE": f"{PROJECT_NAME} Manilva — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vesta Mare: 145 appartementen en penthouses direct aan het strand in Manilva. Vanaf €435.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline appartementen",
    "OG_DESCRIPTION": "Ontdek Vesta Mare: infinity zwembad met zeezicht, fitnessruimte en co-workingruimte direct aan het strand. Vanaf €435.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/04/Vesta-Mare-Manilva.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/04/Vesta-Mare-Manilva.jpg",
    "HERO_BG_ALT": "Vesta Mare — wooncomplex direct aan het strand",
    "HERO_NAME": "VESTA MARE",
    "HERO_LOCATION": "MANILVA",
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
    "META_DESCRIPTION": "Vesta Mare: 145 apartments and penthouses right on the beach in Manilva. From €435.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline Apartments",
    "OG_DESCRIPTION": "Discover Vesta Mare: infinity pool with sea view, fitness room and coworking space right on the beach. From €435.000.",
    "HERO_BG_ALT": "Vesta Mare — residential complex right on the beach",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Manilva",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/vesta-mare/thumb.webp",
    "LAT": 36.351875,
    "LNG": -5.233278,
    "HREF": "/vesta-mare/",
}
