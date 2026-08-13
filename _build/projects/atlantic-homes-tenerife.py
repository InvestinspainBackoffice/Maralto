from urllib.parse import quote

PROJECT_NAME = "Atlantic Homes"
PRICE_FROM = "Vanaf € 500.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "atlantic-homes-tenerife",
    "TITLE": f"{PROJECT_NAME} Tenerife — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Atlantic Homes: moderne appartementen met uitzicht op de Atlantische Oceaan in Costa Adeje, Tenerife. 1-2-3 slaapkamers, op wandelafstand van het strand. Vanaf € 500.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Appartementen met Atlantisch uitzicht in Costa Adeje, Tenerife",
    "OG_DESCRIPTION": "Atlantic Homes in Costa Adeje, Tenerife: eigentijdse appartementen met 1-2-3 slaapkamers, panoramisch zicht op de Atlantische Oceaan, zwembad en op loopafstand van het strand. Vanaf € 500.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/atlantic-homes-tenerife/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/atlantic-homes-tenerife/hero.webp",
    "HERO_BG_ALT": "Atlantic Homes Tenerife exterieur appartementen Costa Adeje",
    "HERO_NAME": "Atlantic Homes",
    "HERO_LOCATION": "COSTA ADEJE, TENERIFE",
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
    "META_DESCRIPTION": "Atlantic Homes: modern apartments with Atlantic Ocean views in Costa Adeje, Tenerife. 1-2-3 bedrooms, walking distance to the beach. From € 500,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Apartments with Atlantic views in Costa Adeje, Tenerife",
    "OG_DESCRIPTION": "Atlantic Homes in Costa Adeje, Tenerife: contemporary apartments with 1-2-3 bedrooms, panoramic views over the Atlantic Ocean, pool and walking distance to the beach. From € 500,000.",
    "HERO_BG_ALT": "Atlantic Homes Tenerife exterior apartments Costa Adeje",
}
