from urllib.parse import quote

PROJECT_NAME = "Nalu Suites"
PRICE_FROM = "Vanaf € 560.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "nalu-suites",
    "TITLE": f"{PROJECT_NAME} Casares — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Nalu Suites: 144 woningen in Casares (Costa del Sol) in 3 fases met 2-3 slaapkamers, spa en zeezicht. Vanaf € 560.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Casares",
    "OG_DESCRIPTION": "144 woningen in 3 fases met spa, zeezicht en pools in Casares.",
    "OG_IMAGE": "https://projects.investinspain.be/images/nalu-suites/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/nalu-suites/hero.webp",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Appartementen in Casares",
    "HERO_NAME": "Nalu Suites",
    "HERO_LOCATION": "CASARES",
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
    "META_DESCRIPTION": "Nalu Suites: 144 homes in Casares (Costa del Sol) in 3 phases with 2-3 bedrooms, spa and sea views. From € 560,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in Casares",
    "OG_DESCRIPTION": "144 homes in 3 phases with spa, sea views and pools in Casares.",
    "HERO_BG_ALT": f"{PROJECT_NAME} — Apartments in Casares",
}

HUB = {
    "NAME": "Nalu Suites",
    "LOCATION": "Casares",
    "PRICE": "Vanaf € 560.000",
    "THUMB": "https://projects.investinspain.be/images/nalu-suites/hero.webp",
    "LAT": 36.398431,
    "LNG": -5.214275,
    "HREF": "/nalu-suites/",
}
