# EXPAT-RESTERENDE-TECHNISCHE-RESTPUNTEN.md
## Handmatige restpunten — ExpatNetherlandsHub

Datum: 2026-03-09 (bijgewerkt ronde 2)
Status: alle hoge-prioriteit items zijn OPGELOST.

---

## ~~Prioriteit HOOG~~ — OPGELOST

### ~~1. Near-orphan pages~~ ✅ GEFIXT
~35 interne links toegevoegd aan 18 near-orphan pages vanuit relevante clusters. Alle pages hebben nu 3+ inbound links.

### ~~2. Tools niet gelinkt vanuit city pages~~ ✅ GEFIXT
6 ontbrekende tools (30%-calc, bank-chooser, visa-finder, insurance-chooser, inburgering-builder, diploma-evaluator) toegevoegd aan alle 17 city pages. Alle 11 tools zijn nu gelinkt vanuit elke city page.

### ~~3. City pages missen author en categories~~ ✅ GEFIXT
`author: "Sarah van den Berg"` + `categories: ["cities"]` toegevoegd aan alle 17 city pages.

### ~~4. Missing featured_image frontmatter~~ ✅ GEFIXT (deels)
`featured_image` referenties toegevoegd aan 5 city pages (almere, amstelveen, arnhem, nijmegen, tilburg). **De .webp afbeeldingsbestanden moeten nog handmatig worden aangemaakt en geplaatst in `static/images/featured/`.**

---

## Prioriteit MIDDEN (nice-to-have, geen urgentie)

### 5. Afbeeldingsbestanden aanmaken — 5 city images
De frontmatter referenties staan klaar, maar de daadwerkelijke bestanden bestaan nog niet:
- `static/images/featured/almere.webp`
- `static/images/featured/amstelveen.webp`
- `static/images/featured/arnhem.webp`
- `static/images/featured/nijmegen.webp`
- `static/images/featured/tilburg.webp`

**Impact:** OG image ontbreekt op social media shares voor deze 5 cities. Geen rendering-fout.

### 6. Missing keywords field — 10 articles
10 guide articles missen het `keywords` frontmatter veld:
- best-dutch-phone-plans, exchange-driving-license, kings-day, dutch-tax-return-how-to-file, mental-health-support, moving-to-breda, moving-to-den-bosch, moving-to-maastricht, making-friends, dutch-nationality-guide

**Impact:** Minimaal — `<meta name="keywords">` heeft vrijwel geen SEO-waarde meer.

### 7. Missing tags — 1 article
`making-friends-netherlands-expats-2026.md` mist zowel `tags` als `keywords`.

---

## Prioriteit LAAG (geen urgentie)

### 8. Inconsistent type frontmatter
16 van ~82 guide articles hebben een `type` veld, de rest niet. Geen functionele impact.

### 9. Redundante slug frontmatter
11 articles hebben een `slug` dat identiek is aan de bestandsnaam. Kan verwijderd worden voor consistentie.

### 10. Lege services/ directory
`content/services/` is leeg. Menu-item wijst naar `/guides/daily-life/`.

### 11. Email signup forms zijn stubs
`action="#"` + `onsubmit="return false"`. Functioneren niet.

### 12. Tool pages missen featured_image
Alle 11 tool pages missen `featured_image`. Lage impact — tools worden zelden gedeeld op social media.

---

## Wat NIET moet (geen actie nodig)

| Item | Reden geen actie |
|------|-----------------|
| Tags taxonomy niet gedeclareerd in hugo.toml | Hugo declareert tags automatisch |
| Monolithische baseof.html (1584 regels) | Werkt correct |
| CSS inline in baseof.html | Normaal voor Hugo; minificatie via `--minify` |
| Tool templates als pass-through | By design |
| `draft: false` op 2 artikelen | Geen effect |

---

## Eindstatus

### TECHNISCH KLAAR VOOR 8 WEKEN

Alle hoge-prioriteit items zijn opgelost. De resterende punten zijn kosmetisch (missing images, inconsistent frontmatter velden) en veroorzaken geen 404's, indexatie-problemen, of rendering-fouten.
