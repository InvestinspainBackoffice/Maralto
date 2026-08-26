from urllib.parse import quote

PROJECT_NAME = "EVOQUE"
PRICE_FROM = "Vanaf € 490.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "evoque",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "EVOQUE: meer dan 200 moderne appartementen en penthouses met panoramisch uitzicht in de Higuerón-regio, Fuengirola. Vanaf € 490.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Higuerón, Fuengirola",
    "OG_DESCRIPTION": "EVOQUE: wellnesscentrum met sauna en hammam, gourmet lounge en ondergrondse parking met laadpunten in Fuengirola. Vanaf € 490.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/evoque/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/evoque/hero.webp",
    "HERO_BG_ALT": "EVOQUE — moderne appartementen in Higuerón, Fuengirola",
    "HERO_NAME": "EVOQUE",
    "HERO_LOCATION": "HIGUERÓN, FUENGIROLA",
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
    "META_DESCRIPTION": "EVOQUE: more than 200 modern apartments and penthouses with panoramic views in the Higuerón area, Fuengirola. From € 490,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Higuerón, Fuengirola",
    "OG_DESCRIPTION": "EVOQUE: wellness centre with sauna and hammam, gourmet lounge and underground parking with charging points in Fuengirola. From € 490,000.",
    "HERO_BG_ALT": "EVOQUE — modern apartments in Higuerón, Fuengirola",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Higuerón, Fuengirola",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/evoque/hero.webp",
    "LAT": 36.593,
    "LNG": -4.618,
    "HREF": "/evoque/",
}
