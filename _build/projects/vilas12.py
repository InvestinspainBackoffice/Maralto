from urllib.parse import quote

PROJECT_NAME = "Vilas12"
PRICE_FROM = "Vanaf € 7.900.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "vilas12",
    "TITLE": f"{PROJECT_NAME} Golden Mile Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Vilas12: 12 exclusieve villa's op de Golden Mile in Marbella. Villa 9 — 4 slaapkamers, privélift, privézwembad op dakterras, interieur door Pedro Peña. Vanaf € 7.900.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve villa's op de Golden Mile, Marbella",
    "OG_DESCRIPTION": "Vilas12: 12 unieke villa's met zeezicht op de Golden Mile. Villa 9 — 4 verdiepingen, Gaggenau-keuken, rooftop pool, interieur door Pedro Peña. Instapklaar.",
    "OG_IMAGE": "https://projects.investinspain.be/images/vilas12/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/vilas12/hero.webp",
    "HERO_BG_ALT": "Exterieur van Vilas12 villa op de Golden Mile in Marbella",
    "HERO_NAME": "Vilas12",
    "HERO_LOCATION": "GOLDEN MILE, MARBELLA",
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
    "META_DESCRIPTION": "Vilas12: 12 exclusive villas on the Golden Mile in Marbella. Villa 9 — 4 bedrooms, private lift, private rooftop pool, interior by Pedro Peña. From € 7,900,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive villas on the Golden Mile, Marbella",
    "OG_DESCRIPTION": "Vilas12: 12 unique villas with sea views on the Golden Mile. Villa 9 — 4 floors, Gaggenau kitchen, rooftop pool, interiors by Pedro Peña. Move-in ready.",
    "HERO_BG_ALT": "Exterior of Vilas12 villa on the Golden Mile in Marbella",
}

HUB = {
    "NAME": "Vilas12",
    "LOCATION": "Marbella",
    "PRICE": "Vanaf € 7.900.000",
    "THUMB": "https://projects.investinspain.be/images/vilas12/hero.webp",
    "LAT": 36.502023,
    "LNG": -4.935312,
    "HREF": "/vilas12/",
}
