from urllib.parse import quote

PROJECT_NAME = "ABRIL"
PRICE_FROM = "Vanaf € 400.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "abril",
    "TITLE": f"{PROJECT_NAME} Casares — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "ABRIL: 65 appartementen en penthouses in Doña Julia Golf, Casares. 2-3 slaapkamers, zwembad, spa, fitness, zeezicht. Vanaf € 400.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen bij Doña Julia Golf, Casares",
    "OG_DESCRIPTION": "ABRIL: 65 woningen met overflow-zwembad, spa, zen-zone en panoramisch uitzicht op zee, bergen en golf in Casares. Vanaf € 400.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/abril/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/abril/hero.webp",
    "HERO_BG_ALT": "ABRIL — modern appartementencomplex met zeezicht bij Doña Julia Golf, Casares",
    "HERO_NAME": "ABRIL",
    "HERO_LOCATION": "DOÑA JULIA GOLF, CASARES",
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
    "META_DESCRIPTION": "ABRIL: 65 apartments and penthouses at Doña Julia Golf, Casares. 2-3 bedrooms, pool, spa, gym, sea views. From € 400,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments at Doña Julia Golf, Casares",
    "OG_DESCRIPTION": "ABRIL: 65 homes with overflow pool, spa, zen zone and panoramic views of sea, mountains and golf in Casares. From € 400,000.",
    "HERO_BG_ALT": "ABRIL — modern apartment complex with sea views at Doña Julia Golf, Casares",
}

HUB = {
    "NAME": "ABRIL",
    "LOCATION": "Casares",
    "PRICE": "Vanaf € 400.000",
    "THUMB": "https://projects.investinspain.be/images/abril/hero.webp",
    "LAT": 36.394516,
    "LNG": -5.238496,
    "HREF": "/abril/",
}
