from urllib.parse import quote

PROJECT_NAME = "Vission Hills"
PRICE_FROM = "Vanaf € 426.300"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vission-hills",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vission Hills: appartementen en halfvrijstaande woningen met 1 tot 4 slaapkamers in La Cala de Mijas. Energielabel A, zwembaden, social club, spa. Vanaf € 426.300.",
    "OG_TITLE": f"{PROJECT_NAME} · Appartementen & Woningen La Cala de Mijas",
    "OG_DESCRIPTION": "Exclusief afgesloten nieuwbouwcomplex in La Cala de Mijas: appartementen en halfvrijstaande woningen met privétuin en privézwembad. Vanaf € 426.300.",
    "OG_IMAGE": "https://projects.investinspain.be/images/vission-hills/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/vission-hills/hero.webp",
    "HERO_BG_ALT": "Vission Hills — nieuwbouwcomplex in La Cala de Mijas bij schemering",
    "HERO_NAME": "VISSION HILLS",
    "HERO_LOCATION": "LA CALA DE MIJAS",
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
    "MAP_LAT": "36.5122259",
    "MAP_LNG": "-4.6835495",
}

DATA_EN = {
    "META_DESCRIPTION": "Vission Hills: apartments and semi-detached homes with 1 to 4 bedrooms in La Cala de Mijas. Energy rating A, swimming pools, social club, spa. From € 426,300.",
    "OG_TITLE": f"{PROJECT_NAME} · Apartments & Homes La Cala de Mijas",
    "OG_DESCRIPTION": "Exclusive gated new-build development in La Cala de Mijas: apartments and semi-detached homes with private garden and private pool. From € 426,300.",
    "HERO_BG_ALT": "Vission Hills — new-build development in La Cala de Mijas at dusk",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Cala de Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/vission-hills/hero.webp",
    "LAT": 36.5122259,
    "LNG": -4.6835495,
    "HREF": "/vission-hills/",
}
