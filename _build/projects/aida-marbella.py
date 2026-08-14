from urllib.parse import quote

PROJECT_NAME = "AÍDA"
PRICE_FROM = "Vanaf € 3.450.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "aida-marbella",
    "TITLE": f"{PROJECT_NAME} Golden Mile Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "AÍDA: slechts 8 exclusieve duplexwoningen op de Golden Mile van Marbella, 50m van het Puente Romano. Privézwembad, Bentley Home afwerking, 500m²+. Vanaf € 3.450.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 8 luxe duplexwoningen Golden Mile Marbella",
    "OG_DESCRIPTION": "8 exclusieve duplexwoningen op 50m van Puente Romano Beach Resort. Privézwembad, Bentley Home afwerking, panoramische ramen, domotica. Vanaf € 3.450.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/aida-marbella/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/aida-marbella/hero.webp",
    "HERO_BG_ALT": "AÍDA Golden Mile Marbella gevel Puente Romano",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "GOLDEN MILE, MARBELLA",
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
    "MAP_LAT": "36.50580911160476",
    "MAP_LNG": "-4.925236386402663",
}

DATA_EN = {
    "META_DESCRIPTION": "AÍDA: only 8 exclusive duplex residences on the Golden Mile of Marbella, 50m from Puente Romano. Private pool, Bentley Home interiors, 500m²+. From € 3,450,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 8 luxury duplex residences Golden Mile Marbella",
    "OG_DESCRIPTION": "8 exclusive duplex residences 50m from Puente Romano Beach Resort. Private pool, Bentley Home interiors, panoramic windows, home automation. From € 3,450,000.",
    "HERO_BG_ALT": "AÍDA Golden Mile Marbella facade Puente Romano",
}
