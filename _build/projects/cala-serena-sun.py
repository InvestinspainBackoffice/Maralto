from urllib.parse import quote

PROJECT_NAME = "Cala Serena Sun"
PRICE_FROM = "Vanaf € 676.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "cala-serena-sun",
    "TITLE": f"{PROJECT_NAME} LA CALA DE MIJAS — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Cala Serena Sun La Cala de Mijas: 68 geschakelde woningen met 3-4 slaapkamers, zeezicht, privétuinen en gemeenschappelijk zwembad. Vanaf € 676.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Schakelwoningen met zeezicht in La Cala de Mijas",
    "OG_DESCRIPTION": "68 zuidgerichte schakelwoningen met terras, tuin, zeezicht en gedeeld zwembad in de gewilde La Cala de Mijas.",
    "OG_IMAGE": "https://projects.investinspain.be/images/cala-serena-sun/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/cala-serena-sun/hero.webp",
    "HERO_BG_ALT": "Cala Serena Sun — gemeenschappelijk zwembad met ligzetels en mediterrane tuinen",
    "HERO_NAME": "Cala Serena Sun",
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
}

DATA_EN = {
    "META_DESCRIPTION": "Cala Serena Sun La Cala de Mijas: 68 terraced homes with 3-4 bedrooms, sea views, private gardens and communal pool. From € 676,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Terraced homes with sea views in La Cala de Mijas",
    "OG_DESCRIPTION": "68 south-facing terraced homes with terrace, garden, sea views and shared pool in the sought-after La Cala de Mijas.",
    "HERO_BG_ALT": "Cala Serena Sun — communal pool with sun loungers and Mediterranean gardens",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Cala de Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/cala-serena-sun/hero.webp",
    "LAT": 36.507878,
    "LNG": -4.683832,
    "HREF": "/cala-serena-sun/",
}
