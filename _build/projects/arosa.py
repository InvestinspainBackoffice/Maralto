from urllib.parse import quote

PROJECT_NAME = "Arosa"
PRICE_FROM = "Vanaf € 550.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "arosa",
    "TITLE": f"{PROJECT_NAME} Mijas Costa — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Arosa: 54 appartementen met 1 tot 3 slaapkamers en zeezicht op 500m van het strand in Torrenueva, Mijas Costa. Vanaf €550.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met Zeezicht op 500m van het Strand",
    "OG_DESCRIPTION": "Ontdek Arosa: 54 zuidgerichte appartementen met privé-solarium, frontaal zeezicht, binnen- en buitenzwembad en fitness in Torrenueva, Mijas Costa. Vanaf €550.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/arosa/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/arosa/hero.webp",
    "HERO_BG_ALT": "Arosa — luchtfoto van het complex aan de kust van Torrenueva",
    "HERO_NAME": "AROSA",
    "HERO_LOCATION": "MIJAS COSTA",
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
    "META_DESCRIPTION": "Arosa: 54 apartments with 1 to 3 bedrooms and sea views, 500m from the beach in Torrenueva, Mijas Costa. From €550,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Sea-view Apartments 500m from the Beach",
    "OG_DESCRIPTION": "Discover Arosa: 54 south-facing apartments with a private solarium, frontal sea views, indoor and outdoor pools and a gym in Torrenueva, Mijas Costa. From €550,000.",
    "HERO_BG_ALT": "Arosa — aerial view of the complex on the Torrenueva coastline",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
