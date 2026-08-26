from urllib.parse import quote

PROJECT_NAME = "Vangård"
PRICE_FROM = "Vanaf € 565.250"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vangard",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vangård: moderne luxe appartementen en penthouses met 2, 3 en 4 slaapkamers op een toplocatie in Fuengirola. Vanaf €565.250.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne Luxe Appartementen in Fuengirola",
    "OG_DESCRIPTION": "Ontdek Vangård: appartementen en penthouses met indrukwekkend zeezicht, meerdere zwembaden, wellnesszones en coworkingruimtes in Fuengirola. Vanaf €565.250.",
    "OG_IMAGE": "https://projects.investinspain.be/images/vangard/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/vangard/hero.webp",
    "HERO_BG_ALT": "Vangård — gevelaanzicht van het gebouw in Fuengirola",
    "HERO_NAME": "VANGÅRD",
    "HERO_LOCATION": "FUENGIROLA",
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
    "META_DESCRIPTION": "Vangård: modern luxury apartments and penthouses with 2, 3 and 4 bedrooms in a prime location in Fuengirola. From €565,250.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern Luxury Apartments in Fuengirola",
    "OG_DESCRIPTION": "Discover Vangård: apartments and penthouses with impressive sea views, multiple pools, wellness zones and coworking spaces in Fuengirola. From €565,250.",
    "HERO_BG_ALT": "Vangård — facade view of the building in Fuengirola",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Fuengirola",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/vangard/hero.webp",
    "LAT": 36.570048,
    "LNG": -4.609375,
    "HREF": "/vangard/",
}
