from urllib.parse import quote

PROJECT_NAME = "One Oak"
PRICE_FROM = "Vanaf € 563.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "one-oak",
    "TITLE": f"{PROJECT_NAME} Torremolinos — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "One Oak: appartementen, penthouses en gelijkvloerse woningen met 1 tot 4 slaapkamers en zeezicht in Torremolinos. Vanaf € 563.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Torremolinos",
    "OG_DESCRIPTION": "One Oak: panoramisch zeezicht over de Baai van Málaga, twee buitenzwembaden en fitnessruimte, vlak bij Pinar del Moro. Vanaf € 563.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/one-oak/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/one-oak/hero.webp",
    "HERO_BG_ALT": "One Oak — moderne appartementen met zeezicht in Torremolinos",
    "HERO_NAME": "One Oak",
    "HERO_LOCATION": "TORREMOLINOS",
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
    "META_DESCRIPTION": "One Oak: apartments, penthouses and ground-floor homes with 1 to 4 bedrooms and sea views in Torremolinos. From € 563,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Torremolinos",
    "OG_DESCRIPTION": "One Oak: panoramic views over the Bay of Málaga, two outdoor pools and a gym, right next to Pinar del Moro. From € 563,000.",
    "HERO_BG_ALT": "One Oak — modern apartments with sea views in Torremolinos",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Torremolinos",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/one-oak/hero.webp",
    "LAT": 36.6281,
    "LNG": -4.5032,
    "HREF": "/one-oak/",
}
