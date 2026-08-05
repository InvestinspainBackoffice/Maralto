from urllib.parse import quote

PROJECT_NAME = "Oceana Views"
PRICE_FROM = "€ 460.000 Incl. meubels"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "oceana-views",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Oceana Views: instapklaar 2 slaapkamer appartement met zeezicht in Cancelada, Estepona. €460.000 incl. meubels.",
    "OG_TITLE": f"{PROJECT_NAME} — Instapklaar Appartement met Zeezicht",
    "OG_DESCRIPTION": "Ontdek Oceana Views: een volledig ingericht appartement met privéterras, zeezicht en gemeenschappelijk zwembad in Norte de Cancelada. €460.000 incl. meubels.",
    "OG_IMAGE": "https://projects.investinspain.be/images/oceana-views/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/oceana-views/hero.webp",
    "HERO_BG_ALT": "Oceana Views — leefruimte met open keuken en zicht op het terras",
    "HERO_NAME": "OCEANA VIEWS",
    "HERO_LOCATION": "CANCELADA",
    "HERO_PRICE": PRICE_FROM,
    "PRICE_FROM": PRICE_FROM,
    "PRICE_LABEL": "",
    "PRICE_AMOUNT": PRICE_FROM,
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
    "META_DESCRIPTION": "Oceana Views: move-in ready 2-bedroom apartment with sea views in Cancelada, Estepona. €460,000 incl. furniture.",
    "OG_TITLE": f"{PROJECT_NAME} — Move-in Ready Apartment with Sea Views",
    "OG_DESCRIPTION": "Discover Oceana Views: a fully furnished apartment with a private terrace, sea views and a communal pool in Norte de Cancelada. €460,000 incl. furniture.",
    "HERO_BG_ALT": "Oceana Views — living area with open kitchen and terrace view",
    "PRICE_FROM": "€ 460,000 Furniture incl.",
    "HERO_PRICE": "€ 460,000 Furniture incl.",
    "PRICE_AMOUNT": "€ 460,000 Furniture incl.",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
