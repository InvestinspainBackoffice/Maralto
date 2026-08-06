"""
Vertaalwoordenboek voor de vaste UI-teksten in de gedeelde templates
(head/hero/tail/hub/thanks). Dit is bewust GESCHEIDEN van de content
per project (die staat in <slug>_body.html / <slug>_body_en.html en
in de DATA/DATA_EN-dicts) - het dekt enkel knoppen, labels, foutmeldingen
en andere terugkerende interface-tekst.

Nieuwe __I_KEY__-tokens: voeg de key toe aan ZOWEL "nl" als "en" hier,
en gebruik "__I_KEY__" in de template. generate.py/generate_hub.py/
generate_thanks.py vullen het per taal in - één bewerking hier (of in
een gedeelde template) geldt dus automatisch voor beide taalversies.
"""

STRINGS = {
    "nl": {
        "LANG": "nl",
        "LANG_SWITCH_LABEL": "EN",
        "SCROLL_HINT": "Ontdek",

        "FORM_VOORNAAM": "Voornaam",
        "FORM_ACHTERNAAM": "Achternaam",
        "FORM_EMAIL": "E-mailadres",
        "FORM_GSM": "GSM-nummer",
        "FORM_LANDCODE_ARIA": "Landcode",
        "PHONE_POPULAR": "Veelgekozen",
        "PHONE_ALL_COUNTRIES": "Alle landen",
        "FORM_CONSENT_PRE": "Ja, ik ga akkoord met het",
        "FORM_CONSENT_PRIVACY": "privacybeleid",
        "FORM_CONSENT_MID": "en de",
        "FORM_CONSENT_TERMS": "algemene voorwaarden",
        "FORM_SEND": "Verzenden",
        "ERR_REQUIRED": "Dit veld is verplicht",
        "ERR_EMAIL": "Ongeldig e-mailadres",
        "ERR_CONSENT": "U moet akkoord gaan om verder te gaan",

        "FOOTER_COPYRIGHT": "&copy; INVESTINSPAIN.BE 2026 &mdash; Alle rechten voorbehouden",
        "FOOTER_BA": "BA en borgstelling via NV AXA Belgium (polisnr. 730.390.160)",
        "FOOTER_PRIVACY": "Privacybeleid",
        "FOOTER_TERMS": "Algemene voorwaarden",

        "COOKIE_TEXT_PRE": "We gebruiken cookies om het bezoek van deze website te analyseren via Google Analytics. Meer info in ons",
        "COOKIE_PRIVACY": "privacybeleid",
        "COOKIE_DECLINE": "Weigeren",
        "COOKIE_ACCEPT": "Accepteren",
        "COOKIE_ARIA": "Cookievoorkeuren",

        "WA_ARIA": "Contact via WhatsApp",
        "IIS_LOGO_ALT": "INVESTINSPAIN.BE logo",
        "BIV_ALT": "BIV erkend vastgoedmakelaar",

        "AGENT_LABEL": "Uw contactpersoon",
        "AGENT_ROLE": "Real estate associate",
        "OFFICE_LABEL": "Kantoor",
        "AGENT_TRUST": "Uw inspectiereis naar Spanje wordt 100% vergoed door ons.",
        "AGENT_TRUST_CTA": "Ontdek de voorwaarden &rarr;",

        "CONTACT_LABEL": "Contact",
        "CONTACT_HEADING_PRE": "Ontvang prijzen &",
        "CONTACT_HEADING_EM": "beschikbaarheid",
        "CONTACT_INTRO": "Vul uw gegevens in en ontvang alle projectinformatie rechtstreeks in uw inbox.",

        "STICKY_CTA_BTN": "Ontvang info",

        "MODAL_HEADING_PRE": "Ontvang prijzen &",
        "MODAL_HEADING_EM": "beschikbaarheid",
        "MODAL_INTRO": "Laat uw gegevens achter en ontvang alle projectinformatie over __PROJECT_NAME__ rechtstreeks in uw inbox.",

        "DOCK_TRIGGER": "Prijzen aanvragen",
        "DOCK_HEADING_PRE": "Prijzen &",
        "DOCK_HEADING_EM": "beschikbaarheid",
        "DOCK_CLOSE_ARIA": "Sluiten",
        "DOCK_ARIA": "Ontvang projectinformatie",

        "CHAT_TRIGGER": "Stel een vraag",
        "CHAT_ARIA": "Chat over dit project",
        "CHAT_TITLE": "Vraag het ons",
        "CHAT_SUBTITLE": "Antwoord binnen enkele seconden",
        "CHAT_CLOSE_ARIA": "Chat sluiten",
        # Let op: deze tekst gaat via JS door escapeHtml() heen (net als elk
        # modelantwoord), dus hier letterlijke tekens gebruiken en geen
        # HTML-entities - die zouden als &mdash; in beeld komen.
        "CHAT_GREETING": "Goeiedag. Ik help u graag met vragen over __PROJECT_NAME__ — prijzen, ligging, faciliteiten of het aankoopproces in Spanje. Waar kan ik u mee helpen?",
        "CHAT_PLACEHOLDER": "Typ uw vraag&hellip;",
        "CHAT_SEND_ARIA": "Versturen",
        "CHAT_THINKING": "Aan het typen",
        "CHAT_ERROR": "Er ging iets mis. Probeer het opnieuw of bel Gunther op +32 496 57 13 97.",
        "CHAT_DISCLAIMER": "AI-assistent &mdash; gesprekken worden bewaard om onze dienstverlening te verbeteren.",
        "CHAT_WA": "Liever WhatsApp?",
        # Hub: geen huidig project, dus een begroeting gericht op kiezen.
        # Ook deze gaat door escapeHtml(): geen HTML-entities gebruiken.
        "CHAT_HUB_TITLE": "Zoek mee",
        "CHAT_HUB_SUBTITLE": "Vind het project dat bij u past",
        "CHAT_HUB_GREETING": "Goeiedag. Er staan meer dan honderd projecten aan de Costa del Sol op deze site. Vertel me waar u naar zoekt — streek, budget, eigen gebruik of verhuur — en ik zet de passende projecten voor u op een rij.",

        "HUB_HERO_TITLE": "PROJECTEN",
        "HUB_HERO_INTRO": "Ontdek onze actuele nieuwbouwprojecten aan de Costa del Sol &mdash; op kaart, en op naam.",
        "HUB_ROTATOR_ARIA": "Sfeerbeelden van onze recentste projecten",
        "HUB_MAP_ARIA": "Kaart met de locaties van onze projecten",
        "HUB_MAP_TOUCH_HINT": "Tik om de kaart te bedienen",
        "HUB_ALL_PROJECTS_LABEL": "Alle projecten",
        "HUB_FILTER_LOC_ARIA": "Filter op locatie",
        "HUB_FILTER_LOC_ALL": "Alle locaties",
        "HUB_FILTER_PRICE_ARIA": "Filter op prijs",
        "HUB_FILTER_PRICE_ALL": "Alle prijzen",
        "HUB_FILTER_EMPTY": "Geen projecten gevonden binnen deze selectie.",
        "HUB_CARD_CTA": "Bekijk project &rarr;",
        "HUB_DOCK_HEADING_PRE": "Interesse in",
        "HUB_DOCK_HEADING_EM": "een van onze projecten",

        "THANKS_LABEL": "Bedankt",
        "THANKS_HEADING_PRE": "Uw aanvraag is",
        "THANKS_HEADING_EM": "verzonden",
        "THANKS_INTRO": "We nemen zo snel mogelijk persoonlijk contact met u op. Terwijl u wacht: download gerust &eacute;&eacute;n van onze gratis gidsen hieronder.",
        "GUIDE1_TITLE": "Investeringschecklist",
        "GUIDE1_DESC": "De ideale nieuwbouwinvestering in Zuid-Spanje: waar u op moet letten voor een goed rendement.",
        "GUIDE2_TITLE": "Financi&euml;le checklist",
        "GUIDE2_DESC": "Nieuwbouw kopen in Spanje: alle financi&euml;le aspecten op een rij, van belastingen tot financiering.",
        "GUIDE3_TITLE": "IIS Showcase",
        "GUIDE3_DESC": "Kopen en inrichten aan de Costa del Sol: ontdek hoe IIS en HIS u van A tot Z begeleiden.",
        "DOWNLOAD_PDF": "Download PDF",
        "BROWSE_PROJECTS": "Bekijk al onze projecten",
    },
    "en": {
        "LANG": "en",
        "LANG_SWITCH_LABEL": "NL",
        "SCROLL_HINT": "Discover",

        "FORM_VOORNAAM": "First name",
        "FORM_ACHTERNAAM": "Last name",
        "FORM_EMAIL": "Email address",
        "FORM_GSM": "Mobile number",
        "FORM_LANDCODE_ARIA": "Country code",
        "PHONE_POPULAR": "Popular",
        "PHONE_ALL_COUNTRIES": "All countries",
        "FORM_CONSENT_PRE": "Yes, I agree to the",
        "FORM_CONSENT_PRIVACY": "privacy policy",
        "FORM_CONSENT_MID": "and the",
        "FORM_CONSENT_TERMS": "terms and conditions",
        "FORM_SEND": "Send",
        "ERR_REQUIRED": "This field is required",
        "ERR_EMAIL": "Invalid email address",
        "ERR_CONSENT": "You must agree to continue",

        "FOOTER_COPYRIGHT": "&copy; INVESTINSPAIN.BE 2026 &mdash; All rights reserved",
        "FOOTER_BA": "Professional liability insurance via NV AXA Belgium (policy no. 730.390.160)",
        "FOOTER_PRIVACY": "Privacy policy",
        "FOOTER_TERMS": "Terms and conditions",

        "COOKIE_TEXT_PRE": "We use cookies to analyze visits to this website via Google Analytics. More info in our",
        "COOKIE_PRIVACY": "privacy policy",
        "COOKIE_DECLINE": "Decline",
        "COOKIE_ACCEPT": "Accept",
        "COOKIE_ARIA": "Cookie preferences",

        "WA_ARIA": "Contact via WhatsApp",
        "IIS_LOGO_ALT": "INVESTINSPAIN.BE logo",
        "BIV_ALT": "BIV licensed real estate agent",

        "AGENT_LABEL": "Your contact person",
        "AGENT_ROLE": "Real estate associate",
        "OFFICE_LABEL": "Office",
        "AGENT_TRUST": "Your inspection trip to Spain is 100% reimbursed by us.",
        "AGENT_TRUST_CTA": "Discover the terms &rarr;",

        "CONTACT_LABEL": "Contact",
        "CONTACT_HEADING_PRE": "Receive prices &",
        "CONTACT_HEADING_EM": "availability",
        "CONTACT_INTRO": "Fill in your details and receive all project information directly in your inbox.",

        "STICKY_CTA_BTN": "Get info",

        "MODAL_HEADING_PRE": "Receive prices &",
        "MODAL_HEADING_EM": "availability",
        "MODAL_INTRO": "Leave your details and receive all project information about __PROJECT_NAME__ directly in your inbox.",

        "DOCK_TRIGGER": "Request prices",
        "DOCK_HEADING_PRE": "Prices &",
        "DOCK_HEADING_EM": "availability",
        "DOCK_CLOSE_ARIA": "Close",
        "DOCK_ARIA": "Receive project information",

        "CHAT_TRIGGER": "Ask a question",
        "CHAT_ARIA": "Chat about this project",
        "CHAT_TITLE": "Ask us",
        "CHAT_SUBTITLE": "Answers within seconds",
        "CHAT_CLOSE_ARIA": "Close chat",
        # Zie de NL-variant: gaat door escapeHtml(), dus geen HTML-entities.
        "CHAT_GREETING": "Hello. I'm happy to help with questions about __PROJECT_NAME__ — prices, location, amenities or the buying process in Spain. What would you like to know?",
        "CHAT_PLACEHOLDER": "Type your question&hellip;",
        "CHAT_SEND_ARIA": "Send",
        "CHAT_THINKING": "Typing",
        "CHAT_ERROR": "Something went wrong. Please try again or call Gunther on +32 496 57 13 97.",
        "CHAT_DISCLAIMER": "AI assistant &mdash; conversations are stored to help us improve our service.",
        "CHAT_WA": "Prefer WhatsApp?",
        # Zie de NL-variant: hub-begroeting, gaat door escapeHtml().
        "CHAT_HUB_TITLE": "Find yours",
        "CHAT_HUB_SUBTITLE": "Find the project that suits you",
        "CHAT_HUB_GREETING": "Hello. There are over a hundred projects on the Costa del Sol on this site. Tell me what you're looking for — area, budget, own use or rental — and I'll line up the ones that fit.",

        "HUB_HERO_TITLE": "PROJECTS",
        "HUB_HERO_INTRO": "Discover our current new-build projects on the Costa del Sol &mdash; by map, and by name.",
        "HUB_ROTATOR_ARIA": "Impressions of our most recent projects",
        "HUB_MAP_ARIA": "Map with the locations of our projects",
        "HUB_MAP_TOUCH_HINT": "Tap to use the map",
        "HUB_ALL_PROJECTS_LABEL": "All projects",
        "HUB_FILTER_LOC_ARIA": "Filter by location",
        "HUB_FILTER_LOC_ALL": "All locations",
        "HUB_FILTER_PRICE_ARIA": "Filter by price",
        "HUB_FILTER_PRICE_ALL": "All prices",
        "HUB_FILTER_EMPTY": "No projects found within this selection.",
        "HUB_CARD_CTA": "View project &rarr;",
        "HUB_DOCK_HEADING_PRE": "Interested in",
        "HUB_DOCK_HEADING_EM": "one of our projects",

        "THANKS_LABEL": "Thank you",
        "THANKS_HEADING_PRE": "Your request has been",
        "THANKS_HEADING_EM": "sent",
        "THANKS_INTRO": "We will get in touch with you personally as soon as possible. While you wait, feel free to download one of our free guides below.",
        "GUIDE1_TITLE": "Investment checklist",
        "GUIDE1_DESC": "The ideal new-build investment in southern Spain: what to look out for to secure a good return.",
        "GUIDE2_TITLE": "Financial checklist",
        "GUIDE2_DESC": "Buying new-build property in Spain: every financial aspect at a glance, from taxes to financing.",
        "GUIDE3_TITLE": "IIS Showcase",
        "GUIDE3_DESC": "Buying and furnishing on the Costa del Sol: discover how IIS and HIS guide you from A to Z.",
        "DOWNLOAD_PDF": "Download PDF",
        "BROWSE_PROJECTS": "View all our projects",
    },
}


def strings_for(lang):
    return dict(STRINGS[lang])
