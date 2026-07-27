"""
Bouwt projecten/index.html: een overzichtspagina met kaart + kaartjes voor
elk project dat een HUB-dict definieert in _build/projects/*.py. Wordt
automatisch bijgewerkt zodra een nieuw project-bestand een HUB toevoegt -
geen handmatige HTML-bewerking nodig.

Gebruik: python3 _build/generate_hub.py
"""
import html
import importlib.util
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "_build", "templates")
PROJECTS_DIR = os.path.join(ROOT, "_build", "projects")

# Maralto eerst (vlaggenschip), daarna alfabetisch. Nieuwe projecten die hier
# niet in staan, komen automatisch achteraan (alfabetisch) terecht.
ORDER = ["maralto"]


def load_hub_entries():
    entries = {}
    for fname in sorted(os.listdir(PROJECTS_DIR)):
        if not fname.endswith(".py"):
            continue
        slug = fname[:-3]
        spec = importlib.util.spec_from_file_location(slug, os.path.join(PROJECTS_DIR, fname))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "HUB"):
            entry = dict(mod.HUB)
            entry["SLUG"] = slug
            entries[slug] = entry

    ordered_slugs = [s for s in ORDER if s in entries]
    ordered_slugs += sorted(s for s in entries if s not in ORDER)
    return [entries[s] for s in ordered_slugs]


def render_card(entry):
    return f"""    <a class="project-card" href="{entry['HREF']}">
      <div class="project-card__img-wrap">
        <img class="project-card__img" src="{entry['THUMB']}" alt="{html.escape(entry['NAME'])}" loading="lazy">
      </div>
      <div class="project-card__body">
        <div class="project-card__name">{html.escape(entry['NAME'])}</div>
        <div class="project-card__location">{html.escape(entry['LOCATION'])}</div>
        <div class="project-card__price">{html.escape(entry['PRICE'])}</div>
      </div>
    </a>"""


def main():
    entries = load_hub_entries()
    if not entries:
        raise SystemExit("Geen enkel project-bestand met een HUB-dict gevonden.")

    cards_html = "\n".join(render_card(e) for e in entries)
    markers = [
        {
            "name": e["NAME"],
            "location": e["LOCATION"],
            "price": e["PRICE"],
            "href": e["HREF"],
            "lat": e["LAT"],
            "lng": e["LNG"],
        }
        for e in entries
    ]

    with open(os.path.join(TEMPLATES, "hub.html"), encoding="utf-8") as f:
        page = f.read()

    page = page.replace("__PROJECT_CARDS__", cards_html)
    page = page.replace("__MAP_MARKERS_JSON__", json.dumps(markers, ensure_ascii=False))

    out_dir = os.path.join(ROOT, "projecten")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"projecten/index.html -> {len(entries)} projecten ({len(page)} chars)")


if __name__ == "__main__":
    main()
