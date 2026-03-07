# Technische SEO Audit — expatnetherlandshub.com

**Datum:** 7 maart 2026
**Overall score:** 7.3 / 10
**Doel:** 10/10 via gefaseerd actieplan

---

## Scores per categorie

| # | Categorie | Score | Status |
|---|-----------|-------|--------|
| 1 | Crawlability & Indexing | 6/10 | Kritieke problemen |
| 2 | Site Architecture & Internal Links | 5/10 | 227 broken links |
| 3 | On-Page SEO | 7/10 | Descriptions te lang |
| 4 | Structured Data / Schema | 6/10 | Duplicate JSON-LD |
| 5 | Page Speed & Core Web Vitals | 7/10 | Inline CSS, font loading |
| 6 | Mobile & UX | 8/10 | Goed |
| 7 | Content Quality & Thin Pages | 8/10 | Near-duplicates, geen images |
| 8 | Security & Technical | 9/10 | HTTPS, headers OK |
| 9 | International SEO | 8/10 | hreflang aanwezig |
| 10 | Monitoring & Analytics | 8/10 | GA4 + Consent Mode v2 |

---

## 1. Crawlability & Indexing (6/10)

### Problemen

**KRITIEK — Sitemap XML namespace is verkeerd**
- `themes/starter/layouts/_default/sitemap.xml` gebruikt `http://www.w3.org/2000/Sitemaps/0.9`
- Moet zijn: `http://www.sitemaps.org/schemas/sitemap/0.9`
- Google kan de sitemap hierdoor mogelijk niet correct parsen

**KRITIEK — 10 tool pages niet in sitemap**
- Alle tools in `static/tools/` zijn statische HTML buiten Hugo's content pipeline
- Hugo genereert de sitemap alleen voor content/ — tools worden overgeslagen
- Tools hebben ook geen canonical tags

**HOOG — Geen 404 template**
- `themes/starter/layouts/404.html` bestaat niet
- Hugo valt terug op een kale pagina zonder navigatie
- Bezoekers die op een broken link landen krijgen geen helpende pagina

**INFO — robots.txt is correct**
```
User-agent: *
Allow: /
Sitemap: https://expatnetherlandshub.com/sitemap.xml
```

**INFO — buildFuture = false werkt correct**
- Toekomstige artikelen worden niet gebouwd tot hun publicatiedatum
- Deploy draait dagelijks om 08:00 UTC → artikelen gaan automatisch live

### Fixes
1. Fix sitemap namespace URL
2. Voeg 10 tool pages toe aan sitemap (custom sitemap template of handmatige entries)
3. Voeg canonical tags toe aan alle 10 tool HTML pagina's
4. Maak 404.html template aan met navigatie en zoeksuggesties

---

## 2. Site Architecture & Internal Links (5/10)

### Problemen

**KRITIEK — 227 broken interne links naar /posts/**
- 38 content bestanden bevatten links naar `/posts/...` in plaats van `/guides/[cluster]/...`
- Dit zijn legacy URLs van vóór de site-restructurering
- Hugo genereert alias-redirects (meta-refresh) van `/posts/` naar `/guides/`, maar:
  - Meta-refresh redirects zijn NIET gelijk aan 301 redirects voor SEO
  - Link equity gaat verloren
  - Crawl budget wordt verspild op redirect chains
- **Voorbeeld:** `/posts/30-percent-ruling-explained/` → moet zijn `/guides/finance/30-percent-ruling-explained/`

**MEDIUM — Geen pagination op list pages**
- `themes/starter/layouts/_default/list.html` toont alle artikelen in een sectie zonder pagination
- Bij groei naar 100+ artikelen wordt dit een performance probleem

### Fixes
1. Vervang alle 227 `/posts/`-links door correcte `/guides/[cluster]/slug/` paden in 38 bestanden
2. Overweeg pagination voor sectiepagina's (niet urgent bij huidige schaal)

---

## 3. On-Page SEO (7/10)

### Problemen

**MEDIUM — 64 artikelen missen lastmod**
- Front matter bevat `date` maar geen `lastmod`
- Google gebruikt lastmod voor freshness signalen in de sitemap
- Zonder lastmod toont de sitemap alleen de publicatiedatum

**MEDIUM — 26 descriptions langer dan 155 karakters**
- Google kapt meta descriptions af na ~155 tekens
- Langere descriptions worden afgebroken in zoekresultaten

**LAAG — 4 artikelen gebruiken `category:` i.p.v. `categories:`**
- Hugo verwacht `categories:` (array) — `category:` (singular) wordt mogelijk niet correct verwerkt
- Artikelen verschijnen mogelijk niet in de juiste categorie-listing

### Fixes
1. Voeg `lastmod:` toe aan alle 64 artikelen (= publicatiedatum als startwaarde)
2. Verkort 26 descriptions tot max 155 karakters
3. Fix 4 artikelen: `category:` → `categories:` array

---

## 4. Structured Data / Schema (6/10)

### Problemen

**KRITIEK — Duplicate JSON-LD blocks**
- `baseof.html` bevat JSON-LD voor: Article + BreadcrumbList (op artikel-pagina's)
- `single.html` bevat OOK JSON-LD voor: Article + BreadcrumbList
- Resultaat: elke artikelpagina heeft DUBBELE Article en BreadcrumbList schemas
- Google's Rich Results Test kan hierdoor verwarrende resultaten geven
- Zelfde probleem op `list.html` (duplicate BreadcrumbList) en `index.html` (duplicate WebSite)

**HOOG — Tool pages missen structured data**
- 10 statische tool HTML pagina's hebben geen WebApplication of SoftwareApplication schema
- Kans gemist voor rich snippets bij tool-gerelateerde zoekopdrachten

**INFO — Aanwezige schemas (als ze niet dubbel waren):**
- Article + FAQPage op artikelpagina's ✓
- BreadcrumbList op alle pagina's ✓
- WebSite + Organization op homepage ✓

### Fixes
1. Verwijder duplicate JSON-LD uit single.html, list.html en index.html (behoud in baseof.html met conditionals)
2. OF: verwijder uit baseof.html en houd per-template schemas (schonere aanpak)
3. Voeg WebApplication schema toe aan tool pages

---

## 5. Page Speed & Core Web Vitals (7/10)

### Problemen

**HOOG — ~60KB inline CSS in baseof.html**
- Alle CSS staat inline in `<style>` tags in baseof.html (~1527 regels totaal in het template)
- Voordeel: geen render-blocking CSS request
- Nadeel: CSS is NIET cacheable — elke pageload downloadt de volledige CSS opnieuw
- Bij terugkerende bezoekers is een extern CSS-bestand met caching efficienter

**MEDIUM — Google Fonts loading incomplete**
- `preconnect` naar fonts.googleapis.com en fonts.gstatic.com ✓
- Maar font stylesheet wordt geladen als render-blocking `<link rel="stylesheet">`
- Beter: `font-display: swap` + async loading of `<link rel="preload" as="style">`

**INFO — Geen JavaScript frameworks**
- Site is pure HTML/CSS — geen React, Vue, etc.
- Dit is een groot voordeel voor Core Web Vitals

### Fixes
1. Overweeg CSS naar extern bestand met caching headers (optioneel — afweging inline vs cached)
2. Voeg `&display=swap` toe aan Google Fonts URL als dat nog niet het geval is
3. Laad Google Fonts async met media="print" onload pattern

---

## 6. Mobile & UX (8/10)

### Sterke punten
- Responsive design met CSS Grid/Flexbox ✓
- Mobile hamburger menu via CSS checkbox hack (geen JS) ✓
- Touch targets zijn groot genoeg ✓
- Viewport meta tag correct ✓

### Problemen

**LAAG — Mega-menu hover op mobile**
- Desktop mega-menu werkt op hover — op mobile via checkbox toggle
- Werkt functioneel maar de transitie is niet smooth

---

## 7. Content Quality (8/10)

### Problemen

**MEDIUM — 2 near-duplicate artikelparen**
- Tax return + tax system: overlappende content over belastingaangifte
- Mortgage + mortgage options: beide behandelen hypotheken voor expats
- Risico op keyword cannibalisatie

**MEDIUM — Geen inline images in artikelen**
- Alle ~70 artikelen bevatten alleen tekst — geen screenshots, infographics, foto's
- featured_image is ingesteld (SVG per categorie) maar er zijn geen images IN de artikeltekst
- Google beloont visueel rijke content; concurrenten als IamExpat en DutchReview gebruiken inline images

**INFO — Forbidden words check: CLEAN**
- Alle 137 hits in 51 bestanden gefixt op 7 maart 2026
- "dynamic" behouden in energy-providers (technische term)

### Fixes
1. Consolideer of differentieer de 2 near-duplicate paren (canonical of merge)
2. Start met inline images toevoegen — minimaal 1-2 per pillar artikel

---

## 8. Security & Technical (9/10)

### Sterke punten
- HTTPS via GitHub Pages ✓
- Geen mixed content ✓
- Geen open redirects ✓
- CSP headers via GitHub Pages defaults ✓

---

## 9. International SEO (8/10)

### Sterke punten
- hreflang="en" aanwezig ✓
- Alle content in het Engels ✓
- .com domein (internationaal neutraal) ✓

### Problemen

**LAAG — Geen x-default hreflang**
- `x-default` ontbreekt — best practice voor single-language sites is `x-default` + `en`

---

## 10. Monitoring & Analytics (8/10)

### Sterke punten
- GA4 (G-2TJSDJB4CG) met Consent Mode v2 ✓
- Google Search Console verified + sitemap submitted ✓

### Problemen

**LAAG — Geen event tracking op tool interactions**
- Tools hebben geen GA4 custom events voor conversies (calculator submits, wizard completions)
- Geen manier om tool engagement te meten

---

## Actieplan — Gefaseerd naar 10/10

### Fase 1 — KRITIEK (direct uitvoeren, score 7.3 → 8.5)

| # | Actie | Impact | Effort | Bestanden |
|---|-------|--------|--------|-----------|
| 1 | Fix 227 /posts/-links → /guides/ paden | Kritiek | Hoog | 38 content files |
| 2 | Fix sitemap XML namespace | Kritiek | Laag | 1 template |
| 3 | Verwijder duplicate JSON-LD | Kritiek | Medium | 3-4 templates |
| 4 | Voeg 10 tool pages toe aan sitemap | Kritiek | Medium | sitemap template + 10 HTML files |
| 5 | Voeg canonical tags toe aan tool pages | Hoog | Laag | 10 HTML files |
| 6 | Maak 404.html template | Hoog | Laag | 1 nieuw template |
| 7 | Voeg lastmod toe aan 64 artikelen | Hoog | Medium | 64 content files |
| 8 | Fix 4x category: → categories: | Hoog | Laag | 4 content files |

### Fase 2 — HOOG (week 2, score 8.5 → 9.0)

| # | Actie | Impact | Effort |
|---|-------|--------|--------|
| 9 | Verkort 26 descriptions tot max 155 chars | Medium | Medium |
| 10 | Fix Google Fonts async loading | Medium | Laag |
| 11 | Voeg WebApplication schema toe aan tools | Medium | Medium |
| 12 | Consolideer 2 near-duplicate paren | Medium | Medium |

### Fase 3 — MEDIUM (week 3-4, score 9.0 → 9.5)

| # | Actie | Impact | Effort |
|---|-------|--------|--------|
| 13 | Voeg inline images toe aan pillar artikelen | Medium | Hoog |
| 14 | CSS naar extern bestand met caching | Laag | Medium |
| 15 | GA4 event tracking op tools | Laag | Medium |
| 16 | Voeg x-default hreflang toe | Laag | Laag |

### Fase 4 — LAAG (maand 2, score 9.5 → 10)

| # | Actie | Impact | Effort |
|---|-------|--------|--------|
| 17 | Pagination op list pages | Laag | Medium |
| 18 | Image optimization pipeline (WebP/AVIF) | Laag | Hoog |
| 19 | Preload critical fonts | Laag | Laag |
| 20 | Structured data testing & validation pass | Laag | Medium |
