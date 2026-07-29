from urllib.parse import quote

PROJECT_NAME = "Ikkil Bay"
PRICE_FROM = "Vanaf € 3.003.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "ikkil-bay",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Ikkil Bay: 9 villa-appartementen en 1 duplex penthouse, frontline beach aan Playa del Cristo in Estepona. Verwarmd binnenzwembad, sauna en directe strandtoegang. Vanaf €3.003.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa-appartementen & Penthouse",
    "OG_DESCRIPTION": "Ontdek Ikkil Bay: frontline beach wonen met privézwembad, adembenemend zeezicht en directe toegang tot het strand in Estepona. Vanaf €3.003.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2020/07/Ikkil-Bay-Showflat3.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2020/07/Ikkil-Bay-Showflat3.jpg",
    "HERO_BG_ALT": "Ikkil Bay — terras met loungebank en panoramisch zeezicht",
    "HERO_NAME": "IKKIL BAY",
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
    "META_DESCRIPTION": "Ikkil Bay: 9 villa-apartments and 1 duplex penthouse, frontline beach on Playa del Cristo in Estepona. Heated indoor pool, sauna and direct beach access. From €3,003,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa-apartments & Penthouse",
    "OG_DESCRIPTION": "Discover Ikkil Bay: frontline beach living with a private pool, breathtaking sea views and direct beach access in Estepona. From €3,003,000.",
    "HERO_BG_ALT": "Ikkil Bay — terrace with lounge seating and panoramic sea view",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2020/07/Ikkil-Bay-Showflat3.jpg",
    "LAT": 36.417125823855,
    "LNG": -5.1652550752558,
    "HREF": "/ikkil-bay/",
}
