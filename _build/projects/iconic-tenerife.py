from urllib.parse import quote

PROJECT_NAME = "Iconic Tenerife"
PRICE_FROM = "Vanaf € 1.005.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "iconic-tenerife",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Iconic Tenerife: exclusieve appartementen en penthouses met spectaculair zeezicht op Tenerife. Moderne architectuur, dakterrassen en topfaciliteiten. Vanaf € 1.005.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve appartementen met zeezicht op Tenerife",
    "OG_DESCRIPTION": "Iconic Tenerife: luxueuze appartementen en sky penthouses met panoramisch zeezicht, moderne architectuur en eersteklas faciliteiten op de Canarische Eilanden. Vanaf € 1.005.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/iconic-tenerife/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/iconic-tenerife/hero.webp",
    "HERO_BG_ALT": "Iconic Tenerife exterieur luchtfoto met zeezicht",
    "HERO_NAME": "Iconic Tenerife",
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
    "META_DESCRIPTION": "Iconic Tenerife: exclusive apartments and penthouses with spectacular sea views in Tenerife. Modern architecture, roof terraces and top-class amenities. From € 1,005,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive apartments with sea views in Tenerife",
    "OG_DESCRIPTION": "Iconic Tenerife: luxury apartments and sky penthouses with panoramic sea views, modern architecture and first-class amenities in the Canary Islands. From € 1,005,000.",
    "HERO_BG_ALT": "Iconic Tenerife aerial exterior with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Tenerife",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/iconic-tenerife/hero.webp",
    "LAT": 28.134004,
    "LNG": -16.784921,
    "HREF": "/iconic-tenerife/",
}
