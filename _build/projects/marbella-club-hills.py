from urllib.parse import quote

PROJECT_NAME = "Marbella Club Hills"
PRICE_FROM = "Vanaf € 830.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "marbella-club-hills",
    "TITLE": f"{PROJECT_NAME} Benahavís — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Marbella Club Hills: 17 luxevilla's en 110 villa-appartementen van Marbella Club Group, aan de voet van Marbella Club Golf in Benahavís. Vanaf €830.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villa's & Villa-appartementen",
    "OG_DESCRIPTION": "Ontdek Marbella Club Hills: dezelfde stijl, elegantie en luxe als Marbella Club & Puente Romano, met gratis golflidmaatschap en toegang tot het ruitersportcentrum. Vanaf €830.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2022/10/2022.10.04-Sofie-Marbella-Club-Hills-Opportunity-Apartment-P11.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2022/10/2022.10.04-Sofie-Marbella-Club-Hills-Opportunity-Apartment-P11.jpg",
    "HERO_BG_ALT": "Marbella Club Hills — terras met eettafel en zicht op de bergen",
    "HERO_NAME": "MARBELLA CLUB HILLS",
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
    "META_DESCRIPTION": "Marbella Club Hills: 17 luxury villas and 110 villa-apartments by Marbella Club Group, at the foot of Marbella Club Golf in Benahavís. From €830,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Villas & Villa-Apartments",
    "OG_DESCRIPTION": "Discover Marbella Club Hills: the same style, elegance and luxury as Marbella Club & Puente Romano, with free golf membership and access to the equestrian centre. From €830,000.",
    "HERO_BG_ALT": "Marbella Club Hills — terrace with dining table and mountain views",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Benahavís",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2022/10/2022.10.04-Sofie-Marbella-Club-Hills-Opportunity-Apartment-P11.jpg",
    "LAT": 36.5145,
    "LNG": -5.0180,
    "HREF": "/marbella-club-hills/",
}
