# SEO Audit — ExpatNetherlandsHub.com — Maart 2026

## Directe Concurrenten

| Concurrent | DA (est.) | Content | Tools | Monetisatie | Zwakte |
|---|---|---|---|---|---|
| **IamExpat.nl** | 70+ | 500+ pagina's, job board, events | Geen eigen tools | Ads, sponsored, directory | Ad-heavy, geen calculators |
| **Expatica.com** | 70+ | 1000+ pagina's, 50+ landen | Geen tools | Ads, sponsored | Generiek, niet NL-specifiek |
| **DutchReview.com** | 50+ | 300+ pagina's, nieuws + guides | Geen tools | Ads, affiliate | Meer nieuws dan tools |
| **NLCompass.com** | Laag (nieuw) | 46+ guides, 181 FAQs | 30% calc, cost-of-living, checklist | Service directory (330 listings) | Dunne content, weinig deep tools |
| **ExpatGuide.nl** | 40+ | Blog + directory | Geen tools | Directory listings | Verouderd |
| **Zorgwijzer.nl** | 60+ | Health insurance focus | Vergelijker | Affiliate (Independer) | Alleen verzekeringen |

**Onze USP:** 10 interactieve tools > alle concurrenten gecombineerd.

---

## Score: 7.2 / 10

### Sterke punten
- 10 unieke tools (9/10) — geen concurrent heeft dit
- 38 guides, 22 boven 3000 woorden (8/10)
- On-page basics: canonical, OG, twitter cards, meta desc (8/10)
- Duidelijke /guides/[cluster]/ structuur (7/10)

---

## KRITIEKE PROBLEMEN

### 1. Nauwelijks geindexeerd (KRITIEK)
`site:expatnetherlandshub.com` = 1 resultaat. Oorzaken: nieuwe site, tag page bloat, geen actieve indexing push.

### 2. 196 tags → ~98 dunne tag-pagina's (KRITIEK)
Hugo genereert automatisch pagina per tag. Verspilt crawl budget, thin content signalen.
**Fix:** noindex op tags OF taxonomie uitschakelen.

### 3. Geen Article schema (HOOG)
`single.html` heeft alleen BreadcrumbList. Mist Article/BlogPosting JSON-LD → geen rich snippets.

### 4. Geen WebSite/Organization schema homepage (HOOG)
Mist WebSite + SearchAction + Organization. Concurrenten hebben dit wel.

### 5. 7 van 12 featured_image SVGs bestaan niet (HOOG)
Breekt OG images voor social sharing. Ontbrekend: career, culture, family, housing, insurance, lifestyle, transport, work.

### 6. /services/ in nav maar pagina bestaat niet (MEDIUM)

### 7. 4 artikelen met 0 interne links (MEDIUM)
grocery delivery, cycling, NL vs DE, OV-chipkaart

---

## ACTIEPLAN

| # | Actie | Impact | Effort | Status |
|---|---|---|---|---|
| 1 | Tag pagina's noindex of taxonomy disablen | Kritiek | Laag | DONE (d39b250) |
| 2 | Article + FAQPage schema op single.html | Hoog | Medium | DONE (d39b250) |
| 3 | WebSite + Organization schema homepage | Hoog | Laag | DONE (d39b250) |
| 4 | Ontbrekende category SVGs aanmaken (8) | Hoog | Laag | DONE (d39b250) |
| 5 | Search Console indexing push | Kritiek | Laag | SCRIPT KLAAR — handmatig uitvoeren |
| 6 | 4 artikelen internal links toevoegen | Medium | Laag | DONE (d39b250) |
| 7 | About page uitbreiden (E-E-A-T, 1000+ woorden) | Medium | Laag | DONE (d39b250) |
| 8 | /services/ pagina bouwen | Medium | Laag | DONE (d39b250) |
| 9 | Sitemap priorities fixen | Laag | Medium | DONE (d39b250) |
| 10 | hreflang toevoegen | Laag | Laag | DONE (d39b250) |

---

## KANSEN vs. CONCURRENTIE

1. **Tool-zoekwoorden:** 7 tools zonder concurrentie (housing budget, inburgering, diploma, BSN, insurance chooser, visa finder, bank chooser)
2. **City long-tails:** "cost of living eindhoven 2026", "BSN appointment rotterdam"
3. **FAQ rich snippets:** FAQPage schema op artikelen → featured snippets
4. **Vergelijkings-content:** "ING vs ABN AMRO expat", "Zilveren Kruis vs CZ"
5. **Backlinks via tools:** Elk tool is linkbaar content → outreach naar expat communities
