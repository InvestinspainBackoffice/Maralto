from urllib.parse import quote

PROJECT_NAME = "Ocho de Oro"
PRICE_FROM = "Vanaf € 11.500.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "ocho-de-oro",
    "TITLE": f"{PROJECT_NAME} Nueva Andalucía — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Ocho de Oro: exclusieve collectie van 8 villa's met interieur van Versace Home, in de heuvels van Nueva Andalucía, Marbella. Vanaf €11.500.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's met Versace Home Interieur",
    "OG_DESCRIPTION": "Ontdek Ocho de Oro: 8 villa's waar mediterrane schoonheid samenkomt met de couture-signatuur van Versace Home, in de rustige heuvels van Nueva Andalucía. Vanaf €11.500.000.",
    "OG_IMAGE": "https://marbellaprestige.realestate/wp-content/uploads/2025/09/Exterior-Villa-1_Ocho-de-Oro.webp",
    "HERO_BG": "https://marbellaprestige.realestate/wp-content/uploads/2025/09/Exterior-Villa-1_Ocho-de-Oro.webp",
    "HERO_BG_ALT": "Ocho de Oro — villa met zwembad en zeezicht tussen palmbomen",
    "HERO_NAME": "OCHO DE ORO",
    "HERO_LOCATION": "NUEVA ANDALUCÍA",
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
    "META_DESCRIPTION": "Ocho de Oro: an exclusive collection of 8 villas with interior design by Versace Home, in the hills of Nueva Andalucía, Marbella. From €11,500,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas with Versace Home Interiors",
    "OG_DESCRIPTION": "Discover Ocho de Oro: 8 villas where Mediterranean beauty meets the couture signature of Versace Home, in the tranquil hills of Nueva Andalucía. From €11,500,000.",
    "HERO_BG_ALT": "Ocho de Oro — villa with swimming pool and sea view among palm trees",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Nueva Andalucía",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/ocho-de-oro/thumb.webp",
    "LAT": 36.5238841,
    "LNG": -4.9696537,
    "HREF": "/ocho-de-oro/",
}
