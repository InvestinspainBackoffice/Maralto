from urllib.parse import quote

PROJECT_NAME = "Kosmos"
PRICE_FROM = "Vanaf € 415.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "kosmos",
    "TITLE": f"{PROJECT_NAME} Oost-Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Kosmos: welness-appartementen en penthouses met 2 en 3 slaapkamers in Oost-Marbella. Zwembaden, spa, fitness en co-working. Vanaf € 415.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Oost-Marbella",
    "OG_DESCRIPTION": "Kosmos: wellness-concept met domotica, privéterrassen en panoramisch berg- en zeezicht nabij Marbella. Vanaf € 415.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/kosmos/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/kosmos/hero.webp",
    "HERO_BG_ALT": "Kosmos — modern wellnessproject met zwembad in Oost-Marbella",
    "HERO_NAME": "Kosmos",
    "HERO_LOCATION": "TORREMOLINOS",
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
    "META_DESCRIPTION": "Kosmos: wellness apartments and penthouses with 2 and 3 bedrooms in East Marbella. Pools, spa, gym and co-working. From € 415,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in East Marbella",
    "OG_DESCRIPTION": "Kosmos: wellness concept with smart home technology, private terraces and panoramic mountain and sea views near Marbella. From € 415,000.",
    "HERO_BG_ALT": "Kosmos — modern wellness project with pool in East Marbella",
}

HUB = {
    "NAME": "Kosmos",
    "LOCATION": "Torremolinos",
    "PRICE": "Vanaf € 415.000",
    "THUMB": "https://projects.investinspain.be/images/kosmos/hero.webp",
    "LAT": 36.617088,
    "LNG": -4.51644,
    "HREF": "/kosmos/",
}
