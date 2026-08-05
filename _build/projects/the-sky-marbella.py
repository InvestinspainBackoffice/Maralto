from urllib.parse import quote

PROJECT_NAME = "The Sky Marbella"
PRICE_FROM = "Vanaf € 1.495.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-sky-marbella",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Sky Marbella: luxe appartementen, penthouses en villa's boven La Quinta, Benahavís. Vanaf €1.495.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Appartementen & Villa's",
    "OG_DESCRIPTION": "Ontdek The Sky Marbella: panoramisch zee- en bergzicht, 24/7 security en afwerkingen van Gunni & Trentino. Vanaf €1.495.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/08/The-Sky-scaled.jpeg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/08/The-Sky-scaled.jpeg",
    "HERO_BG_ALT": "The Sky Marbella — gebogen gevel met zwembad en bergzicht",
    "HERO_NAME": "THE SKY",
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
    "META_DESCRIPTION": "The Sky Marbella: luxury apartments, penthouses and villas above La Quinta, Benahavís. From €1,495,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Apartments & Villas",
    "OG_DESCRIPTION": "Discover The Sky Marbella: panoramic sea and mountain views, 24/7 security and finishes by Gunni & Trentino. From €1,495,000.",
    "HERO_BG_ALT": "The Sky Marbella — curved facade with pool and mountain views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benahavís",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/the-sky-marbella/thumb.webp",
    "LAT": 36.5226179,
    "LNG": -4.9993343,
    "HREF": "/the-sky-marbella/",
}
