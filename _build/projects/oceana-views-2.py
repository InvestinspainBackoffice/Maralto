from urllib.parse import quote

PROJECT_NAME = "Oceana Views"
PRICE_FROM = "Vanaf € 460.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "oceana-views-2",
    "TITLE": f"{PROJECT_NAME} Cancelada — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Oceana Views: gemeubeld appartement 2 slaapkamers met zeezicht en privéterras in Cancelada. Turn-key klaar, gedeeld zwembad en garage. Vanaf €460.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Zeezicht & Turn-Key in Cancelada",
    "OG_DESCRIPTION": "Ontdek Oceana Views: volledig gemeubeld appartement 2 slaapkamers met prachtig zeezicht en privéterras in Cancelada. Gedeeld zwembad, airco en garage inbegrepen. Vanaf €460.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/oceana-views-2/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/oceana-views-2/hero.webp",
    "HERO_BG_ALT": "Oceana Views — appartement met zeezicht in Cancelada",
    "HERO_NAME": "OCEANA VIEWS",
    "HERO_LOCATION": "CANCELADA",
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
    "META_DESCRIPTION": "Oceana Views: furnished 2-bedroom apartment with sea views and private terrace in Cancelada. Turn-key ready, shared pool and garage. From €460,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Sea Views & Turn-Key in Cancelada",
    "OG_DESCRIPTION": "Discover Oceana Views: fully furnished 2-bedroom apartment with beautiful sea views and private terrace in Cancelada. Shared pool, air conditioning and garage included. From €460,000.",
    "HERO_BG_ALT": "Oceana Views — apartment with sea views in Cancelada",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
