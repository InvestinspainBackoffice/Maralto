from urllib.parse import quote

PROJECT_NAME = "Tierra Viva"
PRICE_FROM = "Vanaf € 8.236.532"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "tierra-viva",
    "TITLE": f"{PROJECT_NAME} Benahavís — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Tierra Viva: 53 exclusieve villa's geïnspireerd door Automobili Lamborghini in Benahavís. Privézwembad, sauna, infinity pool en gated community. Vanaf € 8.236.532.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusieve Lamborghini-geïnspireerde villa's in Benahavís",
    "OG_DESCRIPTION": "Tierra Viva in Benahavís: 53 ultra-luxe villa's met Lamborghini-design, privé infinity-zwembad, sauna, Turks bad en 24/7 beveiligde gated community nabij de golfbanen van Marbella. Vanaf € 8.236.532.",
    "OG_IMAGE": "https://projects.investinspain.be/images/tierra-viva/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/tierra-viva/hero.webp",
    "HERO_BG_ALT": "Tierra Viva Benahavís luchtfoto exclusieve villa's",
    "HERO_NAME": "Tierra Viva",
    "HERO_LOCATION": "BENAHAVÍS, MARBELLA",
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
    "META_DESCRIPTION": "Tierra Viva: 53 exclusive villas inspired by Automobili Lamborghini in Benahavís. Private pool, sauna, infinity pool and gated community. From € 8,236,532.",
    "OG_TITLE": f"{PROJECT_NAME} — Exclusive Lamborghini-inspired villas in Benahavís",
    "OG_DESCRIPTION": "Tierra Viva in Benahavís: 53 ultra-luxury villas with Lamborghini-inspired design, private infinity pool, sauna, Turkish bath and 24/7 gated community near Marbella's golf courses. From € 8,236,532.",
    "HERO_BG_ALT": "Tierra Viva Benahavís aerial view exclusive villas",
}
