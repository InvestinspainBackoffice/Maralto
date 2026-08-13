from urllib.parse import quote

PROJECT_NAME = "Armonia"
PRICE_FROM = "Vanaf € 467.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "armonia",
    "TITLE": f"{PROJECT_NAME} San Pedro de Alcántara — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Armonia: moderne appartementen met 2-3 slaapkamers nabij strand en golf in San Pedro de Alcántara. Vanaf € 467.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in San Pedro de Alcántara",
    "OG_DESCRIPTION": "Moderne appartementen nabij strand, jachthavens en golf in San Pedro de Alcántara.",
    "OG_IMAGE": "https://projects.investinspain.be/images/armonia/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/armonia/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Appartementen in San Pedro de Alcántara",
    "HERO_NAME": "Armonia",
    "HERO_LOCATION": "SAN PEDRO DE ALCÁNTARA",
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
    "META_DESCRIPTION": "Armonia: modern apartments with 2-3 bedrooms near beach and golf in San Pedro de Alcántara. From € 467,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in San Pedro de Alcántara",
    "OG_DESCRIPTION": "Modern apartments near beach, marinas and golf in San Pedro de Alcántara.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Apartments in San Pedro de Alcántara",
}

HUB = {
    "NAME": "Armonia",
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": "Vanaf € 467.000",
    "THUMB": "https://projects.investinspain.be/images/armonia/hero.webp",
    "LAT": 36.491237,
    "LNG": -4.992611,
    "HREF": "/armonia/",
}
