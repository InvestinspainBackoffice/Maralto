from urllib.parse import quote

PROJECT_NAME = "Sphere Sotogrande"
PRICE_FROM = "Vanaf € 1.409.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "sphere",
    "TITLE": f"{PROJECT_NAME} — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Sphere Sotogrande: 33 appartementen en penthouses 2-3-4 slaapkamers met panoramisch natuurzicht. Terrassen tot 260m², privétuinen tot 155m², hotel-achtige diensten. Vanaf € 1.409.000.",
    "OG_TITLE": f"{PROJECT_NAME} · 33 woningen panoramisch uitzicht terrassen tot 260m²",
    "OG_DESCRIPTION": "33 imposante appartementen en penthouses 2-3-4 slaapkamers in Sotogrande. Panoramisch uitzicht, terrassen tot 260m², tuinen tot 155m², hotelachtige diensten. Vanaf € 1.409.000.",
    "OG_IMAGE": "https://projects.investinspain.be/images/sphere/hero.webp",
    "HERO_BG": "https://projects.investinspain.be/images/sphere/hero.webp",
    "HERO_BG_ALT": "Sphere Sotogrande appartementen panoramisch uitzicht natuur",
    "HERO_NAME": PROJECT_NAME,
    "HERO_LOCATION": "SOTOGRANDE, COSTA DEL SOL",
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
    "MAP_LAT": "36.294529434241",
    "MAP_LNG": "-5.3545382028955",
}

DATA_EN = {
    "META_DESCRIPTION": "Sphere Sotogrande: 33 apartments and penthouses 2-3-4 bedrooms with panoramic nature views. Terraces up to 260m², private gardens up to 155m², hotel-like services. From € 1,409,000.",
    "OG_TITLE": f"{PROJECT_NAME} · 33 homes panoramic views terraces up to 260m²",
    "OG_DESCRIPTION": "33 impressive apartments and penthouses 2-3-4 bedrooms in Sotogrande. Panoramic views, terraces up to 260m², gardens up to 155m², hotel-like services. From € 1,409,000.",
    "HERO_BG_ALT": "Sphere Sotogrande apartments panoramic nature views",
}
