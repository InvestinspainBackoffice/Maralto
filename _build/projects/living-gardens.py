from urllib.parse import quote

PROJECT_NAME = "Living Gardens"
PRICE_FROM = "Vanaf € 350.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "living-gardens",
    "TITLE": f"{PROJECT_NAME} TORREMOLINOS — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Living Gardens Torremolinos: moderne appartementen met terras, communaal zwembad en tuinen. Op korte afstand van het strand en Málaga Airport. Vanaf € 350.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen in Torremolinos",
    "OG_DESCRIPTION": "Living Gardens biedt stijlvolle appartementen met terras en gemeenschappelijke tuinen in Torremolinos, dicht bij het strand en Málaga Airport.",
    "OG_IMAGE": "https://projects.investinspain.be/images/living-gardens/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/living-gardens/hero.webp",
    "HERO_BG_ALT": "Living Gardens — modern appartementencomplex in Torremolinos",
    "HERO_NAME": "Living Gardens",
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
    "META_DESCRIPTION": "Living Gardens Torremolinos: modern apartments with terrace, communal pool and gardens. Short distance to the beach and Málaga Airport. From € 350,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments in Torremolinos",
    "OG_DESCRIPTION": "Living Gardens offers stylish apartments with terrace and communal gardens in Torremolinos, close to the beach and Málaga Airport.",
    "HERO_BG_ALT": "Living Gardens — modern apartment complex in Torremolinos",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
