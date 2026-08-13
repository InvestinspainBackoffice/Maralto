from urllib.parse import quote

PROJECT_NAME = "4our Villas"
PRICE_FROM = "Vanaf € 4.850.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "4our-villas",
    "TITLE": f"{PROJECT_NAME} Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "4our Villas: 4 exclusieve privévilla's op de Golden Mile in Marbella met eigen zwembad. 900m van strand. Vanaf € 4.850.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's in Marbella",
    "OG_DESCRIPTION": "4 exclusieve privévilla's op de Golden Mile in Marbella, elk met eigen zwembad.",
    "OG_IMAGE": "https://projects.investinspain.be/images/4our-villas/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/4our-villas/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villa's in Marbella",
    "HERO_NAME": "4our Villas",
    "HERO_LOCATION": "MARBELLA",
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
    "META_DESCRIPTION": "4our Villas: 4 exclusive private villas on the Golden Mile in Marbella with private pool. 900m from the beach. From € 4,850,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas in Marbella",
    "OG_DESCRIPTION": "4 exclusive private villas on the Golden Mile in Marbella, each with private pool.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Villas in Marbella",
}

HUB = {
    "NAME": "4our Villas",
    "LOCATION": "Marbella",
    "PRICE": "Vanaf € 4.850.000",
    "THUMB": "https://projects.investinspain.be/images/4our-villas/hero.webp",
    "LAT": 36.517026,
    "LNG": -4.935211,
    "HREF": "/4our-villas/",
}
