from urllib.parse import quote

PROJECT_NAME = "Vanian Gardens"
PRICE_FROM = "Vanaf € 432.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vanian-gardens",
    "TITLE": f"{PROJECT_NAME} ESTEPONA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vanian Gardens: 281 moderne appartementen en penthouses te midden van prachtig aangelegde tuinen en aan Resina Golf, tussen Estepona en Marbella. Vanaf € 432.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen tussen Estepona en Marbella",
    "OG_DESCRIPTION": "Vanian Gardens biedt 281 moderne appartementen en penthouses in weelderige tuinen aan Resina Golf, tussen Estepona en Marbella.",
    "OG_IMAGE": "https://projects.investinspain.be/images/vanian-gardens/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/vanian-gardens/hero.webp",
    "HERO_BG_ALT": "Vanian Gardens — appartementencomplex met tuinen tussen Estepona en Marbella",
    "HERO_NAME": "Vanian Gardens",
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
    "META_DESCRIPTION": "Vanian Gardens: 281 modern apartments and penthouses amid beautifully landscaped gardens on Resina Golf, between Estepona and Marbella. From € 432,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments between Estepona and Marbella",
    "OG_DESCRIPTION": "Vanian Gardens offers 281 modern apartments and penthouses in lush gardens on Resina Golf, between Estepona and Marbella.",
    "HERO_BG_ALT": "Vanian Gardens — apartment complex with gardens between Estepona and Marbella",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/vanian-gardens/hero.webp",
    "LAT": 36.439006,
    "LNG": -5.126186,
    "HREF": "/vanian-gardens/",
}
