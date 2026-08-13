from urllib.parse import quote

PROJECT_NAME = "WaveView"
PRICE_FROM = "Vanaf € 1.750.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "waveview",
    "TITLE": f"{PROJECT_NAME} Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "WaveView: 3 frontline beach villa's in Las Farolas, Mijas Costa. 4 slaapkamers, privézwembad, lift, vloerverwarming, solarium met jacuzzi. Vanaf € 1.750.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline Beach Villa's in Mijas Costa",
    "OG_DESCRIPTION": "WaveView: exclusieve strandvilla's met privézwembad, lift en panoramisch zeezicht nabij Chaparral Golf Club. Vanaf € 1.750.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/waveview/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/waveview/hero.webp",
    "HERO_BG_ALT": "WaveView — frontline beach villa met privézwembad in Mijas Costa",
    "HERO_NAME": "WaveView",
    "HERO_LOCATION": "LAS FAROLAS, MIJAS COSTA",
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
    "META_DESCRIPTION": "WaveView: 3 frontline beach villas in Las Farolas, Mijas Costa. 4 bedrooms, private pool, elevator, underfloor heating, solarium with jacuzzi. From € 1,750,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline Beach Villas in Mijas Costa",
    "OG_DESCRIPTION": "WaveView: exclusive beachfront villas with private pool, elevator and panoramic sea views near Chaparral Golf Club. From € 1,750,000.",
    "HERO_BG_ALT": "WaveView — frontline beach villa with private pool in Mijas Costa",
}

HUB = {
    "NAME": "WaveView",
    "LOCATION": "Mijas Costa",
    "PRICE": "Vanaf € 1.750.000",
    "THUMB": "https://projects.investinspain.be/images/waveview/hero.webp",
    "LAT": 36.531098,
    "LNG": -4.698739,
    "HREF": "/waveview/",
}
