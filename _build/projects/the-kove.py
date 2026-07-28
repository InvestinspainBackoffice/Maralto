from urllib.parse import quote

PROJECT_NAME = "The Kove"
PRICE_FROM = "Vanaf € 410.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-kove",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Kove: appartementen met 2-3 slaapkamers en adembenemende zeezichten in Mijas. Vanaf €410.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met zeezicht",
    "OG_DESCRIPTION": "Ontdek The Kove: ontworpen door architect Manuel Clave, met zwembaden, spa, gym en co-working ruimte in Mijas. Vanaf €410.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/06/1748445724_thekoveokkkllll.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/06/1748445724_thekoveokkkllll.jpg",
    "HERO_BG_ALT": "The Kove — zwembad omgeven door het wooncomplex",
    "HERO_NAME": "THE KOVE",
    "HERO_LOCATION": "MIJAS",
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

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2025/06/1748445724_thekoveokkkllll.jpg",
    "LAT": 36.5208373,
    "LNG": -4.6509914,
    "HREF": "/the-kove/",
}
