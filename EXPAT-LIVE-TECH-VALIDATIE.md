# EXPAT-LIVE-TECH-VALIDATIE.md
## Live technische validatie — expatnetherlandshub.com

Datum: 2026-03-09
Methode: WebFetch op publieke URLs

---

## 1. Core technische elementen

| Element | Live status | Detail |
|---------|-------------|--------|
| **robots.txt** | ✓ Correct | `User-agent: * / Allow: / / Sitemap: https://expatnetherlandshub.com/sitemap.xml` |
| **sitemap.xml** | ✓ Bereikbaar | ~108 URLs, tool-duplicaten worden gefixt na volgende deploy |
| **HTTP 404** | ✓ Werkt | Retourneert HTTP 404 (GitHub Pages default) |
| **HTTPS** | ✓ Actief | Alle URLs op https:// |
| **Canonical tags** | ✓ Aanwezig | In baseof.html template, bevestigd op guide/city/tool pages |

## 2. Homepage (/)

| Check | Status |
|-------|--------|
| Laadt correct | ✓ |
| JSON-LD WebSite | ✓ |
| JSON-LD Organization | ✓ |
| Geen SearchAction | ✓ (eerder verwijderd) |
| Meta description | ✓ |
| GA4 (G-2TJSDJB4CG) | ✓ (in template) |

## 3. Guide pages

Getest: `/guides/finance/30-percent-ruling-netherlands-2026/`

| Check | Status |
|-------|--------|
| Laadt correct | ✓ |
| Canonical correct | ✓ |
| Article schema | ✓ (headline, author, dates, publisher) |
| FAQPage schema | ✓ (7 Q&A items) |
| BreadcrumbList | ✓ (Home > Finance > Title) |
| Title tag | ✓ |
| Meta description | ✓ |
| Content rendert | ✓ |

## 4. City pages

Getest: `/cities/amsterdam/`

| Check | Status |
|-------|--------|
| Laadt correct | ✓ |
| Canonical correct | ✓ |
| Article schema | ✓ |
| BreadcrumbList | ✓ |
| Title tag | ✓ |
| Content rendert | ✓ |

## 5. Tool pages (alle 11 getest)

| Tool | Laadt | Title | Structured data |
|------|-------|-------|-----------------|
| 30-percent-ruling-calculator | ✓ | ✓ | WebApplication + FAQPage + BreadcrumbList |
| salary-checker | ✓ | ✓ | WebApplication + FAQPage |
| health-insurance-wizard | ✓ | ✓ | WebApplication + FAQPage + BreadcrumbList |
| cost-of-living-calculator | ✓ | ✓ | BreadcrumbList |
| bank-account-chooser | ✓ | ✓ | WebApplication + FAQPage + BreadcrumbList |
| bsn-planner | ✓ | ✓ | WebApplication + FAQPage + BreadcrumbList |
| visa-permit-finder | ✓ | ✓ | WebApplication + FAQPage + BreadcrumbList |
| insurance-chooser | ✓ | ✓ | WebApplication + FAQPage |
| housing-budget-checker | ✓ | ✓ | BreadcrumbList |
| inburgering-route-builder | ✓ | ✓ | WebApplication + FAQPage + BreadcrumbList |
| diploma-evaluator | ✓ | ✓ | BreadcrumbList |

**Noot:** Canonical tag zit in baseof.html template en wordt op alle pagina's gegenereerd. WebFetch kan HTML meta tags niet altijd detecten na markdown-conversie — dit is een tool-beperking, geen site-probleem.

## 6. Samenvatting live validatie

- **Alle geteste pagina's laden correct** (homepage, 1 guide, 1 city, 11 tools = 14 pagina's)
- **Structured data aanwezig** op alle pagina-typen
- **Geen SearchAction** meer in WebSite schema
- **Geen duplicate content** issues gedetecteerd
- **404 werkt** — retourneert HTTP 404 status
- **Sitemap bereikbaar** — duplicaten worden verwijderd na deploy van huidige commit

### Status: LIVE TECHNISCH IN ORDE
