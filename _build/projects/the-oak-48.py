from urllib.parse import quote

PROJECT_NAME = "The Oak 48"
PRICE_FROM = "Vanaf € 511.500"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-oak-48",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Oak 48: 48 exclusieve woningen vlakbij het centrum van Estepona. Eigentijdse architectuur, adembenemend zeezicht, solarium en zwembad. Vanaf € 511.500.",
    "OG_TITLE": f"{PROJECT_NAME} · 48 exclusieve woningen Estepona centrum",
    "OG_DESCRIPTION": "48 exclusieve woningen op een bevoorrechte locatie in Estepona. Eigentijdse architectuur, design en functionaliteit, adembenemend uitzicht. Vanaf € 511.500.",
    "OG_IMAGE": "https://projects.investinspain.be/images/the-oak-48/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/the-oak-48/hero.webp",
    "HERO_BG_ALT": "The Oak 48 gevel zwembad Estepona",
    "HERO_NAME": PROJECT_NAME,
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
    "MAP_LAT": "36.43479861235",
    "MAP_LNG": "-5.151185335531",
}

DATA_EN = {
    "META_DESCRIPTION": "The Oak 48: 48 exclusive homes near the centre of Estepona. Contemporary architecture, breathtaking sea views, solarium and pool. From € 511,500.",
    "OG_TITLE": f"{PROJECT_NAME} · 48 exclusive homes Estepona centre",
    "OG_DESCRIPTION": "48 exclusive homes in a privileged location in Estepona. Contemporary architecture, design and functionality, breathtaking views. From € 511,500.",
    "HERO_BG_ALT": "The Oak 48 facade pool Estepona",
}
