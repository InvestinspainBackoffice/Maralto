from urllib.parse import quote

PROJECT_NAME = "Villa Syzygy"
PRICE_FROM = "€ 2.450.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "villa-syzygy",
    "TITLE": f"{PROJECT_NAME} — Exclusieve villa tussen Estepona & Marbella · INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Villa Syzygy: exclusieve villa nabij Cancelada met privézwembad, sauna, home cinema, bar en biljart. 5 slaapkamers. Prijs: € 2.450.000.",
    "OG_TITLE": f"{PROJECT_NAME} · Exclusieve villa Estepona–Marbella",
    "OG_DESCRIPTION": "Luxueuze villa nabij Cancelada met wellness-verdieping (sauna, home cinema, bar), privézwembad en 5 slaapkamers. Tussen Estepona en Marbella.",
    "OG_IMAGE": "https://projects.investinspain.be/images/villa-syzygy/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/villa-syzygy/hero.webp",
    "HERO_BG_ALT": "Villa Syzygy zwembad en terras tussen Estepona en Marbella",
    "HERO_VIDEO_ID": "aDkwabDGrcc",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "CANCELADA, ESTEPONA",
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
    "MAP_LAT": "36.4677714",
    "MAP_LNG": "-5.056617",
}

DATA_EN = {
    "META_DESCRIPTION": "Villa Syzygy: exclusive villa near Cancelada with private pool, sauna, home cinema, bar and billiards. 5 bedrooms. Price: € 2,450,000.",
    "OG_TITLE": f"{PROJECT_NAME} · Exclusive villa Estepona–Marbella",
    "OG_DESCRIPTION": "Luxury villa near Cancelada with wellness floor (sauna, home cinema, bar), private pool and 5 bedrooms. Between Estepona and Marbella.",
    "HERO_BG_ALT": "Villa Syzygy pool and terrace between Estepona and Marbella",
}
