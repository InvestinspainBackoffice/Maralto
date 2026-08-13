from urllib.parse import quote

PROJECT_NAME = "South Sand"
PRICE_FROM = "Vanaf € 702.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "south-sand",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "South Sand: moderne appartementen en penthouses met zeezicht nabij Estepona. Grote terrassen, communaal zwembad en rustige ligging dicht bij het strand. Vanaf € 702.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met zeezicht en grote terrassen, Estepona",
    "OG_DESCRIPTION": "South Sand nabij Estepona: eigentijdse appartementen en penthouses met zeezicht, ruime terrassen en communale faciliteiten dicht bij het strand. Vanaf € 702.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/south-sand/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/south-sand/hero.webp",
    "HERO_BG_ALT": "South Sand appartementen met zeezicht Estepona",
    "HERO_NAME": "South Sand",
    "HERO_LOCATION": "ESTEPONA, COSTA DEL SOL",
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
    "META_DESCRIPTION": "South Sand: modern apartments and penthouses with sea views near Estepona. Large terraces, communal pool and a quiet setting close to the beach. From € 702,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with sea views and large terraces, Estepona",
    "OG_DESCRIPTION": "South Sand near Estepona: contemporary apartments and penthouses with sea views, spacious terraces and communal amenities close to the beach. From € 702,000.",
    "HERO_BG_ALT": "South Sand apartments with sea views Estepona",
}
