from urllib.parse import quote

PROJECT_NAME = "Blue Marine"
PRICE_FROM = "Vanaf € 465.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "blue-marine",
    "TITLE": f"{PROJECT_NAME} MANILVA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Blue Marine Manilva: moderne appartementen met zwembad en zeezicht aan de westelijke Costa del Sol. Op korte afstand van Sotogrande en Gibraltar. Vanaf € 465.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen met zeezicht in Manilva",
    "OG_DESCRIPTION": "Blue Marine biedt stijlvolle appartementen met zwembad en weids zeezicht in Manilva, aan de westelijke Costa del Sol, dicht bij Sotogrande.",
    "OG_IMAGE": "https://projects.investinspain.be/images/blue-marine/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/blue-marine/hero.webp",
    "HERO_BG_ALT": "Blue Marine — modern appartementencomplex met zeezicht in Manilva",
    "HERO_NAME": "Blue Marine",
    "HERO_LOCATION": "MANILVA",
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
    "META_DESCRIPTION": "Blue Marine Manilva: modern apartments with pool and sea views on the western Costa del Sol. Short distance to Sotogrande and Gibraltar. From € 465,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments with sea views in Manilva",
    "OG_DESCRIPTION": "Blue Marine offers stylish apartments with pool and sweeping sea views in Manilva, on the western Costa del Sol, close to Sotogrande.",
    "HERO_BG_ALT": "Blue Marine — modern apartment complex with sea views in Manilva",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Manilva",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/blue-marine/hero.webp",
    "LAT": 36.347712,
    "LNG": -5.239791,
    "HREF": "/blue-marine/",
}
