# EXPAT-RESTERENDE-TECHNISCHE-RESTPUNTEN.md
## Handmatige restpunten — ExpatNetherlandsHub

Datum: 2026-03-09
Status: geen van deze items blokkeert de site of veroorzaakt SEO-schade de komende 8 weken.

---

## Prioriteit HOOG (aanbevolen binnen 2 weken)

### 1. Near-orphan pages — meer interne links nodig
18 pagina's hebben slechts 1 inbound link. Belangrijkste:

| Pagina | Huidige inbound | Aanbevolen actie |
|--------|----------------|-----------------|
| `/guides/housing/best-cities-netherlands-expats-2026/` | 1 | Linken vanuit housing, finance en daily-life pillar guides |
| `/guides/housing/energy-providers-expats-netherlands-2026/` | 1 | Linken vanuit cost-of-living en finding-housing guides |
| `/guides/work/best-coworking-spaces-netherlands-2026/` | 1 | Linken vanuit freelancer-zzp en city guides |
| `/guides/work/kvk-registration-expat-guide-2026/` | 1 | Linken vanuit freelancer-zzp guide |
| `/guides/legal/dutch-nationality-guide-expats-2026/` | 1 | Linken vanuit bsn-registration en digid guides |
| `/guides/legal/leaving-netherlands-expat-checklist-2026/` | 1 | Linken vanuit tax, banking en insurance guides |
| `/guides/finance/dutch-tax-return-checklist-expats-2026/` | 1 | Linken vanuit tax-system en 30-percent-ruling guides |
| `/guides/daily-life/best-dutch-phone-plans-expats-2026/` | 1 | Linken vanuit sim-card en internet-providers guides |

### 2. Tools niet gelinkt vanuit city pages
6 tools krijgen 0 links vanuit de 17 city pages:

| Tool | Guide links | City links | Actie |
|------|------------|-----------|-------|
| `/tools/30-percent-ruling-calculator/` | 19 | **0** | Toevoegen aan alle city pages in "Working" sectie |
| `/tools/bank-account-chooser/` | 9 | **0** | Toevoegen aan city pages in "Getting Started" sectie |
| `/tools/inburgering-route-builder/` | 9 | **0** | Toevoegen aan city pages met integratie-context |
| `/tools/insurance-chooser/` | 6 | **0** | Toevoegen aan city pages in "Healthcare" sectie |
| `/tools/visa-permit-finder/` | 7 | **0** | Toevoegen aan city pages in "Getting Registered" sectie |
| `/tools/diploma-evaluator/` | 6 | **0** | Toevoegen aan city pages met werk/onderwijs-context |

---

## Prioriteit MIDDEN (aanbevolen binnen 4 weken)

### 3. Missing featured_image — 5 city pages
Almere, Amstelveen, Arnhem, Nijmegen, Tilburg hebben geen `featured_image`. Dit beïnvloedt OG image sharing op social media.

**Actie:** Webp afbeeldingen maken en toevoegen aan frontmatter.

### 4. City pages missen author en categories
Alle 17 city pages missen `author` en `categories` frontmatter. Dit beïnvloedt Article schema (geen author) en related-content matching.

**Actie:** Toevoegen aan alle city files:
```yaml
author: "Sarah van den Berg"
categories: ["cities"]
```

### 5. Missing keywords field — 10 articles
10 guide articles missen het `keywords` frontmatter veld (gebruikt voor `<meta name="keywords">`):
- best-dutch-phone-plans, exchange-driving-license, kings-day, dutch-tax-return-how-to-file, mental-health-support, moving-to-breda, moving-to-den-bosch, moving-to-maastricht, making-friends, dutch-nationality-guide

**Impact:** Minimaal — `<meta name="keywords">` heeft vrijwel geen SEO-waarde meer. Kan voor consistentie worden aangevuld.

### 6. Missing tags — 1 article
`making-friends-netherlands-expats-2026.md` mist zowel `tags` als `keywords`.

**Actie:** Tags toevoegen: `["making friends", "expat community", "social life", "netherlands"]`

---

## Prioriteit LAAG (nice-to-have, geen urgentie)

### 7. Inconsistent type frontmatter
16 van ~82 guide articles hebben een `type` veld (guide, seasonal guide, city-guide, pillar), de rest niet. Hugo gebruikt `type` voor template selectie — in de huidige setup maakt dit geen verschil omdat er geen type-specifieke templates zijn.

**Actie:** Ofwel overal verwijderen, ofwel consistent toevoegen. Geen functionele impact.

### 8. Redundante slug frontmatter
11 articles hebben een `slug` veld dat identiek is aan de bestandsnaam. Hugo leidt slug af uit bestandsnaam als het veld ontbreekt.

**Actie:** Kan verwijderd worden voor consistentie. Geen functionele impact.

### 9. Lege services/ directory
`content/services/` is een lege directory. Menu-item "Services" wijst naar `/guides/daily-life/`, niet naar `/services/`.

**Actie:** Directory verwijderen of `_index.md` toevoegen als de sectie in de toekomst gebruikt wordt.

### 10. Email signup forms zijn stubs
Sidebar en footer email forms hebben `action="#"` en `onsubmit="return false"`. Ze doen niets.

**Actie:** Email service integreren (Mailchimp, ConvertKit, etc.) of forms verwijderen om niet-functionele UI te voorkomen.

### 11. Tool pages missen featured_image
Alle 11 tool pages missen `featured_image`. Dit beïnvloedt OG image op social media.

**Impact:** Laag — tools worden zelden gedeeld op social media. Kan later aangevuld worden.

---

## Wat NIET moet (geen actie nodig)

| Item | Reden geen actie |
|------|-----------------|
| Tags taxonomy niet gedeclareerd in hugo.toml | Hugo declareert tags automatisch. Huidige config werkt correct. |
| Monolithische baseof.html (1584 regels) | Werkt correct, refactoring is risico zonder functioneel voordeel |
| CSS inline in baseof.html | Normal voor Hugo sites zonder build pipeline. Minificatie via `--minify` flag. |
| Tool templates als pass-through | By design — alle tool logica in content files. Werkt correct. |
| `draft: false` op 2 artikelen | Geen effect — Hugo behandelt pages als niet-draft by default |

---

## Eindstatus

**GROTENDEELS IN ORDE, NOG RESTPUNTEN**

De site is technisch stabiel voor 8 weken ongestoord draaien. De geïdentificeerde restpunten zijn:
- **Hoge prioriteit:** meer interne links naar near-orphan pages en tools vanuit city pages
- **Midden prioriteit:** missing images en frontmatter inconsistenties
- **Lage prioriteit:** cleanup items zonder functionele impact

Geen van de restpunten veroorzaakt 404's, indexatie-problemen, of rendering-fouten.
