"""
Eenmalig script: haalt uit de bestaande Maralto index.html de herbruikbare
HEAD/HERO/TAIL-blokken, vervangt de Maralto-specifieke waarden door tokens,
en schrijft ze weg als sjabloonbestanden. Wordt niet automatisch herrun -
de output staat vast in _build/templates/. Maralto's eigen index.html wordt
niet aangeraakt.
"""
import re

SRC = "index.html"
OUT_DIR = "_build/templates"

with open(SRC, encoding="utf-8") as f:
    html = f.read()

HERO_MARK = '<!-- ═══════════ HERO ═══════════ -->'
INTRO_MARK = '<!-- ═══════════ INTRO ═══════════ -->'
CONTACT_MARK = '<!-- ═══════════ CONTACT ═══════════ -->'

i_hero = html.index(HERO_MARK)
i_intro = html.index(INTRO_MARK)
i_contact = html.index(CONTACT_MARK)

head = html[:i_hero]
hero = html[i_hero:i_intro]
tail = html[i_contact:]

# ── HEAD: tokenize title/meta ──
head = head.replace(
    '<title>Maralto Estepona — INVESTINSPAIN.BE</title>',
    '<title>__TITLE__</title>'
)
head = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="__META_DESCRIPTION__">',
    head
)
head = re.sub(
    r'<meta property="og:title" content="[^"]*">',
    '<meta property="og:title" content="__OG_TITLE__">',
    head
)
head = re.sub(
    r'<meta property="og:description" content="[^"]*">',
    '<meta property="og:description" content="__OG_DESCRIPTION__">',
    head
)
head = re.sub(
    r'<meta property="og:image" content="[^"]*">',
    '<meta property="og:image" content="__OG_IMAGE__">',
    head
)
# De DIRECTION CONTRACT-commentaarblok is Maralto-specifieke designnotitie, hoort niet in het sjabloon
head = re.sub(r'<!--\n  DIRECTION CONTRACT.*?-->\n', '', head, flags=re.S)
# De hero-achtergrond staat als CSS-regel in <style>, dus in head, niet in hero
head = head.replace(
    "url('https://investinspain.be/wp-content/uploads/2025/08/Maralto-Estepona-9.png') center 60% / cover no-repeat;",
    "url('__HERO_BG__') center 60% / cover no-repeat;"
)

# ── HERO: tokenize name/location/price + bg alt ──
hero = hero.replace(
    'aria-label="Maralto Estepona — moderne architectuur met gebogen balkons en mediterrane tuinen"',
    'aria-label="__HERO_BG_ALT__"'
)
hero = hero.replace('<h1 class="hero__name">MARALTO</h1>', '<h1 class="hero__name">__HERO_NAME__</h1>')
hero = hero.replace('<p class="hero__location">ESTEPONA</p>', '<p class="hero__location">__HERO_LOCATION__</p>')
hero = hero.replace('<p class="hero__price">Vanaf € 460.000</p>', '<p class="hero__price">__HERO_PRICE__</p>')

# ── TAIL: tokenize project-name-bearing bits + namespace localStorage keys ──
# De sticky-cta bar splitst "Vanaf" en het bedrag met een <span>, dus dat
# vereist een eigen token (alleen het bedrag) naast __PRICE_FROM__.
tail = tail.replace(
    '<div class="sticky-cta__text">Vanaf <span>€ 460.000</span></div>',
    '<div class="sticky-cta__text">Vanaf <span>__PRICE_AMOUNT__</span></div>'
)
tail = tail.replace(
    'https://wa.me/32496571397?text=Hallo%2C%20ik%20heb%20interesse%20in%20Maralto%20Estepona.%20Kan%20ik%20meer%20informatie%20ontvangen%3F',
    'https://wa.me/32496571397?text=__WA_TEXT_ENCODED__'
)
tail = tail.replace('Aanvraag Maralto Estepona', 'Aanvraag __PROJECT_NAME__')
tail = tail.replace('Nieuwe aanvraag Maralto Estepona', 'Nieuwe aanvraag __PROJECT_NAME__')
tail = tail.replace("var MODAL_KEY = 'maralto_modal_shown';", "var MODAL_KEY = '__SLUG___modal_shown';")
tail = tail.replace(
    '<p>U ontvangt binnenkort alle informatie over Maralto in uw inbox.</p>',
    '<p>U ontvangt binnenkort alle informatie over __PROJECT_NAME__ in uw inbox.</p>'
)
tail = tail.replace(
    'Laat uw gegevens achter en ontvang alle projectinformatie over Maralto rechtstreeks in uw inbox.',
    'Laat uw gegevens achter en ontvang alle projectinformatie over __PROJECT_NAME__ rechtstreeks in uw inbox.'
)

# ── TAIL: tokenize de contactpersoon (niet elk project heeft dezelfde makelaar) ──
tail = tail.replace(
    'https://investinspain.be/wp-content/uploads/2020/01/Gunther-De-Vleeschouwer-INVESTINSPAIN.jpg',
    '__AGENT_PHOTO__'
)
tail = tail.replace('alt="Gunther De Vleeschouwer"', 'alt="__AGENT_NAME__"')
tail = tail.replace(
    '<h3 class="agent__name">Gunther De Vleeschouwer</h3>',
    '<h3 class="agent__name">__AGENT_NAME__</h3>'
)
tail = tail.replace('href="tel:+32496571397"', 'href="tel:__AGENT_PHONE_TEL__"')
tail = tail.replace(
    '        +32 496 57 13 97\n      </a>\n      <a href="mailto:gunther@investinspain.be" class="agent__detail">',
    '        __AGENT_PHONE_DISPLAY__\n      </a>\n      <a href="mailto:__AGENT_EMAIL__" class="agent__detail">'
)
tail = tail.replace(
    '        gunther@investinspain.be\n      </a>\n      <a href="tel:+3215257310"',
    '        __AGENT_EMAIL__\n      </a>\n      <a href="tel:+3215257310"'
)
# WhatsApp FAB en de 3 mailto-handlers in de JS gebruiken hetzelfde nummer/adres
tail = tail.replace(
    'href="https://wa.me/32496571397?text=__WA_TEXT_ENCODED__"',
    'href="https://wa.me/__WA_NUMBER__?text=__WA_TEXT_ENCODED__"'
)
tail = tail.replace("mailto:gunther@investinspain.be", "mailto:__AGENT_EMAIL__")

import os
os.makedirs(OUT_DIR, exist_ok=True)
with open(f"{OUT_DIR}/head.html", "w", encoding="utf-8") as f:
    f.write(head)
with open(f"{OUT_DIR}/hero.html", "w", encoding="utf-8") as f:
    f.write(hero)
with open(f"{OUT_DIR}/tail.html", "w", encoding="utf-8") as f:
    f.write(tail)

print("head:", len(head), "chars")
print("hero:", len(hero), "chars")
print("tail:", len(tail), "chars")
print("OK - templates written to", OUT_DIR)
