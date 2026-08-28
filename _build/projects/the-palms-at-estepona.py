from urllib.parse import quote

PROJECT_NAME = "The Palms at Estepona"
PRICE_FROM = "Vanaf € 387.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-palms-at-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Palms at Estepona: moderne appartementen en penthouses met spa, coworking en privézwembad op de begane grond, op wandelafstand van het strand. Vanaf € 387.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Estepona",
    "OG_DESCRIPTION": "The Palms at Estepona: luxe spa met verwarmd binnenbad, sauna en hammam, tienjarige structurele garantie, vlakbij het strand. Vanaf € 387.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/the-palms-at-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/the-palms-at-estepona/hero.webp",
    "HERO_BG_ALT": "The Palms at Estepona — moderne appartementen vlakbij het strand",
    "HERO_NAME": "The Palms at Estepona",
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
    "META_DESCRIPTION": "The Palms at Estepona: modern apartments and penthouses with spa, coworking and private ground-floor pool, within walking distance of the beach. From € 387,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Estepona",
    "OG_DESCRIPTION": "The Palms at Estepona: luxury spa with heated indoor pool, sauna and hammam, ten-year structural warranty, close to the beach. From € 387,000.",
    "HERO_BG_ALT": "The Palms at Estepona — modern apartments close to the beach",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/the-palms-at-estepona/hero.webp",
    "LAT": 36.405899,
    "LNG": -5.193693,
    "HREF": "/the-palms-at-estepona/",
}
