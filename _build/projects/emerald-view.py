from urllib.parse import quote

PROJECT_NAME = "Emerald View"
PRICE_FROM = "Vanaf € 695.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "emerald-view",
    "TITLE": f"{PROJECT_NAME} Mijas Pueblo — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Emerald View: exclusieve villa's en townhouses in Mijas Pueblo met panoramisch zeezicht en privézwembad. Rustige ligging met uitzicht over de Costa del Sol. Vanaf €695.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's met Zeezicht in Mijas Pueblo",
    "OG_DESCRIPTION": "Ontdek Emerald View: exclusieve woningen in het pittoreske Mijas Pueblo met spectaculair panoramisch zeezicht, privézwembad en authentieke charme. Vanaf €695.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/emerald-view/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/emerald-view/hero.webp",
    "HERO_BG_ALT": "Emerald View — woningen met panoramisch zeezicht in Mijas Pueblo",
    "HERO_NAME": "EMERALD VIEW",
    "HERO_LOCATION": "MIJAS PUEBLO",
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
    "META_DESCRIPTION": "Emerald View: exclusive villas and townhouses in Mijas Pueblo with panoramic sea views and private pool. Peaceful setting overlooking the Costa del Sol. From €695,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas with Sea Views in Mijas Pueblo",
    "OG_DESCRIPTION": "Discover Emerald View: exclusive homes in picturesque Mijas Pueblo with spectacular panoramic sea views, private pool and authentic charm. From €695,000.",
    "HERO_BG_ALT": "Emerald View — homes with panoramic sea views in Mijas Pueblo",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas Pueblo",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/emerald-view/hero.webp",
    "LAT": 36.5958,
    "LNG": -4.6372,
    "HREF": "/emerald-view/",
}
