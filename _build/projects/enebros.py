from urllib.parse import quote

PROJECT_NAME = "Enebros"
PRICE_FROM = "Vanaf € 1.600.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "enebros",
    "TITLE": f"{PROJECT_NAME} Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Enebros: exclusieve villa's en appartementen met privézwembad en zeezicht nabij Marbella. Solarium, luxe afwerking en gated community. Vanaf € 1.600.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve woningen met zeezicht en privézwembad, Marbella",
    "OG_DESCRIPTION": "Enebros nabij Marbella: luxueuze villa's en appartementen met privézwembad, zeezicht en solarium. Gated community met hoogwaardige afwerking. Vanaf € 1.600.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/enebros/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/enebros/hero.webp",
    "HERO_BG_ALT": "Zwembad met zeezicht in Enebros Marbella",
    "HERO_NAME": "Enebros",
    "HERO_LOCATION": "MARBELLA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Enebros: exclusive villas and apartments with private pool and sea views near Marbella. Solarium, luxury finishes and gated community. From € 1,600,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive homes with sea views and private pool, Marbella",
    "OG_DESCRIPTION": "Enebros near Marbella: luxury villas and apartments with private pool, sea views and solarium. Gated community with premium finishes. From € 1,600,000.",
    "HERO_BG_ALT": "Pool with sea views at Enebros Marbella",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/enebros/hero.webp",
    "LAT": 36.502843,
    "LNG": -4.913942,
    "HREF": "/enebros/",
}
