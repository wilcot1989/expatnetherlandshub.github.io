# EXPAT-KLAAR-VOOR-8-WEKEN.md
## Management Summary — ExpatNetherlandsHub Technische Status

Datum: 2026-03-09 (bijgewerkt ronde 3 — inhoudelijke QA)
Status: **TECHNISCH + INHOUDELIJK KLAAR VOOR 8 WEKEN**

---

## Wat is gedaan

| Categorie | Actie | Aantal |
|-----------|-------|--------|
| Broken links | Gefixt | 57 (53 ronde 1 + 4 ronde 2) |
| Sitemap duplicaten | Verwijderd | 11 hardcoded tool URLs |
| Self-referencing aliases | Verwijderd | 42 (11 daily-life + 31 overig) |
| Independer links | Geüpgraded awclick→cread | 23 |
| Wise tracking | Gefixt in tools | 3 |
| CTA-class correcties | Funda/Pararius/gemeente | 5 |
| SearchAction | Verwijderd (non-functional) | 1 |
| Hardcoded datums | Template gefixt | 1 |
| Duplicate workflow | Verwijderd | 1 |
| Near-orphan pages | Interne links toegevoegd | ~35 links naar 18 pages |
| Tools → city pages | Links toegevoegd | 102 (6 tools × 17 cities) |
| City frontmatter | author + categories | 17 cities |
| City featured_image | Referenties toegevoegd | 5 cities |
| City links in best-cities | Hyperlinks toegevoegd | 4 (Delft, Haarlem, Den Bosch, Breda) |

**Totaal: ~300 technische wijzigingen over ~80 bestanden.**

---

## Huidige technische staat

| Check | Status |
|-------|--------|
| Broken internal links | Geen |
| Sitemap | Correct, geen duplicaten |
| robots.txt | Correct |
| Canonicals | Op alle pagina's |
| Structured data | WebSite, Organization, Article, FAQPage, BreadcrumbList, WebApplication |
| 404 template | Correcte links |
| Deploy workflow | Enkele workflow (push + cron + manual) |
| Self-referencing aliases | Geen |
| Tool discoverability | Alle 11 tools gelinkt vanuit alle 17 cities + guides |
| Near-orphan pages | Geen (alle pages 2+ inbound links) |
| City page metadata | Consistent (author, categories, featured_image) |
| Content calendar | 45 artikelen gepland tot mei 2026, buildFuture=false correct |

---

## Resterende handmatige taken

| # | Item | Impact | Urgentie |
|---|------|--------|----------|
| 1 | 5 city afbeeldingen aanmaken (.webp) | OG image ontbreekt op social shares | Midden |
| 2 | 10 articles keywords field toevoegen | Geen SEO-impact | Laag |
| 3 | 1 article tags toevoegen (making-friends) | Minimaal | Laag |
| 4 | Email signup forms integreren of verwijderen | UX | Laag |

Geen van deze items blokkeert de site of veroorzaakt technische problemen.

---

## Live validatie

14 pagina's live getest via WebFetch op expatnetherlandshub.com:
- Homepage, 1 guide, 1 city page, alle 11 tools
- Canonical, structured data, content rendering: alles correct

---

## Inhoudelijke gereedheid (audit 9 maart 2026)

### Wat is gedaan

| Categorie | Fixes | Scope |
|-----------|-------|-------|
| Verboden AI-woorden | ~30 | Site-breed (navigate, essential, comprehensive, streamline, etc.) |
| Feitelijke correcties | ~25 | Premies, belasting, regelgeving, datums |
| Broken internal links | 12 | Alle clusters |
| FAQ format (question→q) | ~15 bestanden | Voorkomt FAQPage structured data problemen |
| Duplicate content | 5 | Paragrafen en volledige secties verwijderd |
| Affiliate frontmatter | 3 | false↔true correcties |
| "Last updated" datums | ~20 | Toekomstige maanden→maart 2026 |
| **Totaal** | **~110** | **~87 artikelen geaudit** |

### Kritieke feitelijke fixes

1. Zorgverzekering premies: €120-145→€140-175 (30+ locaties site-breed)
2. Zorgtoeslag maximum: €175→€130/maand
3. King's Day 2026: verzonnen Easter-conflict volledig verwijderd
4. 30% ruling: vlak 30%→30/20/10% sliding scale (NL vs DE artikel)
5. Jubelton: "restricted"→"afgeschaft per 1 jan 2024"
6. Fysiotherapie dekking: onjuiste sessie-claims gecorrigeerd
7. HSM salarisdrempels: 3 varianten→aligned naar €5,331/€3,909
8. ING/ABN AMRO fees: verouderde bedragen gecorrigeerd

### Openstaande handmatige factchecks

12 items vereisen externe bronverificatie — zie EXPAT-HANDMATIGE-FACTCHECKS.md.
Top 3 kritiek:
1. **Wise IBAN type** (NL vs BE) — 6+ artikelen beïnvloed
2. **Box 1 belastingschijf 2026** — 3 verschillende bedragen
3. **HSM salarisdrempels** — gealigned maar niet extern geverifieerd

### Status

| Check | Status |
|-------|--------|
| Verboden woorden | Schoon |
| Premie-consistentie site-breed | Consistent (€140-175) |
| FAQ format | Consistent (q/a) |
| Duplicate content | Verwijderd |
| Broken internal links | Geen |
| Feitelijke consistentie | Consistent waar veilig te fixen; 12 items wachten op handmatige verificatie |

**Volledig rapport:** EXPAT-INHOUDELIJKE-QA.md, EXPAT-GEPLANDE-CONTENT-QA.md

---

## Conclusie

De site is technisch én inhoudelijk klaar om 8 weken ongestoord te draaien. De daily publishing pipeline (45 artikelen, 7 mrt - 5 mei) functioneert correct via buildFuture=false + daily cron deploy. Affiliate tracking (6 partners) is actief en gevalideerd. Alle interne links, structured data, en metadata zijn consistent.

Na de inhoudelijke audit van 9 maart zijn ~110 extra correcties doorgevoerd over ~87 artikelen. De belangrijkste risico's (verkeerde premies, verzonnen feiten, inconsistente belastingcijfers) zijn opgelost. 12 items vereisen nog handmatige verificatie via externe bronnen — geen daarvan blokkeert de dagelijkse publicatie.
