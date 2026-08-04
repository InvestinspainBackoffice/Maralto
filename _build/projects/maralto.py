from urllib.parse import quote

# Maralto is het vlaggenschip en leeft op de root van de site ("/"), niet
# onder een eigen submap. generate.py schrijft daarom naar ROOT/index.html
# in plaats van ROOT/maralto/index.html wanneer SLUG == "maralto".

PROJECT_NAME = "Maralto"
PRICE_FROM = "Vanaf € 460.000"
# Letterlijk behouden zoals de pagina hem al jarenlang gebruikte (incl. "Estepona"),
# in plaats van afgeleid van PROJECT_NAME zoals bij andere projecten.
WA_MESSAGE = "Hallo, ik heb interesse in Maralto Estepona. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "maralto",
    "TITLE": "Maralto Estepona — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Maralto Estepona: Moderne appartementen met panoramisch zee- en bergzicht aan de Costa del Sol. Vanaf €460.000.",
    "OG_TITLE": "Maralto Estepona — Moderne Appartementen",
    "OG_DESCRIPTION": "Ontdek Maralto: resort-style wonen in Estepona met panoramisch uitzicht, zwembaden, spa en meer. Vanaf €460.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/08/Maralto-Estepona-9.webp",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/08/Maralto-Estepona-9.webp",
    "HERO_BG_ALT": "Maralto Estepona — moderne architectuur met gebogen balkons en mediterrane tuinen",
    "HERO_NAME": "MARALTO",
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

# Engelse overrides - enkel de velden die echt vertaald moeten worden.
# Alles wat hier niet in staat (afbeeldingen, prijs, coördinaten, agent-
# gegevens, ...) wordt gewoon van DATA overgenomen.
DATA_EN = {
    "META_DESCRIPTION": "Maralto Estepona: Modern apartments with panoramic sea and mountain views on the Costa del Sol. From €460.000.",
    "OG_TITLE": "Maralto Estepona — Modern Apartments",
    "OG_DESCRIPTION": "Discover Maralto: resort-style living in Estepona with panoramic views, swimming pools, spa and more. From €460.000.",
    "HERO_BG_ALT": "Maralto Estepona — modern architecture with curved balconies and Mediterranean gardens",
    "WA_MESSAGE": "Hello, I'm interested in Maralto Estepona. Could I receive more information?",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Estepona",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/wp-content/uploads/2026/08/Maralto-Estepona-9.webp",
    "LAT": 36.425704,
    "LNG": -5.1626803,
    "HREF": "/maralto/",
}
