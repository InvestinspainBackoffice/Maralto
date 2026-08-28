from urllib.parse import quote

PROJECT_NAME = "Australy Thera"
PRICE_FROM = "Binnenkort beschikbaar"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "australy-thera",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Australy Thera: appartementen en duplexwoningen met 2, 3 of 4 slaapkamers naast Selwo Park in Estepona. Social club, gym en zwembaden. Binnenkort beschikbaar.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Duplexwoningen",
    "OG_DESCRIPTION": "Ontdek Australy Thera: modern wonen met zeezicht naast Selwo Park, enkele minuten van het strand van Estepona. Binnenkort beschikbaar.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/12/Thera-Australy_FaseII-Cam-02-Piscina-Vista-Al-mar-V2.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/12/Thera-Australy_FaseII-Cam-03-Edificio-Frontal.jpg",
    "HERO_BG_ALT": "Australy Thera — gevel van het wooncomplex tussen het groen",
    "HERO_NAME": "AUSTRALY THERA",
    "HERO_LOCATION": "ESTEPONA",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "PRICE_LABEL": "Binnenkort",
    "PRICE_AMOUNT": "beschikbaar",
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
    "META_DESCRIPTION": "Australy Thera: apartments and duplex homes with 2, 3 or 4 bedrooms next to Selwo Park in Estepona. Social club, gym and swimming pools. Coming soon.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Duplex Homes",
    "OG_DESCRIPTION": "Discover Australy Thera: modern living with sea views next to Selwo Park, just minutes from Estepona's beach. Coming soon.",
    "HERO_BG_ALT": "Australy Thera — facade of the residential complex amid greenery",
    "PRICE_FROM": "Coming soon",
    "HERO_PRICE": "Coming soon",
    "PRICE_LABEL": "Coming",
    "PRICE_AMOUNT": "soon",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/australy-thera/thumb.webp",
    "LAT": 36.463867,
    "LNG": -5.087378,
    "HREF": "/australy-thera/",
}
