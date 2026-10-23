"""Rendert alle Assets aus assets/src/*.html nach assets/export/.

Voraussetzung:  pip install playwright && python -m playwright install chromium
Aufruf:         python assets/render.py            (alle)
                python assets/render.py banner     (nur Dateien, deren Name "banner" enthält)

Ist die Schrift "Noway Round" lokal installiert, nutzt Chromium sie automatisch
(siehe brand.css); andernfalls wird Nunito als Ersatz verwendet.
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
SRC, OUT = ROOT / "src", ROOT / "export"

# (Quelldatei, Ausgabedatei, Breite, Höhe, Skalierung)
PNG_JOBS = [
    ("profilbild.html", "wud-ma-2026_profilbild_rot_1080x1080.png", 1080, 1080, 1),
    ("profilbild.html#grau", "wud-ma-2026_profilbild_grau_1080x1080.png", 1080, 1080, 1),
    ("banner.html#gespiegelt", "wud-ma-2026_banner_linkedin-profil_1584x396.png", 1584, 396, 1),
    ("banner.html", "wud-ma-2026_banner_linkedin-event_1776x444.png", 1776, 444, 1),
    ("banner.html", "wud-ma-2026_banner_newsletter-header_1200x300.png", 1200, 300, 1),
    ("banner.html", "wud-ma-2026_banner_newsletter-header_1200x300@2x.png", 1200, 300, 2),
    ("save-the-date-linkedin.html", "wud-ma-2026_save-the-date_linkedin_1080x1350.png", 1080, 1350, 1),
    ("save-the-date-quadrat.html", "wud-ma-2026_save-the-date_quadrat_1080x1080.png", 1080, 1080, 1),
    ("session-card-post.html", "wud-ma-2026_session-card_linkedin_1080x1350.png", 1080, 1350, 1),
]
# Flyer: DIN A5 + 3 mm Beschnitt (154 × 216 mm), Vorder- und Rückseite
PDF_JOBS = [
    ("flyer-a5.html", "wud-ma-2026_flyer_a5_mit-beschnitt.pdf", "154mm", "216mm"),
]


def main(filter_=""):
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for src, out, w, h, scale in PNG_JOBS:
            if filter_ not in src and filter_ not in out:
                continue
            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
            file, _, frag = src.partition("#")
            page.goto((SRC / file).as_uri() + (f"#{frag}" if frag else ""))
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(300)
            page.screenshot(path=str(OUT / out))
            page.close()
            print("✓", out)
        for src, out, w, h in PDF_JOBS:
            if filter_ not in src and filter_ not in out:
                continue
            page = browser.new_page()
            page.goto((SRC / src).as_uri())
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(300)
            page.pdf(path=str(OUT / out), width=w, height=h, print_background=True,
                     margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
            page.close()
            print("✓", out)
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
