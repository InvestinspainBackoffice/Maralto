from urllib.parse import quote

PROJECT_NAME = "Spinto Blu"
PRICE_FROM = "Vanaf € 1.200.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "spinto-blu",
    "TITLE": f"{PROJECT_NAME} CASARES — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Spinto Blu Casares: 55 luxe townhouses met 3 slaapkamers, golf- en zeezicht nabij Finca Cortesín. Exclusief nieuwbouwproject vanaf € 1.200.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve townhouses met zeezicht in Casares",
    "OG_DESCRIPTION": "55 luxe townhouses met golf- en zeezicht in Casares del Sol, op wandelafstand van Azata Golf en Finca Cortesín.",
    "OG_IMAGE": "https://projects.investinspain.be/images/spinto-blu/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/spinto-blu/hero.webp",
    "HERO_BG_ALT": "Spinto Blu — overzicht van het townhouse-complex met golf- en zeezicht in Casares",
    "HERO_NAME": "Spinto Blu",
    "HERO_LOCATION": "CASARES",
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
    "META_DESCRIPTION": "Spinto Blu Casares: 55 luxury townhouses with 3 bedrooms, golf and sea views near Finca Cortesín. Exclusive new development from € 1,200,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive townhouses with sea views in Casares",
    "OG_DESCRIPTION": "55 luxury townhouses with golf and sea views in Casares del Sol, within walking distance of Azata Golf and Finca Cortesín.",
    "HERO_BG_ALT": "Spinto Blu — overview of the townhouse complex with golf and sea views in Casares",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Casares",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/spinto-blu/hero.webp",
    "LAT": 36.387519,
    "LNG": -5.217742,
    "HREF": "/spinto-blu/",
}
