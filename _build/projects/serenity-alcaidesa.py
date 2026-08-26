from urllib.parse import quote

PROJECT_NAME = "Serenity Alcaidesa"
PRICE_FROM = "Vanaf € 549.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "serenity-alcaidesa",
    "TITLE": f"{PROJECT_NAME} LA ALCAIDESA — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Serenity Alcaidesa: moderne appartementen en penthouses met terras en zeezicht richting Gibraltar, in La Alcaidesa. Communaal zwembad en co-working. Vanaf € 549.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met zeezicht in La Alcaidesa",
    "OG_DESCRIPTION": "Serenity Alcaidesa biedt moderne appartementen en penthouses met terras en weids uitzicht richting Gibraltar, in fase I van dit nieuwe project.",
    "OG_IMAGE": "https://projects.investinspain.be/images/serenity-alcaidesa/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/serenity-alcaidesa/hero.webp",
    "HERO_BG_ALT": "Serenity Alcaidesa — modern appartementencomplex in La Alcaidesa",
    "HERO_NAME": "Serenity Alcaidesa",
    "HERO_LOCATION": "LA ALCAIDESA",
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
    "META_DESCRIPTION": "Serenity Alcaidesa: modern apartments and penthouses with terrace and sea views towards Gibraltar, in La Alcaidesa. Communal pool and co-working. From € 549,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with sea views in La Alcaidesa",
    "OG_DESCRIPTION": "Serenity Alcaidesa offers modern apartments and penthouses with terrace and sweeping views towards Gibraltar, in phase I of this new project.",
    "HERO_BG_ALT": "Serenity Alcaidesa — modern apartment complex in La Alcaidesa",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "La Alcaidesa",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/serenity-alcaidesa/hero.webp",
    "LAT": 36.245,
    "LNG": -5.281,
    "HREF": "/serenity-alcaidesa/",
}
