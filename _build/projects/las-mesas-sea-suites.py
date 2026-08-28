from urllib.parse import quote

PROJECT_NAME = "Las Mesas Sea Suites"
PRICE_FROM = "Vanaf € 580.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "las-mesas-sea-suites",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Las Mesas Sea Suites: duurzame appartementen met 2 of 3 slaapkamers, zoutwaterzwembad en wellnessruimte in het hart van Estepona. Vanaf € 580.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Estepona",
    "OG_DESCRIPTION": "Las Mesas Sea Suites: royale terrassen, Bosch-keukens, Turks bad en zonnepanelen in een beveiligd complex in Estepona. Vanaf € 580.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/las-mesas-sea-suites/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/las-mesas-sea-suites/hero.webp",
    "HERO_BG_ALT": "Las Mesas Sea Suites — moderne appartementen in Estepona",
    "HERO_NAME": "Las Mesas Sea Suites",
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
    "META_DESCRIPTION": "Las Mesas Sea Suites: sustainable apartments with 2 or 3 bedrooms, a saltwater pool and wellness area in the heart of Estepona. From € 580,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Estepona",
    "OG_DESCRIPTION": "Las Mesas Sea Suites: generous terraces, Bosch kitchens, Turkish bath and solar panels in a gated complex in Estepona. From € 580,000.",
    "HERO_BG_ALT": "Las Mesas Sea Suites — modern apartments in Estepona",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/las-mesas-sea-suites/hero.webp",
    "LAT": 36.424648,
    "LNG": -5.158481,
    "HREF": "/las-mesas-sea-suites/",
}
