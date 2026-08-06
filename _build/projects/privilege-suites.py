from urllib.parse import quote

PROJECT_NAME = "Privilege Suites"
PRICE_FROM = "Vanaf € 620.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "privilege-suites",
    "TITLE": f"{PROJECT_NAME} CASARES — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Privilege Suites Casares: 15 luxe appartementen en penthouses van 129-252m², op 5 minuten stap van het strand. Privézwembad, solarium en zeezicht. Vanaf € 620.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe appartementen & penthouses op 5 min van het strand in Casares",
    "OG_DESCRIPTION": "15 ruime residenties met privétuinen, brede terrassen en duplex penthouses met privézwembad, op loopafstand van het strand in Casares.",
    "OG_IMAGE": "https://projects.investinspain.be/images/privilege-suites/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/privilege-suites/hero.webp",
    "HERO_BG_ALT": "Privilege Suites — luxe appartementencomplex met zeezicht in Casares",
    "HERO_NAME": "Privilege Suites",
    "HERO_LOCATION": "CASARES",
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
    "META_DESCRIPTION": "Privilege Suites Casares: 15 luxury apartments and penthouses of 129-252m², a 5-minute walk from the beach. Private pool, solarium and sea views. From € 620,000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury apartments & penthouses 5 min from the beach in Casares",
    "OG_DESCRIPTION": "15 spacious residences with private gardens, wide terraces and duplex penthouses with private pool, within walking distance of the beach in Casares.",
    "HERO_BG_ALT": "Privilege Suites — luxury apartment complex with sea views in Casares",
}
# NOTE: geen HUB-dict - dit project komt (voorlopig) niet op de projectenoverzichtspagina
