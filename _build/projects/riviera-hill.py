from urllib.parse import quote

PROJECT_NAME = "Riviera Hill"
PRICE_FROM = "Vanaf € 290.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "riviera-hill",
    "TITLE": f"{PROJECT_NAME} Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Riviera Hill: moderne appartementen en penthouses met 1, 2 of 3 slaapkamers in Riviera del Sol, Mijas Costa. Overloopzwembaden, binnenzwembad met spa en golfsimulator. Vanaf €290.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Riviera Hill: mediterraan wonen met ruime terrassen, in een privé-urbanisatie met gecontroleerde toegang aan de Costa del Sol. Vanaf €290.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/02/ENTRADA-PRINCIPAL_Riviera-Hill.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/02/ENTRADA-PRINCIPAL_Riviera-Hill.jpg",
    "HERO_BG_ALT": "Riviera Hill — hoofdingang van het complex",
    "HERO_NAME": "RIVIERA HILL",
    "HERO_LOCATION": "MIJAS COSTA",
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
    "META_DESCRIPTION": "Riviera Hill: modern apartments and penthouses with 1, 2 or 3 bedrooms in Riviera del Sol, Mijas Costa. Infinity pools, indoor pool with spa and golf simulator. From €290.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Riviera Hill: Mediterranean living with spacious terraces, in a private urbanization with controlled access on the Costa del Sol. From €290.000.",
    "HERO_BG_ALT": "Riviera Hill — main entrance of the complex",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas Costa",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/riviera-hill/thumb.webp",
    "LAT": 36.50408526137212,
    "LNG": -4.713392670308849,
    "HREF": "/riviera-hill/",
}
