# Sjabloonsysteem voor projectpagina's

Genereert `<slug>/index.html` voor elk project, gebaseerd op de Maralto-pagina
als bewezen basis. Head/CSS, lead-capture (paneel, sticky balk, pop-up,
contactformulier) en de hele JavaScript-laag komen uit één gedeelde bron
(`_build/templates/`), zodat een fix daar automatisch in alle projectpagina's
terechtkomt. Alleen de content ertussenin (intro, foto's, faciliteiten,
locatie) is per project handgeschreven.

Maralto's eigen `index.html` (in de root) wordt hierdoor niet aangeraakt en
blijft apart onderhouden — deze pagina's leven ernaast, niet erbovenop.

## Een nieuw project toevoegen

1. Maak `_build/projects/<slug>.py` met een `DATA`-dict. Kopieer een bestaand
   bestand (bv. `adagio.py`) en pas de velden aan: `SLUG`, `TITLE`,
   `META_DESCRIPTION`, `OG_TITLE`, `OG_DESCRIPTION`, `OG_IMAGE`, `HERO_BG`,
   `HERO_BG_ALT`, `HERO_NAME`, `HERO_LOCATION`, `HERO_PRICE`, `PRICE_FROM`,
   `WA_TEXT_ENCODED` (via `urllib.parse.quote`), `PROJECT_NAME`.
2. Maak `_build/projects/<slug>_body.html` met de unieke content tussen intro
   en contactsectie (foto's, stats, faciliteiten, locatie, kaart). Gebruik de
   bestaande CSS-klassen (`content`, `full-image`, `image-pair`, `stats`,
   `amenities-list`, `location-grid`, `map-wrap`, `inline-cta`, `rule--gold`).
   Verzin nooit cijfers (m², bouwjaar, reistijden) die niet bevestigd zijn op
   de bron-pagina — laat een stat gewoon weg in plaats van te gokken.
3. Run `python3 _build/generate.py <slug>` (of zonder argument voor alle
   projecten). Dat schrijft `<slug>/index.html` in de projectroot.
4. Test lokaal (`python3 -m http.server 8091` in de projectroot, dan
   `/<slug>/`), commit en push.

## Het sjabloon zelf aanpassen

`_build/templates/{head,hero,tail}.html` zijn geëxtraheerd uit Maralto's
`index.html` via `_build/extract_template.py` — bewerk ze niet direct.
Wijzig in plaats daarvan `extract_template.py` (of, voor een structurele
wijziging, eerst Maralto's eigen `index.html`, en run dan
`python3 _build/extract_template.py` opnieuw) en regenereer daarna alle
projectpagina's met `python3 _build/generate.py`.

## Kaart-embeds

Gebruik `https://www.google.com/maps?q=<lat>,<lng>&z=15&output=embed` — geen
API-key nodig. Haal de coördinaten van het echte project op (niet gokken):
open de WordPress-projectpagina en zoek in de HTML naar een
`lat,lng`-patroon (`36.xxxxx,-5.xxxxx`).

## De selectiepagina (/selectie/, /en/selection/)

Eigen vervanger voor de Typeform-vragenlijst: tien vragen, één per scherm, en
op het eind meteen de best passende projecten als klikbare kaartjes.

- `python3 _build/generate_selectie.py` bouwt beide taalversies uit
  `_build/templates/selectie.html`. Draai eerst `generate_data.py`: de
  vanaf-prijzen per regio op de kaart bij vraag 1 komen uit
  `api/_projects.json`, niet uit een handmatig lijstje.
- De vragen en antwoordopties staan in `QUESTIONS` in
  `generate_selectie.py` — dat is inhoud van die ene pagina en hoort dus niet
  in `_build/i18n.py` (dat blijft beperkt tot gedeelde UI-tekst).
- Het matchen zelf gebeurt in `api/match.js`. De browser stuurt alleen de
  antwoorden door; naam, prijs, foto en URL komen daar uit `_projects.json`,
  zodat een kaartje nooit verzonnen data kan tonen.
- Harde filters zijn alleen regio (uit de coördinaten), budget en woningtype.
  Slaapkamers, oppervlakte, ligging en uitzicht wegen mee in de rangschikking
  maar filteren niet: die staan in vrije tekst en zijn lang niet voor elk
  project af te leiden. Buitenruimte in m² staat nergens in de data en telt
  daarom helemaal niet mee — die vraag dient alleen de opvolging.
- Een vraag toevoegen: zet hem in `QUESTIONS` met een `param` die `match.js`
  kent, of met `param: ""` als het antwoord alleen met de lead mee moet.
