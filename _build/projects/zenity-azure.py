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
    "AGENT_NAME": "Sofie Claes",
    "AGENT_PHOTO": "https://investinspain.be/wp-content/uploads/2020/01/Sofie-Claes.jpg",
    "AGENT_PHONE_TEL": "+32477482662",
    "AGENT_PHONE_DISPLAY": "+32 477 48 26 62",
    "AGENT_EMAIL": "sofie@investinspain.be",
    "WA_NUMBER": "32477482662",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2022/09/INVESTINSPAIN-Azure_Cam02-1-scaled.jpg",
    "LAT": 36.4139368,
    "LNG": -5.1836025,
    "HREF": "/zenity-azure/",
}
