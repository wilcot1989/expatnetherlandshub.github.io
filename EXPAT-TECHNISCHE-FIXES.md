# EXPAT-TECHNISCHE-FIXES.md
Peildatum: 9 maart 2026 | Definitieve versie

---

## Broken Internal Links — 49 instances opgelost

| Fout | Correct | Bestanden | Instances |
|------|---------|-----------|-----------|
| 30-percent-ruling-guide-2026 | 30-percent-ruling-netherlands-2026 | 5 | 16 |
| zzp-freelancer-guide-netherlands-2026 | freelancer-zzp-guide-netherlands-2026 | 4 | 7 |
| dutch-tax-system-expats-2026 (zonder -guide-) | dutch-tax-system-expats-guide-2026 | 4 | 11 |
| /guides/healthcare/ | /guides/health/ | 8 city pages | 8 |
| expat-insurance-netherlands-2026 | best-expat-insurance-netherlands-2026 | 1 | 3 |
| health-insurance-expats-netherlands-2026 | dutch-health-insurance-guide-expats-2026 | 1 | 2 |
| finding-housing-netherlands-2026 | finding-housing-netherlands-expats-2026 | 2 | 4 |
| moving-to-maastricht-guide-2026 | moving-to-maastricht-expat-guide-2026 | 1 | 1 |
| /guides/digid-guide-expats-2026/ | /guides/legal/digid-guide-expats-2026/ | 1 | 2 |
| dutch-language-courses-netherlands-2026 | best-dutch-language-courses-2026 | 1 | 2 |
| best-language-learning-apps-2026 | best-apps-learn-dutch-2026 | 1 | 2 |

---

## Affiliate Tracking Fixes

| Fix | Bestanden | Details |
|-----|-----------|---------|
| Wise bare/truncated URL → invite link | 3 tools | 30%-calc, bsn-planner, salary-checker |
| Independer awclick → cread deep link | 8 bestanden | 23 vervangingen totaal |
| Funda/Pararius cta-affiliate → cta | 1 tool | 4 links in housing-budget-checker |
| BSN planner gemeente cta-affiliate → cta | 1 tool | 1 link |

---

## Template Fixes

| Fix | Bestand | Details |
|-----|---------|---------|
| SearchAction verwijderd | baseof.html | Niet-functioneel endpoint /guides/?q= |
| Hardcoded "March 2026" → dynamisch | list.html | Nu {{ now.Format "January 2006" }} |
| Meta author per-page fallback | baseof.html | Was altijd global, nu pagina-specifiek |

---

## Content Hygiene

| Fix | Bestanden | Details |
|-----|-----------|---------|
| Self-referencing aliases verwijderd | 11 daily-life | Redundante aliases naar eigen URL |
| CTAs toegevoegd aan affiliate-flagged artikelen | 4 | tax-return-checklist, open-bank-account, best-cities, leaving-NL |
| Orphan pages gelinkt | 8+ | safetywing-vs-cigna, preply-vs-italki, phone-plans, etc. |

---

## Eerdere Sessie Fixes (commit 51c9714)

| Fix | Bestanden | Details |
|-----|-----------|---------|
| SafetyWing referenceID | 4 | Was DSP ID → correct 26482728 |
| NordVPN url_id | 3 | Was leeg → 14830 |
| Wise tracking inconsistentie | 2 | wise.prf.hn → invite link |
| Duplicate deploy workflow | 1 | scheduled-deploy.yml verwijderd |
| 51 nieuwe CTAs | 17 city pages | Wise + Independer + SafetyWing |
| Orphan pages + under-linked artikelen | 14+ | City index + guide artikelen |
