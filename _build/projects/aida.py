from urllib.parse import quote

PROJECT_NAME = "AÍDA"
PRICE_FROM = "Vanaf € 3.450.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "aida",
    "TITLE": f"{PROJECT_NAME} Golden Mile, Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "AÍDA: 8 exclusieve duplex-residenties op 50 m van Puente Romano Beach Resort. 500+ m², Bentley Home, privézwembad, smart home. Vanaf € 3.450.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve Residenties op de Golden Mile",
    "OG_DESCRIPTION": "AÍDA: 8 duplex-residenties met Bentley Home afwerking, privézwembad en panoramische ramen. 50 m van Puente Romano, Marbella. Vanaf € 3.450.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/aida/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/aida/hero.webp",
    "HERO_BG_ALT": "AÍDA — exclusieve duplex-residentie op de Golden Mile in Marbella",
    "HERO_NAME": "AÍDA",
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
}

DATA_EN = {
    "META_DESCRIPTION": "AÍDA: 8 exclusive duplex residences 50 m from Puente Romano Beach Resort. 500+ m², Bentley Home, private pool, smart home. From € 3,450,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive Residences on the Golden Mile",
    "OG_DESCRIPTION": "AÍDA: 8 duplex residences with Bentley Home finishes, private pool and panoramic windows. 50 m from Puente Romano, Marbella. From € 3,450,000.",
    "HERO_BG_ALT": "AÍDA — exclusive duplex residence on the Golden Mile in Marbella",
}

HUB = {
    "NAME": "AÍDA",
    "LOCATION": "Marbella",
    "PRICE": "Vanaf € 3.450.000",
    "THUMB": "https://projects.investinspain.be/images/aida/hero.webp",
    "LAT": 36.505809,
    "LNG": -4.925236,
    "HREF": "/aida/",
}
