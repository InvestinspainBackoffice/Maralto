from urllib.parse import quote

PROJECT_NAME = "La Algaba"
PRICE_FROM = "Vanaf € 1.510.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "la-algaba",
    "TITLE": f"{PROJECT_NAME} Casares — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "La Algaba: luxe appartementen en penthouses in Casares met domotica, Siemens apparatuur en ruime terrassen. Privacy en natuur centraal. Vanaf €1.510.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe & Natuur in Casares",
    "OG_DESCRIPTION": "Ontdek La Algaba: exclusieve residentie in Casares met premium afwerking, domotica, thermische isolatie en weelderige buitenruimtes. Rust, privacy en verbinding met de natuur. Vanaf €1.510.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/la-algaba/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/la-algaba/hero.webp",
    "HERO_BG_ALT": "La Algaba — luxe zwembad met terras in Casares",
    "HERO_NAME": "LA ALGABA",
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
    "META_DESCRIPTION": "La Algaba: luxury apartments and penthouses in Casares with home automation, Siemens appliances and spacious terraces. Privacy and nature at the centre. From €1,510,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury & Nature in Casares",
    "OG_DESCRIPTION": "Discover La Algaba: exclusive residence in Casares with premium finishes, home automation, thermal insulation and generous outdoor spaces. Tranquility, privacy and connection with nature. From €1,510,000.",
    "HERO_BG_ALT": "La Algaba — luxury pool with terrace in Casares",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Casares",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/la-algaba/hero.webp",
    "LAT": 36.397359,
    "LNG": -5.225527,
    "HREF": "/la-algaba/",
}
