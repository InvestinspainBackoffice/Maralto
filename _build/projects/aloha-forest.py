from urllib.parse import quote

PROJECT_NAME = "Aloha Forest"
PRICE_FROM = "Vanaf € 1.176.270"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "aloha-forest",
    "TITLE": f"{PROJECT_NAME} Nueva Andalucía — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Aloha Forest: appartementen, penthouses en duplex-penthouses met 2 en 3 slaapkamers, vlakbij de Golden Mile in Nueva Andalucía. Vanaf € 1.176.270.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Nueva Andalucía",
    "OG_DESCRIPTION": "Aloha Forest: vloer-tot-plafond ramen, privézwembad bij penthouses en gated community vlakbij Aloha Golf Club. Vanaf € 1.176.270.",
    "OG_IMAGE": "https://projects.investinspain.be/images/aloha-forest/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/aloha-forest/hero.webp",
    "HERO_BG_ALT": "Aloha Forest — moderne appartementen met zeezicht in Nueva Andalucía",
    "HERO_NAME": "Aloha Forest",
    "HERO_LOCATION": "NUEVA ANDALUCÍA, MARBELLA",
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
    "META_DESCRIPTION": "Aloha Forest: apartments, penthouses and duplex penthouses with 2 and 3 bedrooms, close to the Golden Mile in Nueva Andalucía. From € 1,176,270.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Nueva Andalucía",
    "OG_DESCRIPTION": "Aloha Forest: floor-to-ceiling windows, private pool for penthouses and a gated community close to Aloha Golf Club. From € 1,176,270.",
    "HERO_BG_ALT": "Aloha Forest — modern apartments with sea views in Nueva Andalucía",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
