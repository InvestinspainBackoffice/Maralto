from urllib.parse import quote

PROJECT_NAME = "Térmica Beach"
PRICE_FROM = "Vanaf € 720.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "termica-beach",
    "TITLE": f"{PROJECT_NAME} Málaga — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Térmica Beach: bijna 400 woningen op frontline beach in Málaga met zeezicht en gemeenschappelijke tuin. Vanaf € 720.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Málaga",
    "OG_DESCRIPTION": "Grootschalig strandproject met ~400 woningen op frontline beach in Málaga.",
    "OG_IMAGE": "https://projects.investinspain.be/images/termica-beach/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/termica-beach/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Appartementen in Málaga",
    "HERO_NAME": "Térmica Beach",
    "HERO_LOCATION": "MÁLAGA",
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
    "META_DESCRIPTION": "Térmica Beach: nearly 400 homes on the beachfront in Málaga with sea views and communal garden. From € 720,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Málaga",
    "OG_DESCRIPTION": "Large-scale beach project with ~400 homes on the beachfront in Málaga.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Apartments in Málaga",
}

HUB = {
    "NAME": "Térmica Beach",
    "LOCATION": "Málaga",
    "PRICE": "Vanaf € 720.000",
    "THUMB": "https://projects.investinspain.be/images/termica-beach/hero.webp",
    "LAT": 36.683061,
    "LNG": -4.447854,
    "HREF": "/termica-beach/",
}
