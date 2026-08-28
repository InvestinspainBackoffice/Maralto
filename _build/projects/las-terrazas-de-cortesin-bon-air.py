from urllib.parse import quote

PROJECT_NAME = "Bon Air"
PRICE_FROM = "Vanaf € 584.500"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "las-terrazas-de-cortesin-bon-air",
    "TITLE": f"{PROJECT_NAME} CASARES — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Bon Air (Las Terrazas de Cortesín) Casares: exclusieve appartementen met zwembad, gym en co-working ruimte, gelegen in het prestigieuze Finca Cortesín. Vanaf € 584.500.",
    "OG_TITLE": f"{PROJECT_NAME} — Las Terrazas de Cortesín, exclusieve appartementen in Casares",
    "OG_DESCRIPTION": "Bon Air maakt deel uit van Las Terrazas de Cortesín en biedt exclusieve appartementen met zwembad, gym en co-working ruimte in het prestigieuze Casares.",
    "OG_IMAGE": "https://projects.investinspain.be/images/las-terrazas-de-cortesin-bon-air/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/las-terrazas-de-cortesin-bon-air/hero.webp",
    "HERO_BG_ALT": "Bon Air — exclusief appartementencomplex met zwembad in Casares",
    "HERO_NAME": "Bon Air",
    "HERO_LOCATION": "CASARES",
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
    "META_DESCRIPTION": "Bon Air (Las Terrazas de Cortesín) Casares: exclusive apartments with pool, gym and co-working space, located in prestigious Finca Cortesín. From € 584,500.",
    "OG_TITLE": f"{PROJECT_NAME} — Las Terrazas de Cortesín, exclusive apartments in Casares",
    "OG_DESCRIPTION": "Bon Air is part of Las Terrazas de Cortesín and offers exclusive apartments with pool, gym and co-working space in prestigious Casares.",
    "HERO_BG_ALT": "Bon Air — exclusive apartment complex with pool in Casares",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Casares",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/las-terrazas-de-cortesin-bon-air/hero.webp",
    "LAT": 36.40101,
    "LNG": -5.215576,
    "HREF": "/las-terrazas-de-cortesin-bon-air/",
}
