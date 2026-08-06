from urllib.parse import quote

PROJECT_NAME = "Alcaidesa Homes"
PRICE_FROM = "Vanaf € 643.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "alcaidesa-homes",
    "TITLE": f"{PROJECT_NAME} LA ALCAIDESA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Alcaidesa Homes: moderne woningen met ruime terrassen en zicht op Gibraltar, in La Alcaidesa. Vanaf € 643.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne woningen met zicht op Gibraltar",
    "OG_DESCRIPTION": "Alcaidesa Homes biedt moderne appartementen en penthouses met ruime terrassen en weids uitzicht op Gibraltar, in La Alcaidesa.",
    "OG_IMAGE": "https://projects.investinspain.be/images/alcaidesa-homes/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/alcaidesa-homes/hero.webp",
    "HERO_BG_ALT": "Alcaidesa Homes — modern appartementencomplex met zicht op Gibraltar",
    "HERO_NAME": "Alcaidesa Homes",
    "HERO_LOCATION": "LA ALCAIDESA",
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
    "META_DESCRIPTION": "Alcaidesa Homes: modern homes with spacious terraces and views of Gibraltar, in La Alcaidesa. From € 643,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern homes with views of Gibraltar",
    "OG_DESCRIPTION": "Alcaidesa Homes offers modern apartments and penthouses with spacious terraces and sweeping views of Gibraltar, in La Alcaidesa.",
    "HERO_BG_ALT": "Alcaidesa Homes — modern apartment complex with views of Gibraltar",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
