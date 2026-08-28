from urllib.parse import quote

PROJECT_NAME = "Palo Alto"
PRICE_FROM = "Vanaf € 795.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "palo-alto",
    "TITLE": f"{PROJECT_NAME} Ojén — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Palo Alto: exclusieve heuveltop community op 50 hectare in de bergen van Ojén, Marbella. Ononderbroken zicht op de Middellandse Zee. Vanaf €795.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen, Penthouses & Villa's",
    "OG_DESCRIPTION": "Ontdek Palo Alto: state-of-the-art architectuur van Villarroel Torrico, met health club, paardensportfaciliteiten en ononderbroken zeezicht in de bergen van Ojén. Vanaf €795.000.",
    "OG_IMAGE": "https://paloalto.immo/wp-content/uploads/2021/08/POOL-VIEW_12000PIX.-background-modified-2.jpg",
    "HERO_BG": "https://paloalto.immo/wp-content/uploads/2021/08/POOL-VIEW_12000PIX.-background-modified-2.jpg",
    "HERO_BG_ALT": "Palo Alto — infinity zwembad met palmbomen en zeezicht",
    "HERO_NAME": "PALO ALTO",
    "HERO_LOCATION": "OJÉN",
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
    "META_DESCRIPTION": "Palo Alto: an exclusive 50-hectare hilltop community in the mountains of Ojén, Marbella. Uninterrupted views of the Mediterranean Sea. From €795,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments, Penthouses & Villas",
    "OG_DESCRIPTION": "Discover Palo Alto: state-of-the-art architecture by Villarroel Torrico, with a health club, equestrian facilities and uninterrupted sea views in the mountains of Ojén. From €795,000.",
    "HERO_BG_ALT": "Palo Alto — infinity pool with palm trees and sea view",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Ojén",
    "PRICE": PRICE_FROM,
    "THUMB": "https://projects.investinspain.be/images/palo-alto/thumb.webp",
    "LAT": 36.54154,
    "LNG": -4.86154,
    "HREF": "/palo-alto/",
}
