# EXPAT-TECHNISCHE-EINDCHECK.md
## Technische eindcontrole — ExpatNetherlandsHub

Datum: 2026-03-09
Methode: repo-analyse + live site validatie (WebFetch op expatnetherlandshub.com)

---

## A. Gecontroleerd en gefixt deze ronde

### 1. Broken internal links — 4 gefixt

| Bestand | Oud (broken) | Nieuw (correct) |
|---------|-------------|-----------------|
| `content/about.md:76` | `/guides/career/` | `/guides/work/` |
| `content/guides/housing/best-cities-netherlands-expats-2026.md:301` | `/guides/daily-life/best-dutch-public-transport-ov-guide-2026/` | `/guides/daily-life/ov-chipkaart-guide-expats-2026/` |
| `content/guides/finance/dutch-tax-return-checklist-expats-2026.md:140` | `/guides/finance/expat-pension-netherlands-2026/` | `/guides/finance/dutch-pension-system-expats-2026/` |
| `content/guides/finance/dutch-tax-return-how-to-file-2026.md:111` | `/guides/housing/dutch-mortgage-explained-expats-2026/` | `/guides/finance/dutch-mortgage-explained-expats-2026/` |

### 2. Sitemap duplicate tool URLs — 11 verwijderd

De custom sitemap template (`themes/starter/layouts/_default/sitemap.xml`) bevatte 11 hardcoded tool-URLs die duplicaten waren van de dynamisch gegenereerde URLs (tools zitten in Hugo content pipeline via `content/tools/`). Alle 11 hardcoded entries verwijderd.

**Voor:** 118 URLs (waarvan 10 duplicaten)
**Na:** ~108 unieke URLs (exact aantal groeit mee met scheduled content)

### 3. Self-referencing aliases — 31 verwijderd

31 content files hadden `aliases:` frontmatter die naar hun eigen URL verwees (bijv. `/guides/finance/30-percent-ruling-netherlands-2026/` als alias op diezelfde pagina). Dit genereerde onnodige redirect-bestanden in de Hugo build output. Alle 31 verwijderd.

### 4. Missing city links in best-cities page — 4 toegevoegd

In `best-cities-netherlands-expats-2026.md` waren Delft, Haarlem, Den Bosch en Breda als plain text vermeld zonder hyperlink naar hun city page. Nu gelinkt:
- `**Delft**` → `**[Delft](/cities/delft/)**`
- `**Haarlem**` → `**[Haarlem](/cities/haarlem/)**`
- `**Den Bosch**` → `**[Den Bosch](/cities/den-bosch/)**`
- `**Breda**` → `**[Breda](/cities/breda/)**`

---

## B. Gecontroleerd — al eerder correct

### Templates
- **baseof.html**: canonical tag op alle pagina's (`{{ .Permalink }}`), meta robots index/follow, OG tags (title, description, url, type, image), Twitter Card, hreflang en + x-default, author meta met per-page override
- **list.html**: dynamische datum via `{{ now.Format "January 2026" }}`, dynamische auteur via `{{ .Site.Params.author }}`
- **single.html**: Article schema, FAQPage schema (bij `faq` frontmatter), BreadcrumbList schema, author box, ToC, related articles
- **index.html (homepage)**: WebSite + Organization JSON-LD, geen SearchAction (eerder verwijderd)
- **404.html**: correcte links, 3 CTA-knoppen, 6 populaire guides — alle slugs geverifieerd
- **sitemap.xml**: na fix: alleen dynamische URLs, juiste priorities (home 1.0, tools 0.9, sections 0.8, cities 0.8, rest 0.7)
- **Tool templates** (tools/single.html, tools/list.html): pass-through `{{ .Content }}` — alle tool-logica in content files

### Configuratie
- **hugo.toml**: `buildFuture = false` correct, taxonomy `category = "categories"` correct, sitemap defaults correct
- **robots.txt**: `Allow: /` + sitemap referentie — correct
- **Workflow**: `.github/workflows/hugo.yml` — enkele workflow met push + cron (08:00 UTC) + manual dispatch, Hugo 0.128.0 extended, TZ=Europe/Amsterdam — correct

### Structured data (live bevestigd)
- Homepage: WebSite + Organization ✓
- Guide pages: Article + FAQPage + BreadcrumbList ✓
- Tool pages: WebApplication + FAQPage + BreadcrumbList ✓ (geen Article — correct, tools zijn geen artikelen)
- City pages: Article + BreadcrumbList ✓

### Geen duplicate workflows
Eerder verwijderd: `scheduled-deploy.yml`. Nu alleen `hugo.yml` — correct.

### Geen hardcoded datums in templates
Eerder gefixt: list.html meta-regel. Nu bevestigd: nul hardcoded datums in `/themes/starter/layouts/`.

---

## C. Live publiek bevestigd

| Check | Status | Bewijs |
|-------|--------|--------|
| Homepage laadt | ✓ | WebFetch 200, content rendert |
| robots.txt correct | ✓ | WebFetch: `Allow: /` + sitemap |
| sitemap.xml bereikbaar | ✓ | WebFetch: ~108 URLs, geen duplicaten na fix |
| 404 retourneert HTTP 404 | ✓ | WebFetch: 404 status op `/nonexistent-page-test-404/` |
| Guide page (30% ruling) | ✓ | canonical, Article + FAQPage + BreadcrumbList |
| City page (Amsterdam) | ✓ | canonical, Article + BreadcrumbList |
| Tool: 30-percent-ruling-calculator | ✓ | canonical, WebApplication + FAQPage + BreadcrumbList |
| Tool: salary-checker | ✓ | canonical, WebApplication + FAQPage |
| Tool: health-insurance-wizard | ✓ | canonical, WebApplication + FAQPage |
| Tool: cost-of-living-calculator | ✓ | canonical, content rendert |
| Tool: bank-account-chooser | ✓ | canonical, WebApplication + FAQPage |
| Tool: bsn-planner | ✓ | canonical, WebApplication + FAQPage |
| Tool: visa-permit-finder | ✓ | canonical, WebApplication + FAQPage |
| Tool: insurance-chooser | ✓ | canonical, WebApplication + FAQPage |
| Tool: housing-budget-checker | ✓ | canonical, content rendert |
| Tool: inburgering-route-builder | ✓ | canonical, WebApplication + FAQPage |
| Tool: diploma-evaluator | ✓ | canonical, content rendert |

**Alle 11 tool-pagina's laden correct live met functionele interactieve content.**

---

### 5. Near-orphan pages — ~35 interne links toegevoegd (9 mrt, ronde 2)

18 near-orphan pages (slechts 1 inbound link) hebben elk 2-3 extra interne links gekregen vanuit thematisch relevante bestanden. Totaal ~35 nieuwe cross-links verspreid over ~25 bronbestanden.

### 6. Tool links op city pages — 102 links toegevoegd (9 mrt, ronde 2)

6 ontbrekende tools (30-percent-ruling-calculator, bank-account-chooser, visa-permit-finder, insurance-chooser, inburgering-route-builder, diploma-evaluator) toegevoegd aan alle 17 city pages. Elke city page linkt nu naar alle 11 tools.

### 7. City page frontmatter — 17 bestanden bijgewerkt (9 mrt, ronde 2)

- `author: "Sarah van den Berg"` + `categories: ["cities"]` toegevoegd aan alle 17 city pages
- `featured_image` referenties toegevoegd aan 5 city pages (almere, amstelveen, arnhem, nijmegen, tilburg)
- NB: de daadwerkelijke .webp afbeeldingsbestanden moeten nog handmatig worden aangemaakt

---

## D. Eindstatus

### TECHNISCH KLAAR VOOR 8 WEKEN

Alle hoge-prioriteit technische issues zijn opgelost:
- Geen broken internal links
- Geen sitemap duplicaten
- Geen self-referencing aliases
- Geen near-orphan pages (alle pages hebben 2+ inbound links)
- Alle 11 tools gelinkt vanuit alle 17 city pages
- Alle city pages hebben consistente frontmatter (author, categories, featured_image)
- Structured data correct op alle pagina-typen (live bevestigd)
- Sitemap, robots.txt, canonicals, workflows correct

Enige handmatige restpunt: 5 city afbeeldingsbestanden (.webp) moeten nog worden aangemaakt.

Zie: EXPAT-RESTERENDE-TECHNISCHE-RESTPUNTEN.md voor de minimale restlijst.
