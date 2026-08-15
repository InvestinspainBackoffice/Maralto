from urllib.parse import quote

PROJECT_NAME = "Jade Tower"
PRICE_FROM = "Vanaf € 659.500"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "jade-tower",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Jade Tower: beachfront toren in Fuengirola, 100m van het strand. Gastro-bar, spa, gym, cinema, co-working, zeezicht. Exclusief resort-leven aan de Costa del Sol. Vanaf € 659.500.",
    "OG_TITLE": f"{PROJECT_NAME} · 100m strand Fuengirola spa gastro-bar cinema",
    "OG_DESCRIPTION": "Beachfront toren 100m van het strand in Fuengirola. Gastro-bar, spa, gym, cinema, co-working en panoramisch zeezicht vanuit elke woning. Vanaf € 659.500.",
    "OG_IMAGE": "https://projects.investinspain.be/images/jade-tower/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/jade-tower/hero.webp",
    "HERO_BG_ALT": "Jade Tower beachfront toren zeezicht Fuengirola",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "FUENGIROLA, COSTA DEL SOL",
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
    "MAP_LAT": "36.531201354901",
    "MAP_LNG": "-4.6265247211622",
}

DATA_EN = {
    "META_DESCRIPTION": "Jade Tower: beachfront tower in Fuengirola, 100m from the beach. Gastro-bar, spa, gym, cinema, co-working, sea views. Exclusive resort living on the Costa del Sol. From € 659,500.",
    "OG_TITLE": f"{PROJECT_NAME} · 100m beach Fuengirola spa gastro-bar cinema",
    "OG_DESCRIPTION": "Beachfront tower 100m from the beach in Fuengirola. Gastro-bar, spa, gym, cinema, co-working and panoramic sea views from every home. From € 659,500.",
    "HERO_BG_ALT": "Jade Tower beachfront tower sea views Fuengirola",
}
