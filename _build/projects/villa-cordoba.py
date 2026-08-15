from urllib.parse import quote

PROJECT_NAME = "Villa Córdoba"
PRICE_FROM = "Vanaf € 1.550.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "villa-cordoba",
    "TITLE": f"{PROJECT_NAME} Mijas Golf — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Villa Córdoba: nieuwbouwvilla's in Andalusische stijl aan Mijas Golf. 4 slaapkamers, weelderig zwembad, aerothermisch, garage met EV-laadpunt, dicht bij Mijas Pueblo. Vanaf € 1.550.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Nieuwbouw Andalusische stijl Mijas Golf 4 slpk",
    "OG_DESCRIPTION": "Nieuwbouwvilla's in Andalusische stijl aan Mijas Golf. 4 slaapkamers, privézwembad, aerothermisch, grote ramen, garage + EV-laadpunt. Dicht bij Mijas Pueblo. Vanaf € 1.550.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/villa-cordoba/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/villa-cordoba/hero.webp",
    "HERO_BG_ALT": "Villa Córdoba nieuwbouwvilla Andalusische stijl Mijas Golf",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "MIJAS GOLF, MIJAS",
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
    "MAP_LAT": "36.560151303259",
    "MAP_LNG": "-4.670458414978",
}

DATA_EN = {
    "META_DESCRIPTION": "Villa Córdoba: new-build villas in Andalusian style at Mijas Golf. 4 bedrooms, luxury pool, aerothermal heating, garage with EV charger, close to Mijas Pueblo. From € 1,550,000.",
    "OG_TITLE": f"{PROJECT_NAME} · New build Andalusian style Mijas Golf 4 bed",
    "OG_DESCRIPTION": "New-build villas in Andalusian style at Mijas Golf. 4 bedrooms, private pool, aerothermal, large windows, garage + EV charger. Close to Mijas Pueblo. From € 1,550,000.",
    "HERO_BG_ALT": "Villa Córdoba new-build villa Andalusian style Mijas Golf",
}
