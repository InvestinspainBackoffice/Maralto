from urllib.parse import quote

PROJECT_NAME = "Skye"
PRICE_FROM = "Vanaf € 423.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "skye",
    "TITLE": f"{PROJECT_NAME} Casares Golf — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "SKYE Casares Golf: moderne architectuur en hoogwaardige afwerking, midden in het groen met de Middellandse Zee op de achtergrond. Vanaf €423.000.",
    "OG_TITLE": f"{PROJECT_NAME} Casares Golf — Moderne Architectuur",
    "OG_DESCRIPTION": "Ontdek SKYE Casares Golf: infinity zwembad, zeezicht en een perfecte combinatie van rust en verfijning. Vanaf €423.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/08/Skye-2.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/08/Skye-2.jpg",
    "HERO_BG_ALT": "SKYE Casares Golf — luchtfoto van het complex met zicht op zee",
    "HERO_NAME": "SKYE",
    "HERO_LOCATION": "CASARES GOLF",
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
    "META_DESCRIPTION": "SKYE Casares Golf: modern architecture and high-end finishes, amid greenery with the Mediterranean Sea as a backdrop. From €423.000.",
    "OG_TITLE": f"{PROJECT_NAME} Casares Golf — Modern Architecture",
    "OG_DESCRIPTION": "Discover SKYE Casares Golf: infinity pool, sea views and the perfect combination of tranquility and refinement. From €423.000.",
    "HERO_BG_ALT": "SKYE Casares Golf — aerial view of the complex overlooking the sea",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Casares",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2025/08/Skye-2.jpg",
    "LAT": 36.395767123581,
    "LNG": -5.2269923686981,
    "HREF": "/skye/",
}
