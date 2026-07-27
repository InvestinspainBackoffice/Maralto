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
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2024/06/Marine-Hills-INVESTINSPAIN.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2024/06/Marine-Hills-INVESTINSPAIN.jpg",
    "HERO_BG_ALT": "Marine Hills — moderne architectuur omgeven door groen op de New Golden Mile",
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

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2024/06/Marine-Hills-INVESTINSPAIN.jpg",
    "LAT": 36.4603322,
    "LNG": -5.0854119,
    "HREF": "/marine-hills/",
}
