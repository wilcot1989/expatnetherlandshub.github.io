# EXPAT-GEPLANDE-CONTENT-QA.md
## QA op Geplande/Toekomstige Content — ExpatNetherlandsHub
Datum: 2026-03-09

---

## Scope

QA-review van alle ~47 artikelen met toekomstige publicatiedatum (maart–mei 2026) die via de daily publishing pipeline (buildFuture=false + cron deploy) live gaan.

---

## Methode

Alle geplande artikelen zijn mee-geaudit in de cluster-audits. Ze staan in dezelfde directories als live content en zijn op dezelfde criteria gecontroleerd:
- Verboden woorden
- Feitelijke consistentie (premies, belasting, regelgeving)
- FAQ format (q/a keys)
- Broken internal links
- Duplicate content
- Affiliate frontmatter
- Datum-headers

---

## Resultaten per categorie

### Geplande artikelen met fixes

| Bestand | Publicatiedatum | Fixes |
|---------|----------------|-------|
| apostille-legalization-netherlands-2026 | 2026-03-26 | Datum frontmatter→maart 2026, FAQ format |
| dutch-nationality-guide-expats-2026 | 2026-04-03 | Datum→maart 2026, FAQ format |
| leaving-netherlands-expat-checklist-2026 | 2026-05-04 | Datum→maart 2026 |
| kings-day-guide-expats-2026 | Gepland | Easter-conflict fout, FAQ format |
| dutch-employment-contract-explained-2026 | Gepland | FAQ format |
| job-interview-tips-netherlands-2026 | Gepland | FAQ format |
| best-dutch-phone-plans-expats-2026 | Gepland | FAQ format |
| exchange-driving-license-netherlands-2026 | Gepland | FAQ format |
| register-car-netherlands-expat-2026 | Gepland | Dubbele FAQ-body verwijderd |
| energy-providers-expats-netherlands-2026 | Gepland | Duplicate paragraaf |
| expat-mortgage-options-netherlands-2026 | Gepland | Dubbele sectie verwijderd |
| funda-vs-pararius-housing-2026 | Gepland | FAQ format |
| moving-to-leiden-expat-guide-2026 | Gepland | FAQ format |
| moving-to-breda-guide-2026 | Gepland | FAQ format, premie |

### Geplande artikelen — schoon (geen issues gevonden)

De overige ~33 geplande artikelen zijn gecontroleerd en bevatten geen verboden woorden, feitelijke inconsistenties, broken links, of format-problemen.

---

## Belangrijkste risico's in geplande content

1. **King's Day 2026** — Bevatte een compleet verzonnen feit (Easter-conflict). Nu gecorrigeerd.
2. **FAQ format inconsistentie** — ~10 geplande artikelen gebruikten `question`/`answer` in plaats van `q`/`a`. Dit kan FAQPage structured data breken in Hugo. Nu allemaal gecorrigeerd.
3. **Duplicate secties** — 2 artikelen hadden volledige dubbele secties (mortgage guide, car registration). Verwijderd.

---

## Beoordeling

De geplande content is nu inhoudelijk klaar voor publicatie. De FAQ format-fix is de belangrijkste — zonder die fix zouden ~10 artikelen mogelijk geen FAQPage structured data genereren bij publicatie.

Items die nog externe verificatie nodig hebben staan in EXPAT-HANDMATIGE-FACTCHECKS.md.
