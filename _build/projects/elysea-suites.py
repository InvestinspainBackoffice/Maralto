from urllib.parse import quote

PROJECT_NAME = "Elysea Suites"
PRICE_FROM = "Vanaf € 1.050.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "elysea-suites",
    "TITLE": f"{PROJECT_NAME} MIJAS COSTA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Elysea Suites Mijas Costa: exclusieve appartementen met premium afwerking en zeezicht aan de Costa del Sol. Vanaf € 1.050.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve appartementen in Mijas Costa",
    "OG_DESCRIPTION": "Elysea Suites biedt luxueuze appartementen met premium afwerking en weids zeezicht in Mijas Costa, aan de Costa del Sol.",
    "OG_IMAGE": "https://projects.investinspain.be/images/elysea-suites/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/elysea-suites/hero.webp",
    "HERO_BG_ALT": "Elysea Suites — exclusief appartementencomplex in Mijas Costa",
    "HERO_NAME": "Elysea Suites",
    "HERO_LOCATION": "MIJAS COSTA",
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
    "META_DESCRIPTION": "Elysea Suites Mijas Costa: exclusive apartments with premium finishes and sea views on the Costa del Sol. From € 1,050,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive apartments in Mijas Costa",
    "OG_DESCRIPTION": "Elysea Suites offers luxurious apartments with premium finishes and sweeping sea views in Mijas Costa, on the Costa del Sol.",
    "HERO_BG_ALT": "Elysea Suites — exclusive apartment complex in Mijas Costa",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
