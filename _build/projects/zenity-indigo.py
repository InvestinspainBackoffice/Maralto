from urllib.parse import quote

PROJECT_NAME = "Zenity Indigo"
PRICE_FROM = "Vanaf € 607.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "zenity-indigo",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Zenity Indigo: 33 luxe appartementen, penthouses en duplexen met 2-3-4 slaapkamers en terrassen tot 120m² vlakbij het strand in Estepona. Gym, social club en zeezicht. Vanaf € 607.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe appartementen en penthouses met zeezicht in Estepona",
    "OG_DESCRIPTION": "Zenity Indigo in Estepona: 33 ruime woningen met 2, 3 of 4 slaapkamers en terrassen tot 120m². Zeezicht, fitness, gym, social club en ondergrondse parking. Op wandelafstand van het strand. Vanaf € 607.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/zenity-indigo/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/zenity-indigo/hero.webp",
    "HERO_BG_ALT": "Zenity Indigo Estepona exterieur appartementen met zeezicht",
    "HERO_NAME": "Zenity Indigo",
    "HERO_LOCATION": "ESTEPONA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Zenity Indigo: 33 luxury apartments, penthouses and duplexes with 2-3-4 bedrooms and terraces up to 120m² near the beach in Estepona. Gym, social club and sea views. From € 607,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury apartments and penthouses with sea views in Estepona",
    "OG_DESCRIPTION": "Zenity Indigo in Estepona: 33 spacious homes with 2, 3 or 4 bedrooms and terraces up to 120m². Sea views, fitness, gym, social club and underground parking. Walking distance to the beach. From € 607,000.",
    "HERO_BG_ALT": "Zenity Indigo Estepona exterior apartments with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/zenity-indigo/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/zenity-indigo/",
}
