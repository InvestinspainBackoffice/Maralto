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
