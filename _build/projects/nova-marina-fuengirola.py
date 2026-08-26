from urllib.parse import quote

PROJECT_NAME = "Nova Marina"
PRICE_FROM = "Vanaf € 520.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "nova-marina-fuengirola",
    "TITLE": f"{PROJECT_NAME} FUENGIROLA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Nova Marina Fuengirola: moderne appartementen met terras en gemeenschappelijk zwembad, dicht bij het strand van Fuengirola. Vanaf € 520.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen in Fuengirola",
    "OG_DESCRIPTION": "Nova Marina biedt stijlvolle appartementen met terras en zwembad, op korte afstand van het strand en het centrum van Fuengirola.",
    "OG_IMAGE": "https://projects.investinspain.be/images/nova-marina-fuengirola/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/nova-marina-fuengirola/hero.webp",
    "HERO_BG_ALT": "Nova Marina — modern appartementencomplex in Fuengirola",
    "HERO_NAME": "Nova Marina",
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
    "META_DESCRIPTION": "Nova Marina Fuengirola: modern apartments with terrace and communal pool, close to Fuengirola's beach. From € 520,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments in Fuengirola",
    "OG_DESCRIPTION": "Nova Marina offers stylish apartments with terrace and pool, a short distance from the beach and centre of Fuengirola.",
    "HERO_BG_ALT": "Nova Marina — modern apartment complex in Fuengirola",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Fuengirola",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/nova-marina-fuengirola/hero.webp",
    "LAT": 36.570048,
    "LNG": -4.609375,
    "HREF": "/nova-marina-fuengirola/",
}
