from urllib.parse import quote

PROJECT_NAME = "Higueron Bay Residences"
PRICE_FROM = "Vanaf € 570.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "higueron-bay-residences",
    "TITLE": f"{PROJECT_NAME} Benalmádena — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Higueron Bay Residences: 60 luxe appartementen met 2-3 slaapkamers in El Higuerón, Benalmádena. Verwarmd zwembad, jacuzzi's, coworking en 500m van het strand. Vanaf € 570.000.",
    "OG_TITLE": f"{PROJECT_NAME} — 60 luxe appartementen in El Higuerón, Benalmádena",
    "OG_DESCRIPTION": "Higueron Bay Residences in Benalmádena: 60 appartementen met 2 of 3 slaapkamers in de meest gewilde wijk El Higuerón. Verwarmd zwembad, jacuzzi's, coworkingruimte en op 500m van de strandpromenade en 300m van treinstation Carvajal. Vanaf € 570.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/higueron-bay-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/higueron-bay-residences/hero.webp",
    "HERO_BG_ALT": "Higueron Bay Residences Benalmádena exterieur appartementen El Higuerón",
    "HERO_NAME": "Higueron Bay Residences",
    "HERO_LOCATION": "EL HIGUERÓN, BENALMÁDENA",
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
    "META_DESCRIPTION": "Higueron Bay Residences: 60 luxury apartments with 2-3 bedrooms in El Higuerón, Benalmádena. Heated pool, jacuzzis, coworking and 500m from the beach. From € 570,000.",
    "OG_TITLE": f"{PROJECT_NAME} — 60 luxury apartments in El Higuerón, Benalmádena",
    "OG_DESCRIPTION": "Higueron Bay Residences in Benalmádena: 60 apartments with 2 or 3 bedrooms in the sought-after El Higuerón neighbourhood. Heated pool, jacuzzis, coworking space and 500m from the beach promenade and 300m from Carvajal train station. From € 570,000.",
    "HERO_BG_ALT": "Higueron Bay Residences Benalmádena exterior apartments El Higuerón",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Higuerón, Benalmádena",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/higueron-bay-residences/hero.webp",
    "LAT": 36.593,
    "LNG": -4.618,
    "HREF": "/higueron-bay-residences/",
}
