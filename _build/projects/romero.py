from urllib.parse import quote

PROJECT_NAME = "Romero"
PRICE_FROM = "Vanaf € 1.150.000"
WA_MESSAGE = f"Hallo, ik heb interesse in {PROJECT_NAME}. Kan ik meer informatie ontvangen?"

DATA = {
    "SLUG": "romero",
    "TITLE": f"{PROJECT_NAME} Real de la Quinta — INVESTINSPAIN.BE",
    "META_DESCRIPTION": "Romero: exclusieve luxe appartementen met zeezicht in Real de la Quinta, Marbella. Vanaf €1.150.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxe Appartementen & Penthouses",
    "OG_DESCRIPTION": "Ontdek Romero: 28 designwoningen met zoutwater infinity pool, gym en coworkingruimte in Real de la Quinta. Vanaf €1.150.000.",
    "OG_IMAGE": "https://investinspain.be/wp-content/uploads/2026/07/Romero-Real-de-la-Quinta_012.Aerial-View.render.jpg",
    "HERO_BG": "https://investinspain.be/wp-content/uploads/2026/07/Romero-Real-de-la-Quinta_101.Pedestrian-entrance-Communal-Swimming-Pool-Block-3-4.render.jpg",
    "HERO_BG_ALT": "Romero — voetgangersentree bij het gemeenschappelijke zwembad",
    "HERO_BG_POSITION": "top",
    # De herofoto heeft een storende watermerktekst in de rechterbenedenhoek;
    # op smalle/mobiele schermen (geen verticale crop) blijft die anders
    # zichtbaar, dus de onderste gradient wordt hier sneller volledig dicht.
    "EXTRA_HEAD_CSS": (
        ".page-romero .hero__bg::after { background: linear-gradient(to bottom, "
        "var(--bg) 0%, rgba(14,19,24,0.7) 25%, rgba(14,19,24,0.25) 55%, "
        "rgba(14,19,24,0.55) 78%, var(--bg) 88%); }"
    ),
    "HERO_NAME": "ROMERO",
    "HERO_LOCATION": "REAL DE LA QUINTA",
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
    "META_DESCRIPTION": "Romero: exclusive luxury apartments with sea views in Real de la Quinta, Marbella. From €1.150.000.",
    "OG_TITLE": f"{PROJECT_NAME} — Luxury Apartments & Penthouses",
    "OG_DESCRIPTION": "Discover Romero: 28 design homes with a saltwater infinity pool, gym and coworking space in Real de la Quinta. From €1.150.000.",
    "HERO_BG_ALT": "Romero — pedestrian entrance by the communal swimming pool",
}

# Gebruikt door de /projecten/ overzichtspagina (kaart + kaartjes)
HUB = {
    "NAME": PROJECT_NAME,
    "LOCATION": "Real de la Quinta",
    "PRICE": PRICE_FROM,
    "THUMB": "https://investinspain.be/images/romero/thumb.webp",
    # Deze render heeft een disclaimer-tekststrook onderaan ("The furniture
    # shown is illustrative..."); de kaart-crop is breder dan de foto zelf,
    # dus er wordt enkel links/rechts bijgesneden en de tekst blijft anders
    # gewoon zichtbaar. Duwt de foto daarom zelf wat naar boven uit, vast.
    "THUMB_EXTRA_CSS": "transform: scale(1.2) !important; transform-origin: center top;",
    # Zonder deze hover-variant zou de !important hierboven de normale
    # hover-zoom van .project-card:hover overschrijven, waardoor dit
    # kaartje als enige geen animatie toont.
    "THUMB_HOVER_EXTRA_CSS": "transform: scale(1.26) !important; transform-origin: center top;",
    "LAT": 36.5353281,
    "LNG": -4.9791269,
    "HREF": "/romero/",
}
