from urllib.parse import quote

PROJECT_NAME = "Navigolf Suites"
PRICE_FROM = "Vanaf € 650.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "navigolf-suites",
    "TITLE": f"{PROJECT_NAME} MIJAS — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Navigolf Suites Mijas: moderne appartementen met panoramisch golfzicht, communaal zwembad en sportfaciliteiten. Op 15 min van het strand. Vanaf € 650.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Moderne appartementen met golfzicht in Mijas",
    "OG_DESCRIPTION": "Exclusief appartementenproject in Mijas met panoramisch golf- en zeezicht, communaal zwembad en eersteklas afwerking. Op korte afstand van strand en Fuengirola.",
    "OG_IMAGE": "https://projects.investinspain.be/images/navigolf-suites/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/navigolf-suites/hero.webp",
    "HERO_BG_ALT": "Navigolf Suites — modern appartementencomplex met golfzicht in Mijas",
    "HERO_NAME": "Navigolf Suites",
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
    "META_DESCRIPTION": "Navigolf Suites Mijas: modern apartments with panoramic golf views, communal pool and sports facilities. 15 min from the beach. From € 650,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Modern apartments with golf views in Mijas",
    "OG_DESCRIPTION": "Exclusive apartment project in Mijas with panoramic golf and sea views, communal pool and premium finishes. Short distance to beach and Fuengirola.",
    "HERO_BG_ALT": "Navigolf Suites — modern apartment complex with golf views in Mijas",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Mijas",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/navigolf-suites/hero.webp",
    "LAT": 36.504034,
    "LNG": -4.687868,
    "HREF": "/navigolf-suites/",
}
