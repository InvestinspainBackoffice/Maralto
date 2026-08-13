from urllib.parse import quote

PROJECT_NAME = "Horizonte Village"
PRICE_FROM = "Vanaf € 650.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "horizonte-village",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Horizonte Village: 62 luxe woningen in de bergen van Mijas met privézwembad, vloerverwarming en panoramisch zeezicht. Vanaf € 650.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's in Mijas",
    "OG_DESCRIPTION": "62 woningen in de bergen van Mijas met privézwembad, vloerverwarming en smart home.",
    "OG_IMAGE": "https://projects.investinspain.be/images/horizonte-village/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/horizonte-village/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villa's in Mijas",
    "HERO_NAME": "Horizonte Village",
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
    "META_DESCRIPTION": "Horizonte Village: 62 luxury homes in the Mijas mountains with private pool, underfloor heating and panoramic sea views. From € 650,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas in Mijas",
    "OG_DESCRIPTION": "62 homes in the Mijas mountains with private pool, underfloor heating and smart home.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villas in Mijas",
}

HUB = {
    "NAME": "Horizonte Village",
    "LOCATION": "Mijas",
    "PRICE": "Vanaf € 650.000",
    "THUMB": "https://projects.investinspain.be/images/horizonte-village/hero.webp",
    "LAT": 36.589803,
    "LNG": -4.605264,
    "HREF": "/horizonte-village/",
}
