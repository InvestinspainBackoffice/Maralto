from urllib.parse import quote

PROJECT_NAME = "Balance Mijas"
PRICE_FROM = "Vanaf € 461.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "balance-mijas",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Balance Mijas: 75 appartementen en penthouses met 2 en 3 slaapkamers in Las Lagunas de Mijas. 13.000 m² tuinen, zwembad en fitnessruimte. Vanaf € 461.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses in Mijas",
    "OG_DESCRIPTION": "Balance Mijas: eigentijds project met terrassen tot 100 m², uitgeruste keukens en panoramisch zee- en bergzicht. Vanaf € 461.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/balance-mijas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/balance-mijas/hero.webp",
    "HERO_BG_ALT": "Balance Mijas — modern appartementscomplex met zwembad en zeezicht",
    "HERO_NAME": "Balance Mijas",
    "HERO_LOCATION": "LAS LAGUNAS DE MIJAS",
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
    "META_DESCRIPTION": "Balance Mijas: 75 apartments and penthouses with 2 and 3 bedrooms in Las Lagunas de Mijas. 13,000 m² gardens, pool and gym. From € 461,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses in Mijas",
    "OG_DESCRIPTION": "Balance Mijas: contemporary project with terraces up to 100 m², fitted kitchens and panoramic sea and mountain views. From € 461,000.",
    "HERO_BG_ALT": "Balance Mijas — modern apartment complex with pool and sea views",
}

HUB = {
    "NAME": "Balance Mijas",
    "LOCATION": "Mijas",
    "PRICE": "Vanaf € 461.000",
    "THUMB": "https://projects.investinspain.be/images/balance-mijas/hero.webp",
    "LAT": 36.522928,
    "LNG": -4.661297,
    "HREF": "/balance-mijas/",
}
