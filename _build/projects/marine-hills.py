from urllib.parse import quote

PROJECT_NAME = "Marine Hills"
PRICE_FROM = "Vanaf € 464.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "marine-hills",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Marine Hills: appartementen en villa's tot 4 slaapkamers op de New Golden Mile, Estepona. Vanaf €464.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Villa's",
    "OG_DESCRIPTION": "Ontdek Marine Hills: zeezicht, verwarmde zwembaden, spa, padelbaan en co-working ruimte op de New Golden Mile. Vanaf €464.000.",
    "OG_IMAGE": "https://homeinspain.be/wp-content/uploads/2026/07/Marine-Hills.jpg",
    "HERO_BG": "https://homeinspain.be/wp-content/uploads/2026/07/Marine-Hills.jpg",
    "HERO_BG_ALT": "Marine Hills — terras met loungezetels, zwembad en zeezicht",
    "HERO_NAME": "MARINE HILLS",
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
    "META_DESCRIPTION": "Marine Hills: apartments and villas with up to 4 bedrooms on the New Golden Mile, Estepona. From €464.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Villas",
    "OG_DESCRIPTION": "Discover Marine Hills: sea views, heated swimming pools, spa, padel court and coworking space on the New Golden Mile. From €464.000.",
    "HERO_BG_ALT": "Marine Hills — terrace with lounge seating, pool and sea view",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/marine-hills/thumb.webp",
    "LAT": 36.4603322,
    "LNG": -5.0854119,
    "HREF": "/marine-hills/",
}
