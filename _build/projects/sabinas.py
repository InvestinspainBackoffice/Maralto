from urllib.parse import quote

PROJECT_NAME = "Sabinas"
PRICE_FROM = "Vanaf € 1.395.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "sabinas",
    "TITLE": f"{PROJECT_NAME} LA QUINTA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Sabinas La Quinta: exclusieve villa's en appartementen in fase I & II, met zwembad en panoramisch uitzicht in het bevoorrechte La Quinta bij Marbella. Vanaf € 1.395.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve residenties in La Quinta, Marbella",
    "OG_DESCRIPTION": "Sabinas fase I & II biedt luxueuze woningen met zwembad en panoramisch uitzicht in het gegeerde La Quinta, op korte afstand van Marbella centrum.",
    "OG_IMAGE": "https://projects.investinspain.be/images/sabinas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/sabinas/hero.webp",
    "HERO_BG_ALT": "Sabinas — exclusieve residenties met zwembad in La Quinta, Marbella",
    "HERO_NAME": "Sabinas",
    "HERO_LOCATION": "LA QUINTA, MARBELLA",
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
    "META_DESCRIPTION": "Sabinas La Quinta: exclusive villas and apartments in phase I & II, with pool and panoramic views in privileged La Quinta near Marbella. From € 1,395,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive residences in La Quinta, Marbella",
    "OG_DESCRIPTION": "Sabinas phase I & II offers luxurious homes with pool and panoramic views in sought-after La Quinta, a short distance from Marbella centre.",
    "HERO_BG_ALT": "Sabinas — exclusive residences with pool in La Quinta, Marbella",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
