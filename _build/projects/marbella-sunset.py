from urllib.parse import quote

PROJECT_NAME = "Marbella Sunset"
PRICE_FROM = "Vanaf € 1.150.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "marbella-sunset",
    "TITLE": f"{PROJECT_NAME} Cabopino — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Marbella Sunset – luxe appartementen en penthouses met panoramische terrassen en zeezicht bij Cabopino, Marbella. Moderne architectuur dicht bij het strand. Vanaf € 1.150.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxe appartementen Cabopino Marbella · INVESTINSPAIN.BE",
    "OG_DESCRIPTION": "Exclusieve appartementen met panoramische terrassen en zeezicht bij Cabopino, Marbella. Moderne architectuur op toplocatie. Vraag brochure aan bij INVESTINSPAIN.",
    "OG_IMAGE": "https://projects.investinspain.be/images/marbella-sunset/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/marbella-sunset/hero.webp",
    "HERO_BG_ALT": "Marbella Sunset exterieur luxe appartementen Cabopino Marbella zeezicht",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "CABOPINO, MARBELLA",
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
    "MAP_LAT": "36.49179139507",
    "MAP_LNG": "-4.7443778399995",
}

DATA_EN = {
    "META_DESCRIPTION": "Marbella Sunset – luxury apartments and penthouses with panoramic terraces and sea views near Cabopino, Marbella. Modern architecture close to the beach. From € 1,150,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Luxury apartments Cabopino Marbella · INVESTINSPAIN.BE",
    "OG_DESCRIPTION": "Exclusive apartments with panoramic terraces and sea views near Cabopino, Marbella. Modern architecture at a prime location. Request the brochure at INVESTINSPAIN.",
    "HERO_BG_ALT": "Marbella Sunset exterior luxury apartments Cabopino Marbella sea views",
}
