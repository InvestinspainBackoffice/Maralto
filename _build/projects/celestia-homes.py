from urllib.parse import quote

PROJECT_NAME = "Celestia Homes"
PRICE_FROM = "Vanaf € 530.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "celestia-homes",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Celestia Homes: 25 boutique appartementen met 1-3 slaapkamers en zeezicht in La Gaspara, Estepona. Vanaf € 530.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Estepona",
    "OG_DESCRIPTION": "25 boutique appartementen met zeezicht in La Gaspara, Estepona.",
    "OG_IMAGE": "https://projects.investinspain.be/images/celestia-homes/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/celestia-homes/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Appartementen in Estepona",
    "HERO_NAME": "Celestia Homes",
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
    "META_DESCRIPTION": "Celestia Homes: 25 boutique apartments with 1-3 bedrooms and sea views in La Gaspara, Estepona. From € 530,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Estepona",
    "OG_DESCRIPTION": "25 boutique apartments with sea views in La Gaspara, Estepona.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Apartments in Estepona",
}

HUB = {
    "NAME": "Celestia Homes",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 530.000",
    "THUMB": "https://projects.investinspain.be/images/celestia-homes/hero.webp",
    "LAT": 36.407665,
    "LNG": -5.190725,
    "HREF": "/celestia-homes/",
}
