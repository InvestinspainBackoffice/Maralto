from urllib.parse import quote

PROJECT_NAME = "Altura Residences"
PRICE_FROM = "Vanaf € 3.995.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "altura-residences",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Altura Residences: ultra-luxe penthouse-villa's op de New Golden Mile in Estepona. Privézwembad, panoramisch zeezicht en de hoogste afwerking. Vanaf €3.995.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-Luxe Penthouse-Villa's in Estepona",
    "OG_DESCRIPTION": "Ontdek Altura Residences: exceptionele penthouse-villa's op de New Golden Mile in Estepona met privézwembad, eigen lift en spectaculair panoramisch zeezicht. Vanaf €3.995.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/altura-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/altura-residences/hero.webp",
    "HERO_BG_ALT": "Altura Residences — ultra-luxe penthouse-villa met zeezicht in Estepona",
    "HERO_NAME": "ALTURA RESIDENCES",
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
    "META_DESCRIPTION": "Altura Residences: ultra-luxury penthouse villas on the New Golden Mile in Estepona. Private pool, panoramic sea views and the finest finishes. From €3,995,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-Luxury Penthouse Villas in Estepona",
    "OG_DESCRIPTION": "Discover Altura Residences: exceptional penthouse villas on the New Golden Mile in Estepona with private pool, private lift and spectacular panoramic sea views. From €3,995,000.",
    "HERO_BG_ALT": "Altura Residences — ultra-luxury penthouse villa with sea views in Estepona",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
