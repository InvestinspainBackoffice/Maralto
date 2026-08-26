from urllib.parse import quote

PROJECT_NAME = "Villa Europa 6"
PRICE_FROM = "Vanaf € 1.515.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "villa-europa-6",
    "TITLE": f"{PROJECT_NAME} La Cala Golf, Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Villa Europa 6: luxueuze villa met 4 slaapkamers, infinity zwembad en uitzicht op drie golfbanen in La Cala Golf, Mijas. Vanaf € 1.515.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxevilla in La Cala Golf, Mijas",
    "OG_DESCRIPTION": "Villa Europa 6: 1.439 m² perceel, infinity zwembad, SIEMENS-keuken en 24-uurs beveiliging tussen golf en natuur in Mijas Costa. Vanaf € 1.515.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/villa-europa-6/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/villa-europa-6/hero.webp",
    "HERO_BG_ALT": "Villa Europa 6 — luxevilla met infinity zwembad in La Cala Golf, Mijas",
    "HERO_NAME": "Villa Europa 6",
    "HERO_LOCATION": "LA CALA GOLF, MIJAS",
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
    "META_DESCRIPTION": "Villa Europa 6: luxury villa with 4 bedrooms, infinity pool and views over three golf courses in La Cala Golf, Mijas. From € 1,515,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury villa in La Cala Golf, Mijas",
    "OG_DESCRIPTION": "Villa Europa 6: 1,439 m² plot, infinity pool, SIEMENS kitchen and 24-hour security between golf and nature in Mijas Costa. From € 1,515,000.",
    "HERO_BG_ALT": "Villa Europa 6 — luxury villa with infinity pool in La Cala Golf, Mijas",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Cala Golf, Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/villa-europa-6/hero.webp",
    "LAT": 36.5252,
    "LNG": -4.7434,
    "HREF": "/villa-europa-6/",
}
