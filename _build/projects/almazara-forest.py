from urllib.parse import quote

PROJECT_NAME = "Almazara Forest"
PRICE_FROM = "Vanaf € 580.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "almazara-forest",
    "TITLE": f"{PROJECT_NAME} Istán — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Almazara Forest: moderne appartementen in Istán bij Marbella. 2-3 slaapkamers, zwembad, Balay-keuken, Energieklasse A, omringd door natuur. Vanaf € 580.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in de Sierra de las Nieves",
    "OG_DESCRIPTION": "Almazara Forest: exclusieve appartementen met panoramisch uitzicht, zwembad, EV-laders en Energieklasse A in Istán nabij Marbella. Vanaf € 580.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/almazara-forest/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/almazara-forest/hero.webp",
    "HERO_BG_ALT": "Almazara Forest — modern appartementencomplex omringd door natuur in Istán",
    "HERO_NAME": "Almazara Forest",
    "HERO_LOCATION": "ISTÁN, MARBELLA",
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
    "META_DESCRIPTION": "Almazara Forest: modern apartments in Istán near Marbella. 2-3 bedrooms, pool, Balay kitchen, Energy class A, surrounded by nature. From € 580,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in the Sierra de las Nieves",
    "OG_DESCRIPTION": "Almazara Forest: exclusive apartments with panoramic views, pool, EV charging and Energy class A in Istán near Marbella. From € 580,000.",
    "HERO_BG_ALT": "Almazara Forest — modern apartment complex surrounded by nature in Istán",
}

HUB = {
    "NAME": "Almazara Forest",
    "LOCATION": "Istán",
    "PRICE": "Vanaf € 580.000",
    "THUMB": "https://projects.investinspain.be/images/almazara-forest/hero.webp",
    "LAT": 36.542061,
    "LNG": -4.950392,
    "HREF": "/almazara-forest/",
}
