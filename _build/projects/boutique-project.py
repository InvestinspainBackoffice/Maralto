from urllib.parse import quote

PROJECT_NAME = "Boutique Project"
PRICE_FROM = "Vanaf € 775.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "boutique-project",
    "TITLE": f"{PROJECT_NAME} La Cala de Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Boutique Project: slechts 16 premium appartementen met 180° zeezicht in La Cala de Mijas. Privé gated community, privézwembad of jacuzzi per appartement. Vanaf € 775.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 16 boutique appartementen La Cala de Mijas",
    "OG_DESCRIPTION": "16 exclusieve appartementen met spectaculair 180° zeezicht in La Cala de Mijas. Privézwembad of jacuzzi, gated community, uitzonderlijke afwerking. Vanaf € 775.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/boutique-project/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/boutique-project/hero.webp",
    "HERO_BG_ALT": "Boutique Project zwembad La Cala de Mijas zeezicht",
    "HERO_NAME": PROJECT_NAME,
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
    "MAP_LAT": "36.509115801898",
    "MAP_LNG": "-4.7089432378842",
}

DATA_EN = {
    "META_DESCRIPTION": "Boutique Project: only 16 premium apartments with 180° sea views in La Cala de Mijas. Private gated community, private pool or jacuzzi per apartment. From € 775,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 16 boutique apartments La Cala de Mijas",
    "OG_DESCRIPTION": "16 exclusive apartments with spectacular 180° sea views in La Cala de Mijas. Private pool or jacuzzi, gated community, exceptional finish. From € 775,000.",
    "HERO_BG_ALT": "Boutique Project pool La Cala de Mijas sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Cala de Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/boutique-project/hero.webp",
    "LAT": 36.509116,
    "LNG": -4.708943,
    "HREF": "/boutique-project/",
}
