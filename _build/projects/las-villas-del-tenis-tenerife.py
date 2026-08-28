from urllib.parse import quote

PROJECT_NAME = "Las Villas del Tenis"
PRICE_FROM = "Vanaf € 2.050.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "las-villas-del-tenis-tenerife",
    "TITLE": f"{PROJECT_NAME} Tenerife — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Las Villas del Tenis: exclusieve villa's op het prestigieuze Abama Resort in Tenerife. Privézwembad, zeezicht en 5-sterrenresortfaciliteiten in Guía de Isora. Vanaf € 2.050.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve villa's op Abama Resort, Tenerife",
    "OG_DESCRIPTION": "Las Villas del Tenis op het Abama Resort in Tenerife: luxueuze villa's met privézwembad, zeezicht en toegang tot alle 5-sterren resortfaciliteiten. Vanaf € 2.050.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/las-villas-del-tenis-tenerife/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/las-villas-del-tenis-tenerife/hero.webp",
    "HERO_BG_ALT": "Las Villas del Tenis Tenerife exterieur op Abama Resort",
    "HERO_NAME": "Las Villas del Tenis",
    "HERO_LOCATION": "TENERIFE, CANARISCHE EILANDEN",
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
    "META_DESCRIPTION": "Las Villas del Tenis: exclusive villas at the prestigious Abama Resort in Tenerife. Private pool, sea views and 5-star resort amenities in Guía de Isora. From € 2,050,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive villas at Abama Resort, Tenerife",
    "OG_DESCRIPTION": "Las Villas del Tenis at Abama Resort in Tenerife: luxury villas with private pool, sea views and access to all 5-star resort amenities. From € 2,050,000.",
    "HERO_BG_ALT": "Las Villas del Tenis Tenerife exterior at Abama Resort",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Tenerife",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/las-villas-del-tenis-tenerife/hero.webp",
    "LAT": 28.17194,
    "LNG": -16.785994,
    "HREF": "/las-villas-del-tenis-tenerife/",
}
