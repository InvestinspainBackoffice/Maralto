from urllib.parse import quote

PROJECT_NAME = "Isidora Living"
PRICE_FROM = "Vanaf € 759.650"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "isidora-living",
    "TITLE": f"{PROJECT_NAME} Centrum Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Isidora Living: 102 appartementen en penthouses 1-3 slaapkamers in het centrum van Estepona. Co-working, fitness, zwembaden, groene zones, speelzone. Vanaf € 759.650.",
    "OG_TITLE": f"{PROJECT_NAME} · 102 woningen centrum Estepona",
    "OG_DESCRIPTION": "102 appartementen en penthouses 1-3 slaapkamers in het centrum van Estepona, op wandelafstand van het strand. Co-working, fitness, zwembaden. Vanaf € 759.650.",
    "OG_IMAGE": "https://projects.investinspain.be/images/isidora-living/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/isidora-living/hero.webp",
    "HERO_BG_ALT": "Isidora Living appartementen gemeenschappelijke zones Estepona centrum",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "CENTRUM ESTEPONA",
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
    "MAP_LAT": "36.422935523448",
    "MAP_LNG": "-5.1543836993471",
}

DATA_EN = {
    "META_DESCRIPTION": "Isidora Living: 102 apartments and penthouses 1-3 bedrooms in Estepona town centre. Co-working, fitness, pools, green areas, play zone. From € 759,650.",
    "OG_TITLE": f"{PROJECT_NAME} · 102 homes Estepona centre",
    "OG_DESCRIPTION": "102 apartments and penthouses 1-3 bedrooms in Estepona town centre, walking distance from the beach. Co-working, fitness, pools. From € 759,650.",
    "HERO_BG_ALT": "Isidora Living apartments communal areas Estepona centre",
}
