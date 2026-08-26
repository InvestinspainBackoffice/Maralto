from urllib.parse import quote

PROJECT_NAME = "Azahar de Estepona"
PRICE_FROM = "Vanaf € 625.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "azahar-de-estepona-2",
    "TITLE": f"{PROJECT_NAME} Penthouse — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Azahar de Estepona: exclusief penthouse 2 slaapkamers met dakterras, meerdere terrassen en zeezicht. 61 moderne woningen, gym, zwembad en golfnabijheid. Vanaf €625.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Penthouse met Dakterras en Zeezicht",
    "OG_DESCRIPTION": "Ontdek dit exclusieve penthouse in Azahar de Estepona: 2 slaapkamers, meerdere terrassen, dakterras met spiraaltrap en prachtig zeezicht. Complex met gym, gedeeld zwembad en groene zones. Vanaf €625.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/azahar-de-estepona-2/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/azahar-de-estepona-2/hero.webp",
    "HERO_BG_ALT": "Azahar de Estepona — modern complex met zeezicht",
    "HERO_NAME": "AZAHAR DE ESTEPONA",
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
    "META_DESCRIPTION": "Azahar de Estepona: exclusive 2-bedroom penthouse with rooftop terrace, multiple terraces and sea views. 61 modern homes, gym, pool and golf proximity. From €625,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Penthouse with Rooftop Terrace and Sea Views",
    "OG_DESCRIPTION": "Discover this exclusive penthouse in Azahar de Estepona: 2 bedrooms, multiple terraces, rooftop terrace with spiral staircase and beautiful sea views. Complex with gym, shared pool and green zones. From €625,000.",
    "HERO_BG_ALT": "Azahar de Estepona — modern complex with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/azahar-de-estepona-2/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/azahar-de-estepona-2/",
}
