from urllib.parse import quote

PROJECT_NAME = "Vitta Marina"
PRICE_FROM = "Vanaf € 451.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vitta-marina",
    "TITLE": f"{PROJECT_NAME} La Cala de Mijas — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vitta Marina: 72 moderne appartementen met 1, 2 en 3 slaapkamers op 2 minuten van het strand in La Cala de Mijas. Zuidoriëntatie, zeezicht, privétuinen en penthouses. Vanaf € 451.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Appartementen La Cala de Mijas",
    "OG_DESCRIPTION": "72 appartementen met zuidoriëntatie op 2 min van het strand in La Cala de Mijas. Zeezicht, gelijkvloerse eenheden met tuin, penthouses met groot terras. Vanaf € 451.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/vitta-marina/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/vitta-marina/hero.webp",
    "HERO_BG_ALT": "Vitta Marina terras met zeezicht La Cala de Mijas",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "LA CALA DE MIJAS",
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
    "MAP_LAT": "36.509607970541",
    "MAP_LNG": "-4.650319323332",
}

DATA_EN = {
    "META_DESCRIPTION": "Vitta Marina: 72 modern apartments with 1, 2 and 3 bedrooms just 2 minutes from the beach in La Cala de Mijas. South-facing, sea views, private gardens and penthouses. From € 451,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Apartments La Cala de Mijas",
    "OG_DESCRIPTION": "72 south-facing apartments 2 min from the beach in La Cala de Mijas. Sea views, ground-floor units with garden, penthouses with generous terrace. From € 451,000.",
    "HERO_BG_ALT": "Vitta Marina terrace with sea views La Cala de Mijas",
}
