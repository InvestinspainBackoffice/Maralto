from urllib.parse import quote

PROJECT_NAME = "Bliss Homes"
PRICE_FROM = "Vanaf € 380.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "bliss-homes",
    "TITLE": f"{PROJECT_NAME} Casares — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Bliss Homes: 134 appartementen en penthouses in Casares. 2-4 slaapkamers, zwembad, fitness, nabij golf en strand. Vanaf € 380.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Casares",
    "OG_DESCRIPTION": "Bliss Homes: modern woonproject met 134 woningen, zwembad, fitnessruimte en prachtig uitzicht op zee en bergen in Casares. Vanaf € 380.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/bliss-homes/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/bliss-homes/hero.webp",
    "HERO_BG_ALT": "Bliss Homes — modern appartementencomplex met zwembad in Casares",
    "HERO_NAME": "Bliss Homes",
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
    "META_DESCRIPTION": "Bliss Homes: 134 apartments and penthouses in Casares. 2-4 bedrooms, pool, gym, near golf and beach. From € 380,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Casares",
    "OG_DESCRIPTION": "Bliss Homes: modern development with 134 homes, pool, gym and stunning sea and mountain views in Casares. From € 380,000.",
    "HERO_BG_ALT": "Bliss Homes — modern apartment complex with pool in Casares",
}

HUB = {
    "NAME": "Bliss Homes",
    "LOCATION": "Casares",
    "PRICE": "Vanaf € 380.000",
    "THUMB": "https://projects.investinspain.be/images/bliss-homes/hero.webp",
    "LAT": 36.393760,
    "LNG": -5.227498,
    "HREF": "/bliss-homes/",
}
