from urllib.parse import quote

PROJECT_NAME = "Attire Estepona"
PRICE_FROM = "Vanaf € 601.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "attire-estepona",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Attire Estepona: 40 halfvrijstaande woningen met 3 slaapkamers, frontline Estepona Golf. Vanaf €601.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Halfvrijstaande Woningen aan Estepona Golf",
    "OG_DESCRIPTION": "Ontdek Attire Estepona: ruime halfvrijstaande woningen met masterbedroom suite, gemeenschappelijk zwembad en buitengymnasium, grenzend aan de golfbaan van Estepona. Vanaf €601.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/attire-estepona/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/attire-estepona/hero.webp",
    "HERO_BG_ALT": "Attire Estepona — gemeenschappelijk zwembad langs de woningen",
    "HERO_NAME": "ATTIRE ESTEPONA",
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
    "META_DESCRIPTION": "Attire Estepona: 40 semi-detached homes with 3 bedrooms, frontline Estepona Golf. From €601,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Semi-detached Homes on Estepona Golf",
    "OG_DESCRIPTION": "Discover Attire Estepona: spacious semi-detached homes with a master bedroom suite, a communal pool and an outdoor gym, bordering Estepona golf course. From €601,000.",
    "HERO_BG_ALT": "Attire Estepona — communal pool alongside the homes",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
