from urllib.parse import quote

PROJECT_NAME = "Noura"
PRICE_FROM = "Vanaf € 6.790.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "noura",
    "TITLE": f"{PROJECT_NAME} Golden Mile, Marbella — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Noura: 3 unieke villa's op de Golden Mile van Marbella. Infinity pool, privélift, wijnkelder, domotica en Miele-keuken. Vanaf € 6.790.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Villa's op de Golden Mile, Marbella",
    "OG_DESCRIPTION": "Noura: villa's Moon, Sky en Sun boven Puente Romano met panoramisch zeezicht, jacuzzi en Sonos-audiosysteem. Vanaf € 6.790.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/noura/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/noura/hero.webp",
    "HERO_BG_ALT": "Noura — luxe villa met infinity pool op de Golden Mile in Marbella",
    "HERO_NAME": "Noura",
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
    "META_DESCRIPTION": "Noura: 3 unique villas on Marbella's Golden Mile. Infinity pool, private lift, wine cellar, domotics and Miele kitchen. From € 6,790,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Villas on the Golden Mile, Marbella",
    "OG_DESCRIPTION": "Noura: villas Moon, Sky and Sun above Puente Romano with panoramic sea views, jacuzzi and Sonos audio system. From € 6,790,000.",
    "HERO_BG_ALT": "Noura — luxury villa with infinity pool on the Golden Mile in Marbella",
}

HUB = {
    "NAME": "Noura",
    "LOCATION": "Marbella",
    "PRICE": "Vanaf € 6.790.000",
    "THUMB": "https://projects.investinspain.be/images/noura/hero.webp",
    "LAT": 36.509524,
    "LNG": -4.931563,
    "HREF": "/noura/",
}
