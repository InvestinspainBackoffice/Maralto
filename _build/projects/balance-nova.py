from urllib.parse import quote

PROJECT_NAME = "Balance Nova"
PRICE_FROM = "Vanaf € 320.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "balance-nova",
    "TITLE": f"{PROJECT_NAME} Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Balance Nova: 142 stijlvolle appartementen met 2 en 3 slaapkamers in een groene, goed verbonden omgeving in Mijas Costa. Vanaf €320.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met Zeezicht in Mijas Costa",
    "OG_DESCRIPTION": "Ontdek Balance Nova: 142 appartementen met zwembad, spa, social club, coworkingruimte en fitness, op minder dan 10 minuten van het strand. Vanaf €320.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/balance-nova/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/balance-nova/hero.webp",
    "HERO_BG_ALT": "Balance Nova — gebouw met zwembad en palmbomen",
    "HERO_NAME": "BALANCE NOVA",
    "HERO_LOCATION": "MIJAS",
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
    "META_DESCRIPTION": "Balance Nova: 142 stylish apartments with 2 and 3 bedrooms in a green, well-connected setting in Mijas Costa. From €320,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Sea-view Apartments in Mijas Costa",
    "OG_DESCRIPTION": "Discover Balance Nova: 142 apartments with a pool, spa, social club, coworking space and gym, less than 10 minutes from the beach. From €320,000.",
    "HERO_BG_ALT": "Balance Nova — building with pool and palm trees",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
