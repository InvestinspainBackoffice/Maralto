from urllib.parse import quote

PROJECT_NAME = "Las Villas Sotogrande"
PRICE_FROM = "Vanaf € 954.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "las-villas-sotogrande",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Las Villas Sotogrande: 49 luxe villa's met 3 en 4 slaapkamers naast de golfbaan van La Cañada in Sotogrande Alto. Vanaf €954.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Villa's aan de Golf",
    "OG_DESCRIPTION": "Ontdek Las Villas Sotogrande: patio-woningen, geschakelde woningen en vrijstaande villa's met privétuin en eigen zwembad, opgevat als 'tuin met woningen'. Vanaf €954.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/las-villas-sotogrande/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/las-villas-sotogrande/hero.webp",
    "HERO_BG_ALT": "Las Villas Sotogrande — villa met zwembad in weelderige tuin",
    "HERO_NAME": "LAS VILLAS SOTOGRANDE",
    "HERO_LOCATION": "SOTOGRANDE",
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
    "META_DESCRIPTION": "Las Villas Sotogrande: 49 luxury villas with 3 and 4 bedrooms next to the La Cañada golf course in Sotogrande Alto. From €954,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Villas on the Golf Course",
    "OG_DESCRIPTION": "Discover Las Villas Sotogrande: patio homes, semi-detached homes and detached villas with a private garden and pool, conceived as a 'garden with homes'. From €954,000.",
    "HERO_BG_ALT": "Las Villas Sotogrande — villa with pool in a lush garden",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Sotogrande",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/las-villas-sotogrande/hero.webp",
    "LAT": 36.291884,
    "LNG": -5.31292,
    "HREF": "/las-villas-sotogrande/",
}
