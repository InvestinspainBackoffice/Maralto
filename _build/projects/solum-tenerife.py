from urllib.parse import quote

PROJECT_NAME = "Solum"
PRICE_FROM = "Vanaf € 987.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "solum-tenerife",
    "TITLE": f"{PROJECT_NAME} Tenerife — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Solum Tenerife: frontline luxeappartementen met spectaculair zicht op de Atlantische Oceaan en La Gomera. 1-4 slaapkamers, sauna, wellness en 50m van het strand. Vanaf € 987.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline appartementen met Atlantisch uitzicht in Tenerife",
    "OG_DESCRIPTION": "Solum in Tenerife: exclusieve frontline appartementen met 1 tot 4 slaapkamers en spectaculair uitzicht op de Atlantische Oceaan en het eiland La Gomera. Sauna, Turks bad, fitness en wellness. Op 50m van het strand. Vanaf € 987.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/solum-tenerife/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/solum-tenerife/hero.webp",
    "HERO_BG_ALT": "Solum Tenerife frontline appartementen exterieur Atlantische Oceaan zicht",
    "HERO_NAME": "Solum",
    "HERO_LOCATION": "GUÍA DE ISORA, TENERIFE",
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
    "META_DESCRIPTION": "Solum Tenerife: frontline luxury apartments with spectacular views over the Atlantic Ocean and La Gomera. 1-4 bedrooms, sauna, wellness and 50m from the beach. From € 987,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Frontline apartments with Atlantic views in Tenerife",
    "OG_DESCRIPTION": "Solum in Tenerife: exclusive frontline apartments with 1 to 4 bedrooms and spectacular views over the Atlantic Ocean and the island of La Gomera. Sauna, Turkish bath, fitness and wellness. 50m from the beach. From € 987,000.",
    "HERO_BG_ALT": "Solum Tenerife frontline apartments exterior Atlantic Ocean views",
}
