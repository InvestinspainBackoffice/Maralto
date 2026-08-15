from urllib.parse import quote

PROJECT_NAME = "Villa Monte Mayor"
PRICE_FROM = "€ 4.200.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "villa-in-monte-mayor",
    "TITLE": f"{PROJECT_NAME} Benahavís — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Villa Monte Mayor: instapklare luxevilla met 7 slaapkamers in de gated community Monte Mayor, Benahavís. Verwarmde pool, panoramisch berg- en zeezicht, kelderverdieping. € 4.200.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 7 slpk instapklaar gated community Benahavís",
    "OG_DESCRIPTION": "Instapklare luxevilla 7 slaapkamers in Monte Mayor, Benahavís. Verwarmde pool, buiten zithoek vuurplaats, panoramisch berg- en zeezicht, kelder met extra mogelijkheden. € 4.200.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/villa-in-monte-mayor/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/villa-in-monte-mayor/hero.webp",
    "HERO_BG_ALT": "Villa Monte Mayor luxevilla droneview gated community Benahavís",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "MONTE MAYOR, BENAHAVÍS",
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
    "MAP_LAT": "36.49425344623",
    "MAP_LNG": "-5.069591033524",
}

DATA_EN = {
    "META_DESCRIPTION": "Villa Monte Mayor: move-in ready luxury villa with 7 bedrooms in the gated community Monte Mayor, Benahavís. Heated pool, panoramic mountain and sea views, basement. € 4,200,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 7 bed move-in ready gated community Benahavís",
    "OG_DESCRIPTION": "Move-in ready luxury villa 7 bedrooms in Monte Mayor, Benahavís. Heated pool, outdoor fireplace lounge, panoramic mountain and sea views, basement with options. € 4,200,000.",
    "HERO_BG_ALT": "Villa Monte Mayor luxury villa drone view gated community Benahavís",
}
