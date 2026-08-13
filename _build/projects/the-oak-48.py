from urllib.parse import quote

PROJECT_NAME = "The Oak 48"
PRICE_FROM = "Vanaf € 511.500"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-oak-48",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Oak 48: 48 exclusieve appartementen en penthouses in Estepona. 2-3 slaapkamers, zwembad, gym, co-working, solarium. Vanaf € 511.500.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "The Oak 48: modern woonproject met panoramisch zeezicht, zwembad, fitnessruimte, co-working en social lounge in Estepona. Vanaf € 511.500.",
    "OG_IMAGE": "https://projects.investinspain.be/images/the-oak-48/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/the-oak-48/hero.webp",
    "HERO_BG_ALT": "The Oak 48 — modern appartementencomplex met zwembad in Estepona",
    "HERO_NAME": "The Oak 48",
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
    "META_DESCRIPTION": "The Oak 48: 48 exclusive apartments and penthouses in Estepona. 2-3 bedrooms, pool, gym, co-working, solarium. From € 511,500.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "The Oak 48: modern residential project with panoramic sea views, pool, gym, co-working and social lounge in Estepona. From € 511,500.",
    "HERO_BG_ALT": "The Oak 48 — modern apartment complex with pool in Estepona",
}

HUB = {
    "NAME": "The Oak 48",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 511.500",
    "THUMB": "https://projects.investinspain.be/images/the-oak-48/hero.webp",
    "LAT": 36.434799,
    "LNG": -5.151185,
    "HREF": "/the-oak-48/",
}
