from urllib.parse import quote

PROJECT_NAME = "Siam Blue"
PRICE_FROM = "Vanaf € 3.650.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "siam-blue",
    "TITLE": f"{PROJECT_NAME} Tenerife — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Siam Blue: 10 exclusieve moderne villa's met infinity-zwembad en spectaculair zeezicht in Costa Adeje, Tenerife. Tegenover Siam Park, 3-4 slaapkamers op 3 niveaus. Vanaf € 3.650.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe villa's met zeezicht in Costa Adeje, Tenerife",
    "OG_DESCRIPTION": "Siam Blue in Costa Adeje, Tenerife: 10 moderne luxevilla's met infinity-zwembad, panoramisch zeezicht en premium afwerking. Gelegen tegenover Siam Park. Vanaf € 3.650.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/siam-blue/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/siam-blue/hero.webp",
    "HERO_BG_ALT": "Siam Blue Tenerife exterieur moderne villa met zeezicht",
    "HERO_NAME": "Siam Blue",
    "HERO_LOCATION": "COSTA ADEJE, TENERIFE",
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
    "META_DESCRIPTION": "Siam Blue: 10 exclusive modern villas with infinity pool and spectacular sea views in Costa Adeje, Tenerife. Opposite Siam Park, 3-4 bedrooms over 3 levels. From € 3,650,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury villas with sea views in Costa Adeje, Tenerife",
    "OG_DESCRIPTION": "Siam Blue in Costa Adeje, Tenerife: 10 modern luxury villas with infinity pool, panoramic sea views and premium finishes. Located opposite Siam Park. From € 3,650,000.",
    "HERO_BG_ALT": "Siam Blue Tenerife exterior modern villa with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Costa Adeje, Tenerife",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/siam-blue/hero.webp",
    "LAT": 28.073812,
    "LNG": -16.723237,
    "HREF": "/siam-blue/",
}
