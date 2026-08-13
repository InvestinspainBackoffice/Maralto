from urllib.parse import quote

PROJECT_NAME = "Savia"
PRICE_FROM = "Vanaf € 406.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "savia",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Savia: townhouses met 3-4 slaapkamers, privé tuinen en ingerichte keukens in Mijas. Vanaf € 406.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses in Mijas",
    "OG_DESCRIPTION": "Townhouses met 3-4 slaapkamers, tuinen en ingerichte keukens in Mijas.",
    "OG_IMAGE": "https://projects.investinspain.be/images/savia/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/savia/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Townhouses in Mijas",
    "HERO_NAME": "Savia",
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
    "META_DESCRIPTION": "Savia: townhouses with 3-4 bedrooms, private gardens and fitted kitchens in Mijas. From € 406,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses in Mijas",
    "OG_DESCRIPTION": "Townhouses with 3-4 bedrooms, gardens and fitted kitchens in Mijas.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Townhouses in Mijas",
}

HUB = {
    "NAME": "Savia",
    "LOCATION": "Mijas",
    "PRICE": "Vanaf € 406.000",
    "THUMB": "https://projects.investinspain.be/images/savia/hero.webp",
    "LAT": 36.520652,
    "LNG": -4.652819,
    "HREF": "/savia/",
}
