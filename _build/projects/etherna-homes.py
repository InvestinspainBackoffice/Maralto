from urllib.parse import quote

PROJECT_NAME = "Etherna Homes"
PRICE_FROM = "Vanaf € 302.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "etherna-homes",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Etherna Homes: 135 woningen met 1, 2 of 3 slaapkamers naast Valle Romano Golf Club in Estepona. Zwembad met solarium en fitnessruimte. Vanaf €302.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Etherna Homes: eigentijds wonen naast Valle Romano Golf Club, met gelijkvloerse woningen met tuin en penthouses met solarium. Vanaf €302.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2024/05/003A_250416_Etherna-Homes_info-1_piscina-scaled-1.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2024/05/003A_250416_Etherna-Homes_info-1_piscina-scaled-1.jpg",
    "HERO_BG_ALT": "Etherna Homes — wooncomplex met zwembad naast de golfbaan",
    "HERO_NAME": "ETHERNA HOMES",
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
    "META_DESCRIPTION": "Etherna Homes: 135 homes with 1, 2 or 3 bedrooms next to Valle Romano Golf Club in Estepona. Swimming pool with solarium and fitness room. From €302,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Etherna Homes: contemporary living next to Valle Romano Golf Club, with ground-floor homes with garden and penthouses with solarium. From €302,000.",
    "HERO_BG_ALT": "Etherna Homes — residential complex with swimming pool next to the golf course",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/etherna-homes/thumb.webp",
    "LAT": 36.428940219532,
    "LNG": -5.200425298379,
    "HREF": "/etherna-homes/",
}
