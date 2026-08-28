from urllib.parse import quote

PROJECT_NAME = "Moon64"
PRICE_FROM = "Vanaf € 381.800"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "moon64",
    "TITLE": f"{PROJECT_NAME} Manilva — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Moon64: 64 exclusieve appartementen en penthouses met 2 of 3 slaapkamers in Los Hidalgos, Manilva. Vanaf € 381.800.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Los Hidalgos",
    "OG_DESCRIPTION": "Moon64: sikkelvormige architectuur, overloopzwembad, fitnessruimte en sociale club in Los Hidalgos, Manilva, nabij La Duquesa en Sotogrande. Vanaf € 381.800.",
    "OG_IMAGE": "https://projects.investinspain.be/images/moon64/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/moon64/hero.webp",
    "HERO_BG_ALT": "Moon64 — moderne appartementen in Los Hidalgos, Manilva",
    "HERO_NAME": "Moon64",
    "HERO_LOCATION": "LOS HIDALGOS, MANILVA",
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
    "META_DESCRIPTION": "Moon64: 64 exclusive apartments and penthouses with 2 or 3 bedrooms in Los Hidalgos, Manilva. From € 381,800.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Los Hidalgos",
    "OG_DESCRIPTION": "Moon64: crescent-shaped architecture, infinity pool, gym and social club in Los Hidalgos, Manilva, close to La Duquesa and Sotogrande. From € 381,800.",
    "HERO_BG_ALT": "Moon64 — modern apartments in Los Hidalgos, Manilva",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Los Hidalgos, Manilva",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/moon64/hero.webp",
    "LAT": 36.349384,
    "LNG": -5.238762,
    "HREF": "/moon64/",
}
