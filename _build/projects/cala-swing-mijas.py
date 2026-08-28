from urllib.parse import quote

PROJECT_NAME = "Cala Swing Mijas"
PRICE_FROM = "Vanaf € 303.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "cala-swing-mijas",
    "TITLE": f"{PROJECT_NAME} La Cala de Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Cala Swing Mijas: 155 moderne appartementen naast Calanova Golf en dichtbij het strand. Zwembad, gym, social club en ruime terrassen. Vanaf €303.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Golf, Strand & Modern Wonen in Mijas",
    "OG_DESCRIPTION": "Ontdek Cala Swing Mijas: 155 appartementen met 1, 2 en 3 slaapkamers naast de Calanova Golf Club in La Cala de Mijas. Zwembad, gym, social club en geweldige terrassen. Vanaf €303.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/cala-swing-mijas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/cala-swing-mijas/hero.webp",
    "HERO_BG_ALT": "Cala Swing Mijas — modern appartementencomplex naast golf en zee",
    "HERO_NAME": "CALA SWING MIJAS",
    "HERO_LOCATION": "LA CALA DE MIJAS",
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
    "META_DESCRIPTION": "Cala Swing Mijas: 155 modern apartments next to Calanova Golf and close to the beach. Pool, gym, social club and spacious terraces. From €303,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Golf, Beach & Modern Living in Mijas",
    "OG_DESCRIPTION": "Discover Cala Swing Mijas: 155 apartments with 1, 2 and 3 bedrooms next to Calanova Golf Club in La Cala de Mijas. Pool, gym, social club and great terraces. From €303,000.",
    "HERO_BG_ALT": "Cala Swing Mijas — modern apartment complex next to golf and sea",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Cala de Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/cala-swing-mijas/hero.webp",
    "LAT": 36.509395,
    "LNG": -4.698286,
    "HREF": "/cala-swing-mijas/",
}
