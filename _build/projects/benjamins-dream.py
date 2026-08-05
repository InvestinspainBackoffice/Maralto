from urllib.parse import quote

PROJECT_NAME = "Benjamin's Dream"
PRICE_FROM = "Vanaf € 899.950"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "benjamins-dream",
    "TITLE": f"{PROJECT_NAME} Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Benjamin's Dream: exclusieve villa's met zeezicht in Mijas Costa. Privézwembad, moderne architectuur en panoramisch uitzicht op zee. Vanaf €899.950.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's met Zeezicht in Mijas Costa",
    "OG_DESCRIPTION": "Ontdek Benjamin's Dream: exclusieve villa's met privézwembad en panoramisch zeezicht in Mijas Costa. Moderne architectuur op een unieke locatie. Vanaf €899.950.",
    "OG_IMAGE": "https://projects.investinspain.be/images/benjamins-dream/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/benjamins-dream/hero.webp",
    "HERO_BG_ALT": "Benjamin's Dream — villa met privézwembad en zeezicht in Mijas Costa",
    "HERO_NAME": "BENJAMIN'S DREAM",
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
    "META_DESCRIPTION": "Benjamin's Dream: exclusive villas with sea views in Mijas Costa. Private pool, modern architecture and panoramic views over the Mediterranean. From €899,950.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas with Sea Views in Mijas Costa",
    "OG_DESCRIPTION": "Discover Benjamin's Dream: exclusive villas with private pool and panoramic sea views in Mijas Costa. Modern architecture in a unique setting. From €899,950.",
    "HERO_BG_ALT": "Benjamin's Dream — villa with private pool and sea views in Mijas Costa",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
