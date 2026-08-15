from urllib.parse import quote

PROJECT_NAME = "Living Estepona"
PRICE_FROM = "Vanaf € 448.500"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "living-estepona",
    "TITLE": f"{PROJECT_NAME} Centrum Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Living Estepona: 23 woningen met 1 en 2 slaapkamers vlakbij het strand in het centrum van Estepona. Gemeenschappelijk zwembad, terrassen, toplocatie. Vanaf € 448.500.",
    "OG_TITLE": f"{PROJECT_NAME} · 23 woningen centrum Estepona strand",
    "OG_DESCRIPTION": "23 moderne appartementen 1-2 slaapkamers in het centrum van Estepona, op wandelafstand van het strand. Gemeenschappelijk zwembad, terrassen. Vanaf € 448.500.",
    "OG_IMAGE": "https://projects.investinspain.be/images/living-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/living-estepona/hero.webp",
    "HERO_BG_ALT": "Living Estepona appartementen gemeenschappelijk zwembad terras Estepona",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "CENTRUM ESTEPONA",
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
    "MAP_LAT": "36.420317295539",
    "MAP_LNG": "-5.1516255749233",
}

DATA_EN = {
    "META_DESCRIPTION": "Living Estepona: 23 homes with 1 and 2 bedrooms close to the beach in Estepona town centre. Communal pool, terraces, prime location. From € 448,500.",
    "OG_TITLE": f"{PROJECT_NAME} · 23 homes Estepona centre beach",
    "OG_DESCRIPTION": "23 modern apartments 1-2 bedrooms in Estepona town centre, walking distance from the beach. Communal pool, terraces. From € 448,500.",
    "HERO_BG_ALT": "Living Estepona apartments communal pool terrace Estepona",
}
