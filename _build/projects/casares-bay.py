from urllib.parse import quote

PROJECT_NAME = "Casares Bay"
PRICE_FROM = "Vanaf € 467.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "casares-bay",
    "TITLE": f"{PROJECT_NAME} Casares — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Casares Bay: moderne appartementen met zeezicht en gemeenschappelijk zwembad in Casares Costa. Rustige omgeving nabij Sotogrande en de westkust. Vanaf €467.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met Zeezicht in Casares",
    "OG_DESCRIPTION": "Ontdek Casares Bay: eigentijdse appartementen met zeezicht en gemeenschappelijk zwembad in de rustige omgeving van Casares Costa, nabij Sotogrande. Vanaf €467.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/casares-bay/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/casares-bay/hero.webp",
    "HERO_BG_ALT": "Casares Bay — moderne appartementen met zeezicht in Casares Costa",
    "HERO_NAME": "CASARES BAY",
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
    "META_DESCRIPTION": "Casares Bay: modern apartments with sea views and communal pool in Casares Costa. Peaceful setting near Sotogrande and the western coastline. From €467,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with Sea Views in Casares",
    "OG_DESCRIPTION": "Discover Casares Bay: contemporary apartments with sea views and communal pool in the peaceful surroundings of Casares Costa, near Sotogrande. From €467,000.",
    "HERO_BG_ALT": "Casares Bay — modern apartments with sea views in Casares Costa",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
