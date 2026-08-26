from urllib.parse import quote

PROJECT_NAME = "Macan Beach Residences"
PRICE_FROM = "Vanaf € 1.040.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "macan-beach-residences",
    "TITLE": f"{PROJECT_NAME} TORRE DEL MAR — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Macan Beach Residences Torre del Mar: strandappartementen en penthouses met directe toegang tot het strand, spectaculaire zeezichten en premium afwerking. Vanaf € 1.040.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Strandresidenties met zeezicht in Torre del Mar",
    "OG_DESCRIPTION": "Macan Beach Residences biedt uitzonderlijke strandappartementen en penthouses aan de Middellandse Zee, met directe strandtoegang en panoramische zeezichten.",
    "OG_IMAGE": "https://projects.investinspain.be/images/macan-beach-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/macan-beach-residences/hero.webp",
    "HERO_BG_ALT": "Macan Beach Residences — strandappartementen met spectaculair zeezicht",
    "HERO_NAME": "Macan Beach Residences",
    "HERO_LOCATION": "TORRE DEL MAR",
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
    "META_DESCRIPTION": "Macan Beach Residences Torre del Mar: beachfront apartments and penthouses with direct beach access, spectacular sea views and premium finishes. From € 1,040,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Beachfront residences with sea views in Torre del Mar",
    "OG_DESCRIPTION": "Macan Beach Residences offers exceptional beachfront apartments and penthouses on the Mediterranean, with direct beach access and panoramic sea views.",
    "HERO_BG_ALT": "Macan Beach Residences — beachfront apartments with spectacular sea views",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Torre del Mar",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/macan-beach-residences/hero.webp",
    "LAT": 36.7434,
    "LNG": -4.0947,
    "HREF": "/macan-beach-residences/",
}
