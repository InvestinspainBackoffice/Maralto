from urllib.parse import quote

PROJECT_NAME = "Eagle Hills"
PRICE_FROM = "Vanaf € 365.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "eagle-hills",
    "TITLE": f"{PROJECT_NAME} Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Eagle Hills Estepona: luxe appartementen met panoramisch zeezicht, sky pool, sauna, gym en privébioscoop. Gated resort-achtig complex. Vanaf €365.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Appartementen met Zeezicht",
    "OG_DESCRIPTION": "Ontdek Eagle Hills: exclusieve appartementen met cascaderende terrassen, panora misch zeezicht, sky infinity pool, spa en wellness. Resort-achtig gated complex in Estepona. Vanaf €365.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/eagle-hills/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/eagle-hills/hero.webp",
    "HERO_BG_ALT": "Eagle Hills — gevelaanzicht bij zonsondergang met cascaderende terrassen",
    "HERO_NAME": "EAGLE HILLS",
    "HERO_LOCATION": "ESTEPONA",
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
    "META_DESCRIPTION": "Eagle Hills Estepona: luxury apartments with panoramic sea views, sky pool, sauna, gym and private cinema. Gated resort-like complex. From €365,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Apartments with Sea Views",
    "OG_DESCRIPTION": "Discover Eagle Hills: exclusive apartments with cascading terraces, panoramic sea views, sky infinity pool, spa and wellness. Resort-like gated complex in Estepona. From €365,000.",
    "HERO_BG_ALT": "Eagle Hills — facade view at sunset with cascading terraces",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
