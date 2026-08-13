from urllib.parse import quote

PROJECT_NAME = "Taray"
PRICE_FROM = "Vanaf € 750.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "taray",
    "TITLE": f"{PROJECT_NAME} Benahavís — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Taray Residences: 21 moderne woningen met 3 slaapkamers en berg- en zeezicht in Benahavís. Vanaf € 750.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Benahavís",
    "OG_DESCRIPTION": "21 moderne woningen met berg- en zeezicht in Benahavís — exclusief gated community.",
    "OG_IMAGE": "https://projects.investinspain.be/images/taray/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/taray/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Appartementen in Benahavís",
    "HERO_NAME": "Taray",
    "HERO_LOCATION": "BENAHAVÍS",
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
    "META_DESCRIPTION": "Taray Residences: 21 modern homes with 3 bedrooms and mountain & sea views in Benahavís. From € 750,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Benahavís",
    "OG_DESCRIPTION": "21 modern homes with mountain & sea views in Benahavís — exclusive gated community.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Apartments in Benahavís",
}

HUB = {
    "NAME": "Taray",
    "LOCATION": "Benahavís",
    "PRICE": "Vanaf € 750.000",
    "THUMB": "https://projects.investinspain.be/images/taray/hero.webp",
    "LAT": 36.469381,
    "LNG": -5.050931,
    "HREF": "/taray/",
}
