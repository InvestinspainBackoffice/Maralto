from urllib.parse import quote

PROJECT_NAME = "Zenity Cyan"
PRICE_FROM = "Vanaf € 1.779.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "zenity-cyan",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Zenity Cyan: exclusieve luxevilla's met privézwembad, zeezicht en hoogwaardige afwerking in Estepona. Gated community met superieur wooncomfort. Vanaf € 1.779.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve luxevilla's met privézwembad en zeezicht, Estepona",
    "OG_DESCRIPTION": "Zenity Cyan in Estepona: exclusieve villa's met privézwembad, zeezicht en premium afwerking in een gated community. Ultiem wooncomfort aan de Costa del Sol. Vanaf € 1.779.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/zenity-cyan/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/zenity-cyan/hero.webp",
    "HERO_BG_ALT": "Zenity Cyan Estepona luxevilla met privézwembad",
    "HERO_NAME": "Zenity Cyan",
    "HERO_LOCATION": "ESTEPONA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "Zenity Cyan: exclusive luxury villas with private pool, sea views and premium finishes in Estepona. Gated community with superior comfort. From € 1,779,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive luxury villas with private pool and sea views, Estepona",
    "OG_DESCRIPTION": "Zenity Cyan in Estepona: exclusive villas with private pool, sea views and premium finishes in a gated community. Ultimate luxury living on the Costa del Sol. From € 1,779,000.",
    "HERO_BG_ALT": "Zenity Cyan Estepona luxury villa with private pool",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/zenity-cyan/hero.webp",
    "LAT": 36.414531,
    "LNG": -5.18368,
    "HREF": "/zenity-cyan/",
}
