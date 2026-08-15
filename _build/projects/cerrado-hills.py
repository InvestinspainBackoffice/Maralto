from urllib.parse import quote

PROJECT_NAME = "Cerrado Hills"
PRICE_FROM = "Vanaf € 2.300.240"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "cerrado-hills",
    "TITLE": f"{PROJECT_NAME} Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Cerrado Hills: 13 luxe villa's met 4 slaapkamers en golf- en zeezicht in Mijas. High-end afwerking, fitness, kelderverdieping, 20 min van Málaga. Vanaf € 2.300.240.",
    "OG_TITLE": f"{PROJECT_NAME} · 13 luxe villa's 4 slpk golf- en zeezicht Mijas",
    "OG_DESCRIPTION": "13 exclusieve luxevilla's met 4 slaapkamers en panoramisch golf- en zeezicht in Mijas. High-end bouw- en afwerkingskwaliteit, fitness, kelderverdieping. Vanaf € 2.300.240.",
    "OG_IMAGE": "https://projects.investinspain.be/images/cerrado-hills/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/cerrado-hills/hero.webp",
    "HERO_BG_ALT": "Cerrado Hills luxevilla's golfzicht zeezicht Mijas",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "MIJAS, COSTA DEL SOL",
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
    "MAP_LAT": "36.529853396044",
    "MAP_LNG": "-4.6588677324932",
}

DATA_EN = {
    "META_DESCRIPTION": "Cerrado Hills: 13 luxury villas with 4 bedrooms and golf and sea views in Mijas. High-end construction quality, fitness, basement, 20 min from Málaga. From € 2,300,240.",
    "OG_TITLE": f"{PROJECT_NAME} · 13 luxury villas 4 bed golf and sea views Mijas",
    "OG_DESCRIPTION": "13 exclusive luxury villas with 4 bedrooms and panoramic golf and sea views in Mijas. High-end quality, fitness, basement options. From € 2,300,240.",
    "HERO_BG_ALT": "Cerrado Hills luxury villas golf views sea views Mijas",
}
