from urllib.parse import quote

PROJECT_NAME = "Naya Residences"
PRICE_FROM = "Vanaf € 735.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "naya-residences",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Naya Residences: moderne appartementen met zeezicht en grote terrassen in Atalaya, Estepona. Communale faciliteiten en topligging nabij strand en golf. Vanaf € 735.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen met zeezicht, Estepona",
    "OG_DESCRIPTION": "Naya Residences in Atalaya, Estepona: eigentijdse appartementen met zeezicht, ruime terrassen en kwalitatieve afwerking nabij strand en golf. Vanaf € 735.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/naya-residences/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/naya-residences/hero.webp",
    "HERO_BG_ALT": "Naya Residences Estepona exterieur met zeezicht",
    "HERO_NAME": "Naya Residences",
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
    "META_DESCRIPTION": "Naya Residences: modern apartments with sea views and large terraces in Atalaya, Estepona. Communal amenities and a prime location near the beach and golf. From € 735,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments with sea views, Estepona",
    "OG_DESCRIPTION": "Naya Residences in Atalaya, Estepona: contemporary apartments with sea views, spacious terraces and quality finishes near the beach and golf. From € 735,000.",
    "HERO_BG_ALT": "Naya Residences Estepona exterior with sea views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/naya-residences/hero.webp",
    "LAT": 36.481322,
    "LNG": -5.021394,
    "HREF": "/naya-residences/",
}
