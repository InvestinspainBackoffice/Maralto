from urllib.parse import quote

PROJECT_NAME = "Tiara"
PRICE_FROM = "Vanaf € 1.550.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "tiara",
    "TITLE": f"{PROJECT_NAME} BENAHAVÍS — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Tiara Benahavís: exclusieve appartementen en penthouses met solarium, jacuzzi en panoramisch uitzicht in het prestigieuze Benahavís. Vanaf € 1.550.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve residenties in Benahavís",
    "OG_DESCRIPTION": "Tiara biedt luxueuze appartementen en penthouses met solarium en jacuzzi in Benahavís, één van de meest exclusieve gemeenten van de Costa del Sol.",
    "OG_IMAGE": "https://projects.investinspain.be/images/tiara/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/tiara/hero.webp",
    "HERO_BG_ALT": "Tiara — exclusief appartementencomplex in Benahavís",
    "HERO_NAME": "Tiara",
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
}

DATA_EN = {
    "META_DESCRIPTION": "Tiara Benahavís: exclusive apartments and penthouses with solarium, jacuzzi and panoramic views in prestigious Benahavís. From € 1,550,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive residences in Benahavís",
    "OG_DESCRIPTION": "Tiara offers luxurious apartments and penthouses with solarium and jacuzzi in Benahavís, one of the most exclusive municipalities on the Costa del Sol.",
    "HERO_BG_ALT": "Tiara — exclusive apartment complex in Benahavís",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
