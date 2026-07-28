from urllib.parse import quote

PROJECT_NAME = "Beyond Homes"
PRICE_FROM = "Vanaf € 1.480.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "beyond-homes",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Beyond Homes: 16 moderne halfvrijstaande villa's met 3 slaapkamers, privézwembad en solarium in Estepona. Op wandelafstand van het strand. Vanaf €1.480.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Halfvrijstaande Villa's",
    "OG_DESCRIPTION": "Ontdek Beyond Homes: hedendaagse architectuur, comfort en privacy in een rustige, groene omgeving vlakbij het strand van Estepona. Vanaf €1.480.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/03/prime-invest-beyond-homes-02.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/03/prime-invest-beyond-homes-02.jpg",
    "HERO_BG_ALT": "Beyond Homes — halfvrijstaande villa's met privézwembad tegen de heuvel",
    "HERO_NAME": "BEYOND HOMES",
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

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2026/03/prime-invest-beyond-homes-02.jpg",
    "LAT": 36.4186770196193,
    "LNG": -5.173404476101808,
    "HREF": "/beyond-homes/",
}
