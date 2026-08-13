from urllib.parse import quote

PROJECT_NAME = "Terra Homes"
PRICE_FROM = "Uitverkocht"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "terra-homes",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Terra Homes: 11 exclusieve townhouses in Fuengirola met 3 slaapkamers, zeezicht en solarium. Uitverkocht.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses in Fuengirola",
    "OG_DESCRIPTION": "11 townhouses met zeezicht en solarium in Fuengirola — Costa del Sol.",
    "OG_IMAGE": "https://projects.investinspain.be/images/terra-homes/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/terra-homes/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Townhouses in Fuengirola",
    "HERO_NAME": "Terra Homes",
    "HERO_LOCATION": "FUENGIROLA",
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
    "META_DESCRIPTION": "Terra Homes: 11 exclusive townhouses in Fuengirola with 3 bedrooms, sea views and solarium. Sold out.",
    "OG_TITLE": f"{PROJECT_NAME} — Townhouses in Fuengirola",
    "OG_DESCRIPTION": "11 townhouses with sea views and solarium in Fuengirola — Costa del Sol.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Townhouses in Fuengirola",
}

HUB = {
    "NAME": "Terra Homes",
    "LOCATION": "Fuengirola",
    "PRICE": "Uitverkocht",
    "THUMB": "https://projects.investinspain.be/images/terra-homes/hero.webp",
    "LAT": 36.559949,
    "LNG": -4.621622,
    "HREF": "/terra-homes/",
}
