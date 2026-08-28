from urllib.parse import quote

PROJECT_NAME = "Almazara Views"
PRICE_FROM = "Vanaf € 620.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "almazara-views",
    "TITLE": f"{PROJECT_NAME} Istán — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Almazara Views: 23 exclusieve townhouses met 3 slaapkamers in Istán, met panoramisch berg- en zeezicht naast Sierra Blanca Country Club. Gemeenschappelijk zwembad. Vanaf € 620.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve townhouses met panoramisch zicht in Istán",
    "OG_DESCRIPTION": "Almazara Views in Istán: 23 townhouses met 3 slaapkamers aan de voet van La Concha, omgeven door de Sierra de las Nieves. Panoramisch zee- en bergzicht, gemeenschappelijk zwembad en inheemse tuinen. Vanaf € 620.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/almazara-views/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/almazara-views/hero.webp",
    "HERO_BG_ALT": "Almazara Views Istán townhouses exterieur panoramisch zicht",
    "HERO_NAME": "Almazara Views",
    "HERO_LOCATION": "ISTÁN, MARBELLA",
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
    "META_DESCRIPTION": "Almazara Views: 23 exclusive townhouses with 3 bedrooms in Istán, with panoramic mountain and sea views next to Sierra Blanca Country Club. Communal pool. From € 620,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive townhouses with panoramic views in Istán",
    "OG_DESCRIPTION": "Almazara Views in Istán: 23 townhouses with 3 bedrooms at the foot of La Concha, surrounded by the Sierra de las Nieves. Panoramic sea and mountain views, communal pool and native gardens. From € 620,000.",
    "HERO_BG_ALT": "Almazara Views Istán townhouses exterior panoramic view",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Istán",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/almazara-views/hero.webp",
    "LAT": 36.546707,
    "LNG": -4.947803,
    "HREF": "/almazara-views/",
}
