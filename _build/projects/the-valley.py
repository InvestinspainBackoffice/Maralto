from urllib.parse import quote

PROJECT_NAME = "The Valley"
PRICE_FROM = "Vanaf € 1.395.275"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "the-valley",
    "TITLE": f"{PROJECT_NAME} Elviria — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "The Valley: exclusief boutiqueproject van 23 eigentijdse townhouses in de heuvels van Elviria, Marbella East. Vanaf €1.395.275.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutiqueproject van Townhouses in Elviria",
    "OG_DESCRIPTION": "Ontdek The Valley: 23 townhouses met privé-infinity zwembaden, twee gemeenschappelijke zwembaden, fitness en wellnesszones in de rustige heuvels van Elviria. Vanaf €1.395.275.",
    "OG_IMAGE": "https://projects.investinspain.be/images/the-valley/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/the-valley/hero.webp",
    "HERO_BG_ALT": "The Valley — toegangsbrug naar de townhouses tussen groen",
    "HERO_NAME": "THE VALLEY",
    "HERO_LOCATION": "ELVIRIA",
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
    "META_DESCRIPTION": "The Valley: an exclusive boutique project of 23 contemporary townhouses in the hills of Elviria, Marbella East. From €1,395,275.",
    "OG_TITLE": f"{PROJECT_NAME} — Boutique Townhouse Project in Elviria",
    "OG_DESCRIPTION": "Discover The Valley: 23 townhouses with private infinity pools, two communal pools, a gym and wellness zones in the quiet hills of Elviria. From €1,395,275.",
    "HERO_BG_ALT": "The Valley — approach bridge to the townhouses through greenery",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Elviria",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/the-valley/hero.webp",
    "LAT": 36.507567,
    "LNG": -4.787271,
    "HREF": "/the-valley/",
}
