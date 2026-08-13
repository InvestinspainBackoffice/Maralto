from urllib.parse import quote

PROJECT_NAME = "Valley Views"
PRICE_FROM = "Vanaf € 357.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "valley-views",
    "TITLE": f"{PROJECT_NAME} Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Valley Views: hedendaagse appartementen in Mijas Costa met panoramisch uitzicht. 2-3 slaapkamers, gemeenschappelijk zwembad, EV-laders, Energielabel A. Vanaf € 357.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Mijas Costa",
    "OG_DESCRIPTION": "Valley Views: moderne appartementen met panoramisch uitzicht, groot zwembad, aangelegde tuinen en Energielabel A in Mijas Costa. Vanaf € 357.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/valley-views/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/valley-views/hero.webp",
    "HERO_BG_ALT": "Valley Views — modern appartementencomplex met panoramisch uitzicht in Mijas Costa",
    "HERO_NAME": "Valley Views",
    "HERO_LOCATION": "MIJAS COSTA",
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
    "META_DESCRIPTION": "Valley Views: contemporary apartments in Mijas Costa with panoramic views. 2-3 bedrooms, communal pool, EV charging, Energy Label A. From € 357,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Mijas Costa",
    "OG_DESCRIPTION": "Valley Views: modern apartments with panoramic views, large pool, landscaped gardens and Energy Label A in Mijas Costa. From € 357,000.",
    "HERO_BG_ALT": "Valley Views — modern apartment complex with panoramic views in Mijas Costa",
}

HUB = {
    "NAME": "Valley Views",
    "LOCATION": "Mijas Costa",
    "PRICE": "Vanaf € 357.000",
    "THUMB": "https://projects.investinspain.be/images/valley-views/hero.webp",
    "LAT": 36.521841,
    "LNG": -4.659773,
    "HREF": "/valley-views/",
}
