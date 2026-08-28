from urllib.parse import quote

PROJECT_NAME = "Soul Marbella"
PRICE_FROM = "Vanaf € 1.500.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "soul-marbella-1",
    "TITLE": f"{PROJECT_NAME} OOST-MARBELLA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Soul Marbella: top appartementen, penthouses en villa's met 3 slaapkamers in Oost-Marbella. Bouwjaar 2022, premium afwerking. Vanaf € 1.500.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen, penthouses en villa's in Oost-Marbella",
    "OG_DESCRIPTION": "Soul Marbella biedt top appartementen, penthouses en villa's met 3 slaapkamers en premium afwerking in Oost-Marbella.",
    "OG_IMAGE": "https://projects.investinspain.be/images/soul-marbella-1/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/soul-marbella-1/hero.webp",
    "HERO_BG_ALT": "Soul Marbella — exclusieve residenties in Oost-Marbella",
    "HERO_NAME": "Soul Marbella",
    "HERO_LOCATION": "OOST-MARBELLA",
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
    "META_DESCRIPTION": "Soul Marbella: top apartments, penthouses and villas with 3 bedrooms in East Marbella. Built 2022, premium finishes. From € 1,500,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments, penthouses and villas in East Marbella",
    "OG_DESCRIPTION": "Soul Marbella offers top apartments, penthouses and villas with 3 bedrooms and premium finishes in East Marbella.",
    "HERO_BG_ALT": "Soul Marbella — exclusive residences in East Marbella",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella Oost",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/soul-marbella-1/hero.webp",
    "LAT": 36.507513,
    "LNG": -4.829909,
    "HREF": "/soul-marbella-1/",
}
