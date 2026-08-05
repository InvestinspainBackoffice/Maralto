from urllib.parse import quote

PROJECT_NAME = "Almazara Gardens"
PRICE_FROM = "Vanaf € 460.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "almazara-gardens",
    "TITLE": f"{PROJECT_NAME} Istán — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Almazara Gardens: moderne appartementen in Istán met bergzicht, zwembaden en energiëfficiëncy A-rating. Premium afwerking met Bosch, Saloni, Jacob Delafon. Vanaf €460.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen in Natuurlijk Paradijs",
    "OG_DESCRIPTION": "Ontdek Almazara Gardens: exclusieve appartementen met panoramisch bergzicht en water, premium afwerking, zwembaden en zonnepanelen. Energiëfficiëncy A-rating in Istán. Vanaf €460.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/almazara-gardens/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/almazara-gardens/hero.webp",
    "HERO_BG_ALT": "Almazara Gardens — gevelaanzicht van het complex in bergachtige omgeving",
    "HERO_NAME": "ALMAZARA GARDENS",
    "HERO_LOCATION": "ISTÁN",
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
    "META_DESCRIPTION": "Almazara Gardens: modern apartments in Istán with mountain views, pools and A-energy rating. Premium finishes with Bosch, Saloni, Jacob Delafon. From €460,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments in a Natural Paradise",
    "OG_DESCRIPTION": "Discover Almazara Gardens: exclusive apartments with panoramic mountain and water views, premium finishes, pools and solar panels. A-energy rating in Istán. From €460,000.",
    "HERO_BG_ALT": "Almazara Gardens — facade view of the complex in mountainous setting",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
