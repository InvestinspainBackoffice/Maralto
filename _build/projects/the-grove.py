from urllib.parse import quote

PROJECT_NAME = "The Grove"
PRICE_FROM = "Vanaf € 390.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-grove",
    "TITLE": f"{PROJECT_NAME} San Pedro — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Grove: appartementen met 1-4 slaapkamers in San Pedro de Alcántara, met skypool en spa. Vanaf €390.000.",
    "OG_TITLE": f"{PROJECT_NAME} San Pedro — Appartementen",
    "OG_DESCRIPTION": "Ontdek The Grove: rooftop lounge met skypool, verwarmd binnenzwembad, gym en spa in San Pedro de Alcántara. Vanaf €390.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/01/06-The-Grove-1110x623.png",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/01/06-The-Grove-1110x623.png",
    "HERO_BG_ALT": "The Grove — appartementencomplex met zwembad en weelderige tuinen",
    "HERO_NAME": "THE GROVE",
    "HERO_LOCATION": "SAN PEDRO",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "WA_TEXT_ENCODED": quote(WA_MESSAGE),
    "PROJECT_NAME": PROJECT_NAME,
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "San Pedro de Alcántara",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2026/01/06-The-Grove-1110x623.png",
    "LAT": 36.4873997,
    "LNG": -4.9843947,
    "HREF": "/the-grove/",
}
