from urllib.parse import quote

PROJECT_NAME = "Soleil"
PRICE_FROM = "Vanaf € 530.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "soleil",
    "TITLE": f"{PROJECT_NAME} MARBELLA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Soleil Marbella: luxe appartementen met infinity-pool, sociale lounges en co-working spaces. Nabij golf en strand in Nueva Andalucía. Vanaf € 530.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe appartementen met infinity-pool in Marbella",
    "OG_DESCRIPTION": "Soleil biedt moderne residenties met infinity-pool, sociale lounges en co-working ruimtes in Marbella. Het perfecte adres voor wie levensstijl en comfort combineert.",
    "OG_IMAGE": "https://projects.investinspain.be/images/soleil/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/soleil/hero.webp",
    "HERO_BG_ALT": "Soleil Marbella — luxe appartementencomplex met infinity-pool",
    "HERO_NAME": "Soleil",
    "HERO_LOCATION": "MARBELLA",
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
    "META_DESCRIPTION": "Soleil Marbella: luxury apartments with infinity pool, social lounges and co-working spaces. Near golf and beach in Nueva Andalucía. From € 530,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury apartments with infinity pool in Marbella",
    "OG_DESCRIPTION": "Soleil offers modern residences with infinity pool, social lounges and co-working spaces in Marbella. The perfect address for those combining lifestyle and comfort.",
    "HERO_BG_ALT": "Soleil Marbella — luxury apartment complex with infinity pool",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/soleil/hero.webp",
    "LAT": 36.502843,
    "LNG": -4.913942,
    "HREF": "/soleil/",
}
