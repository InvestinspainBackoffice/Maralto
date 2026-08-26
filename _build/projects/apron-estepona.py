from urllib.parse import quote

PROJECT_NAME = "Apron Estepona"
PRICE_FROM = "Vanaf € 834.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "apron-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Apron Estepona: 23 ruime townhouses met 3 of 4 slaapkamers grenzend aan Estepona Golf. Vanaf €834.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses aan Estepona Golf",
    "OG_DESCRIPTION": "Ontdek Apron Estepona: townhouses vanaf 180 m² met groot terras, dubbele parking en gemeenschappelijk zwembad, grenzend aan Estepona Golf. Vanaf €834.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/apron-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/apron-estepona/hero.webp",
    "HERO_BG_ALT": "Apron Estepona — gevel van de townhouses met tuin bij schemering",
    "HERO_NAME": "APRON ESTEPONA",
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
    "META_DESCRIPTION": "Apron Estepona: 23 spacious townhouses with 3 or 4 bedrooms bordering Estepona Golf. From €834,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses on Estepona Golf",
    "OG_DESCRIPTION": "Discover Apron Estepona: townhouses from 180 m² with a large terrace, two-car parking and a communal pool, bordering Estepona Golf. From €834,000.",
    "HERO_BG_ALT": "Apron Estepona — facade of the townhouses with garden at dusk",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/apron-estepona/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/apron-estepona/",
}
