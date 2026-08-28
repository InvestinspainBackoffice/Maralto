from urllib.parse import quote

PROJECT_NAME = "Villa Batur"
PRICE_FROM = "Prijs op aanvraag"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "villa-batur",
    "TITLE": f"{PROJECT_NAME} — Luxevilla Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Villa Batur: spectaculaire luxevilla met panoramisch zeezicht in Marbella. Privézwembad, meerdere terrassen en uitzonderlijk design. Prijs op aanvraag.",
    "OG_TITLE": f"{PROJECT_NAME} — Spectaculaire luxevilla met zeezicht, Marbella",
    "OG_DESCRIPTION": "Villa Batur in Marbella: een architecturaal meesterwerk met panoramisch zeezicht, privézwembad en uitzonderlijke afwerking. Prijs op aanvraag.",
    "OG_IMAGE": "https://projects.investinspain.be/images/villa-batur/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/villa-batur/hero.webp",
    "HERO_BG_ALT": "Exterieur van Villa Batur met zeezicht in Marbella",
    "HERO_NAME": "Villa Batur",
    "HERO_LOCATION": "SOTOGRANDE",
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
    "META_DESCRIPTION": "Villa Batur: spectacular luxury villa with panoramic sea views in Marbella. Private pool, multiple terraces and exceptional design. Price on request.",
    "OG_TITLE": f"{PROJECT_NAME} — Spectacular luxury villa with sea views, Marbella",
    "OG_DESCRIPTION": "Villa Batur in Marbella: an architectural masterpiece with panoramic sea views, private pool and exceptional finishes. Price on request.",
    "HERO_BG_ALT": "Exterior of Villa Batur with sea views in Marbella",
}

HUB = {
    "NAME": "Villa Batur",
    "LOCATION": "Sotogrande",
    "PRICE": "Prijs op aanvraag",
    "THUMB": "https://projects.investinspain.be/images/villa-batur/hero.webp",
    "LAT": 36.285039,
    "LNG": -5.300833,
    "HREF": "/villa-batur/",
}
