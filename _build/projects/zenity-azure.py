from urllib.parse import quote

PROJECT_NAME = "Zenity Azure"
PRICE_FROM = "Vanaf € 550.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "zenity-azure",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Zenity Azure: appartementen en townhouses met 2-4 slaapkamers vlakbij het strand in Estepona. Vanaf €550.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Townhouses",
    "OG_DESCRIPTION": "Ontdek Zenity Azure: onovertroffen zeezicht, terrassen tot 80m², zwembaden en een social club in Estepona. Vanaf €550.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2022/09/INVESTINSPAIN-Azure_Cam02-1-scaled.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2022/09/INVESTINSPAIN-Azure_Cam02-1-scaled.jpg",
    "HERO_BG_ALT": "Zenity Azure — wooncomplex met zwembad en panoramisch zeezicht",
    "HERO_NAME": "ZENITY AZURE",
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
    "META_DESCRIPTION": "Zenity Azure: apartments and townhouses with 2-4 bedrooms close to the beach in Estepona. From €550.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Townhouses",
    "OG_DESCRIPTION": "Discover Zenity Azure: unrivalled sea views, terraces up to 80m², swimming pools and a social club in Estepona. From €550.000.",
    "HERO_BG_ALT": "Zenity Azure — residential complex with swimming pool and panoramic sea view",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/zenity-azure/thumb.webp",
    "LAT": 36.4139368,
    "LNG": -5.1836025,
    "HREF": "/zenity-azure/",
}
