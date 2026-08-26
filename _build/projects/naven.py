from urllib.parse import quote

PROJECT_NAME = "Naven"
PRICE_FROM = "Vanaf € 375.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "naven",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Naven: nieuwbouwappartementen met 1 tot 4 slaapkamers vlakbij centrum Fuengirola, met volledig resort-aanbod. Vanaf €375.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met Resort-aanbod nabij Centrum Fuengirola",
    "OG_DESCRIPTION": "Ontdek Naven: appartementen met 1 tot 4 slaapkamers, binnen-wellnesszwembad, sauna, hamam en fitness, op wandelafstand van het strand van Fuengirola. Vanaf €375.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/naven/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/naven/hero.webp",
    "HERO_BG_ALT": "Naven — luchtfoto van het complex bij zonsondergang, Fuengirola",
    "HERO_NAME": "NAVEN",
    "HERO_LOCATION": "FUENGIROLA",
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
    "META_DESCRIPTION": "Naven: new-build apartments with 1 to 4 bedrooms near central Fuengirola, with a full resort offering. From €375,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with a Resort Offering near Central Fuengirola",
    "OG_DESCRIPTION": "Discover Naven: apartments with 1 to 4 bedrooms, an indoor wellness pool, sauna, hammam and gym, within walking distance of Fuengirola beach. From €375,000.",
    "HERO_BG_ALT": "Naven — aerial view of the complex at dusk, Fuengirola",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Fuengirola",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/naven/hero.webp",
    "LAT": 36.570048,
    "LNG": -4.609375,
    "HREF": "/naven/",
}
