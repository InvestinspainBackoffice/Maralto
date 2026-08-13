from urllib.parse import quote

PROJECT_NAME = "Golden Eight"
PRICE_FROM = "Vanaf € 1.750.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "golden-eight",
    "TITLE": f"{PROJECT_NAME} Cabopino Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Golden Eight: exclusieve boutique-appartementen met spectaculair zeezicht en ultra-luxe afwerking in Cabopino, Marbella. Slechts 8 unieke woningen. Vanaf € 1.750.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-luxe boutique-appartementen met zeezicht, Cabopino Marbella",
    "OG_DESCRIPTION": "Golden Eight in Cabopino, Marbella: 8 exclusieve appartementen met panoramisch zeezicht, premium afwerking en architecturale kwaliteit op de eerste lijn. Vanaf € 1.750.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/golden-eight/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/golden-eight/hero.webp",
    "HERO_BG_ALT": "Golden Eight Cabopino Marbella exterieur met zeezicht",
    "HERO_NAME": "Golden Eight",
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
}

DATA_EN = {
    "META_DESCRIPTION": "Golden Eight: exclusive boutique apartments with spectacular sea views and ultra-luxury finishes in Cabopino, Marbella. Only 8 unique homes. From € 1,750,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-luxury boutique apartments with sea views, Cabopino Marbella",
    "OG_DESCRIPTION": "Golden Eight in Cabopino, Marbella: 8 exclusive apartments with panoramic sea views, premium finishes and architectural quality on the frontline. From € 1,750,000.",
    "HERO_BG_ALT": "Golden Eight Cabopino Marbella exterior with sea views",
}
