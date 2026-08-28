from urllib.parse import quote

PROJECT_NAME = "The KOS"
PRICE_FROM = "Vanaf € 1.100.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-kos",
    "TITLE": f"{PROJECT_NAME} Benalmádena — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The KOS: duurzame luxe townhouses en sky top villas in Benalmádena met 3 zwembaden, spa, gym en coworking. Ecologisch ontwerp in harmonie met natuur en zeezicht. Vanaf € 1.100.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Duurzame luxe townhouses met zeezicht, Benalmádena",
    "OG_DESCRIPTION": "The KOS in Benalmádena: ecologische luxe townhouses en sky top villas met zeezicht, 3 infinity-zwembaden, binnenzwembad, spa, gym en coworking. Wonen in harmonie met de natuur. Vanaf € 1.100.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/the-kos/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/the-kos/hero.webp",
    "HERO_BG_ALT": "The KOS Benalmádena exterieur duurzame luxe townhouses",
    "HERO_NAME": "The KOS",
    "HERO_LOCATION": "BENALMÁDENA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "The KOS: sustainable luxury townhouses and sky top villas in Benalmádena with 3 pools, spa, gym and coworking. Ecological design in harmony with nature and sea views. From € 1,100,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Sustainable luxury townhouses with sea views, Benalmádena",
    "OG_DESCRIPTION": "The KOS in Benalmádena: ecological luxury townhouses and sky top villas with sea views, 3 infinity pools, indoor pool, spa, gym and coworking. Living in harmony with nature. From € 1,100,000.",
    "HERO_BG_ALT": "The KOS Benalmádena exterior sustainable luxury townhouses",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benalmádena",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/the-kos/hero.webp",
    "LAT": 36.571471,
    "LNG": -4.598245,
    "HREF": "/the-kos/",
}
