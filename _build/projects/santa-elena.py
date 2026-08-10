from urllib.parse import quote

PROJECT_NAME = "Santa Elena"
PRICE_FROM = "Vanaf € 374.950"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "santa-elena",
    "TITLE": f"{PROJECT_NAME} Fuengirola — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Santa Elena: 108 moderne appartementen met 1 tot 3 slaapkamers op 750 m van het centrum van Fuengirola. Vanaf € 374.950.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen & Penthouses vlakbij centrum Fuengirola",
    "OG_DESCRIPTION": "Santa Elena: dakterras met zwembad en zonneterras, co-workingruimte en fitnesszaal, 750 m van het centrum van Fuengirola. Vanaf € 374.950.",
    "OG_IMAGE": "https://projects.investinspain.be/images/santa-elena/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/santa-elena/hero.webp",
    "HERO_BG_ALT": "Santa Elena — moderne appartementen vlakbij centrum Fuengirola",
    "HERO_NAME": "Santa Elena",
    "HERO_LOCATION": "FUENGIROLA",
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
    "META_DESCRIPTION": "Santa Elena: 108 modern apartments with 1 to 3 bedrooms, 750 m from the centre of Fuengirola. From € 374,950.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments & Penthouses near Fuengirola centre",
    "OG_DESCRIPTION": "Santa Elena: rooftop pool and sun terrace, coworking space and gym, 750 m from the centre of Fuengirola. From € 374,950.",
    "HERO_BG_ALT": "Santa Elena — modern apartments near Fuengirola centre",
}

# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
