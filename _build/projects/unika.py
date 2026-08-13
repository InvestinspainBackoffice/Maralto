from urllib.parse import quote

PROJECT_NAME = "Unika"
PRICE_FROM = "Vanaf € 550.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "unika",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Unika: 149 appartementen in 2 fases in Estepona met 2 slaapkamers, 3 zwembaden, bar, sauna en Turks bad. Vanaf € 550.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "149 luxe appartementen in Estepona met 3 zwembaden, bar, sauna en Turks bad.",
    "OG_IMAGE": "https://projects.investinspain.be/images/unika/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/unika/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Appartementen in Estepona",
    "HERO_NAME": "Unika",
    "HERO_LOCATION": "ESTEPONA",
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
    "META_DESCRIPTION": "Unika: 149 apartments in 2 phases in Estepona with 2 bedrooms, 3 pools, bar, sauna and Turkish bath. From € 550,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "149 luxury apartments in Estepona with 3 pools, bar, sauna and Turkish bath.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Apartments in Estepona",
}

HUB = {
    "NAME": "Unika",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 550.000",
    "THUMB": "https://projects.investinspain.be/images/unika/hero.webp",
    "LAT": 36.395374,
    "LNG": -5.206996,
    "HREF": "/unika/",
}
