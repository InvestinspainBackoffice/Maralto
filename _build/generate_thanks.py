"""
Bouwt bedankt/index.html (NL) en en/thank-you/index.html (EN): de pagina
waarnaar alle leadformulieren doorsturen na een geslaagde inzending.
Statische pagina, geen per-project tokens nodig.

Gebruik: python3 _build/generate_thanks.py
"""
import os
import re
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "_build", "templates")

LANGUAGES = ["nl", "en"]

# Welke gidsen per taal getoond worden, en met welke i18n-sleutel (titel/
# omschrijving, zie _build/i18n.py) elke kaart gevuld wordt. De Engelse
# IIS Showcase bestaat nog niet, dus die kaart valt daar gewoon weg.
GUIDES = {
    "nl": [
        {"pdf": "investeringschecklist-nl.pdf", "cover": "investeringschecklist-nl.jpg", "title_key": "GUIDE1_TITLE", "desc_key": "GUIDE1_DESC"},
        {"pdf": "financiele-checklist-nl.pdf", "cover": "financiele-checklist-nl.jpg", "title_key": "GUIDE2_TITLE", "desc_key": "GUIDE2_DESC"},
        {"pdf": "iis-showcase.pdf", "cover": "iis-showcase.jpg", "title_key": "GUIDE3_TITLE", "desc_key": "GUIDE3_DESC"},
    ],
    "en": [
        {"pdf": "investment-checklist-en.pdf", "cover": "investment-checklist-en.jpg", "title_key": "GUIDE1_TITLE", "desc_key": "GUIDE1_DESC"},
        {"pdf": "financial-checklist-en.pdf", "cover": "financial-checklist-en.jpg", "title_key": "GUIDE2_TITLE", "desc_key": "GUIDE2_DESC"},
    ],
}

GUIDE_CARD = """    <a class="guide-card" href="/downloads/{pdf}" download target="_blank" rel="noopener">
      <div class="guide-card__img-wrap">
        <img src="/downloads/covers/{cover}" alt="{title}" loading="lazy">
      </div>
      <div class="guide-card__body">
        <div class="guide-card__title">{title}</div>
        <p class="guide-card__desc">{desc}</p>
        <span class="guide-card__cta">{download_label} <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m0 0l-5-5m5 5l5-5M5 21h14"/></svg></span>
      </div>
    </a>"""

THANKS_TEXT = {
    "nl": {
        "TITLE": "Bedankt voor uw aanvraag — INVESTINSPAIN.BE",
        "META_DESCRIPTION": "Bedankt voor uw aanvraag bij INVESTINSPAIN.BE. Download alvast één van onze gratis gidsen over investeren in nieuwbouw aan de Costa del Sol.",
        "OG_DESCRIPTION": "We nemen snel contact met u op. Download alvast één van onze gratis gidsen.",
        "WA_MESSAGE": "Hallo, ik heb een vraag over jullie projecten.",
        "OUT_DIR": ["bedankt"],
        "HOME_HREF": "/",
    },
    "en": {
        "TITLE": "Thank you for your request — INVESTINSPAIN.BE",
        "META_DESCRIPTION": "Thank you for your request to INVESTINSPAIN.BE. Feel free to download one of our free guides about investing in new-build property on the Costa del Sol.",
        "OG_DESCRIPTION": "We will get in touch with you shortly. Feel free to download one of our free guides.",
        "WA_MESSAGE": "Hello, I have a question about your projects.",
        "OUT_DIR": ["en", "thank-you"],
        "HOME_HREF": "/en/",
    },
}


def build(lang):
    with open(os.path.join(TEMPLATES, "thanks.html"), encoding="utf-8") as f:
        page = f.read()

    strings = i18n.strings_for(lang)
    guide_cards = "\n".join(
        GUIDE_CARD.format(
            pdf=g["pdf"],
            cover=g["cover"],
            title=strings[g["title_key"]],
            desc=strings[g["desc_key"]],
            download_label=strings["DOWNLOAD_PDF"],
        )
        for g in GUIDES[lang]
    )
    page = page.replace("__GUIDE_CARDS__", guide_cards)

    text = THANKS_TEXT[lang]
    page = page.replace("__THANKS_TITLE__", text["TITLE"])
    page = page.replace("__THANKS_META_DESCRIPTION__", text["META_DESCRIPTION"])
    page = page.replace("__THANKS_OG_DESCRIPTION__", text["OG_DESCRIPTION"])
    page = page.replace("__HOME_HREF__", text["HOME_HREF"])
    page = page.replace(
        "__WA_HREF__",
        f"https://wa.me/32496571397?text={quote(text['WA_MESSAGE'])}",
    )
    for key, value in i18n.strings_for(lang).items():
        page = page.replace(f"__I_{key}__", value)
    page = page.replace("__LANG_SWITCH_HREF__", "/bedankt/" if lang == "en" else "/en/thank-you/")

    leftovers = set(re.findall(r"__[A-Z0-9_]+__", page))
    if leftovers:
        raise SystemExit(f"bedankt ({lang}) Niet-ingevulde tokens: {sorted(leftovers)}")

    out_dir = os.path.join(ROOT, *text["OUT_DIR"])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"{'/'.join(text['OUT_DIR'])}/index.html ({lang}) -> {len(page)} chars")


def main():
    for lang in LANGUAGES:
        build(lang)


if __name__ == "__main__":
    main()
