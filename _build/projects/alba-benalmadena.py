from urllib.parse import quote

PROJECT_NAME = "Alba Benalmádena"
PRICE_FROM = "Vanaf € 678.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "alba-benalmadena",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Alba Benalmádena: appartementen en townhouses met adembenemend panoramisch zeezicht in Torremuelle, Benalmádena. Infinity-zwembad, gym en groenomgeving. Vanaf € 678.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen en townhouses met panoramisch zeezicht in Benalmádena",
    "OG_DESCRIPTION": "Alba Benalmádena in Torremuelle: moderne appartementen en townhouses met spectaculair zeezicht, infinity-zwembad, gym en aangelegde tuinen. Vanaf € 678.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/alba-benalmadena/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/alba-benalmadena/hero.webp",
    "HERO_BG_ALT": "Alba Benalmádena exterieur met panoramisch zeezicht",
    "HERO_NAME": "Alba Benalmádena",
    "HERO_LOCATION": "BENALMÁDENA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Alba Benalmádena: apartments and townhouses with breathtaking panoramic sea views in Torremuelle, Benalmádena. Infinity pool, gym and green surroundings. From € 678,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments and townhouses with panoramic sea views in Benalmádena",
    "OG_DESCRIPTION": "Alba Benalmádena in Torremuelle: modern apartments and townhouses with spectacular sea views, infinity pool, gym and landscaped gardens. From € 678,000.",
    "HERO_BG_ALT": "Alba Benalmádena exterior with panoramic sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benalmádena",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/alba-benalmadena/hero.webp",
    "LAT": 36.585403,
    "LNG": -4.562159,
    "HREF": "/alba-benalmadena/",
}
