# Expat Netherlands Hub — Afbeeldingen Automatisering Plan 2026

## Probleem

Alle ~76 artikelen gebruiken generieke SVG category banners (`/images/categories/*.svg`). Er zijn geen productscreenshots, echte foto's of vergelijkingsafbeeldingen. Dit kost ons:

- **Google Image Search traffic** (nu 0 clicks)
- **Social media previews** (geen OG images)
- **CTR in zoekresultaten** (geen rich snippets met afbeelding)
- **E-E-A-T signaal** (generieke content oogt niet authentiek)

## Schrijfstijl constraint

Onze stijlgids verbiedt: stockfoto's, AI-gegenereerde afbeeldingen, generieke illustraties.
Wel toegestaan: echte foto's (Wikimedia Commons), eigen screenshots, branded graphics.

---

## Strategie: 4 Lagen

### Laag 1: Branded Featured Images (ALLE artikelen)

**Doel:** Elke pagina een unieke 1200x630 OG image.

| Item | Detail |
|------|--------|
| Script | `scripts/generate-featured-images.js` (Node.js + Sharp + @napi-rs/canvas) |
| Input | Front matter van elk `.md` bestand (title, categories, type) |
| Output | 1200x630 WebP per artikel |
| Design | Categorie-kleur achtergrond + titel tekst + site logo |
| Locatie | `/static/images/featured/[slug].webp` |
| Front matter | `featured_image: "/images/featured/[slug].webp"` |
| Dekking | Alle ~76 artikelen |

**Kleuren per categorie:**

| Categorie | Hex | Naam |
|-----------|-----|------|
| finance | #1B6B4A | groen |
| health | #2563EB | blauw |
| housing | #E8832A | oranje |
| legal | #7C3AED | paars |
| work | #0891B2 | teal |
| integration | #DC2626 | rood |
| daily-life | #4F46E5 | indigo |
| cities | #059669 | emerald |

**Design specificatie:**
- Achtergrond: solid categorie-kleur
- Titel: wit, DM Sans Bold, max 3 regels, auto-size
- Logo: site logo rechtsonder (klein, wit)
- Subtitel: categorie naam + "| Expat Netherlands Hub"
- Rand: 2px wit border-radius 12px

### Laag 2: Stadsfoto's (city guides + housing)

**Doel:** Echte foto's van Nederlandse steden in artikelen.

| Item | Detail |
|------|--------|
| Script | `scripts/fetch-city-photos.py` (Python + Pillow + requests) |
| Bron | Wikimedia Commons API (gratis, CC-BY-SA) |
| Output | 1200x800 WebP, geoptimaliseerd |
| Locatie | `/static/images/cities/[city].webp` |
| Gebruik | Inline afbeelding in city pages + moving guides |
| Dekking | 12 steden, ~20 artikelen |

**Steden:**
Amsterdam, Rotterdam, Den Haag, Utrecht, Eindhoven, Leiden, Groningen, Maastricht, Delft, Haarlem, Den Bosch, Breda

**Werkwijze:**
1. Wikimedia Commons API: zoek `[city] skyline` of `[city] panorama`
2. Filter op licentie (CC-BY-SA 4.0 of CC0)
3. Download hoogste resolutie
4. Resize naar 1200x800, compress naar WebP (quality 80)
5. Sla attributie op in `images/cities/ATTRIBUTIONS.md`

### Laag 3: Tool Screenshots (tool pages)

**Doel:** Automatische screenshots van alle 11 tools als OG images.

| Item | Detail |
|------|--------|
| Script | `scripts/screenshot-tools.js` (Playwright) |
| Actie | Screenshot van elke tool page (desktop 1280x800) |
| Output | 1200x630 WebP |
| Locatie | `/static/images/tools/[tool-slug]-screenshot.webp` |
| Gebruik | OG image + /tools/ overview pagina |
| Dekking | 11 tool pages |

**Werkwijze:**
1. Start Hugo dev server (`hugo server --port 1313`)
2. Playwright opent elke tool URL
3. Wacht op volledige load (networkidle)
4. Screenshot viewport 1280x800
5. Crop naar 1200x630 (center)
6. Convert naar WebP (quality 85)

### Laag 4: Vergelijkingstabellen als afbeelding (versus/pillar)

**Doel:** Shareable vergelijkingstabellen voor social media en Google Images.

| Item | Detail |
|------|--------|
| Script | `scripts/generate-comparison-images.js` (Puppeteer of html-to-image) |
| Input | Vergelijkingstabel data uit artikelen |
| Output | 800x600 WebP |
| Design | Site kleuren, DM Sans font, schone tabel layout |
| Locatie | `/static/images/comparisons/[slug]-table.webp` |
| Dekking | ~15-20 vergelijkingsartikelen |

---

## Uitvoeringsplan

### Fase 1: Branded Featured Images (HOOGSTE PRIORITEIT)

**Geschatte effort:** 2-3 uur script + generatie

1. Installeer dependencies: `npm install sharp @napi-rs/canvas`
2. Bouw `scripts/generate-featured-images.js`:
   - Lees alle `.md` bestanden uit `content/`
   - Parse front matter (title, categories)
   - Genereer 1200x630 canvas per artikel
   - Exporteer als WebP naar `static/images/featured/`
3. Update front matter `featured_image` in elk bestand
4. Voeg OG image meta tag toe in `baseof.html` (als nog niet aanwezig):
   ```html
   {{ with .Params.featured_image }}
   <meta property="og:image" content="{{ . | absURL }}" />
   {{ end }}
   ```
5. Commit + push

### Fase 2: Stadsfoto's

**Geschatte effort:** 1-2 uur script + download

1. Bouw `scripts/fetch-city-photos.py`
2. Download + resize 12 stadsfoto's
3. Voeg inline `![Amsterdam skyline](/images/cities/amsterdam.webp)` toe in city articles
4. Maak `ATTRIBUTIONS.md` met licentie-info
5. Commit + push

### Fase 3: Tool Screenshots

**Geschatte effort:** 1 uur script + generatie

1. Installeer Playwright: `npm install playwright`
2. Bouw `scripts/screenshot-tools.js`
3. Start Hugo server, screenshot alle 11 tools
4. Update tool pages met OG image
5. Commit + push

### Fase 4: Vergelijkingstabellen

**Geschatte effort:** 2-3 uur script + generatie

1. Bouw `scripts/generate-comparison-images.js`
2. Parse tabellen uit `.md` bestanden
3. Render als gestileerde HTML, screenshot, convert naar WebP
4. Voeg afbeeldingen toe aan vergelijkingsartikelen
5. Commit + push

---

## Bestandsstructuur na implementatie

```
static/images/
  featured/          <- branded featured images (76 bestanden)
  cities/            <- echte stadsfoto's (12 bestanden)
  tools/             <- tool screenshots (11 bestanden)
  comparisons/       <- vergelijkingstabellen (15-20 bestanden)
  categories/        <- bestaande SVG banners (behouden als fallback)
```

## Technische vereisten

```bash
# Node.js dependencies
npm install sharp @napi-rs/canvas playwright

# Python dependencies
pip install Pillow requests
```

## Rolverdeling

- **Opus (kwaliteitsborger):** reviewt design, controleert output, valideert SEO impact
- **Sonnet (uitvoerder):** schrijft scripts, genereert afbeeldingen, update front matter

## Impact

| Metric | Nu | Na implementatie |
|--------|-----|-----------------|
| Google Image Search clicks | 0 | 50-200/maand (verwacht) |
| OG image dekking | 0% | 100% |
| Social media CTR | laag | 2-3x hoger (verwacht) |
| Unieke afbeeldingen | 8 SVG | 100+ WebP |
| E-E-A-T signaal | zwak (generiek) | sterk (branded + echt) |
