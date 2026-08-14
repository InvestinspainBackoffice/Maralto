from urllib.parse import quote

PROJECT_NAME = "Valley Views"
PRICE_FROM = "Vanaf € 357.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "valley-views-2",
    "TITLE": f"{PROJECT_NAME} Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Valley Views: moderne appartementen met 2 en 3 slaapkamers in Mijas Costa. Panoramisch vallei- en zeezicht, zwembad met solarium, energie-efficiënt. Vanaf € 357.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Appartementen Mijas Costa",
    "OG_DESCRIPTION": "2 en 3 slaapkamer appartementen met panoramisch uitzicht op de vallei in Mijas Costa. Zwembad, solarium, tuinen, EV-laadpunten, klasse A energie. Vanaf € 357.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/valley-views-2/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/valley-views-2/hero.webp",
    "HERO_BG_ALT": "Valley Views appartementen panoramisch uitzicht Mijas Costa",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "MIJAS COSTA",
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
    "MAP_LAT": "36.521841422545",
    "MAP_LNG": "-4.659773350735",
}

DATA_EN = {
    "META_DESCRIPTION": "Valley Views: modern apartments with 2 and 3 bedrooms in Mijas Costa. Panoramic valley and sea views, pool with solarium, energy-efficient. From € 357,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Apartments Mijas Costa",
    "OG_DESCRIPTION": "2 and 3 bedroom apartments with panoramic valley views in Mijas Costa. Pool, solarium, gardens, EV charging points, class A energy. From € 357,000.",
    "HERO_BG_ALT": "Valley Views apartments panoramic views Mijas Costa",
}
