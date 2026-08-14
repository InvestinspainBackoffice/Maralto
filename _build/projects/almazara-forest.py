from urllib.parse import quote

PROJECT_NAME = "Almazara Forest"
PRICE_FROM = "Vanaf € 580.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "almazara-forest",
    "TITLE": f"{PROJECT_NAME} Istán Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Almazara Forest: appartementen met 2 en 3 slaapkamers in de Sierra de las Nieves nabij Marbella. Panoramisch uitzicht op de baai, klasse A energie. Vanaf € 580.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Appartementen Sierra de las Nieves Marbella",
    "OG_DESCRIPTION": "Moderne appartementen in Istán, Sierra de las Nieves. Adembenemend zicht op de baai van Marbella, klasse A energie, Balay apparaten, grote terrassen. Vanaf € 580.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/almazara-forest/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/almazara-forest/hero.webp",
    "HERO_BG_ALT": "Almazara Forest appartementen panoramisch uitzicht Istán Marbella",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "ISTÁN · SIERRA DE LAS NIEVES",
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
    "MAP_LAT": "36.542061392487",
    "MAP_LNG": "-4.9503918706358",
}

DATA_EN = {
    "META_DESCRIPTION": "Almazara Forest: apartments with 2 and 3 bedrooms in the Sierra de las Nieves near Marbella. Panoramic bay views, class A energy. From € 580,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Apartments Sierra de las Nieves Marbella",
    "OG_DESCRIPTION": "Modern apartments in Istán, Sierra de las Nieves. Breathtaking views of the bay of Marbella, class A energy, Balay appliances, generous terraces. From € 580,000.",
    "HERO_BG_ALT": "Almazara Forest apartments panoramic views Istán Marbella",
    "HERO_LOCATION": "ISTÁN · SIERRA DE LAS NIEVES",
}
