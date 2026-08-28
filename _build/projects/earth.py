from urllib.parse import quote

PROJECT_NAME = "Earth"
PRICE_FROM = "Vanaf € 5.095.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "earth",
    "TITLE": f"{PROJECT_NAME} Golden Mile Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Earth: ultra-luxe appartementen met tuin, semi-penthouses en penthouses aan de Golden Mile in Marbella. Spa, indoor zwembad, gym en yoga room in groene setting. Vanaf € 5.095.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-luxe penthouses en appartementen aan de Golden Mile, Marbella",
    "OG_DESCRIPTION": "Earth aan de Golden Mile in Marbella: appartementen met privétuin, semi-penthouses en penthouses omgeven door prachtige tuinen, spa, verwarm zwembad, gym en yoga room. Vanaf € 5.095.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/earth/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/earth/hero.webp",
    "HERO_BG_ALT": "Earth Golden Mile Marbella exterieur luxe appartementen en penthouses",
    "HERO_NAME": "Earth",
    "HERO_LOCATION": "GOLDEN MILE, MARBELLA",
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
    "META_DESCRIPTION": "Earth: ultra-luxury garden apartments, semi-penthouses and penthouses on the Golden Mile in Marbella. Spa, indoor pool, gym and yoga room in a lush green setting. From € 5,095,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-luxury penthouses and apartments on the Golden Mile, Marbella",
    "OG_DESCRIPTION": "Earth on the Golden Mile in Marbella: garden apartments, semi-penthouses and penthouses surrounded by beautiful gardens, spa, heated pool, gym and yoga room. From € 5,095,000.",
    "HERO_BG_ALT": "Earth Golden Mile Marbella exterior luxury apartments and penthouses",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Golden Mile, Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/earth/hero.webp",
    "LAT": 36.507855,
    "LNG": -4.928872,
    "HREF": "/earth/",
}
