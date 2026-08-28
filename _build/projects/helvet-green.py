from urllib.parse import quote

PROJECT_NAME = "Helvet Green"
PRICE_FROM = "Vanaf € 248.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "helvet-green",
    "TITLE": f"{PROJECT_NAME} MIJAS — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Helvet Green Mijas: 103 moderne appartementen met 1-3 slaapkamers, mediterrane tuinen en natuurlijk zwembad. Rust en natuur nabij de kust. Vanaf € 248.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen in Mijas",
    "OG_DESCRIPTION": "103 lichte appartementen met mediterrane tuinen, natuurlijk zwembad en ontspanningsruimtes in Mijas, oost-Marbella.",
    "OG_IMAGE": "https://projects.investinspain.be/images/helvet-green/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/helvet-green/hero.webp",
    "HERO_BG_ALT": "Helvet Green — appartementencomplex met mediterrane tuinen in Mijas",
    "HERO_NAME": "Helvet Green",
    "HERO_LOCATION": "MIJAS",
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
    "META_DESCRIPTION": "Helvet Green Mijas: 103 modern apartments with 1-3 bedrooms, Mediterranean gardens and natural pool. Peace and nature near the coast. From € 248,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments in Mijas",
    "OG_DESCRIPTION": "103 bright apartments with Mediterranean gardens, natural pool and relaxation areas in Mijas, east of Marbella.",
    "HERO_BG_ALT": "Helvet Green — apartment complex with Mediterranean gardens in Mijas",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/helvet-green/hero.webp",
    "LAT": 36.551093,
    "LNG": -4.659861,
    "HREF": "/helvet-green/",
}
