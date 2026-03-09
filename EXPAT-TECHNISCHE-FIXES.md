# EXPAT — Technische Fixes Stabilisatiepass
Peildatum: 9 maart 2026

---

## Affiliate Link Fixes

### 1. SafetyWing referenceID fout (4 bestanden)
Was: `digitalshieldpro` (DSP site ID) — Gecorrigeerd naar: `26482728`

- best-expat-insurance-netherlands-2026.md
- safetywing-vs-cigna-expat-insurance-2026.md
- highly-skilled-migrant-visa-netherlands-2026.md
- complete-guide-moving-to-netherlands-2026.md (already correct, verified)

### 2. NordVPN url_id leeg (3 bestanden)
Was: `url_id=` — Gecorrigeerd naar: `url_id=14830`

- best-gyms-fitness-netherlands-2026.md (2x)
- dutch-holidays-traditions-expat-guide-2026.md

### 3. Wise tracking URL inconsistentie (2 bestanden)
Was: `wise.prf.hn` — Gecorrigeerd naar: `wise.com/invite/ihpc/willemt52`

- dutch-pension-system-expats-2026.md
- moving-to-utrecht-guide-2026.md

---

## Structurele Fixes

### 4. Duplicate deploy workflow
`scheduled-deploy.yml` verwijderd — was identiek aan de cron trigger in `hugo.yml`.

### 5. Cities index bijgewerkt
`content/cities/_index.md` bijgewerkt met alle 17 stadsgidsen.

### 6. Orphan pages opgelost
5 steden + 9 artikelen voorzien van inbound links vanuit relevante pillar- en cluster-pagina's.

### 7. Diploma-evaluator tool
4 nieuwe inbound links toegevoegd vanuit relevante artikelen.

---

## Monetisatie Verbeteringen

### 8. Stadspagina's — Getting Started sectie
Alle 17 stadsgidsen voorzien van een "Getting Started" sectie met 3 affiliate CTAs:
- Wise (bankrekening openen)
- Independer (zorgverzekering vergelijken)
- SafetyWing (tijdelijke expat verzekering)

Totaal: 51 nieuwe CTAs toegevoegd.

### 9. preply-vs-italki artikel geactiveerd
`affiliate: false` gewijzigd naar `true`, Preply + iTalki CTAs toegevoegd.

### 10. Surfshark CTA
Surfshark CTA toegevoegd aan best-vpn artikel.

---

## Niet gewijzigd / bewust gelaten

| Issue | Reden |
|-------|-------|
| Babbel/Preply bare URLs | AWIN/PartnerStack nog niet goedgekeurd; placeholder links functioneel |
| Funda/Pararius `cta-affiliate` class | Geen affiliate programma beschikbaar; cosmetisch issue |
