from urllib.parse import quote

PROJECT_NAME = "Asperia"
PRICE_FROM = "Vanaf € 530.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "asperia",
    "TITLE": f"{PROJECT_NAME} Centrum Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Asperia: 43 exclusieve appartementen met 1, 2 en 3 slaapkamers in het centrum van Estepona. Zwembad, sportschool, receptie, 4 commerciële ruimtes. Vanaf € 530.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 43 appartementen centrum Estepona",
    "OG_DESCRIPTION": "43 exclusieve appartementen 1-3 slaapkamers in het centrum van Estepona. Zwembad, sportschool, receptie, commerciële ruimtes. Vanaf € 530.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/asperia/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/asperia/hero.webp",
    "HERO_BG_ALT": "Asperia appartementen exterieur zwembad centrum Estepona",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "CENTRUM ESTEPONA",
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
    "MAP_LAT": "36.42694786879",
    "MAP_LNG": "-5.1525885879303",
}

DATA_EN = {
    "META_DESCRIPTION": "Asperia: 43 exclusive apartments with 1, 2 and 3 bedrooms in the centre of Estepona. Pool, gym, reception, 4 commercial spaces. From € 530,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 43 apartments Estepona centre",
    "OG_DESCRIPTION": "43 exclusive apartments 1-3 bedrooms in the centre of Estepona. Pool, gym, reception, commercial spaces. From € 530,000.",
    "HERO_BG_ALT": "Asperia apartments exterior pool Estepona centre",
}
