from urllib.parse import quote

PROJECT_NAME = "Alexandra's Dream"
PRICE_FROM = "Vanaf € 950.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "alexandras-dream",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Alexandra's Dream: luxueuze appartementen met privézwembad, jacuzzi en bioscoop in Mijas. Hoge afwerking, zeezicht en spectaculaire gemeenschappelijke faciliteiten. Vanaf €950.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Appartementen in Mijas",
    "OG_DESCRIPTION": "Ontdek Alexandra's Dream: uitzonderlijk luxueuze appartementen in Mijas met jacuzzi, bioscoop, sauna en privézwembad. Zeezicht en topafwerking inbegrepen. Vanaf €950.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/alexandras-dream/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/alexandras-dream/hero.webp",
    "HERO_BG_ALT": "Alexandra's Dream — luxueus appartementencomplex in Mijas",
    "HERO_NAME": "ALEXANDRA'S DREAM",
    "HERO_LOCATION": "MIJAS",
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
    "META_DESCRIPTION": "Alexandra's Dream: luxury apartments with private pool, jacuzzi and cinema room in Mijas. High-end finishes, sea views and spectacular communal facilities. From €950,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Apartments in Mijas",
    "OG_DESCRIPTION": "Discover Alexandra's Dream: exceptionally luxurious apartments in Mijas with jacuzzi, cinema, sauna and private pool. Sea views and premium finishes included. From €950,000.",
    "HERO_BG_ALT": "Alexandra's Dream — luxury apartment complex in Mijas",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/alexandras-dream/hero.webp",
    "LAT": 36.512536,
    "LNG": -4.654089,
    "HREF": "/alexandras-dream/",
}
