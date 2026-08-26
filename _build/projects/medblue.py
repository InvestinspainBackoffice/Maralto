from urllib.parse import quote

PROJECT_NAME = "Medblue"
PRICE_FROM = "Vanaf € 509.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "medblue",
    "TITLE": f"{PROJECT_NAME} LOS MONTEROS — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Medblue Los Monteros: exclusief project van 39 luxe appartementen en duplex penthouses met zeezicht in Marbella, op 10 minuten van het strand. Vanaf € 509.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe appartementen met zeezicht in Los Monteros, Marbella",
    "OG_DESCRIPTION": "Medblue biedt 39 exclusieve appartementen en duplex penthouses met zeezicht in het bovenste deel van Los Monteros, op korte afstand van Marbella centrum.",
    "OG_IMAGE": "https://projects.investinspain.be/images/medblue/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/medblue/hero.webp",
    "HERO_BG_ALT": "Medblue — exclusief appartementencomplex met zeezicht in Los Monteros, Marbella",
    "HERO_NAME": "Medblue",
    "HERO_LOCATION": "LOS MONTEROS, MARBELLA",
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
    "META_DESCRIPTION": "Medblue Los Monteros: exclusive project of 39 luxury apartments and duplex penthouses with sea views in Marbella, 10 minutes from the beach. From € 509,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury apartments with sea views in Los Monteros, Marbella",
    "OG_DESCRIPTION": "Medblue offers 39 exclusive apartments and duplex penthouses with sea views in the upper part of Los Monteros, a short distance from Marbella centre.",
    "HERO_BG_ALT": "Medblue — exclusive apartment complex with sea views in Los Monteros, Marbella",
}


# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Los Monteros, Marbella",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/medblue/hero.webp",
    "LAT": 36.499,
    "LNG": -4.816,
    "HREF": "/medblue/",
}
