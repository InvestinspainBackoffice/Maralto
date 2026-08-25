from urllib.parse import quote

PROJECT_NAME = "Marbella Club Hills Penthouse"
PRICE_FROM = "Prijs op aanvraag"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "marbella-club-hills-penthouse-2",
    "TITLE": f"{PROJECT_NAME} — Panoramisch penthouse in Benahavís · INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Marbella Club Hills Penthouse: exclusief 4-slaapkamer penthouse met panoramisch zeezicht, privésolarium en terrassen in Benahavís. Prijs op aanvraag.",
    "OG_TITLE": f"{PROJECT_NAME} · Panoramisch penthouse Benahavís",
    "OG_DESCRIPTION": "Exclusief penthouse in Marbella Club Hills, Benahavís: 4 slaapkamers, adembenemend zeezicht, privésolarium en grote terrassen aan de voet van Marbella Club Golf.",
    "OG_IMAGE": "https://projects.investinspain.be/images/marbella-club-hills-penthouse-2/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/marbella-club-hills-penthouse-2/hero.webp",
    "HERO_BG_ALT": "Marbella Club Hills Penthouse — solarium met panoramisch zeezicht Benahavís",
    "HERO_NAME": "MARBELLA CLUB HILLS PENTHOUSE",
    "HERO_LOCATION": "BENAHAVÍS",
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
    "MAP_LAT": "36.4933",
    "MAP_LNG": "-5.0690",
}

DATA_EN = {
    "META_DESCRIPTION": "Marbella Club Hills Penthouse: exclusive 4-bedroom penthouse with panoramic sea views, private solarium and terraces in Benahavís. Price on request.",
    "OG_TITLE": f"{PROJECT_NAME} · Panoramic penthouse Benahavís",
    "OG_DESCRIPTION": "Exclusive penthouse in Marbella Club Hills, Benahavís: 4 bedrooms, breathtaking sea views, private solarium and large terraces at the foot of Marbella Club Golf.",
    "HERO_BG_ALT": "Marbella Club Hills Penthouse — solarium with panoramic sea views Benahavís",
}

# NOTE: geen HUB-dict — dit project verschijnt niet op de projectenoverzichtspagina.
