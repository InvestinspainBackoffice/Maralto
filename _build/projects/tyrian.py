from urllib.parse import quote

PROJECT_NAME = "Tyrian"
PRICE_FROM = "Vanaf € 3.550.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "tyrian",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Tyrian: 40 high-end appartementen en penthouses in Estepona, waar architectuur, design en service samenkomen. Wellness, spa en conciërgeservice. Vanaf €3.550.000.",
    "OG_TITLE": f"{PROJECT_NAME} — High-end Appartementen",
    "OG_DESCRIPTION": "Ontdek Tyrian: high-rise villa's met panoramisch zeezicht, 24u beveiliging, spa, sauna en conciërgeservice in Estepona. Vanaf €3.550.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/04/Tyrian26.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/04/Tyrian26.jpg",
    "HERO_BG_ALT": "Tyrian — luchtfoto van de kust van Estepona bij zonsopgang",
    "HERO_NAME": "TYRIAN",
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
    "META_DESCRIPTION": "Tyrian: 40 high-end apartments and penthouses in Estepona, where architecture, design and service come together. Wellness, spa and concierge service. From €3,550,000.",
    "OG_TITLE": f"{PROJECT_NAME} — High-end Apartments",
    "OG_DESCRIPTION": "Discover Tyrian: high-rise villas with panoramic sea views, 24-hour security, spa, sauna and concierge service in Estepona. From €3,550,000.",
    "HERO_BG_ALT": "Tyrian — aerial view of the Estepona coastline at sunrise",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/tyrian/thumb.webp",
    "LAT": 36.428903398234844,
    "LNG": -5.134858087115643,
    "HREF": "/tyrian/",
}
