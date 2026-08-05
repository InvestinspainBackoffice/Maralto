from urllib.parse import quote

PROJECT_NAME = "Amaranta Living"
PRICE_FROM = "Vanaf € 446.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "amaranta-living",
    "TITLE": f"{PROJECT_NAME} Casares — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Amaranta Living: moderne appartementen met zeezicht en gemeenschappelijk zwembad in Casares Costa. Rustige ligging, natuur en de kust op minuten. Vanaf €446.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne Appartementen in Casares Costa",
    "OG_DESCRIPTION": "Ontdek Amaranta Living: stijlvolle appartementen in Casares Costa met zeezicht, gemeenschappelijk zwembad en een rustige, groene omgeving dicht bij de kust. Vanaf €446.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/amaranta-living/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/amaranta-living/hero.webp",
    "HERO_BG_ALT": "Amaranta Living — moderne appartementen met zeezicht in Casares Costa",
    "HERO_NAME": "AMARANTA LIVING",
    "HERO_LOCATION": "CASARES",
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
    "META_DESCRIPTION": "Amaranta Living: modern apartments with sea views and communal pool in Casares Costa. Peaceful setting, nature and the coast minutes away. From €446,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Apartments in Casares Costa",
    "OG_DESCRIPTION": "Discover Amaranta Living: stylish apartments in Casares Costa with sea views, communal pool and a peaceful, green setting close to the coast. From €446,000.",
    "HERO_BG_ALT": "Amaranta Living — modern apartments with sea views in Casares Costa",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
