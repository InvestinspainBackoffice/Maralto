from urllib.parse import quote

PROJECT_NAME = "Symphony Suites"
PRICE_FROM = "Vanaf € 494.900"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "symphony-suites",
    "TITLE": f"{PROJECT_NAME} CANCELADA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Symphony Suites Cancelada: 69 luxueuze appartementen met zeezicht, verdeeld over 4 blokken in West-Marbella. Vanaf € 494.900.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met zeezicht in Cancelada",
    "OG_DESCRIPTION": "Symphony Suites biedt 69 moderne appartementen met 2 of 3 slaapkamers, allemaal met zeezicht, in Cancelada, West-Marbella.",
    "OG_IMAGE": "https://projects.investinspain.be/images/symphony-suites/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/symphony-suites/hero.webp",
    "HERO_BG_ALT": "Symphony Suites — modern appartementencomplex met zeezicht in Cancelada",
    "HERO_NAME": "Symphony Suites",
    "HERO_LOCATION": "CANCELADA, MARBELLA",
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
    "META_DESCRIPTION": "Symphony Suites Cancelada: 69 luxurious apartments with sea views, spread across 4 blocks in West Marbella. From € 494,900.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with sea views in Cancelada",
    "OG_DESCRIPTION": "Symphony Suites offers 69 modern apartments with 2 or 3 bedrooms, all with sea views, in Cancelada, West Marbella.",
    "HERO_BG_ALT": "Symphony Suites — modern apartment complex with sea views in Cancelada",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
