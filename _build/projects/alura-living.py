from urllib.parse import quote

PROJECT_NAME = "Alura Living"
PRICE_FROM = "Vanaf € 440.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "alura-living",
    "TITLE": f"{PROJECT_NAME} Casares — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Alura Living: moderne appartementen en penthouses met 2 en 3 slaapkamers in Casares. Zwembaden, spa, fitness en golfsimulator. Vanaf € 440.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Casares",
    "OG_DESCRIPTION": "Alura Living: Mediterraan wonen met wellness, sauna, hammam en nabij strand en golf in Casares. Vanaf € 440.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/alura-living/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/alura-living/hero.webp",
    "HERO_BG_ALT": "Alura Living — modern appartementscomplex met zwembad in Casares",
    "HERO_NAME": "Alura Living",
    "HERO_LOCATION": "CASARES, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Alura Living: modern apartments and penthouses with 2 and 3 bedrooms in Casares. Pools, spa, gym and golf simulator. From € 440,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Casares",
    "OG_DESCRIPTION": "Alura Living: Mediterranean living with wellness, sauna, hammam and close to beach and golf in Casares. From € 440,000.",
    "HERO_BG_ALT": "Alura Living — modern apartment complex with pool in Casares",
}

HUB = {
    "NAME": "Alura Living",
    "LOCATION": "Casares",
    "PRICE": "Vanaf € 440.000",
    "THUMB": "https://projects.investinspain.be/images/alura-living/hero.webp",
    "LAT": 36.3835,
    "LNG": -5.2247,
    "HREF": "/alura-living/",
}
