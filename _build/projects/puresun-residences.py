from urllib.parse import quote

PROJECT_NAME = "PureSun Residences"
PRICE_FROM = "Vanaf € 398.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "puresun-residences",
    "TITLE": f"{PROJECT_NAME} Manilva Costa del Sol — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "PureSun Residences: 159 appartementen met zeezicht in Manilva. 2-3 slaapkamers, ruime terrassen en uitgebreide wellness — Turks bad, jacuzzi, sauna, coworking. Vanaf € 398.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Zeezicht in Manilva",
    "OG_DESCRIPTION": "Appartementen met 2-3 slaapkamers en onbelemmerd zeezicht in Manilva. Resort-faciliteiten: Turks bad, jacuzzi, sauna, gym, coworking. Nabij Estepona en golfbanen.",
    "OG_IMAGE": "https://projects.investinspain.be/images/puresun-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/puresun-residences/hero.webp",
    "HERO_BG_ALT": "PureSun Residences Manilva appartementen met zeezicht",
    "HERO_NAME": "PureSun Residences",
    "HERO_LOCATION": "MANILVA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "PureSun Residences: 159 apartments with sea views in Manilva. 2-3 bedrooms, generous terraces and full wellness — Turkish bath, jacuzzi, sauna, coworking. From € 398,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Sea views in Manilva",
    "OG_DESCRIPTION": "Apartments with 2-3 bedrooms and unobstructed sea views in Manilva. Resort facilities: Turkish bath, jacuzzi, sauna, gym, coworking. Near Estepona and golf courses.",
    "HERO_BG_ALT": "PureSun Residences Manilva apartments with sea views",
}
