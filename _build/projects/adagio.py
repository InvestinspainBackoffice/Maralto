from urllib.parse import quote

PROJECT_NAME = "Adagio"
PRICE_FROM = "Vanaf € 512.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "adagio",
    "TITLE": f"{PROJECT_NAME} Cancelada — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Adagio: appartementen en penthouses met ruime terrassen in Cancelada, New Golden Mile. Vanaf €512.000.",
    "OG_TITLE": f"{PROJECT_NAME} Cancelada — Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Adagio: 80 woningen omgeven door golfterreinen op de New Golden Mile, met zwembad, gym en Zen-zone. Vanaf €512.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/04/Adagio-Cancelada-6.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/04/Adagio-Cancelada-6.jpg",
    "HERO_BG_ALT": "Adagio Cancelada — appartementen rond een zwembad met palmbomen",
    "HERO_NAME": "ADAGIO",
    "HERO_LOCATION": "CANCELADA",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "WA_TEXT_ENCODED": quote(WA_MESSAGE),
    "PROJECT_NAME": PROJECT_NAME,
}
