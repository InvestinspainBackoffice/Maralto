from urllib.parse import quote

PROJECT_NAME = "The View Marbella"
PRICE_FROM = "Vanaf € 899.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-view",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The View Marbella: luxe appartementen tussen Marbella en Benahavís met panoramisch zee- en golfzicht. Vanaf €899.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Appartementen",
    "OG_DESCRIPTION": "Ontdek The View Marbella: boutique complex met 24u beveiliging, conciërgedienst, spa en binnen- en buitenzwembaden. Vanaf €899.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2020/03/Facade-Close-Up-1110x623.png",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2020/03/Facade-Close-Up-1110x623.png",
    "HERO_BG_ALT": "The View Marbella — gebogen architectuur met terrassen tussen het groen",
    "HERO_NAME": "THE VIEW",
    "HERO_LOCATION": "BENAHAVÍS",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "WA_TEXT_ENCODED": quote(WA_MESSAGE),
    "PROJECT_NAME": PROJECT_NAME,
}
