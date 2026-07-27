from urllib.parse import quote

PROJECT_NAME = "Romero"
PRICE_FROM = "Vanaf € 1.150.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "romero",
    "TITLE": f"{PROJECT_NAME} Real de la Quinta — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Romero: exclusieve luxe appartementen met zeezicht in Real de la Quinta, Marbella. Vanaf €1.150.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Romero: 28 designwoningen met zoutwater infinity pool, gym en coworkingruimte in Real de la Quinta. Vanaf €1.150.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/05/Romero-Real-de-la-Quinta_012.Aerial-View.render-1110x623.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/05/Romero-Real-de-la-Quinta_012.Aerial-View.render-1110x623.jpg",
    "HERO_BG_ALT": "Romero — luchtfoto van het exclusieve complex in de heuvels met zeezicht",
    "HERO_NAME": "ROMERO",
    "HERO_LOCATION": "REAL DE LA QUINTA",
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
    "LOCATION": "Real de la Quinta",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2025/05/Romero-Real-de-la-Quinta_012.Aerial-View.render-1110x623.jpg",
    "LAT": 36.5353281,
    "LNG": -4.9791269,
    "HREF": "/romero/",
}
