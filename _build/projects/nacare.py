from urllib.parse import quote

PROJECT_NAME = "Nacaré"
PRICE_FROM = "Vanaf € 2.500.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "nacare",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Nacaré: 20 exclusieve appartementen met 3 of 4 slaapkamers in Estepona, met panoramisch zeezicht en een private Owners Club. Vanaf €2.500.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve Appartementen",
    "OG_DESCRIPTION": "Ontdek Nacaré: architectuur, design en beleving komen samen in dit nieuwbouwproject in Estepona, met een private Owners Club vol wellness en sportvoorzieningen. Vanaf €2.500.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/04/NA-001.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/04/NA-001.jpg",
    "HERO_BG_ALT": "Nacaré — luchtfoto van de kust van Estepona",
    "HERO_NAME": "NACARÉ",
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
    "THUMB": "https://investinspain.be/wp-content/uploads/2026/04/NA-001.jpg",
    "LAT": 36.42980056060396,
    "LNG": -5.134549942285611,
    "HREF": "/nacare/",
}
