from urllib.parse import quote

PROJECT_NAME = "Villa Halo"
PRICE_FROM = "Vanaf € 9.800.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "villa-halo",
    "TITLE": f"{PROJECT_NAME} SOTOGRANDE — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Villa Halo Sotogrande: ultra-moderne designvilla met 5 slaapkamers, privézwembad en golf- & zeezicht in La Reserva de Sotogrande. Energieneutraal. Vanaf € 9.800.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-moderne designvilla in La Reserva de Sotogrande",
    "OG_DESCRIPTION": "Energieneutrale luxevilla met 5 slaapkamers, privézwembad van 93m² en panoramisch golf- en zeezicht in La Reserva de Sotogrande.",
    "OG_IMAGE": "https://projects.investinspain.be/images/villa-halo/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/villa-halo/hero.webp",
    "HERO_BG_ALT": "Villa Halo — ultra-moderne designvilla met zeezicht in La Reserva de Sotogrande",
    "HERO_NAME": "Villa Halo",
    "HERO_LOCATION": "SOTOGRANDE",
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
    "META_DESCRIPTION": "Villa Halo Sotogrande: ultra-modern design villa with 5 bedrooms, private pool and golf & sea views in La Reserva de Sotogrande. Energy-neutral. From € 9,800,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Ultra-modern design villa in La Reserva de Sotogrande",
    "OG_DESCRIPTION": "Energy-neutral luxury villa with 5 bedrooms, 93m² private pool and panoramic golf and sea views in La Reserva de Sotogrande.",
    "HERO_BG_ALT": "Villa Halo — ultra-modern design villa with sea views in La Reserva de Sotogrande",
}
# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
