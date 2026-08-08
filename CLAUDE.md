# Projectpagina - Maralto

Statische site (Python-generator in `_build/`, geen build-pipeline) met
project-landingspagina's voor INVESTINSPAIN.BE, gedeployed op Vercel.

## Foto's bij nieuwe projecten of hero-wissels

Gebruik **niet** rechtstreeks een hotlink naar de bronsite (WordPress-media,
een developer-site, ...). Haal de foto op, zet ze om naar WebP en host ze
zelf in deze repo:

```bash
_build/fetch_image.sh <bron-url> <project-slug> <output-naam>
# bv: _build/fetch_image.sh https://emare.immo/.../084A5415x.jpg emare hero
```

Dit zet de foto om naar WebP (kwaliteit 88, zelfde resolutie - visueel
lossless) en bewaart ze in `images/<slug>/<naam>.webp`. Vercel serveert de
hele repo statisch op **`projects.investinspain.be`** (niet op
`investinspain.be` zelf - dat is de losstaande WordPress-site). Verwijs in
`_build/projects/<slug>.py` dus naar
`https://projects.investinspain.be/images/<slug>/<naam>.webp`.

⚠️ Test na het regenereren altijd even met `curl -sI` of het pad ook
écht 200 teruggeeft op `projects.investinspain.be` - een verkeerde host
hier heeft eerder alle kaartjes op de projectenpagina gebroken.

Reden: hotlinken naar externe sites levert vaak zware PNG's/ongecomprimeerde
JPEG's op (trage FCP/LCP, zie Vercel Speed Insights) en is kwetsbaar als de
bronsite foto's verplaatst of verwijdert. Zelf hosten als WebP lost beide op
zonder kwaliteitsverlies.

Na het toevoegen van foto's: `python3 _build/generate.py && python3
_build/generate_hub.py` om alles te regenereren.

## Regenereren

```bash
python3 _build/generate_data.py     # api/_projects.json (bron voor /api/match)
python3 _build/generate.py          # alle projectpagina's
python3 _build/generate_hub.py      # de overzichtspagina
python3 _build/generate_selectie.py # /selectie/ en /en/selection/
```

`generate_selectie.py` leest `api/_projects.json`, dus draai `generate_data.py`
eerst wanneer er projecten of prijzen zijn gewijzigd.
