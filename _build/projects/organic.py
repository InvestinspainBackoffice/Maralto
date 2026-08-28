from urllib.parse import quote

PROJECT_NAME = "Organic"
PRICE_FROM = "Vanaf € 747.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "organic",
    "TITLE": f"{PROJECT_NAME} El Higuerón Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Organic: exclusief boutiqueproject met 25 woningen in El Higuerón, Fuengirola. 3-4 slaapkamers, privézwembad per woning en panoramisch zeezicht. Costa del Sol. Vanaf € 747.000.",
    "OG_TITLE": f"{PROJECT_NAME} · El Higuerón Fuengirola",
    "OG_DESCRIPTION": "Slechts 25 exclusieve woningen met 3-4 slaapkamers en privézwembad in El Higuerón, Fuengirola. Architectuur in harmonie met de natuur, panoramisch zeezicht.",
    "OG_IMAGE": "https://projects.investinspain.be/images/organic/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/organic/hero.webp",
    "HERO_BG_ALT": "Organic El Higuerón Fuengirola woningen met zeezicht en privézwembad",
    "HERO_NAME": "Organic",
    "HERO_LOCATION": "EL HIGUERÓN, FUENGIROLA",
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
    "META_DESCRIPTION": "Organic: exclusive boutique project with 25 homes in El Higuerón, Fuengirola. 3-4 bedrooms, private pool per home and panoramic sea views. Costa del Sol. From € 747,000.",
    "OG_TITLE": f"{PROJECT_NAME} · El Higuerón Fuengirola",
    "OG_DESCRIPTION": "Just 25 exclusive homes with 3-4 bedrooms and private pools in El Higuerón, Fuengirola. Architecture in harmony with nature, panoramic sea views.",
    "HERO_BG_ALT": "Organic El Higuerón Fuengirola homes with sea views and private pool",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Higuerón, Fuengirola",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/organic/hero.webp",
    "LAT": 36.577985,
    "LNG": -4.602902,
    "HREF": "/organic/",
}
