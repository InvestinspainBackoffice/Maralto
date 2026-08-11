from urllib.parse import quote

PROJECT_NAME = "Octavia"
PRICE_FROM = "Vanaf € 2.150.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "octavia",
    "TITLE": f"{PROJECT_NAME} Málaga — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Octavia: luxe appartementen en penthouses met 2 tot 4 slaapkamers in Málaga. Rooftop zwembad, fitnessruimte en zeezicht over de baai. Vanaf € 2.150.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Appartementen & Penthouses in Málaga",
    "OG_DESCRIPTION": "Octavia: eigentijds project met rooftop zwembad en panoramisch uitzicht over de baai van Málaga. Vanaf € 2.150.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/octavia/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/octavia/hero.webp",
    "HERO_BG_ALT": "Octavia — luxe appartementen met zeezicht in Málaga",
    "HERO_NAME": "Octavia",
    "HERO_LOCATION": "MÁLAGA",
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
    "META_DESCRIPTION": "Octavia: luxury apartments and penthouses with 2 to 4 bedrooms in Málaga. Rooftop pool, gym and sea views over the bay. From € 2,150,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Apartments & Penthouses in Málaga",
    "OG_DESCRIPTION": "Octavia: contemporary project with rooftop pool and panoramic views over Málaga bay. From € 2,150,000.",
    "HERO_BG_ALT": "Octavia — luxury apartments with sea views in Málaga",
}

HUB = {
    "NAME": "Octavia",
    "LOCATION": "Málaga",
    "PRICE": "Vanaf € 2.150.000",
    "THUMB": "https://projects.investinspain.be/images/octavia/hero.webp",
    "LAT": 36.6905,
    "LNG": -4.4421,
    "HREF": "/octavia/",
}
