from urllib.parse import quote

PROJECT_NAME = "Velaya Villa"
PRICE_FROM = "Vanaf € 4.500.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "velaya-villa",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Velaya Villa: 2 luxueuze strandvilla's nabij Estepona. 4 slaapkamers, ~1.000 m², infinity pool, jacuzzi, padel, tennis, 100 m van het strand. Vanaf € 4.500.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Beachfront Villa's nabij Estepona",
    "OG_DESCRIPTION": "Velaya Villa: exclusieve villa's van ~1.000 m² met infinity pool, buitenkeuken, padel- en tennisbaan, op 100 m van het strand. Vanaf € 4.500.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/velaya-villa/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/velaya-villa/hero.webp",
    "HERO_BG_ALT": "Velaya Villa — luxueuze beachfront villa nabij Estepona",
    "HERO_NAME": "Velaya Villa",
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
    "META_DESCRIPTION": "Velaya Villa: 2 luxury beachfront villas near Estepona. 4 bedrooms, ~1,000 m², infinity pool, jacuzzi, padel, tennis, 100 m from the beach. From € 4,500,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Beachfront Villas near Estepona",
    "OG_DESCRIPTION": "Velaya Villa: exclusive villas of ~1,000 m² with infinity pool, outdoor kitchen, padel and tennis court, 100 m from the beach. From € 4,500,000.",
    "HERO_BG_ALT": "Velaya Villa — luxury beachfront villa near Estepona",
}

HUB = {
    "NAME": "Velaya Villa",
    "LOCATION": "Estepona",
    "PRICE": "Vanaf € 4.500.000",
    "THUMB": "https://projects.investinspain.be/images/velaya-villa/hero.webp",
    "LAT": 36.448016,
    "LNG": -5.088088,
    "HREF": "/velaya-villa/",
}
