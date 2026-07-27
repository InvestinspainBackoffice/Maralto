from urllib.parse import quote

PROJECT_NAME = "ZEW Elviria"
PRICE_FROM = "Vanaf € 770.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "zew-elviria",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "ZEW Elviria: duplexappartementen omringd door natuur in Elviria Hill, Oost-Marbella. Vanaf €770.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Duplexappartementen",
    "OG_DESCRIPTION": "Ontdek ZEW Elviria: 88 duplexappartementen in de dennenbossen van Elviria Hill, met 4 zwembaden, co-working space en gym. Vanaf €770.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2025/06/ZEW-Elviria-INVESTINSPAIN-1110x623.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2025/06/ZEW-Elviria-INVESTINSPAIN-1110x623.jpg",
    "HERO_BG_ALT": "ZEW Elviria — terrasvormig complex met zwembad omgeven door dennenbossen",
    "HERO_NAME": "ZEW ELVIRIA",
    "HERO_LOCATION": "ELVIRIA",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "WA_TEXT_ENCODED": quote(WA_MESSAGE),
    "PROJECT_NAME": PROJECT_NAME,
}
