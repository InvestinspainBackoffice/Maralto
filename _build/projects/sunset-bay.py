from urllib.parse import quote

PROJECT_NAME = "Sunset Bay"
PRICE_FROM = "Vanaf € 452.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "sunset-bay",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Sunset Bay Estepona: 41 nieuwbouwappartementen op 300m van het strand. 1, 2 en 3 slaapkamers. Prijzen vanaf € 452.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Strandnabij Nieuwbouw in Estepona",
    "OG_DESCRIPTION": "41 nieuwbouwappartementen op 300m van het strand in Estepona. 1, 2 en 3 slaapkamers met zeezicht. Ontdek Sunset Bay via INVESTINSPAIN.BE.",
    "OG_IMAGE": "https://projects.investinspain.be/images/sunset-bay/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/sunset-bay/hero.webp",
    "HERO_BG_ALT": "Sunset Bay Estepona exterieur appartementen strandnabij",
    "HERO_NAME": "Sunset Bay",
    "HERO_LOCATION": "ESTEPONA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Sunset Bay Estepona: 41 new build apartments just 300m from the beach. 1, 2 and 3 bedrooms. Prices from € 452,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Beachside New Build in Estepona",
    "OG_DESCRIPTION": "41 new build apartments 300m from the beach in Estepona. 1, 2 and 3 bedrooms with sea views. Discover Sunset Bay via INVESTINSPAIN.BE.",
    "HERO_BG_ALT": "Sunset Bay Estepona exterior apartments beachside",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/sunset-bay/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/sunset-bay/",
}
