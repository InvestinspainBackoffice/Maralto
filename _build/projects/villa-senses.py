from urllib.parse import quote

PROJECT_NAME = "Villa Senses"
PRICE_FROM = "€ 3.695.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "villa-senses",
    "TITLE": f"{PROJECT_NAME} Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Villa Senses: instapklare 4-slaapkamer villa in Ibiza-style bij Marbella. Privézwembad, jacuzzi, zeezicht, gym in kelder, vloerverwarming, 5 min strand, 15 min Marbella centrum. € 3.695.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 4 slpk instapklaar Ibiza-style Marbella zeezicht",
    "OG_DESCRIPTION": "Instapklare 4-slaapkamer villa volledig ingericht in Ibiza-style bij Marbella. Privézwembad, jacuzzi, zeezicht, gym, 5 min strand, 15 min Marbella. € 3.695.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/villa-senses/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/villa-senses/hero.webp",
    "HERO_BG_ALT": "Villa Senses luxevilla privézwembad jacuzzi zeezicht Marbella",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "ELVIRIA, MARBELLA",
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
    "MAP_LAT": "36.490378881561",
    "MAP_LNG": "-4.7555279019071",
}

DATA_EN = {
    "META_DESCRIPTION": "Villa Senses: move-in ready 4-bedroom villa in Ibiza style near Marbella. Private pool, jacuzzi, sea views, gym in basement, underfloor heating, 5 min beach, 15 min Marbella centre. € 3,695,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 4 bed move-in ready Ibiza style Marbella sea views",
    "OG_DESCRIPTION": "Move-in ready 4-bedroom villa fully furnished in Ibiza style near Marbella. Private pool, jacuzzi, sea views, gym, 5 min beach, 15 min Marbella. € 3,695,000.",
    "HERO_BG_ALT": "Villa Senses luxury villa private pool jacuzzi sea views Marbella",
}
