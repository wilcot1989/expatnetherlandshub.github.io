# ExpatNetherlandsHub.com — Masterplan 2026

> **Versie:** 1.0 | **Datum:** 6 maart 2026
> **Doel:** ExpatNetherlandsHub transformeren van informatieve blog naar een 10/10 tool-gedreven affiliate decision platform
> **Target:** €3.000/maand recurring affiliate revenue binnen 12 maanden
> **Auteur:** Sarah van den Berg (site persona)

---

## Inhoudsopgave

1. [Executive Summary](#1-executive-summary)
2. [Huidige Situatie & Audit](#2-huidige-situatie--audit)
3. [Strategische Visie](#3-strategische-visie)
4. [Lessen uit BSG — Wat Werkt](#4-lessen-uit-bsg--wat-werkt)
5. [Nieuw Design & UX](#5-nieuw-design--ux)
6. [URL-Structuur & Informatiearchitectuur](#6-url-structuur--informatiearchitectuur)
7. [Tool Suite — 10 Interactieve Tools](#7-tool-suite--10-interactieve-tools)
8. [Content Strategie — Money Pages](#8-content-strategie--money-pages)
9. [Content Strategie — Supporting Articles](#9-content-strategie--supporting-articles)
10. [Content Strategie — City Guides](#10-content-strategie--city-guides)
11. [SEO Strategie](#11-seo-strategie)
12. [E-E-A-T & YMYL Compliance](#12-e-e-a-t--ymyl-compliance)
13. [Affiliate Programma's & Monetisatie](#13-affiliate-programmas--monetisatie)
14. [Technische Architectuur](#14-technische-architectuur)
15. [Schema.org & Structured Data](#15-schemaorg--structured-data)
16. [Conversie-Optimalisatie (CRO)](#16-conversie-optimalisatie-cro)
17. [Backlink & Outreach Strategie](#17-backlink--outreach-strategie)
18. [Analytics & KPI Dashboard](#18-analytics--kpi-dashboard)
19. [Implementatie Roadmap (12 maanden)](#19-implementatie-roadmap-12-maanden)
20. [Revenue Projecties](#20-revenue-projecties)
21. [Risico's & Mitigatie](#21-risicos--mitigatie)
22. [Bijlagen](#22-bijlagen)

---

## 1. Executive Summary

ExpatNetherlandsHub.com wordt getransformeerd van een informatieve expat-blog (38 artikelen, geen tools, minimale affiliate links) naar een **tool-gedreven decision platform** dat expats in Nederland begeleidt bij hun belangrijkste financiele en administratieve beslissingen.

**Kernstrategie:** Expats in Nederland staan voor 10-15 complexe beslissingen in hun eerste 2 jaar. Elke beslissing heeft een bijbehorend financieel product. Wij bouwen voor elke beslissing een **interactieve tool** die de expat helpt kiezen, en verdienen via affiliate links naar de gekozen oplossing.

**Waarom dit werkt:**
- 95.000+ expats verhuizen jaarlijks naar Nederland (CBS 2025)
- Expats hebben hoog besteedbaar inkomen (gemiddeld 30% ruling = €15.000+/jaar extra)
- Financiele productkeuzes zijn complex en high-value (zorgverzekering €1.200-2.400/jaar, bankrekening, transfers)
- Engelstalige concurrentie is zwak — geen enkele site combineert tools + content + affiliate
- YMYL-niche met hoge E-E-A-T drempel = moeilijk te kopiëren = duurzaam voordeel

**Unique Selling Proposition:** "The only expat platform that doesn't just tell you what to do — it calculates, compares, and recommends the best option for YOUR situation."

---

## 2. Huidige Situatie & Audit

### 2.1 Wat we hebben (maart 2026)

| Aspect | Status |
|--------|--------|
| Artikelen | 38 gepubliceerd (info + guides) |
| Tools | 0 |
| Design | Basis Hugo starter theme |
| Affiliate links | Minimaal (NordVPN, enkele Awin) |
| GA4 | Actief (G-2TJSDJB4CG) |
| Search Console | Geverifieerd, sitemap ingediend |
| Indexering | Via Indexing API ingediend |
| Auteur | Sarah van den Berg (expat coach persona) |
| Schema | Article + FAQPage + BreadcrumbList |

### 2.2 Wat er mis is

1. **Geen interactieve tools** — puur informatief, geen reden om terug te komen
2. **Geen duidelijke money pages** — artikelen linken niet strategisch naar affiliate producten
3. **Generiek design** — zelfde starter theme als BSG, geen expat-identiteit
4. **Geen funnel structuur** — content staat los, geen pad van informatie → beslissing → conversie
5. **Zwakke interne linking** — artikelen verwijzen niet systematisch naar tools of naar elkaar
6. **Geen city guides** — expats zoeken stad-specifiek ("health insurance Amsterdam", "bank account Rotterdam")
7. **Geen lead capture** — geen email lijst, geen retargeting mogelijkheid
8. **Content te breed** — sommige artikelen overlappen, geen duidelijke pillar/cluster structuur

### 2.3 Wat wél goed is

- Domein is geïndexeerd en heeft eerste impressies
- GA4 + Search Console operationeel
- Sarah van den Berg persona is geloofwaardig en consistent
- Hugo + GitHub Pages infrastructuur staat en werkt
- Deployment pipeline (Actions + daily cron) is bewezen via BSG
- E-E-A-T basis is gelegd (author box, structured data)

---

## 3. Strategische Visie

### 3.1 Positionering

**Van:** "Informatieve expat blog"
**Naar:** "De #1 decision engine voor expats in Nederland"

Concurrenten vergelijken:

| Site | Content | Tools | Affiliate | Design | Score |
|------|---------|-------|-----------|--------|-------|
| iamexpat.nl | Veel, breed | Geen | Display ads | Rommelig | 6/10 |
| expatica.com | Veel, generiek | Geen | Display ads | Gedateerd | 5/10 |
| dutchreview.nl | Lifestyle focus | Geen | Enkele links | Modern | 6/10 |
| 30percentruling.com | Niche, diep | Calculator | Geen | Basic | 7/10 |
| **expatnetherlandshub.com** | **Gericht, diep** | **10 tools** | **High-value** | **Modern** | **10/10** |

### 3.2 Doelgroep Segmenten

| Segment | % Traffic | Gemiddelde waarde | Primary need |
|---------|-----------|-------------------|--------------|
| **Knowledge migrants (30% ruling)** | 40% | Hoog (€60-100K salaris) | Tax optimization, banking, insurance |
| **EU movers** | 25% | Gemiddeld | Registration, insurance, housing |
| **Students** | 15% | Laag nu, hoog later | Banking, insurance, housing |
| **Partners/family** | 10% | Indirect (via primary) | Integration, insurance, banking |
| **Digital nomads/freelancers** | 10% | Gemiddeld-hoog | Tax, banking, insurance |

### 3.3 User Journey Mapping

```
AWARENESS          CONSIDERATION         DECISION            ACTION
"Moving to NL"     "How does X work?"    "Which is best?"    "Sign up"
   |                    |                     |                  |
   v                    v                     v                  v
Blog articles    →  Guide pages      →   Tool pages      →  Affiliate click
(SEO traffic)      (internal links)     (calculator/wizard)   (conversion)
                                              |
                                              v
                                        Email capture
                                        (retargeting)
```

---

## 4. Lessen uit BSG — Wat Werkt

Concrete takeaways uit 3 maanden BSG bouwen die we 1:1 toepassen:

### 4.1 Tools zijn de #1 conversie-driver
- BSG tools (keuzehulp, kosten-berekenen, stack-planner) genereren 3-5x meer clicks dan pure artikelen
- **Toepassen:** 10 interactieve tools bouwen, elke tool = eigen landing page met SEO content

### 4.2 WebApplication schema werkt
- BSG's 10 pillar pages met WebApplication schema kregen sneller rich results
- **Toepassen:** SoftwareApplication + FAQPage schema op alle tool pages

### 4.3 Interne links moeten strategisch
- BSG audit toonde: artikelen zonder interne links ranken slechter
- **Toepassen:** Elke pagina minimaal 5 interne links, elke tool gelinkt vanuit 3+ artikelen

### 4.4 Prijzen en reviews maken het verschil
- BSG artikelen met actuele prijzen en Trustpilot scores scoren beter
- **Toepassen:** Trustpilot/Google Reviews integreren voor banken, verzekeraars, diensten

### 4.5 Meta descriptions moeten 140-160 chars + CTA
- BSG SEO audit: descriptions <140 chars misten kansen, >160 werden afgekapt
- **Toepassen:** Strikte 140-160 regel + eindigen op CTA ("Calculate yours free →")

### 4.6 Category pages moeten substantief zijn
- BSG categoriepagina's met 500+ woorden extra content rankten hoger
- **Toepassen:** Elke hub page minimaal 800 woorden unieke content

### 4.7 CTA styling en placement
- BSG `.cta-affiliate` oranje buttons + `target="_blank"` rel="noopener nofollow sponsored"
- **Toepassen:** Zelfde CTA structuur, maar met expat-brand kleuren

### 4.8 Schrijfstijl die converteert
- Probleemoplossend, persoonlijk, data-driven, eerlijk (zie memory/schrijfstijl.md)
- **Toepassen:** Sarah's stem: warm maar no-nonsense, altijd concrete cijfers, nooit vage beloftes

---

## 5. Nieuw Design & UX

### 5.1 Design Filosofie

**BSG = zakelijk blauw, B2B, Nederlands**
**Expat = warm, internationaal, toegankelijk, Engels**

Het design moet zeggen: "Ik ben hier al doorheen gegaan en ik help je er doorheen."

### 5.2 Kleurenpalet

```css
/* Primary */
--expat-primary: #1B6B4A;       /* Donkergroen — vertrouwen, Nederland, groei */
--expat-primary-light: #2D9B6A;  /* Hover state */
--expat-primary-dark: #145236;   /* Active state */

/* Secondary */
--expat-accent: #E8832A;         /* Warm oranje — Dutch accent, CTA kleur */
--expat-accent-light: #F5A623;   /* Highlight */

/* Neutrals */
--expat-bg: #FAFBF9;            /* Licht warm grijs-groen */
--expat-card: #FFFFFF;
--expat-text: #1A1A2E;          /* Bijna zwart, warm */
--expat-muted: #6B7280;         /* Subtekst */
--expat-border: #E5E7EB;

/* Semantic */
--expat-success: #10B981;       /* Afgerond/goed */
--expat-warning: #F59E0B;       /* Let op */
--expat-info: #3B82F6;          /* Info */
```

### 5.3 Typografie

```css
/* Headings */
font-family: 'DM Sans', sans-serif;
/* Body */
font-family: 'Inter', sans-serif;
/* Tool displays/numbers */
font-family: 'JetBrains Mono', monospace;
```

- H1: 2.25rem, bold, --expat-text
- H2: 1.75rem, semibold
- H3: 1.25rem, semibold
- Body: 1.05rem, line-height 1.75
- CTA buttons: 1rem, semibold, uppercase tracking

### 5.4 Layout Componenten

#### Homepage
```
┌─────────────────────────────────────────────────┐
│  HERO: "Moving to the Netherlands?              │
│   Your step-by-step decision engine."           │
│   [Start the 30% Ruling Calculator →]           │
│   [Browse All Tools]                            │
├─────────────────────────────────────────────────┤
│  TOOL GRID (2x5)                                │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │ 30%  │ │Salary│ │ Visa │ │ BSN  │ │Zorg- │  │
│  │Ruling│ │Check │ │Finder│ │Plan  │ │verz. │  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘  │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │Insur.│ │ Bank │ │House │ │Inburg│ │Diplom│  │
│  │Choose│ │Choose│ │Check │ │Route │ │Eval. │  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘  │
├─────────────────────────────────────────────────┤
│  "HOW IT WORKS" — 3 stappen visueel             │
│  1. Answer a few questions                      │
│  2. Get personalized recommendations            │
│  3. Sign up with our trusted partners           │
├─────────────────────────────────────────────────┤
│  LATEST GUIDES (3-card grid)                    │
├─────────────────────────────────────────────────┤
│  TRUST BAR: "Trusted by 5,000+ expats"          │
│  Partner logos: Wise, bunq, SafetyWing           │
├─────────────────────────────────────────────────┤
│  CITY QUICK LINKS: Amsterdam | Rotterdam |       │
│  The Hague | Eindhoven | Utrecht                │
└─────────────────────────────────────────────────┘
```

#### Tool Page Layout
```
┌─────────────────────────────────────────────────┐
│  Breadcrumb: Home > Tools > 30% Ruling Calc.    │
├─────────────────────────────────────────────────┤
│  H1: "30% Ruling Calculator 2026"               │
│  Subtitle: "Calculate your exact tax benefit     │
│  in 30 seconds"                                 │
├────────────────────────┬────────────────────────┤
│                        │                        │
│  INTERACTIVE TOOL      │  SIDEBAR               │
│  (calculator/wizard)   │  - Quick facts box     │
│                        │  - Related tools       │
│  [Input fields]        │  - "Need help?"        │
│  [Sliders]             │    → Email capture     │
│  [Result display]      │  - Trust badges        │
│                        │                        │
├────────────────────────┴────────────────────────┤
│  RESULTS SECTION                                │
│  - Personalized recommendation                  │
│  - Affiliate CTA buttons                        │
│  - Comparison table (if applicable)             │
├─────────────────────────────────────────────────┤
│  SEO CONTENT (800-1500 words)                   │
│  - H2: How does [topic] work?                   │
│  - H2: Who is eligible?                         │
│  - H2: Step-by-step guide                       │
│  - H2: FAQ (5-8 questions, FAQPage schema)      │
├─────────────────────────────────────────────────┤
│  RELATED ARTICLES (3-card grid)                 │
└─────────────────────────────────────────────────┘
```

#### Article Page Layout
```
┌─────────────────────────────────────────────────┐
│  Breadcrumb: Home > Guides > Health Insurance    │
├────────────────────────┬────────────────────────┤
│  ARTICLE CONTENT       │  STICKY SIDEBAR        │
│  - Author box (Sarah)  │  - Table of Contents   │
│  - Last updated date   │  - Tool CTA            │
│  - Reading time        │  - Related guides      │
│  - Content...          │  - Email signup         │
│                        │                        │
│  [Inline tool CTA]     │                        │
│  [Comparison table]    │                        │
│  [Affiliate buttons]   │                        │
│                        │                        │
├────────────────────────┴────────────────────────┤
│  FAQ SECTION (collapsible)                      │
├─────────────────────────────────────────────────┤
│  RELATED ARTICLES + TOOLS                       │
└─────────────────────────────────────────────────┘
```

### 5.5 UI Componenten (nieuw te bouwen)

| Component | Beschrijving | Gebruik |
|-----------|-------------|---------|
| `tool-card` | Icon + titel + korte beschrijving + arrow | Homepage grid, related tools |
| `result-card` | Groen/oranje border, grote heading, body | Tool resultaten |
| `comparison-table` | Responsive tabel met highlight kolom | Vergelijkingen in artikelen |
| `affiliate-cta` | Oranje button, partner logo, "Open account →" | Na tool resultaat |
| `trust-badge` | Klein icoon + tekst ("Updated March 2026") | Sidebar, tool pages |
| `step-indicator` | Genummerde stappen met progress bar | Multi-step tools |
| `city-tag` | Klikbare pill met stadsnaam | Artikelen, tool pages |
| `faq-accordion` | Klikbare vraag, animated antwoord | Alle pagina's |
| `email-capture` | Compact form, "Get your free checklist" | Sidebar, na tool result |
| `quick-fact-box` | Gekleurde box met key facts | Sidebar, inline |
| `author-box` | Foto + bio + social links | Artikelen |
| `breadcrumb` | Schema-compliant breadcrumbs | Alle pagina's |

### 5.6 Mobile-First Responsive

- **Mobile (<768px):** Single column, tools stacked, sticky bottom CTA bar
- **Tablet (768-1024px):** 2-column tool grid, sidebar collapses
- **Desktop (1024+):** Full layout met sticky sidebar

---

## 6. URL-Structuur & Informatiearchitectuur

### 6.1 Primaire URL-structuur

```
expatnetherlandshub.com/
├── /tools/                              ← Tools hub page
│   ├── /tools/30-percent-ruling-calculator/
│   ├── /tools/salary-checker/
│   ├── /tools/visa-permit-finder/
│   ├── /tools/bsn-appointment-planner/
│   ├── /tools/health-insurance-wizard/
│   ├── /tools/expat-insurance-chooser/
│   ├── /tools/bank-account-chooser/
│   ├── /tools/housing-budget-checker/
│   ├── /tools/inburgering-route-builder/
│   └── /tools/diploma-evaluation-planner/
│
├── /guides/                             ← Guide hub page
│   ├── /guides/finance/                 ← Cluster hub
│   │   ├── /guides/30-percent-ruling-complete-guide/
│   │   ├── /guides/dutch-tax-system-expats/
│   │   ├── /guides/best-banks-expats-netherlands/
│   │   ├── /guides/international-money-transfers/
│   │   └── ...
│   ├── /guides/health/                  ← Cluster hub
│   │   ├── /guides/health-insurance-netherlands-expats/
│   │   ├── /guides/best-health-insurance-expats/
│   │   └── ...
│   ├── /guides/housing/                 ← Cluster hub
│   │   ├── /guides/renting-in-netherlands/
│   │   └── ...
│   ├── /guides/legal/                   ← Cluster hub
│   │   ├── /guides/bsn-registration-guide/
│   │   └── ...
│   ├── /guides/work/                    ← Cluster hub
│   │   ├── /guides/work-permit-netherlands/
│   │   └── ...
│   └── /guides/integration/             ← Cluster hub
│       ├── /guides/inburgering-civic-integration/
│       └── ...
│
├── /cities/                             ← City hub page
│   ├── /cities/amsterdam/
│   ├── /cities/rotterdam/
│   ├── /cities/the-hague/
│   ├── /cities/eindhoven/
│   ├── /cities/utrecht/
│   ├── /cities/groningen/
│   ├── /cities/leiden/
│   └── /cities/maastricht/
│
├── /services/                           ← Service comparison hub
│   ├── /services/wise-review/
│   ├── /services/bunq-review/
│   ├── /services/safetywing-review/
│   └── /services/wise-vs-revolut/
│
├── /about/                              ← About + E-E-A-T
├── /contact/
├── /privacy/
├── /disclaimer/
└── /sitemap.xml
```

### 6.2 Interne Link Matrix

Elke pagina linkt naar minimaal 3 andere pagina's. De structuur:

```
TOOL PAGE ←→ GUIDE (same topic)
TOOL PAGE ←→ CITY GUIDE (localized version)
GUIDE ←→ SERVICE REVIEW (product recommendation)
GUIDE ←→ OTHER GUIDES (same cluster)
CITY GUIDE → TOOL PAGES (all relevant tools)
CITY GUIDE → LOCAL GUIDES (housing, registration)
SERVICE REVIEW → TOOL PAGE (where product appears in results)
```

### 6.3 Navigatie

**Desktop Header:**
```
[Logo]   Tools ▼   Guides ▼   Cities ▼   Services   About
                                              [30% Calculator →]
```

**Tools Dropdown:**
```
Financial Tools          Registration Tools       Living in NL
─────────────────        ──────────────────       ─────────────
30% Ruling Calculator    Visa Permit Finder       Health Insurance Wizard
Salary Checker           BSN Planner              Bank Account Chooser
Housing Budget Checker   Diploma Evaluator        Insurance Chooser
                         Inburgering Route
```

**Footer:**
```
TOOLS          POPULAR GUIDES           CITIES           ABOUT
All Tools      30% Ruling Guide         Amsterdam        About Sarah
Calculator     Health Insurance          Rotterdam        Contact
Salary Check   Best Banks               The Hague        Privacy
Visa Finder    Renting Guide            Eindhoven        Disclaimer
               Work Permits             Utrecht
```

---

## 7. Tool Suite — 10 Interactieve Tools

### 7.1 Overzicht

| # | Tool | URL slug | Type | Affiliate hook | Priority |
|---|------|----------|------|----------------|----------|
| 1 | 30% Ruling Calculator | `30-percent-ruling-calculator` | Calculator | Tax advisors | P0 |
| 2 | HSM Salary Checker | `salary-checker` | Calculator | Recruitment, relocation | P0 |
| 3 | Visa & Permit Finder | `visa-permit-finder` | Wizard (decision tree) | Legal services, IND | P1 |
| 4 | BSN Appointment Planner | `bsn-appointment-planner` | Checklist + scheduler | Relocation services | P1 |
| 5 | Zorgverzekering Wizard | `health-insurance-wizard` | Wizard (multi-step) | Independer (Awin), insurers | P0 |
| 6 | Expat Insurance Chooser | `expat-insurance-chooser` | Comparison tool | SafetyWing, Cigna, Allianz | P1 |
| 7 | Bank Account Chooser | `bank-account-chooser` | Quiz + comparison | bunq, Wise, N26, Revolut | P0 |
| 8 | Housing Budget Checker | `housing-budget-checker` | Calculator | Housing platforms, mortgage | P2 |
| 9 | Inburgering Route Builder | `inburgering-route-builder` | Decision tree | Language schools, DUO | P2 |
| 10 | Diploma Evaluation Planner | `diploma-evaluation-planner` | Checklist + timeline | Nuffic, translation services | P2 |

### 7.2 Tool Specificaties

#### Tool 1: 30% Ruling Calculator (P0)

**Doel:** Bereken exact hoeveel belastingvoordeel je krijgt met de 30% ruling

**Inputs:**
- Bruto jaarsalaris (€)
- Leeftijd
- Heeft MSc/PhD? (ja/nee)
- Jaar van aankomst in NL
- Burgerlijke staat (alleenstaand/partner)

**Berekening:**
```
ruling_percentage = 30% (of 27% na 2024 cap: max €233.000 in 2026)
tax_free_allowance = salary * ruling_percentage
taxable_income = salary - tax_free_allowance
tax_without_ruling = calculate_dutch_tax(salary)
tax_with_ruling = calculate_dutch_tax(taxable_income)
annual_benefit = tax_without_ruling - tax_with_ruling
total_benefit_5yr = annual_benefit * 5
```

**Outputs:**
- Jaarlijks belastingvoordeel (groot, groen getal)
- Totaal voordeel over 5 jaar
- Effectief belastingpercentage met vs zonder ruling
- Grafische vergelijking (bar chart)
- Disclaimer: "This is an estimate. Consult a tax advisor for your exact situation."

**Affiliate CTAs na resultaat:**
- "Get professional 30% ruling advice → [Tax advisor partner]"
- "Open a Dutch bank account to receive your salary → bunq / Wise"

**SEO content onder tool (1200+ woorden):**
- H2: What is the 30% ruling?
- H2: Who qualifies for the 30% ruling in 2026?
- H2: How to apply for the 30% ruling
- H2: 30% ruling changes 2024-2026
- H2: FAQ (8 vragen)

---

#### Tool 2: HSM Salary Checker (P0)

**Doel:** Check of je salaris voldoet aan de HSM (Highly Skilled Migrant) drempel

**Inputs:**
- Leeftijd (<30 / ≥30)
- Type: Regular HSM / Scientific researcher / Arts graduate
- Bruto maandsalaris (€)
- Inclusief of exclusief vakantiegeld

**Berekening:**
```
thresholds_2026 = {
  "regular_under_30": 3909,    # Monthly excl. holiday
  "regular_30_plus": 5331,
  "scientific_researcher": 3909,
  "arts_graduate": 2801,       # Orientation year
}
# Adjust for holiday allowance (8%)
if includes_holiday:
  effective_salary = salary / 1.08
meets_threshold = effective_salary >= threshold
margin = effective_salary - threshold
```

**Outputs:**
- Pass/Fail indicator (grote groene check of rood kruis)
- Je salaris vs de drempel (visuele bar)
- Marge boven/onder drempel
- Als "fail": suggestie om 30% ruling mee te tellen (link naar tool 1)

**Affiliate CTAs:**
- "Looking for HSM jobs? → [Recruitment partner]"
- "Need a work permit? Use our Visa Finder → [Tool 3]"

---

#### Tool 3: Visa & Permit Finder (P1)

**Doel:** Wizard die bepaalt welk visum/vergunning je nodig hebt

**Stappen (decision tree):**
```
Step 1: What is your nationality?
  → EU/EEA/Swiss → "No work permit needed" + registration guide
  → Non-EU → Step 2

Step 2: What is your purpose?
  → Employment → Step 3
  → Study → Student permit info
  → Self-employed → DAFT/startup visa info
  → Family → Family reunification info

Step 3: Your salary level?
  → Above HSM threshold → HSM permit path
  → Below threshold → Regular work permit (TWV+GVVA) path
  → Researcher → Scientific researcher path

Step 4: Additional circumstances?
  → Orientation year graduate
  → Transfer within company (ICT)
  → Startup founder
```

**Output per pad:**
- Vereist permit type
- Geschatte doorlooptijd (weken)
- Benodigde documenten (checklist)
- Kosten
- Link naar IND
- Link naar gerelateerde tools (BSN, salary checker)

**Affiliate CTAs:**
- "Get legal help with your application → [Immigration lawyer partner]"
- "Need document translation? → [Translation service]"

---

#### Tool 4: BSN Appointment Planner (P1)

**Doel:** Interactieve checklist + timeline voor je BSN registratie

**Features:**
- Document checklist (per situatie: EU vs non-EU, met partner, met kinderen)
- Interactieve stappen-flow met estimated timeline
- Gemeente-specifieke info (dropdown per stad)
- Appointment booking link per gemeente
- "What to bring" printable checklist

**Output:**
- Gepersonaliseerde checklist
- Estimated timeline (visual)
- Direct booking links per gemeente

---

#### Tool 5: Health Insurance Wizard (P0) — TOP MONEY PAGE

**Doel:** Multi-step wizard die de beste zorgverzekering aanbeveelt

**Dit is de #1 money page.** Iedereen in NL moet een basisverzekering hebben. Gem. €130-150/maand = €1.560-1.800/jaar. Affiliate commissies op verzekeringen zijn hoog.

**Stappen:**
```
Step 1: Your situation
  - New to NL / Already registered
  - EU citizen / Non-EU with permit / Student
  - Age bracket

Step 2: Your needs
  - GP visits frequency
  - Specialist care needed?
  - Dental care? (aanvullend)
  - Mental health care?
  - Physiotherapy?
  - Pregnancy planned?

Step 3: Your budget
  - Eigen risico preference (€385 - €885)
  - Monthly budget range
  - Prefer low premium or low eigen risico?

Step 4: Your preferences
  - Dutch-speaking doctor ok / English required
  - Specific hospital/clinic preferences
  - Alternative medicine interest
```

**Output:**
- Top 3 aanbevolen verzekeringen met:
  - Verzekeraar naam + logo
  - Maandpremie
  - Eigen risico
  - Dekking highlights
  - Trustpilot score
  - **"Compare on Independer →" affiliate button**
  - **"Go to [insurer] website →" affiliate button**
- Side-by-side comparison tabel

**Affiliate flow:**
1. Tool recommends → user clicks "Compare on Independer"
2. Independer (Awin mid=8558) → commissie per lead/sale
3. Alternief: direct naar verzekeraar (als we directe affiliate deals hebben)

**SEO content (1500+ woorden):**
- H2: How health insurance works in the Netherlands
- H2: Basisverzekering vs aanvullende verzekering explained
- H2: How much does health insurance cost in 2026?
- H2: Can I keep my home country insurance?
- H2: Zorgtoeslag: health insurance allowance for expats
- H2: FAQ (10 vragen)

---

#### Tool 6: Expat Insurance Chooser (P1)

**Doel:** Vergelijk internationale verzekeringen (voor wie nog niet ingeschreven is of tijdelijk is)

**Focus:** SafetyWing, Cigna Global, Allianz Care, Aetna International

**Inputs:**
- Duur verblijf (<1 jaar / 1-2 jaar / permanent)
- Gezinssituatie
- Benodigde dekking

**Output:**
- Vergelijkingstabel met prijzen, dekking, ratings
- Aanbeveling per situatie
- Affiliate links naar SafetyWing etc.

---

#### Tool 7: Bank Account Chooser (P0)

**Doel:** Quiz-style tool die de beste bank aanbeveelt

**Stappen:**
```
Step 1: What do you need?
  □ Dutch IBAN (for salary)
  □ International transfers
  □ Joint account
  □ Savings account
  □ Investment options
  □ English mobile app

Step 2: What matters most?
  - Low fees / Best exchange rates / Best app / Most features

Step 3: Your monthly income
  - <€2000 / €2000-4000 / €4000-7000 / €7000+

Step 4: Do you already have?
  - Wise account / Revolut account / N26 account / None
```

**Output:**
- Top 3 recommendations:
  1. **bunq** — "Best expat-friendly Dutch bank"
  2. **Wise** — "Best for international transfers"
  3. **ABN AMRO** — "Best traditional Dutch bank"
- Per recommendation: features, monthly cost, opening time, Trustpilot score
- "Open account →" affiliate button

**Affiliate programma's:**
- bunq: directe affiliate deal (referral program, ~€10-25 per signup)
- Wise: Impact.com (te activeren) — hoge commissie op eerste transfer
- N26: geen NL affiliate
- ABN AMRO: via Daisycon (te activeren)
- Revolut: referral (limited)

---

#### Tool 8: Housing Budget Checker (P2)

**Doel:** Bereken wat je kunt huren/kopen op basis van je salaris

**Inputs:**
- Netto maandinkomen
- Partner inkomen (optioneel)
- Stad
- Huur of koop

**Output:**
- Maximale huurprijs (1/3 netto regel + margin)
- Maximale hypotheek (indicatief)
- Gemiddelde huurprijzen in gekozen stad
- Vergelijking met landelijk gemiddelde
- Tips per stad

---

#### Tool 9: Inburgering Route Builder (P2)

**Doel:** Bepaal welk inburgeringstraject je moet volgen

**Decision tree:**
```
Step 1: When did you arrive in NL?
  → Before Jan 1, 2022 → Old system (Wet inburgering 2013)
  → After Jan 1, 2022 → New system (Wet inburgering 2021)

Step 2: Your route
  → B1 route (standard)
  → Education route
  → Self-reliance route (zelfredzaamheid)
  → Z-route (special circumstances)

Step 3: Your starting level
  → Beginner (A0)
  → Some Dutch (A1-A2)
  → Good Dutch (B1+)
```

**Output:**
- Aanbevolen route + geschatte duur
- Estimated cost + DUO loan info
- Exam overview
- School recommendations per stad

---

#### Tool 10: Diploma Evaluation Planner (P2)

**Doel:** Stap-voor-stap plan voor diplomawaardering

**Inputs:**
- Type diploma (HBO/WO/PhD/Beroepskwalificatie)
- Land van afgifte
- Doel (werk/studie/regulated profession)

**Output:**
- Nuffic evaluatie nodig? Ja/nee
- Geschatte doorlooptijd
- Kosten
- Benodigde documenten checklist
- Link naar Nuffic

---

### 7.3 Technische Implementatie Tools

Alle tools worden gebouwd als **statische HTML/CSS/JS** in `static/tools/`, exact zoals BSG:

```
static/tools/
├── index.html                          ← Tools hub page
├── css/
│   └── tools.css                       ← Gedeelde tool styling
├── js/
│   ├── tools-common.js                 ← Gedeelde functionaliteit
│   ├── 30-percent-calculator.js
│   ├── salary-checker.js
│   ├── visa-finder.js
│   ├── bsn-planner.js
│   ├── health-insurance-wizard.js
│   ├── insurance-chooser.js
│   ├── bank-chooser.js
│   ├── housing-checker.js
│   ├── inburgering-builder.js
│   └── diploma-planner.js
├── data/
│   ├── insurance-providers.json        ← Verzekeraars + prijzen
│   ├── banks.json                      ← Banken + features
│   ├── cities.json                     ← Stad-specifieke data
│   ├── visa-types.json                 ← Visa decision tree data
│   └── tax-brackets.json               ← Belastingschijven 2026
├── 30-percent-ruling-calculator/
│   └── index.html
├── salary-checker/
│   └── index.html
├── visa-permit-finder/
│   └── index.html
├── bsn-appointment-planner/
│   └── index.html
├── health-insurance-wizard/
│   └── index.html
├── expat-insurance-chooser/
│   └── index.html
├── bank-account-chooser/
│   └── index.html
├── housing-budget-checker/
│   └── index.html
├── inburgering-route-builder/
│   └── index.html
└── diploma-evaluation-planner/
    └── index.html
```

**Elke tool page bevat:**
- Standalone HTML met Hugo's baseof.html integratie (conditionele CSS/JS loading)
- SEO content (H1, 800-1500 woorden, FAQ)
- Schema markup (WebApplication + FAQPage)
- Mobile-responsive layout
- No external dependencies (pure vanilla JS)
- GA4 event tracking op elke stap + resultaat + CTA click

---

## 8. Content Strategie — Money Pages

### 8.1 Pillar Pages (10 stuks, 3000-4000+ woorden)

Elke pillar page correspondeert met een tool en is de diepste, meest uitgebreide guide.

| # | Pillar Page | Target Keyword | KD est. | Vol. est. | Tool link |
|---|-------------|----------------|---------|-----------|-----------|
| 1 | Complete Guide to the 30% Ruling | "30% ruling netherlands" | Medium | 12.100 | Calculator |
| 2 | Health Insurance for Expats in the Netherlands | "health insurance netherlands expat" | Medium | 4.400 | Wizard |
| 3 | Best Banks for Expats in the Netherlands 2026 | "best bank expats netherlands" | Low | 2.900 | Bank Chooser |
| 4 | How to Get a BSN Number in the Netherlands | "bsn number netherlands" | Low | 6.600 | BSN Planner |
| 5 | Work Permits & Visa Guide Netherlands | "work permit netherlands" | Medium | 3.600 | Visa Finder |
| 6 | Renting in the Netherlands: Complete Guide | "renting netherlands expat" | Low | 1.900 | Housing Checker |
| 7 | International Money Transfers from the Netherlands | "money transfer netherlands" | Low | 1.300 | Bank Chooser |
| 8 | Dutch Tax System for Expats Explained | "dutch tax system expats" | Low | 1.600 | Calculator |
| 9 | Civic Integration (Inburgering) Guide | "inburgering netherlands" | Low | 2.400 | Route Builder |
| 10 | Diploma Recognition in the Netherlands | "diploma recognition netherlands" | Low | 880 | Diploma Planner |

**Pillar page template:**
```markdown
---
title: "[Full SEO title ≤60 chars]"
description: "[140-160 chars + CTA]"
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
author: "Sarah van den Berg"
author_bio: "Expat coach met 8 jaar ervaring..."
categories: ["[cluster]"]
tags: ["expat", "netherlands", "[topic]"]
images: ["/images/[topic]-hero.svg"]
schema_type: "Article"
tool_link: "/tools/[tool-slug]/"
---

[Intro: 100 words, keyword in first sentence, link to tool]

{{< tool-cta tool="[slug]" text="Calculate yours now →" >}}

## [H2 with keyword] (detailed explanation)
...

## [H2 practical steps]
...

## [H2 costs/prices 2026]
...

## [H2 comparison if applicable]
[Comparison table with affiliate links]

## Tips from Sarah
[Personal experience/advice section — E-E-A-T]

## FAQ

### [Question 1]?
[Answer]

### [Question 2]?
[Answer]

...8-10 questions

## Read also
- [Internal link 1]
- [Internal link 2]
- [Internal link 3]
```

### 8.2 Versus/Comparison Pages (8 stuks, 2000-2500 woorden)

| # | Comparison | Target Keyword | Affiliate hook |
|---|-----------|----------------|----------------|
| 1 | Wise vs Revolut for Expats in NL | "wise vs revolut netherlands" | Wise affiliate |
| 2 | bunq vs ABN AMRO for Expats | "bunq vs abn amro expat" | bunq affiliate |
| 3 | SafetyWing vs Cigna Global | "safetywing vs cigna expat" | SafetyWing affiliate |
| 4 | CZ vs Zilveren Kruis for Expats | "cz vs zilveren kruis english" | Independer |
| 5 | Wise vs Western Union NL | "wise vs western union" | Wise affiliate |
| 6 | N26 vs bunq Netherlands | "n26 vs bunq" | bunq affiliate |
| 7 | Private vs Public Health Insurance NL | "private health insurance netherlands" | Insurers |
| 8 | Renting vs Buying in NL as Expat | "rent vs buy netherlands expat" | Mortgage/housing |

**Versus page template:**
```markdown
---
title: "[Product A] vs [Product B] for Expats (2026)"
description: "[140-160 chars comparing both + CTA]"
...
---

[Quick verdict box: Winner per category]

## Quick Comparison

| Feature | Product A | Product B |
|---------|-----------|-----------|
| Monthly cost | €X | €Y |
| ... | ... | ... |

## [Product A] Review
### Pros
### Cons
### Pricing
### Best for

## [Product B] Review
### Pros
### Cons
### Pricing
### Best for

## Our Verdict
[Recommendation per user type]

[Affiliate CTAs for both products]

## FAQ (5 questions)
```

### 8.3 Service Reviews (5 stuks, 2500+ woorden)

| # | Review | Target Keyword |
|---|--------|----------------|
| 1 | Wise Review: Best for Expats in NL? | "wise review netherlands" |
| 2 | bunq Review: Best Expat Bank? | "bunq review expat" |
| 3 | SafetyWing Review: Worth It for NL Expats? | "safetywing review" |
| 4 | Independer Review: Compare Health Insurance | "independer english review" |
| 5 | NordVPN Review for Expats in NL | "nordvpn netherlands review" |

---

## 9. Content Strategie — Supporting Articles

### 9.1 Cluster Overzicht

30 supporting articles verdeeld over 6 clusters:

#### Cluster 1: Finance & Tax (7 artikelen)
| # | Article | Words | Keyword target |
|---|---------|-------|----------------|
| 1 | How the 30% Ruling Works in 2026 | 3000+ | "30 percent ruling 2026" |
| 2 | Dutch Tax Return (Belastingaangifte) for Expats | 2000 | "dutch tax return expat" |
| 3 | Zorgtoeslag: Health Insurance Allowance Guide | 1500 | "zorgtoeslag expat" |
| 4 | Huurtoeslag: Housing Allowance for Expats | 1500 | "huurtoeslag expat" |
| 5 | Kinderbijslag & Childcare Benefits Explained | 1500 | "kinderbijslag expat" |
| 6 | DigiD: How to Get and Use Your Digital ID | 1200 | "digid expat english" |
| 7 | How to Send Money Home from the Netherlands | 1500 | "send money netherlands" |

#### Cluster 2: Health & Insurance (5 artikelen)
| # | Article | Words | Keyword target |
|---|---------|-------|----------------|
| 1 | Health Insurance Netherlands Expats: Complete Guide | 3000+ | "health insurance netherlands expat" |
| 2 | Eigen Risico Explained: Dutch Deductible Guide | 1500 | "eigen risico netherlands" |
| 3 | Finding an English-Speaking Doctor in NL | 1200 | "english speaking doctor netherlands" |
| 4 | Mental Health Care in the Netherlands | 1500 | "mental health netherlands expat" |
| 5 | Pregnancy & Maternity Care for Expats | 1500 | "pregnancy netherlands expat" |

#### Cluster 3: Housing & Living (5 artikelen)
| # | Article | Words | Keyword target |
|---|---------|-------|----------------|
| 1 | Renting in the Netherlands: Complete Guide | 3000+ | "renting netherlands" |
| 2 | Understanding Dutch Rental Contracts | 1500 | "dutch rental contract explained" |
| 3 | Utilities Setup Guide (Gas, Electric, Internet) | 1200 | "utilities netherlands expat" |
| 4 | Best Internet Providers for Expats | 1500 | "best internet netherlands" |
| 5 | Dutch Housing Market 2026: What Expats Need to Know | 1500 | "housing market netherlands 2026" |

#### Cluster 4: Legal & Registration (5 artikelen)
| # | Article | Words | Keyword target |
|---|---------|-------|----------------|
| 1 | BSN Number: Complete Registration Guide | 2500+ | "bsn number netherlands" |
| 2 | Dutch Residence Permit Types Explained | 1500 | "residence permit netherlands" |
| 3 | How to Register at Your Gemeente | 1200 | "register gemeente netherlands" |
| 4 | Apostille & Document Legalization for NL | 1200 | "apostille netherlands" |
| 5 | Dutch Citizenship: Requirements & Process | 1500 | "dutch citizenship requirements" |

#### Cluster 5: Work & Career (4 artikelen)
| # | Article | Words | Keyword target |
|---|---------|-------|----------------|
| 1 | Highly Skilled Migrant (HSM) Visa Guide | 2500+ | "highly skilled migrant netherlands" |
| 2 | Starting a Business in NL as an Expat | 1500 | "start business netherlands expat" |
| 3 | DAFT Visa: US & Japan Entrepreneur Guide | 1500 | "daft visa netherlands" |
| 4 | Working While Studying in the Netherlands | 1200 | "working student netherlands" |

#### Cluster 6: Integration & Culture (4 artikelen)
| # | Article | Words | Keyword target |
|---|---------|-------|----------------|
| 1 | Civic Integration (Inburgering) Complete Guide | 2500+ | "inburgering netherlands" |
| 2 | Learning Dutch: Best Methods & Schools | 1500 | "learn dutch expat" |
| 3 | Dutch Culture & Social Norms for Newcomers | 1200 | "dutch culture expats" |
| 4 | Making Friends in the Netherlands as an Expat | 1200 | "making friends netherlands" |

### 9.2 Content Productie Richtlijnen

Per artikel:
- **Research:** Minimaal 3 officiële bronnen (rijksoverheid.nl, belastingdienst.nl, ind.nl)
- **Prijzen:** Actuele cijfers 2026, met bron en datum
- **Reviews:** Waar relevant Trustpilot/Google reviews scores
- **Personal touch:** Sarah's ervaring/advies sectie
- **Interne links:** Min. 5 per artikel (naar tools, andere guides, city pages)
- **Affiliate links:** Waar relevant, altijd met `rel="noopener nofollow sponsored"`
- **FAQ:** Min. 5 vragen per artikel (FAQPage schema)
- **Meta:** Title ≤60 chars (keyword voorop), description 140-160 chars + CTA
- **Images:** Custom SVG hero (1200x630), inline screenshots waar nuttig

---

## 10. Content Strategie — City Guides

### 10.1 Waarom City Guides?

Expats zoeken stad-specifiek. "Health insurance Amsterdam" en "BSN appointment Rotterdam" zijn echte zoekopdrachten. City guides:
1. Vangen long-tail traffic
2. Linken naar alle tools (met stad pre-geselecteerd)
3. Bieden lokale context die generieke sites missen
4. Zijn makkelijk schaalbaar (template-based)

### 10.2 City Guide Template (1500-2000 woorden per stad)

```markdown
---
title: "Expat Guide to [City] 2026: Everything You Need to Know"
description: "Moving to [City]? Complete guide: registration, housing, healthcare, costs. Free tools included."
---

## Why [City]?
[Korte intro, key stats, expat community size]

## Registration & BSN in [City]
- Gemeente address + opening hours
- Appointment booking link
- Average wait time
- [Use our BSN Planner →]

## Housing in [City]
- Average rent prices per neighborhood
- Popular expat neighborhoods
- Tips voor woningzoeken
- [Check your budget with our Housing Checker →]

## Healthcare in [City]
- English-speaking GPs (3-5 recommendations)
- Hospitals
- Emergency info
- [Find your health insurance →]

## Banking in [City]
- bunq: mobile-first, no appointment needed
- ABN AMRO: [City] branch info
- [Find your best bank →]

## Transportation
- OV-chipkaart
- Bike rental/purchase
- Key routes

## Expat Community
- Meetup groups
- Facebook groups
- Expat centers

## Cost of Living
| Expense | Average [City] | National Average |
|---------|---------------|------------------|
| Rent (1BR) | €X | €Y |
| Utilities | €X | €Y |
| Groceries | €X | €Y |
| Transport | €X | €Y |

## FAQ (5 questions)
```

### 10.3 Stad Selectie (8 steden)

| Stad | Expat populatie | Priority | Unieke hoek |
|------|----------------|----------|-------------|
| Amsterdam | Zeer groot | P0 | Tech hub, highest costs |
| Rotterdam | Groot | P0 | Port, architecture, affordable |
| The Hague | Groot | P0 | International orgs, embassies |
| Eindhoven | Medium-groot | P1 | Tech (ASML, Philips), Brainport |
| Utrecht | Medium | P1 | Student city, central |
| Groningen | Medium | P2 | Student city, cheap, north |
| Leiden | Klein-medium | P2 | University, expat-friendly |
| Maastricht | Klein-medium | P2 | South, international, EU |

---

## 11. SEO Strategie

### 11.1 Keyword Strategie

**Primary keywords (money keywords):**
```
"30% ruling calculator"           — Volume: 2.400/mo, KD: Low
"health insurance netherlands expat" — Volume: 4.400/mo, KD: Medium
"best bank expats netherlands"    — Volume: 2.900/mo, KD: Low
"bsn number netherlands"          — Volume: 6.600/mo, KD: Low
"work permit netherlands"         — Volume: 3.600/mo, KD: Medium
"wise vs revolut"                 — Volume: 8.100/mo, KD: Medium
"bunq review"                     — Volume: 3.600/mo, KD: Low
"renting netherlands"             — Volume: 1.900/mo, KD: Low
"inburgering netherlands"         — Volume: 2.400/mo, KD: Low
```

**Long-tail keywords (supporting):**
```
"how to get bsn number amsterdam"
"30 percent ruling changes 2026"
"cheapest health insurance netherlands"
"best english speaking doctor amsterdam"
"digid for expats"
"zorgtoeslag income limit 2026"
"dutch tax return expat deadline"
"housing allowance netherlands expat"
"safetywing vs cigna"
"wise netherlands review"
```

**Informational keywords (traffic builders):**
```
"moving to netherlands checklist"
"cost of living netherlands 2026"
"dutch culture tips expats"
"making friends netherlands"
"learn dutch fast"
```

### 11.2 On-Page SEO Checklist (per pagina)

- [ ] Title tag: keyword vooraan, ≤60 characters, jaar waar relevant
- [ ] Meta description: 140-160 chars, keyword, eindigt op CTA
- [ ] H1: Exact 1, bevat primary keyword
- [ ] H2s: Keyword variaties, PAA-vragen als H2
- [ ] Primary keyword in eerste 100 woorden
- [ ] Internal links: minimaal 5
- [ ] External links: minimaal 2 authoritative bronnen (rijksoverheid, IND)
- [ ] Images: Alt text met keyword, WebP format, lazy loading
- [ ] URL: kort, keyword, geen stop words
- [ ] Schema: Article/FAQPage/WebApplication (per pagina type)
- [ ] Breadcrumbs: Geïmplementeerd + BreadcrumbList schema
- [ ] Last updated: Zichtbaar op pagina + in schema
- [ ] Author: Zichtbaar + Person schema link
- [ ] Canonical URL: Self-referencing

### 11.3 Technical SEO

- **Core Web Vitals target:** LCP <2.5s, FID <100ms, CLS <0.1
- **PageSpeed target:** Performance >95, SEO 100, Best Practices 100
- **Sitemap:** Auto-generated, tools + content + cities
- **Robots.txt:** Allow all, link to sitemap
- **HTTPS:** Via GitHub Pages (automatic)
- **Mobile-first:** Alle tools responsive, touch-friendly inputs
- **Page speed:** No external fonts in critical path (preload), minimal JS, no jQuery
- **Hreflang:** Niet nodig (single language: EN)

### 11.4 Content Refresh Cadence

| Content Type | Refresh Frequentie | Wat updaten |
|-------------|-------------------|-------------|
| Tool data (prijzen, drempels) | Januari elk jaar | tax brackets, HSM thresholds, insurance premiums |
| Pillar pages | Elk kwartaal | Prijzen, regelgeving, FAQ |
| City guides | Elk half jaar | Huurprijzen, GP info |
| Versus pages | Elk kwartaal | Prijzen, features, scores |
| Supporting articles | Bij wijzigingen | Regelgeving updates |

---

## 12. E-E-A-T & YMYL Compliance

### 12.1 Waarom dit cruciaal is

ExpatNetherlandsHub valt onder **YMYL** (Your Money or Your Life):
- Belastingadvies (30% ruling)
- Zorgverzekering
- Verblijfsvergunningen
- Financiële productvergelijkingen

Google houdt YMYL-sites aan hogere E-E-A-T standaarden. We moeten dit **perfect** doen.

### 12.2 Experience (Ervaring)

- **Sarah van den Berg persona:** Half-NL, half-UK, 8 jaar expat coaching ervaring
- Elk artikel bevat een "Sarah's experience" of "From my experience" sectie
- Specifieke scenario's en case studies: "When my client Maria moved from Brazil..."
- Tool results bevatten persoonlijke tips: "In my experience, most expats overpay on..."

### 12.3 Expertise

- **Gedetailleerde auteurspagina** (`/about/`):
  - Foto (AI-generated professional headshot)
  - Uitgebreide bio (500+ woorden)
  - Credentials en ervaring
  - Links naar social profiles
  - "Sarah has helped 500+ expats navigate Dutch bureaucracy"
- **Person schema** op auteurspagina
- **Bronvermelding:** Elke claim linkt naar officiële bron (rijksoverheid.nl, belastingdienst.nl, etc.)

### 12.4 Authoritativeness

- **Externe links naar authoritative bronnen** in elk artikel
- **Citeer specifieke wetten en regelgeving** (Wet inburgering 2021, etc.)
- **Datum last updated** prominent zichtbaar
- **Disclaimer op tool pages:** "This calculator provides estimates only. For binding tax advice, consult a qualified tax advisor."
- **Medical disclaimer** op health pages
- **Legal disclaimer** op visa/permit pages

### 12.5 Trustworthiness

- **Duidelijke affiliate disclosure** op elke pagina met affiliate links
- **Privacy policy** compliant met AVG/GDPR
- **Cookie consent** met Consent Mode v2
- **Contact pagina** met echt formulier
- **HTTPS** everywhere
- **Geen misleidende claims** — altijd "estimate", "indication", "check with..."

### 12.6 Implementatie Checklist

- [ ] About page met uitgebreide Sarah bio + credentials
- [ ] Author box op elk artikel met foto + korte bio
- [ ] Person schema op about page
- [ ] Bronnen linken in elk artikel (min. 2 officiële bronnen)
- [ ] Datum "last updated" op elke pagina
- [ ] Affiliate disclosure (globaal + per pagina)
- [ ] Medical/tax/legal disclaimers per relevant pagina type
- [ ] Privacybeleid (AVG-compliant)
- [ ] Cookiebanner met Consent Mode v2
- [ ] Contact pagina met werkend formulier

---

## 13. Affiliate Programma's & Monetisatie

### 13.1 Primaire Affiliate Partners

| Partner | Programma | Commissie (est.) | Product | Pagina's |
|---------|-----------|------------------|---------|----------|
| **Wise** | Impact.com (aan te melden) | £10-15 per signup + first transfer | Money transfers, multi-currency account | Bank chooser, money transfer guide, city guides |
| **bunq** | Direct referral | €10-25 per account opening | Dutch IBAN, expat-friendly bank | Bank chooser, city guides, BSN guide |
| **SafetyWing** | Direct affiliate | 10% recurring | International health/travel insurance | Insurance chooser, expat insurance guide |
| **Independer** | Awin (mid=8558) | Per lead | Zorgverzekering vergelijking | Health insurance wizard, health guides |
| **NordVPN** | Direct (aff_id=141337) | 40-100% first payment | VPN, online privacy | Privacy guide, digital security |
| **NordPass** | Direct (offer_id=488) | Per signup | Password manager | Digital security guide |

### 13.2 Secundaire Partners (aan te melden)

| Partner | Platform | Product | Target pagina's | Geschatte commissie |
|---------|----------|---------|-----------------|-------------------|
| **Cigna Global** | Direct | Expat health insurance | Insurance chooser | €50-100/lead |
| **Allianz Care** | Direct | Expat health insurance | Insurance chooser | €30-80/lead |
| **ING** | Daisycon | Bank account | Bank chooser | €15-30/signup |
| **ABN AMRO** | Daisycon | Bank account | Bank chooser | €15-30/signup |
| **Booking.com** | Direct | Temporary housing | Housing guide, city guides | 25-40% commission |
| **HousingAnywhere** | Direct | Rental platform | Housing guide | Per lead |
| **KLM/Transavia** | Daisycon | Flights | General | Per booking |
| **Babbel** | Awin | Dutch language learning | Learn Dutch guide | Per subscription |
| **Preply** | Impact.com | Online Dutch tutors | Learn Dutch guide | Per booking |
| **Skoove** | — | — | — | — |

### 13.3 Monetisatie Per Pagina Type

| Pagina type | Primaire monetisatie | Secundaire |
|-------------|---------------------|------------|
| Tool page | Affiliate CTA in resultaten | Email capture |
| Pillar guide | Inline affiliate links + CTA boxes | Tool referral |
| Versus page | Affiliate links voor beide producten | Email capture |
| Service review | Affiliate CTA (prominent) | Related reviews |
| City guide | Meerdere affiliate links (bank, insurance, housing) | Tool referrals |
| Info article | Contextual affiliate links | Internal links naar money pages |

### 13.4 Revenue Model

```
TRAFFIC → TOOL USE → PERSONALIZED RESULT → AFFILIATE CLICK → CONVERSION

Conversion funnel:
- 1000 visitors/month to tool page
- 60% use the tool (600)
- 40% click affiliate CTA (240)
- 5% convert (12 signups)
- Average commission: €15
- Revenue per tool: €180/month

x10 tools = €1.800/month (conservative)
+ Article affiliate clicks: €500/month
+ Email list upsell: €200/month
────────────────────────────────
Target month 12: €2.500-3.500/month
```

### 13.5 Affiliate Link Beheer

Alle affiliate URLs opslaan in `data/affiliates.json`:

```json
{
  "wise": {
    "name": "Wise",
    "url": "https://wise.prf.hn/l/XXXXX",
    "platform": "impact",
    "rel": "noopener nofollow sponsored",
    "pages": ["bank-chooser", "money-transfer-guide", "wise-review"]
  },
  "bunq": {
    "name": "bunq",
    "url": "https://www.bunq.com/r/XXXXX",
    "platform": "direct",
    "rel": "noopener nofollow sponsored",
    "pages": ["bank-chooser", "bunq-review", "city-guides"]
  }
}
```

Hugo partial voor affiliate links:
```html
<!-- layouts/partials/affiliate-link.html -->
<a href="{{ .url }}" target="_blank" rel="{{ .rel }}" class="cta-affiliate"
   data-affiliate="{{ .name }}" data-page="{{ .page }}">
  {{ .text }} →
</a>
```

GA4 event tracking op elke affiliate click:
```javascript
gtag('event', 'affiliate_click', {
  'affiliate_partner': partner,
  'affiliate_page': page,
  'affiliate_position': position  // 'tool-result', 'inline', 'sidebar'
});
```

---

## 14. Technische Architectuur

### 14.1 Stack

| Component | Technologie | Reden |
|-----------|------------|-------|
| SSG | Hugo 0.128.0 | Bewezen, snel, same as BSG |
| Hosting | GitHub Pages | Gratis, betrouwbaar, CI/CD |
| Theme | Custom "expat" theme | Nieuw design, niet starter |
| Tools | Static HTML/CSS/JS | Geen server nodig, snel |
| Analytics | GA4 (G-2TJSDJB4CG) | Al actief |
| Search Console | Geverifieerd | Al actief |
| Email | Brevo (toekomstig) | Gratis tier, API |
| Forms | Formspree of Brevo | Contact form |

### 14.2 Hugo Structuur (nieuw)

```
expatnetherlandshub.github.io/
├── config.toml
├── content/
│   ├── _index.md                    ← Homepage
│   ├── guides/
│   │   ├── _index.md               ← Guides hub
│   │   ├── finance/
│   │   │   ├── _index.md           ← Finance cluster hub
│   │   │   └── *.md                ← Finance articles
│   │   ├── health/
│   │   ├── housing/
│   │   ├── legal/
│   │   ├── work/
│   │   └── integration/
│   ├── cities/
│   │   ├── _index.md               ← Cities hub
│   │   └── *.md                    ← City guides
│   ├── services/
│   │   ├── _index.md               ← Services hub
│   │   └── *.md                    ← Reviews + versus
│   ├── about.md
│   ├── contact.md
│   ├── privacy.md
│   └── disclaimer.md
├── static/
│   ├── tools/                       ← Interactieve tools
│   ├── images/
│   │   ├── tools/                   ← Tool icons/illustrations
│   │   ├── cities/                  ← City hero images
│   │   └── guides/                  ← Article hero images
│   └── css/
│       └── custom.css               ← Brand overrides
├── layouts/
│   ├── _default/
│   │   ├── baseof.html             ← Base template
│   │   ├── single.html            ← Article template
│   │   └── list.html              ← Hub page template
│   ├── partials/
│   │   ├── head.html              ← Meta, schema, OG
│   │   ├── header.html            ← Navigation
│   │   ├── footer.html            ← Footer
│   │   ├── author-box.html        ← Author component
│   │   ├── tool-cta.html          ← Tool CTA component
│   │   ├── affiliate-link.html    ← Affiliate link component
│   │   ├── faq.html               ← FAQ accordion
│   │   ├── breadcrumb.html        ← Breadcrumbs
│   │   ├── comparison-table.html  ← Product comparison
│   │   ├── city-card.html         ← City quick link
│   │   └── schema/
│   │       ├── article.html
│   │       ├── faq.html
│   │       ├── webapp.html
│   │       ├── person.html
│   │       └── breadcrumb.html
│   ├── shortcodes/
│   │   ├── tool-cta.html          ← {{< tool-cta >}}
│   │   ├── affiliate-cta.html     ← {{< affiliate-cta >}}
│   │   ├── comparison.html        ← {{< comparison >}}
│   │   ├── quick-fact.html        ← {{< quick-fact >}}
│   │   ├── disclaimer.html        ← {{< disclaimer >}}
│   │   └── city-link.html         ← {{< city-link >}}
│   └── cities/
│       └── single.html            ← City guide template
├── data/
│   ├── affiliates.json            ← Affiliate URLs
│   ├── tools.json                 ← Tool metadata
│   └── cities.json                ← City data
└── .github/
    └── workflows/
        └── deploy.yml             ← GitHub Actions
```

### 14.3 Performance Budget

| Metric | Target | Hoe |
|--------|--------|-----|
| Total page weight | <500KB | No jQuery, minimal images, SVG icons |
| First Contentful Paint | <1.5s | Critical CSS inline, preload fonts |
| Largest Contentful Paint | <2.5s | Optimized hero images, lazy loading |
| JavaScript (tools page) | <50KB | Vanilla JS, no frameworks |
| CSS total | <30KB | Utility-first, purge unused |
| Lighthouse Performance | >95 | |
| Lighthouse SEO | 100 | |

### 14.4 Bestaande Content Migratie

De 38 bestaande artikelen worden:
1. **Geherstructureerd** naar de nieuwe URL-structuur (`/guides/[cluster]/[slug]/`)
2. **301 redirects** voor oude URLs (via Hugo aliases)
3. **Verrijkt** met interne links naar tools en andere guides
4. **Geüpdatet** met affiliate links waar relevant
5. **Geaudit** op kwaliteit (zelfde checklist als BSG audit)

---

## 15. Schema.org & Structured Data

### 15.1 Schema Per Pagina Type

| Pagina type | Schema types |
|-------------|-------------|
| Homepage | WebSite + Organization |
| Tool page | WebApplication + FAQPage + BreadcrumbList |
| Guide/Article | Article + FAQPage + BreadcrumbList |
| City guide | Article + FAQPage + BreadcrumbList + Place |
| Service review | Review + Product + FAQPage + BreadcrumbList |
| About page | Person + BreadcrumbList |
| Hub pages | CollectionPage + BreadcrumbList |

### 15.2 WebApplication Schema (tools)

```json
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "30% Ruling Calculator Netherlands 2026",
  "description": "Calculate your exact tax benefit with the Dutch 30% ruling",
  "url": "https://expatnetherlandshub.com/tools/30-percent-ruling-calculator/",
  "applicationCategory": "FinanceApplication",
  "operatingSystem": "Web",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "EUR"
  },
  "author": {
    "@type": "Person",
    "name": "Sarah van den Berg",
    "url": "https://expatnetherlandshub.com/about/"
  },
  "dateModified": "2026-03-06"
}
```

### 15.3 Article + FAQPage Combo

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Complete Guide to the 30% Ruling Netherlands 2026",
  "author": {
    "@type": "Person",
    "name": "Sarah van den Berg"
  },
  "datePublished": "2026-03-15",
  "dateModified": "2026-03-15",
  "publisher": {
    "@type": "Organization",
    "name": "ExpatNetherlandsHub",
    "logo": { "@type": "ImageObject", "url": "..." }
  }
}
```

---

## 16. Conversie-Optimalisatie (CRO)

### 16.1 CTA Plaatsing Strategie

Elke pagina volgt deze CTA-hiërarchie:

```
1. HERO CTA (above the fold)
   → Tool pages: "Calculate Now" / "Start the Quiz"
   → Articles: "Use our free [tool] →" + tool link

2. INLINE CTA (na eerste waardevolle sectie, ~300 woorden)
   → Contextual affiliate link of tool referral

3. RESULT CTA (na tool resultaat)
   → Primaire affiliate link: "Open account with [Partner] →"
   → Secundaire: "Compare more options on [Partner] →"

4. SIDEBAR CTA (sticky, desktop only)
   → Email capture: "Get your free expat checklist"
   → Related tool link

5. BOTTOM CTA (einde pagina)
   → Recap + affiliate link
   → Related tools/articles
```

### 16.2 Email Lead Capture

**Lead magnet:** "The Ultimate Expat Checklist: 47 Things to Do in Your First 3 Months"

**Placement:**
- Sidebar (sticky)
- Na tool resultaat ("Get this calculation emailed to you")
- Exit intent popup (desktop)
- Bottom of articles

**Email flow (Brevo):**
1. Welcome email + checklist PDF
2. Day 3: "Have you sorted your health insurance?" → wizard link
3. Day 7: "Save money on international transfers" → Wise affiliate
4. Day 14: "Best banks for expats" → bank chooser
5. Monthly: "What's new for expats in NL" → latest articles

**Projected email list growth:**
- Month 1-3: 50-150 subscribers
- Month 4-6: 150-500 subscribers
- Month 7-12: 500-2000 subscribers
- Email conversion rate: 2-3% (€0.50-1.00 per subscriber per month)

### 16.3 A/B Test Plan

| Element | Variant A | Variant B | Metric |
|---------|-----------|-----------|--------|
| Tool CTA text | "Calculate now" | "See your results" | Click rate |
| CTA color | Oranje (#E8832A) | Groen (#1B6B4A) | Click rate |
| Result format | Single recommendation | Top 3 list | Affiliate CTR |
| Email popup | After 30s | After 60% scroll | Signup rate |
| Sidebar CTA | Tool link | Email capture | Overall revenue |

---

## 17. Backlink & Outreach Strategie

### 17.1 Linkable Assets

| Asset | Waarom linkbaar | Target linkers |
|-------|----------------|----------------|
| 30% Ruling Calculator | Unieke tool, nuttig, gratis | Expat blogs, tax advisors, forums |
| City cost-of-living data | Actuele cijfers, vergelijkingen | Relocation companies, real estate |
| Expat Checklist (PDF) | Praktisch, deelbaar | Expat Facebook groepen, blogs |
| Visa Permit Finder | Unieke interactieve decision tree | Immigration lawyers, HR blogs |

### 17.2 Outreach Kanalen

| Kanaal | Strategie | Volume/maand |
|--------|-----------|-------------|
| **Expat forums** | Antwoord geven + tool linken (IAmExpat, Reddit r/Netherlands) | 10 posts |
| **Facebook groepen** | Helpende antwoorden + link (Expats in NL, Amsterdam Expats) | 15 posts |
| **Guest posts** | Schrijf voor DutchReview, Expat Republic | 1-2 per maand |
| **HARO/Qwoted** | Reageer op journalist queries over NL expat topics | 5 pitches/maand |
| **Directories** | Expat directory submissions | 10 (eenmalig) |
| **Partnerships** | Relocation companies, tax advisors → link exchange | 2 per maand |

### 17.3 Directory Submissions

- iamexpat.nl business listing
- expatfocus.com
- internations.org
- angloinfo.com
- expatarrivals.com
- justlanded.com
- expat.com
- linkedin.com (bedrijfspagina)
- google.com/business (indien mogelijk)
- yelp.nl

### 17.4 Content Partnerships

**Tax advisory firms:** Offer free calculator embed in ruil voor backlink
```
"Embed our free 30% ruling calculator on your website:
<iframe src='https://expatnetherlandshub.com/tools/30-percent-ruling-calculator/?embed=true' ...></iframe>"
```

**Relocation companies:** Bied "powered by ExpatNetherlandsHub" tools aan voor hun klanten

---

## 18. Analytics & KPI Dashboard

### 18.1 Primary KPIs

| KPI | Target M3 | Target M6 | Target M12 |
|-----|-----------|-----------|------------|
| Organic sessions/month | 500 | 3.000 | 15.000 |
| Tool interactions/month | 100 | 800 | 5.000 |
| Affiliate clicks/month | 30 | 200 | 1.500 |
| Affiliate revenue/month | €50 | €500 | €3.000 |
| Email subscribers | 50 | 300 | 1.500 |
| Indexed pages | 30 | 60 | 80+ |
| Avg. position (top 20 keywords) | 40 | 20 | 10 |
| Domain Rating (Ahrefs) | 5 | 15 | 30 |

### 18.2 GA4 Event Tracking

```javascript
// Tool events
gtag('event', 'tool_start', { tool_name, step: 1 });
gtag('event', 'tool_step', { tool_name, step: N });
gtag('event', 'tool_complete', { tool_name, result_type });
gtag('event', 'tool_cta_click', { tool_name, partner, position });

// Content events
gtag('event', 'article_scroll', { depth: '25%|50%|75%|100%' });
gtag('event', 'faq_expand', { question });
gtag('event', 'internal_link_click', { from_page, to_page });

// Conversion events
gtag('event', 'affiliate_click', { partner, page, position });
gtag('event', 'email_signup', { source, lead_magnet });
```

### 18.3 Rapportage

- **Dagelijks:** Check indexeringsstatus (script)
- **Wekelijks:** Traffic + affiliate clicks overview
- **Maandelijks:** Full report (traffic, rankings, revenue, content gaps)
- **Kwartaal:** Strategische review + roadmap update

Gebruik bestaand script: `scripts/google-report.py --site expat`

---

## 19. Implementatie Roadmap (12 maanden)

### Fase 1: Foundation (Week 1-4) — MAART 2026

**Week 1: Design & Theme**
- [ ] Nieuw kleurenpalet + typografie implementeren
- [ ] Baseof.html, header, footer, nav redesign
- [ ] Homepage layout bouwen
- [ ] Mobile responsive basis
- [ ] Dark/light mode (optioneel)

**Week 2: Structuur & Migratie**
- [ ] Nieuwe URL-structuur opzetten (content/, static/)
- [ ] 38 bestaande artikelen migreren naar /guides/ structuur
- [ ] 301 redirects configureren (Hugo aliases)
- [ ] Hub pages aanmaken (tools, guides, cities, services)
- [ ] Navigation + footer updaten

**Week 3: Core Components**
- [ ] Author box component
- [ ] Breadcrumbs + schema
- [ ] FAQ accordion + FAQPage schema
- [ ] Tool CTA shortcode
- [ ] Affiliate link shortcode
- [ ] Comparison table component
- [ ] Trust badges

**Week 4: First 2 Tools**
- [ ] 30% Ruling Calculator (P0)
- [ ] Salary Checker (P0)
- [ ] Tool page template
- [ ] WebApplication schema
- [ ] GA4 event tracking

### Fase 2: Core Tools & Money Pages (Week 5-8) — APRIL 2026

**Week 5-6: Tools bouwen**
- [ ] Health Insurance Wizard (P0) — TOP PRIORITY
- [ ] Bank Account Chooser (P0)
- [ ] Tools hub page
- [ ] Data files (insurance-providers.json, banks.json)

**Week 7-8: Money Pages schrijven**
- [ ] 5 pillar pages (30% ruling, health insurance, banks, BSN, work permits)
- [ ] 3 versus pages (Wise vs Revolut, bunq vs ABN AMRO, SafetyWing vs Cigna)
- [ ] 2 service reviews (Wise, bunq)
- [ ] Affiliate links integreren
- [ ] Internal linking audit

### Fase 3: Content Expansion (Week 9-16) — MEI-JUNI 2026

**Week 9-10: Remaining Tools**
- [ ] Visa & Permit Finder (P1)
- [ ] BSN Appointment Planner (P1)
- [ ] Expat Insurance Chooser (P1)

**Week 11-12: City Guides**
- [ ] Amsterdam (P0)
- [ ] Rotterdam (P0)
- [ ] The Hague (P0)
- [ ] City guide template

**Week 13-14: Supporting Content**
- [ ] 10 supporting articles (highest volume keywords)
- [ ] Finance cluster: tax return, zorgtoeslag, DigiD
- [ ] Health cluster: eigen risico, English GP, mental health

**Week 15-16: More Content**
- [ ] 10 more supporting articles
- [ ] Housing cluster: rental contracts, utilities
- [ ] Legal cluster: residence permit, gemeente registration
- [ ] 3 more versus pages
- [ ] 3 more service reviews

### Fase 4: Growth & Optimization (Week 17-26) — JULI-SEPT 2026

**Week 17-18: Remaining Tools**
- [ ] Housing Budget Checker (P2)
- [ ] Inburgering Route Builder (P2)
- [ ] Diploma Evaluation Planner (P2)

**Week 19-20: City Guide Expansion**
- [ ] Eindhoven, Utrecht (P1)
- [ ] Groningen, Leiden, Maastricht (P2)

**Week 21-22: Content Completion**
- [ ] Remaining 10 supporting articles
- [ ] All 30 supporting articles done
- [ ] Remaining versus pages
- [ ] Remaining service reviews

**Week 23-24: Email System**
- [ ] Brevo integration
- [ ] Lead magnet (expat checklist PDF)
- [ ] Email capture forms
- [ ] Welcome email sequence (5 emails)

**Week 25-26: Optimization**
- [ ] Full SEO audit (same methodology as BSG)
- [ ] PageSpeed optimization
- [ ] A/B test setup
- [ ] Content refresh (Q3 data updates)
- [ ] Internal link audit

### Fase 5: Scale & Authority (Week 27-52) — OKT 2026 - MAART 2027

**Maandelijks:**
- [ ] 4-6 nieuwe artikelen per maand (emerging topics, seasonal)
- [ ] 2-3 backlink outreach activiteiten per week
- [ ] Content refresh cycle (quarterly)
- [ ] Affiliate programma's uitbreiden
- [ ] Email list nurturing
- [ ] Performance monitoring + optimization

**Milestones:**
- M9 (Dec 2026): 70+ pages, 5+ tools live, €500+/month revenue
- M12 (Mar 2027): 80+ pages, 10 tools live, €2.500-3.500/month revenue

---

## 20. Revenue Projecties

### 20.1 Conservative Scenario

| Maand | Organic Traffic | Tool Users | Affiliate Clicks | Revenue |
|-------|----------------|------------|------------------|---------|
| M1 | 100 | 20 | 5 | €10 |
| M2 | 200 | 50 | 15 | €30 |
| M3 | 500 | 120 | 40 | €80 |
| M4 | 1.000 | 250 | 80 | €200 |
| M5 | 1.500 | 400 | 120 | €350 |
| M6 | 2.500 | 700 | 200 | €600 |
| M7 | 4.000 | 1.100 | 350 | €900 |
| M8 | 5.500 | 1.500 | 500 | €1.200 |
| M9 | 7.000 | 2.000 | 650 | €1.600 |
| M10 | 9.000 | 2.500 | 850 | €2.000 |
| M11 | 11.000 | 3.200 | 1.100 | €2.500 |
| M12 | 15.000 | 4.500 | 1.500 | €3.000 |

### 20.2 Revenue Per Affiliate Partner (M12 target)

| Partner | Clicks/mo | Conv. rate | Commission | Revenue/mo |
|---------|-----------|------------|------------|------------|
| Independer (health ins.) | 400 | 3% | €15/lead | €180 |
| Wise | 300 | 8% | €12/signup | €288 |
| bunq | 200 | 6% | €20/signup | €240 |
| SafetyWing | 150 | 5% | €8/mo recurring | €480* |
| NordVPN | 100 | 4% | €10/signup | €40 |
| Other partners | 350 | 3% | €10 avg | €105 |
| **Totaal** | **1.500** | | | **€1.333** |

*SafetyWing recurring: builds over time, M12 estimate includes accumulated subscribers

**Aanvullende revenue streams:**
- Email affiliate promos: €200-400/month
- Sponsored content (M9+): €300-500/month
- Tool embeds/licensing (M12+): €200-300/month

**Realistic M12 total: €2.500 - €3.500/month**

### 20.3 Break-Even Analyse

| Kosten | Maandelijks |
|--------|------------|
| Hosting | €0 (GitHub Pages) |
| Domein | €1/month (Strato) |
| Brevo email | €0 (free tier tot 300 emails/dag) |
| Tools/software | €0 |
| Tijd investering | ~20 uur/week |
| **Totaal** | **~€1/month** |

Break-even: dag 1. Alle revenue is winst (na belasting).

---

## 21. Risico's & Mitigatie

| Risico | Impact | Kans | Mitigatie |
|--------|--------|------|----------|
| Google algorithm update raakt rankings | Hoog | Medium | Diversifieer traffic (email, social), focus op E-E-A-T |
| Affiliate programma stopt/wijzigt | Medium | Medium | Multiple partners per categorie, nooit 100% op 1 partner |
| Concurrent lanceert vergelijkbare tools | Medium | Laag | First-mover voordeel, continue verbetering, content diepte |
| 30% ruling wordt afgeschaft/beperkt | Hoog | Laag | Diversifieer naar andere tools/topics (health, banking is altijd nodig) |
| Expat markt NL krimpt | Medium | Zeer laag | NL trekt alleen maar meer kennis migranten aan (Brainport, tech) |
| YMYL penalty door onjuiste info | Hoog | Medium | Altijd bronnen citeren, disclaimers, regular fact-checking |
| Burnout (te veel werk naast BSG) | Medium | Medium | Prioriteer P0 tools eerst, automatiseer waar mogelijk |
| Affiliate commissie daalt | Medium | Medium | Volume compensatie, diversificatie, eigen producten (checklists) |

---

## 22. Bijlagen

### Bijlage A: Bestaande 38 Artikelen — Migratie Plan

Elk bestaand artikel wordt gemapt naar de nieuwe structuur:

```
OLD: /blog/[slug]/
NEW: /guides/[cluster]/[slug]/
REDIRECT: Hugo alias in front matter
```

Migratie stappen per artikel:
1. Verplaats naar juiste cluster directory
2. Voeg Hugo alias toe voor oude URL
3. Update front matter (categories, tags, schema)
4. Voeg affiliate links toe waar relevant
5. Voeg interne links toe (min. 5)
6. Voeg FAQ sectie toe (min. 5 vragen)
7. Controleer schrijfstijl (Sarah's stem)
8. Update meta title en description

### Bijlage B: Concurrentie Analyse

**iamexpat.nl**
- Sterkte: Groot bereik, community, job board
- Zwakte: Display ads overkill, geen tools, gedateerde content
- Kans: Wij bieden betere UX + gratis tools

**expatica.com**
- Sterkte: Multi-country, veel content
- Zwakte: Generiek, niet NL-specifiek genoeg, langzaam
- Kans: Wij zijn 100% NL-focused met lokale details

**30percentruling.com**
- Sterkte: Niche authority, goede calculator
- Zwakte: Alleen 30% ruling, geen andere tools, geen affiliate
- Kans: Wij bouwen bétere calculator + 9 andere tools

**dutchreview.nl**
- Sterkte: Leuk geschreven, goede brand
- Zwakte: Lifestyle focus, weinig practical tools
- Kans: Complementair — wij zijn practical, zij zijn entertaining

### Bijlage C: Seizoenspatronen

| Maand | Trend | Content focus |
|-------|-------|---------------|
| Jan | Health insurance switching deadline (net geweest) | "Did you switch? Compare now" |
| Feb-Mar | Tax return season | Belastingaangifte guide, 30% ruling refresh |
| Apr-Jun | Peak relocation season (university, new jobs) | BSN, housing, banking guides |
| Jul-Aug | Summer move-ins, orientation year start | City guides, registration |
| Sep | University start, HSM peak | Student guides, salary checker |
| Oct-Nov | Open enrollment health insurance | Health insurance wizard PUSH |
| Dec | Year-end tax planning | 30% ruling, zorgtoeslag |

### Bijlage D: Tool Data Update Schema

Alle tool data moet jaarlijks geüpdatet (sommige vaker):

| Data | Update frequentie | Bron |
|------|-------------------|------|
| Tax brackets (schijven) | Januari | belastingdienst.nl |
| HSM salary thresholds | Januari | ind.nl |
| Zorgtoeslag limits | Januari | toeslagen.nl |
| Huurtoeslag limits | Januari | toeslagen.nl |
| Health insurance premiums | November (open enrollment) | verzekeraars, independer |
| Bank fees | Kwartaal | bank websites |
| Rental prices per city | Kwartaal | CBS, Pararius |
| Visa/permit fees | Bij wijziging | ind.nl |

### Bijlage E: Schrijfstijl Sarah van den Berg

**Tone of voice:**
- Warm, friendly, knowledgeable
- "I've been through this myself" attitude
- Never condescending, always helpful
- Uses "you" and "I" — personal, direct
- British English spelling (colour, analyse, etc.)
- Sprinkles in Dutch terms with explanation: "your eigen risico (deductible)"

**Voorbeeld intro:**
> "When I first moved to the Netherlands, figuring out health insurance felt like solving a puzzle in a language I didn't speak. Eight years and hundreds of expat consultations later, I've distilled everything into this guide — and built a free tool that does the comparing for you."

**Nooit:**
- "We recommend" (persoonlijk: "I recommend" of "my advice is")
- Onnodig jargon zonder uitleg
- Vage beloftes ("the best", "amazing") zonder onderbouwing
- AI-achtige zinnen ("It's important to note that...")
- Placeholder-achtige content

### Bijlage F: Design Assets Nodig

| Asset | Formaat | Aantal | Beschrijving |
|-------|---------|--------|-------------|
| Logo | SVG | 1 + dark variant | Modern, clean, "ENH" monogram |
| Favicon | PNG/ICO | 1 set (16-512px) | Herkenbaar op tabblad |
| Tool icons | SVG | 10 | Eén per tool, consistent stijl |
| Hero illustrations | SVG | 5 | Homepage, about, tools, guides, cities |
| City skylines | SVG | 8 | Eén per stad, herkenbaar |
| Social sharing | PNG 1200x630 | Per pagina | OG images |
| Author photo | JPEG/WebP | 1 | Sarah van den Berg (AI-generated) |
| Partner logos | SVG/PNG | 10+ | Wise, bunq, SafetyWing, etc. |
| Step icons | SVG | 20+ | Wizard stappen, checklist items |

---

## Samenvatting: Eerste Actie Items

De eerste week focust op **foundation**. Concreet:

1. **Nieuw theme bouwen** (kleurenpalet, typografie, layout componenten)
2. **URL-structuur opzetten** (content directories, hub pages)
3. **38 artikelen migreren** (verplaatsen + redirects)
4. **Eerste 2 tools bouwen** (30% ruling calculator + salary checker)
5. **Affiliate accounts activeren** (Wise via Impact, bunq referral)

> Dit plan is het complete bouwplan. We volgen het stap voor stap, tool voor tool, pagina voor pagina. Net als BSG — maar dan beter, sneller, en met alle lessen die we geleerd hebben.

---

*Laatst bijgewerkt: 6 maart 2026*
*Volgende review: na Fase 1 (eind maart 2026)*
