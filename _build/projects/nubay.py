from urllib.parse import quote

PROJECT_NAME = "Nubay"
PRICE_FROM = "Vanaf € 1.050.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "nubay",
    "TITLE": f"{PROJECT_NAME} Manilva — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Nubay: appartementen, penthouses en villa's met 2 tot 4 slaapkamers, frontline aan het strand van Manilva. Overloopzwembad en weelderige tuinen. Vanaf €1.050.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen, Penthouses & Villa's",
    "OG_DESCRIPTION": "Ontdek Nubay: het nieuwe toevluchtsoord aan de Costa del Sol, met panoramisch zeezicht, overloopzwembad en villa's naast een beschermd natuurgebied in Manilva. Vanaf €1.050.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/07/14.-NUBAY-Costa-del-Sol-Manilva-NVOGA-Developments-Villa-scaled.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/07/14.-NUBAY-Costa-del-Sol-Manilva-NVOGA-Developments-Villa-scaled.jpg",
    "HERO_BG_ALT": "Nubay — luchtfoto van het complex met zwembad en tuin bij avondlicht",
    "HERO_NAME": "NUBAY",
    "HERO_LOCATION": "MANILVA",
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

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Manilva",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2026/07/14.-NUBAY-Costa-del-Sol-Manilva-NVOGA-Developments-Villa-scaled.jpg",
    "LAT": 36.368092531788,
    "LNG": -5.22610050921,
    "HREF": "/nubay/",
}
