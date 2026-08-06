from urllib.parse import quote

PROJECT_NAME = "Oceana Gardens"
PRICE_FROM = "Vanaf € 419.500"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "oceana-gardens-1",
    "TITLE": f"{PROJECT_NAME} CANCELADA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Oceana Gardens Cancelada: moderne appartementen en townhouses op wandelafstand van Cancelada en prachtige golfterreinen in West-Marbella. Vanaf € 419.500.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen en townhouses in Cancelada",
    "OG_DESCRIPTION": "Oceana Gardens biedt moderne appartementen en townhouses op wandelafstand van Cancelada en de golfterreinen van West-Marbella.",
    "OG_IMAGE": "https://projects.investinspain.be/images/oceana-gardens-1/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/oceana-gardens-1/hero.webp",
    "HERO_BG_ALT": "Oceana Gardens — modern appartementencomplex in Cancelada",
    "HERO_NAME": "Oceana Gardens",
    "HERO_LOCATION": "CANCELADA, MARBELLA",
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
    "META_DESCRIPTION": "Oceana Gardens Cancelada: modern apartments and townhouses within walking distance of Cancelada and beautiful golf courses in West Marbella. From € 419,500.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments and townhouses in Cancelada",
    "OG_DESCRIPTION": "Oceana Gardens offers modern apartments and townhouses within walking distance of Cancelada and the golf courses of West Marbella.",
    "HERO_BG_ALT": "Oceana Gardens — modern apartment complex in Cancelada",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
