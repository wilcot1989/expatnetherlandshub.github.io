# EXPAT-MONETISATIE-GATEN.md
Peildatum: 9 maart 2026 | Definitieve versie

---

## Producten met hoge zichtbaarheid maar geen tracking

| Product | # Bestanden | Commissie | Status |
|---------|-------------|-----------|--------|
| Revolut | 13 | EUR 10-50/ref | Geen link, geen CTA |
| KPN | 8 | EUR 10-50/klant | Alleen mention |
| T-Mobile | 8 | EUR 15-30/klant | Alleen mention |
| Ziggo | 7 | EUR 25-50/klant | Alleen mention |
| bunq | 6 | Referral | Link zonder tracking |
| Cigna Global | 5 | USD 50-200/policy | Alleen mention, titelpagina aanwezig |
| HousingAnywhere | 5 | EUR 15-30/boeking | Alleen mention |

---

## CTAs zonder monetisatiepad

| Product | CTA aanwezig | Tracking | Probleem |
|---------|-------------|----------|----------|
| Babbel | Ja (5 bestanden) | Nee | AWIN nog niet goedgekeurd |
| Preply | Ja (5 bestanden) | Nee | PartnerStack nog niet goedgekeurd |
| iTalki | Ja (1 bestand) | Nee | Direct affiliate nog niet aangemeld |
| Surfshark | Ja (1 bestand) | Nee | Direct affiliate nog niet aangemeld |

---

## Clusters met zwakke partnerdekking

1. **Telecom** — KPN, T-Mobile, Ziggo prominent in 3 artikelen, 0 tracking
2. **Energie** — Vattenfall, Eneco prominent in 1 artikel, alleen Independer vergelijker actief
3. **Housing platforms** — Kamernet 9x, HousingAnywhere 5x, Booking.com 3x — allen zonder tracking
4. **International insurance** — Cigna 5x met titelpagina, Aetna 2x — geen tracking

---

## Tools met conversiepotentieel maar onvolledig

| Tool | Actieve affiliate | Ontbreekt |
|------|-------------------|-----------|
| Bank account chooser | Wise ✅ | bunq, N26 (affiliateUrl: null) |
| Insurance chooser | Independer ✅ | Cigna, Aetna direct links |
| Housing budget checker | Geen (Funda class gefixt) | HousingAnywhere, Kamernet |
| Inburgering route builder | Babbel (met bsc param) | Preply (bare URL) |

---

## Inconsistenties die omzet kosten

1. ✅ OPGELOST: Wise bare/truncated URLs in 3 tools → nu correct
2. ✅ OPGELOST: Independer awclick → cread in 8 bestanden
3. ✅ OPGELOST: SafetyWing verkeerde referenceID
4. ✅ OPGELOST: NordVPN lege url_id
5. NOG OPEN: Babbel/Preply/iTalki/Surfshark bare URLs (wachten op goedkeuring)
