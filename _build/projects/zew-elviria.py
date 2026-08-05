from urllib.parse import quote

PROJECT_NAME = "ZEW Elviria"
PRICE_FROM = "Vanaf € 770.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "zew-elviria",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "ZEW Elviria: duplexappartementen omringd door natuur in Elviria Hill, Oost-Marbella. Vanaf €770.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Duplexappartementen",
    "OG_DESCRIPTION": "Ontdek ZEW Elviria: 88 duplexappartementen in de dennenbossen van Elviria Hill, met 4 zwembaden, co-working space en gym. Vanaf €770.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/07/Concept_Homes_acceso_hd.0000-scaled-1.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/07/Concept_Homes_acceso_hd.0000-scaled-1.jpg",
    "HERO_BG_ALT": "ZEW Elviria — entree met natuurstenen accenten en weelderige tuin",
    "HERO_NAME": "ZEW ELVIRIA",
    "HERO_LOCATION": "ELVIRIA",
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
    "META_DESCRIPTION": "ZEW Elviria: duplex apartments surrounded by nature in Elviria Hill, East Marbella. From €770.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Duplex Apartments",
    "OG_DESCRIPTION": "Discover ZEW Elviria: 88 duplex apartments in the pine forests of Elviria Hill, with 4 swimming pools, coworking space and gym. From €770.000.",
    "HERO_BG_ALT": "ZEW Elviria — entrance with natural stone accents and lush garden",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Elviria",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/zew-elviria/thumb.webp",
    "LAT": 36.5075665,
    "LNG": -4.787271,
    "HREF": "/zew-elviria/",
}
