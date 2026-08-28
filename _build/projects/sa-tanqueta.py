from urllib.parse import quote

PROJECT_NAME = "Sa Tanqueta"
PRICE_FROM = "Vanaf € 570.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "sa-tanqueta",
    "TITLE": f"{PROJECT_NAME} Ibiza — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Sa Tanqueta: moderne villa's en woningen op het zonnige Ibiza. Privézwembad, terras en rust in een groene omgeving. Ideaal voor wie het eilandleven wil beleven. Vanaf € 570.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne woningen met privézwembad op Ibiza",
    "OG_DESCRIPTION": "Sa Tanqueta op Ibiza: eigentijdse woningen met privézwembad, terras en rustige groene omgeving op een van de meest gewilde eilanden van de Middellandse Zee. Vanaf € 570.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/sa-tanqueta/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/sa-tanqueta/hero.webp",
    "HERO_BG_ALT": "Sa Tanqueta Ibiza exterieur met zwembad",
    "HERO_NAME": "Sa Tanqueta",
    "HERO_LOCATION": "IBIZA, BALEAREN",
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
    "META_DESCRIPTION": "Sa Tanqueta: modern villas and homes on sunny Ibiza. Private pool, terrace and tranquility in a green setting. Ideal for those seeking island life. From € 570,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern homes with private pool on Ibiza",
    "OG_DESCRIPTION": "Sa Tanqueta on Ibiza: contemporary homes with private pool, terrace and peaceful green surroundings on one of the most sought-after islands of the Mediterranean. From € 570,000.",
    "HERO_BG_ALT": "Sa Tanqueta Ibiza exterior with pool",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Ibiza",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/sa-tanqueta/hero.webp",
    "LAT": 38.986333,
    "LNG": 1.533689,
    "HREF": "/sa-tanqueta/",
}
