# World Usability Day Mannheim 2026 – Marketing-Kit

Texte und Grafiken für den **WUD Mannheim 2026**
📅 Donnerstag, 12. November 2026 · 14:00–19:00 Uhr · 📍 C-Hub Mannheim, Hafenstraße 25 · 🎟️ kostenlos · 🔗 [wud-ma.de](https://wud-ma.de)

## Inhalt

### 📧 Newsletter → [`newsletter/`](newsletter/)
Versandplan mit Terminen: [`newsletter/README.md`](newsletter/README.md)

| Datei | Wofür |
|---|---|
| [01-angemeldete-weitersagen.md](newsletter/01-angemeldete-weitersagen.md) | An Angemeldete: Leute mitbringen, Session-Idee mitbringen |
| [02-reaktivierung-vorjahr.md](newsletter/02-reaktivierung-vorjahr.md) | An Angemeldete 2025 – inkl. optionaler Nachfass-Mail |
| [03-reminder-1-woche.md](newsletter/03-reminder-1-woche.md) | Reminder 1 Woche vorher, mit Pitch-Tipps und Anfahrt |
| [04-reminder-1-tag.md](newsletter/04-reminder-1-tag.md) | Reminder 1 Tag vorher, kurz & praktisch |
| [05-danke-nach-dem-event.md](newsletter/05-danke-nach-dem-event.md) | *Vorschlag:* Danke-Mail mit Fotos, Session-Doku, Feedback |

### ✍️ Marketing-Texte → [`marketing-texte/`](marketing-texte/)
| Datei | Inhalt |
|---|---|
| [event-vorstellung.md](marketing-texte/event-vorstellung.md) | Event-Beschreibung in XS/S/M/L + fertige Social-Posts |
| [open-space-format.md](marketing-texte/open-space-format.md) | Open Space erklärt in XS/S/M/L + FAQ-Bausteine + Social-Post |
| [save-the-date-linkedin-post.md](marketing-texte/save-the-date-linkedin-post.md) | 3 Post-Texte zum Save-the-Date-Bild |

### 🎨 Grafiken → [`assets/export/`](assets/export/)
| Datei | Format | Einsatz |
|---|---|---|
| `…_profilbild_rot_1080x1080.png` | 1080 × 1080 | Profilbild (LinkedIn-Seite, Meetup, Slack) – funktioniert auch rund |
| `…_profilbild_grau_1080x1080.png` | 1080 × 1080 | ruhigere Variante |
| `…_banner_linkedin-event_1776x444.png` | 4 : 1 | Titelbild LinkedIn-Event |
| `…_banner_linkedin-profil_1584x396.png` | 4 : 1 | Profilbanner (gespiegelt, damit das Profilfoto keinen Text verdeckt) |
| `…_banner_newsletter-header_1200x300(@2x).png` | 4 : 1 | Kopfbild für Newsletter / Website |
| `…_save-the-date_linkedin_1080x1350.png` | 4 : 5 | Save-the-Date-Post (Hochformat, beste Feed-Präsenz) |
| `…_save-the-date_quadrat_1080x1080.png` | 1 : 1 | Save-the-Date für Instagram & Co. |
| `…_flyer_a5_mit-beschnitt.pdf` | DIN A5 + 3 mm | Druckbarer Flyer, Vorder- & Rückseite, QR-Code zur Anmeldung |
| `…_flyer_vorschau-1/2.png` | | Vorschaubilder des Flyers |

Außerdem: [`assets/kalender/wud-mannheim-2026.ics`](assets/kalender/wud-mannheim-2026.ics) – Kalendereintrag zum Verlinken im Newsletter.

## CI (übernommen von wud-ma.de)

| Rolle | Farbe |
|---|---|
| Headlines, Buttons | `#D13327` Rot |
| Text, Primär | `#000427` Navy |
| Flächen | `#F0F0F0` Hellgrau · `#EBE8E0` Creme |
| Post-its | `#EBE8E0` Creme (CI-Sekundärfarbe) |
| Pfeile, gestrichelte „Deine Session?“-Karte | `#D13327` Rot |
| Logo-Akzente | `#40C0CB` Türkis · `#80BD42` Grün |

**Schriften:** Headlines im CI = *Noway Round* · Fließtext = *Plus Jakarta Sans* · Post-its = *Kalam* (Handschrift)

> ⚠️ **Noway Round** ist eine kostenpflichtige Schrift und liegt deshalb **nicht** in diesem öffentlichen Repo. Die Exporte nutzen als Ersatz **Nunito** (sehr ähnlich, frei). Ist Noway Round auf dem Rechner installiert, verwenden die HTML-Vorlagen sie automatisch – einfach neu rendern (s. unten).

> ⚠️ **Logo:** Das verwendete WUD-Logo stammt von wud-ma.de und ist nur ca. 390 px breit. Für den **professionellen Druck** des Flyers besser eine Vektor-Version (SVG/PDF/EPS) einsetzen: Datei als `assets/src/img/wud-logo.png` bzw. in den HTML-Dateien ersetzen. Das Flyer-PDF ist in RGB angelegt – für Büro- und Digitaldruck passt das; eine Online-Druckerei konvertiert in der Regel selbst nach CMYK.

## Grafiken anpassen

Alle Grafiken sind HTML-Vorlagen in [`assets/src/`](assets/src/) – Texte lassen sich direkt im HTML ändern, Farben und Schriften zentral in [`brand.css`](assets/src/brand.css).

```bash
pip install playwright && python -m playwright install chromium
python assets/render.py          # alle Grafiken neu erzeugen
python assets/render.py banner   # nur Banner
```
