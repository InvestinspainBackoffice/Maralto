from urllib.parse import quote

PROJECT_NAME = "Marbella Club Hills Duplex"
PRICE_FROM = "Vanaf € 995.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "marbella-club-hills-duplex",
    "TITLE": f"{PROJECT_NAME} Benahavís — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Marbella Club Hills Duplex: ruim duplex appartement 3 slaapkamers met groot terras, privétuinen en gemeenschapszwembad in Benahavís. Panoramisch zicht. Vanaf €995.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ruim Duplex met Terras in Benahavís",
    "OG_DESCRIPTION": "Ontdek dit exclusieve duplex appartement in Marbella Club Hills, Benahavís: 3 slaapkamers, groot terras, privétuin, panoramisch berg- en zeezicht. Garage inbegrepen. Vanaf €995.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/marbella-club-hills-duplex/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/marbella-club-hills-duplex/hero.webp",
    "HERO_BG_ALT": "Marbella Club Hills Duplex — luxe complex in groene setting Benahavís",
    "HERO_NAME": "MARBELLA CLUB HILLS DUPLEX",
    "HERO_LOCATION": "BENAHAVÍS",
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
    "META_DESCRIPTION": "Marbella Club Hills Duplex: spacious 3-bedroom duplex apartment with large terrace, private gardens and communal pool in Benahavís. Panoramic views. From €995,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Spacious Duplex with Terrace in Benahavís",
    "OG_DESCRIPTION": "Discover this exclusive duplex apartment in Marbella Club Hills, Benahavís: 3 bedrooms, large terrace, private garden, panoramic mountain and sea views. Garage included. From €995,000.",
    "HERO_BG_ALT": "Marbella Club Hills Duplex — luxury complex in green setting Benahavís",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de
# projectenoverzichtspagina, op uitdrukkelijk verzoek.
