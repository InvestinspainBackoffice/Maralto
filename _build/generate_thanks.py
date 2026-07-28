"""
Bouwt bedankt/index.html: de pagina waarnaar alle leadformulieren
doorsturen na een geslaagde inzending. Statische pagina, geen
per-project tokens nodig.

Gebruik: python3 _build/generate_thanks.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "_build", "templates")


def main():
    with open(os.path.join(TEMPLATES, "thanks.html"), encoding="utf-8") as f:
        page = f.read()

    out_dir = os.path.join(ROOT, "bedankt")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"bedankt/index.html -> {len(page)} chars")


if __name__ == "__main__":
    main()
