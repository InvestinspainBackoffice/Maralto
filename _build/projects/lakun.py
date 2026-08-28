from urllib.parse import quote

PROJECT_NAME = "Lakün"
PRICE_FROM = "Vanaf € 405.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "lakun",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Lakün: 233 appartementen en penthouses in Mijas met spa, 3 zwembaden en co-working. 1-4.5 slaapkamers. Vanaf € 405.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Mijas",
    "OG_DESCRIPTION": "Lakün: Groot residentieel complex met 233 eenheden, spa, 3 zwembaden, fitness en co-working ruimte. Vanaf € 405.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/lakun/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/lakun/hero.webp",
    "HERO_BG_ALT": "Lakün — groot residentieel complex in Mijas",
    "HERO_NAME": "Lakün",
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
    "META_DESCRIPTION": "Lakün: 233 apartments and penthouses in Mijas with spa, 3 pools and co-working. 1-4.5 bedrooms. From € 405,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Mijas",
    "OG_DESCRIPTION": "Lakün: Large residential complex with 233 units, spa, 3 pools, fitness and co-working space. From € 405,000.",
    "HERO_BG_ALT": "Lakün — large residential complex in Mijas",
}

HUB = {
    "NAME": "Lakün",
    "LOCATION": "Mijas",
    "PRICE": "Vanaf € 405.000",
    "THUMB": "https://projects.investinspain.be/images/lakun/hero.webp",
    "LAT": 36.537179,
    "LNG": -4.636552,
    "HREF": "/lakun/",
}
