---
title: "Cost of Living Calculator Netherlands 2026 — Monthly Budget Estimator for Expats"
description: "Calculate your monthly cost of living in the Netherlands for 2026. Free calculator with rent, groceries, transport, insurance, and lifestyle costs by city."
type: "tools"
layout: "single"
---

<style>
/* ============================================================
HERO
============================================================ */
.tool-hero {
background:
url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Ccircle cx='40' cy='40' r='1.5' fill='%23ffffff' opacity='0.07'/%3E%3Ccircle cx='0' cy='0' r='1' fill='%23ffffff' opacity='0.05'/%3E%3Ccircle cx='80' cy='0' r='1' fill='%23ffffff' opacity='0.05'/%3E%3Ccircle cx='0' cy='80' r='1' fill='%23ffffff' opacity='0.05'/%3E%3Ccircle cx='80' cy='80' r='1' fill='%23ffffff' opacity='0.05'/%3E%3Cpath d='M0 40h80M40 0v80' stroke='%23ffffff' stroke-width='0.3' opacity='0.04'/%3E%3C/svg%3E"),
linear-gradient(135deg, var(--expat-primary-dark) 0%, var(--expat-primary) 50%, #2D9B6A 100%);
color: #fff;
padding: 3rem 1.5rem 2.5rem;
position: relative;
overflow: hidden;
}
.tool-hero::before {
content: '';
position: absolute;
top: -50%; right: -20%;
width: 500px; height: 500px;
border-radius: 50%;
background: radial-gradient(circle, rgba(232,131,42,0.12) 0%, transparent 70%);
pointer-events: none;
}
.tool-hero::after {
content: '';
position: absolute;
bottom: -40%; left: -15%;
width: 400px; height: 400px;
border-radius: 50%;
background: radial-gradient(circle, rgba(45,155,106,0.15) 0%, transparent 70%);
pointer-events: none;
}
.tool-hero-inner { max-width: 1100px; margin: 0 auto; position: relative; z-index: 1; }
.tool-hero-content { display: flex; align-items: center; justify-content: space-between; gap: 2rem; flex-wrap: wrap; }
.tool-hero-text { flex: 1; }
.tool-hero-icon { width: 100px; height: 100px; flex-shrink: 0; color: rgba(255,255,255,0.25); }
.tool-hero-icon svg { width: 100%; height: 100%; }
.tool-hero .breadcrumb { margin-bottom: 1rem; font-size: 0.85rem; }
.tool-hero .breadcrumb, .tool-hero .breadcrumb a { color: rgba(255,255,255,0.7); text-decoration: none; }
.tool-hero .breadcrumb a:hover { color: #fff; }
.tool-hero h1 { font-family: 'DM Sans', sans-serif; font-size: 2.1rem; font-weight: 700; color: #fff; margin-bottom: 0.6rem; max-width: 700px; letter-spacing: -0.02em; line-height: 1.2; }
.tool-hero .hero-subtitle { color: rgba(255,255,255,0.85); font-size: 1.1rem; margin-bottom: 0; max-width: 580px; }
.tool-hero .meta { color: rgba(255,255,255,0.7); font-size: 0.85rem; margin-top: 0.75rem; }
.hero-badge { display: inline-block; background: rgba(232,131,42,0.2); border: 1px solid rgba(232,131,42,0.5); color: #F5A623; font-size: 0.8rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; padding: 0.3rem 0.9rem; border-radius: 20px; margin-bottom: 1rem; }

/* ============================================================
LAYOUT
============================================================ */
.page-body { max-width: 1100px; margin: 0 auto; padding: 2.5rem 1.5rem 4rem; }
.tool-grid { display: grid; grid-template-columns: 1fr 320px; gap: 2rem; align-items: start; }

/* ============================================================
CARD
============================================================ */
.card { background: var(--expat-card); border: 1px solid var(--expat-border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 1.75rem; }

/* ============================================================
FORM ELEMENTS
============================================================ */
.form-section-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--expat-muted); margin-bottom: 1rem; display: block; }
.form-group { margin-bottom: 1.4rem; }
.form-group label { display: block; font-weight: 600; font-size: 0.92rem; margin-bottom: 0.4rem; color: var(--expat-text); }
.form-group label .label-hint { font-weight: 400; color: var(--expat-muted); font-size: 0.82rem; }

select { width: 100%; padding: 0.7rem 2.5rem 0.7rem 0.85rem; border: 2px solid var(--expat-border); border-radius: var(--radius-sm); font-size: 0.92rem; font-weight: 500; color: var(--expat-text); background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%236B7280' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat right 0.85rem center; -webkit-appearance: none; appearance: none; outline: none; cursor: pointer; transition: border-color 0.2s; font-family: inherit; }
select:focus { border-color: var(--expat-primary); }

.radio-group { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.radio-group label { display: flex; align-items: center; gap: 0.4rem; cursor: pointer; padding: 0.5rem 1rem; border: 2px solid var(--expat-border); border-radius: 100px; font-size: 0.9rem; font-weight: 500; transition: all 0.15s; user-select: none; }
.radio-group input[type="radio"] { display: none; }
.radio-group label:has(input[type="radio"]:checked) { background: var(--expat-primary); border-color: var(--expat-primary); color: #fff; }

.checkbox-group { display: flex; flex-direction: column; gap: 0.55rem; }
.checkbox-group label { display: flex; align-items: center; gap: 0.6rem; cursor: pointer; font-size: 0.92rem; font-weight: 500; user-select: none; }
.checkbox-group input[type="checkbox"] { width: 18px; height: 18px; accent-color: var(--expat-primary); cursor: pointer; flex-shrink: 0; }

.form-divider { border: none; border-top: 1px solid var(--expat-border); margin: 1.5rem 0; }

.btn-calculate { width: 100%; padding: 1rem; background: var(--expat-primary); color: #fff; border: none; border-radius: var(--radius-sm); font-size: 1.05rem; font-weight: 700; cursor: pointer; transition: background 0.2s, transform 0.1s; letter-spacing: 0.01em; font-family: 'DM Sans', sans-serif; margin-top: 0.5rem; }
.btn-calculate:hover { background: var(--expat-primary-dark); }
.btn-calculate:active { transform: scale(0.99); }

/* ============================================================
RESULTS
============================================================ */
#result { margin-top: 2rem; display: none; animation: fadeInUp 0.4s ease; }
@keyframes fadeInUp {
from { opacity: 0; transform: translateY(16px); }
to   { opacity: 1; transform: translateY(0); }
}

/* Total cost card */
.total-cost-card { background: linear-gradient(135deg, var(--expat-primary-dark) 0%, var(--expat-primary) 100%); color: #fff; border-radius: var(--radius); padding: 1.75rem; margin-bottom: 1.25rem; text-align: center; position: relative; overflow: hidden; }
.total-cost-card::before { content: ''; position: absolute; top: -40%; right: -15%; width: 220px; height: 220px; border-radius: 50%; background: rgba(255,255,255,0.06); pointer-events: none; }
.total-cost-label { font-size: 0.82rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: rgba(255,255,255,0.75); margin-bottom: 0.4rem; }
.total-cost-value { font-family: 'DM Sans', sans-serif; font-size: 3rem; font-weight: 700; color: #fff; line-height: 1; letter-spacing: -0.02em; }
.total-cost-city { font-size: 0.9rem; color: rgba(255,255,255,0.75); margin-top: 0.4rem; }
.total-cost-disclaimer { font-size: 0.78rem; color: rgba(255,255,255,0.55); margin-top: 0.75rem; }

/* Breakdown table */
.breakdown-card { margin-bottom: 1.25rem; }
.breakdown-card h3 { font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--expat-muted); margin-bottom: 1rem; }
.breakdown-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.breakdown-table tr { border-bottom: 1px solid var(--expat-border); }
.breakdown-table tr:last-child { border-bottom: 2px solid var(--expat-primary); }
.breakdown-table td { padding: 0.55rem 0; }
.breakdown-table td:last-child { text-align: right; font-weight: 700; color: var(--expat-primary); }
.breakdown-table .label-cell { color: var(--expat-text); }
.breakdown-table .total-row td { font-weight: 800; color: var(--expat-text); padding-top: 0.75rem; font-size: 1rem; }
.breakdown-table .total-row td:last-child { color: var(--expat-primary); }
.breakdown-bar { height: 4px; background: #E5E7EB; border-radius: 100px; margin-top: 0.3rem; overflow: hidden; }
.breakdown-bar-fill { height: 100%; border-radius: 100px; background: var(--expat-primary); transition: width 0.6s cubic-bezier(0.4,0,0.2,1); }

/* Amsterdam comparison */
.comparison-card { margin-bottom: 1.25rem; }
.comparison-card h3 { font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--expat-muted); margin-bottom: 1rem; }
.comparison-bars { display: flex; flex-direction: column; gap: 0.85rem; }
.comp-row-label { display: flex; justify-content: space-between; align-items: center; font-size: 0.88rem; margin-bottom: 0.3rem; }
.comp-row-name { font-weight: 600; }
.comp-row-amount { font-weight: 700; color: var(--expat-primary); }
.comp-bar-track { height: 10px; background: #E5E7EB; border-radius: 100px; overflow: hidden; }
.comp-bar-fill { height: 100%; border-radius: 100px; transition: width 0.7s cubic-bezier(0.4,0,0.2,1); }
.comp-bar-fill.selected { background: var(--expat-primary); }
.comp-bar-fill.amsterdam { background: var(--expat-accent); }
.savings-badge { display: inline-block; margin-top: 0.5rem; padding: 0.3rem 0.85rem; border-radius: 100px; font-size: 0.82rem; font-weight: 700; }
.savings-badge.cheaper { background: var(--expat-success-light); color: #065F46; }
.savings-badge.pricier { background: var(--expat-danger-light); color: #991B1B; }
.savings-badge.same { background: #F3F4F6; color: var(--expat-muted); }

/* Tip box */
.tip-box { background: #FFF7ED; border: 1px solid #FED7AA; border-radius: var(--radius-sm); padding: 1rem 1.1rem; font-size: 0.87rem; margin-bottom: 1.25rem; line-height: 1.55; }
.tip-box strong { color: #92400E; display: block; margin-bottom: 0.3rem; }
.tip-box a { color: var(--expat-primary); font-weight: 600; }

/* CTAs */
.result-ctas { margin-top: 0; }
.result-ctas h3 { font-size: 1rem; font-weight: 700; font-family: 'DM Sans', sans-serif; margin-bottom: 0.85rem; color: var(--expat-text); }
.cta-affiliate { display: flex; align-items: center; justify-content: space-between; padding: 0.85rem 1.1rem; background: var(--expat-primary); color: #fff; text-decoration: none; border-radius: var(--radius-sm); font-size: 0.9rem; font-weight: 600; margin-bottom: 0.6rem; transition: background 0.2s; }
.cta-affiliate:hover { background: var(--expat-primary-dark); color: #fff; text-decoration: none; }
.cta-affiliate.secondary { background: transparent; color: var(--expat-primary); border: 2px solid var(--expat-primary); }
.cta-affiliate.secondary:hover { background: var(--expat-primary); color: #fff; }
.cta-affiliate.accent { background: var(--expat-accent); }
.cta-affiliate.accent:hover { background: #C96B1A; }
.cta-arrow { font-size: 1.1rem; }

/* ============================================================
SIDEBAR
============================================================ */
.sidebar-card { margin-bottom: 1.25rem; }
.sidebar-card h2 { font-size: 1rem; font-weight: 700; font-family: 'DM Sans', sans-serif; margin-bottom: 1rem; color: var(--expat-text); }
.cost-list { list-style: none; padding: 0; }
.cost-list li { display: flex; justify-content: space-between; align-items: baseline; padding: 0.45rem 0; border-bottom: 1px solid var(--expat-border); font-size: 0.87rem; gap: 0.5rem; }
.cost-list li:last-child { border-bottom: none; }
.cost-list .cl-label { color: var(--expat-muted); }
.cost-list .cl-val { font-weight: 700; color: var(--expat-primary); white-space: nowrap; }
.sidebar-note { margin-top: 1rem; font-size: 0.75rem; color: var(--expat-muted); line-height: 1.4; }
.sidebar-note a { color: var(--expat-primary); }

/* ============================================================
SEO CONTENT
============================================================ */
.seo-content { margin-top: 3rem; }
.seo-content h2 { font-size: 1.45rem; font-weight: 800; font-family: 'DM Sans', sans-serif; color: var(--expat-text); margin-top: 2.5rem; margin-bottom: 0.85rem; letter-spacing: -0.015em; }
.seo-content h3 { font-size: 1.1rem; font-weight: 700; font-family: 'DM Sans', sans-serif; margin-top: 1.5rem; margin-bottom: 0.6rem; }
.seo-content p { color: #374151; margin-bottom: 1rem; line-height: 1.75; }
.seo-content ul, .seo-content ol { padding-left: 1.4rem; margin-bottom: 1rem; color: #374151; line-height: 1.75; }
.seo-content li { margin-bottom: 0.35rem; }
.seo-content a { color: var(--expat-primary); }

.table-scroll-wrapper { overflow-x: auto; -webkit-overflow-scrolling: touch; max-width: 100%; margin: 1.25rem 0 1.5rem; }
.data-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; border-radius: var(--radius-sm); overflow: hidden; border: 1px solid var(--expat-border); }
.data-table th { background: var(--expat-primary); color: #fff; padding: 0.7rem 1rem; text-align: left; font-size: 0.82rem; font-weight: 600; letter-spacing: 0.03em; }
.data-table td { padding: 0.65rem 1rem; border-bottom: 1px solid var(--expat-border); }
.data-table tr:last-child td { border-bottom: none; }
.data-table tr:nth-child(even) td { background: #F9FAFB; }
.data-table .bold { font-weight: 700; }

/* ============================================================
RESPONSIVE
============================================================ */
/* Clip any accidental horizontal overflow at section level */
.page-body { overflow-x: hidden; }

@media (max-width: 860px) {
.tool-grid { grid-template-columns: 1fr; }
.tool-grid { gap: 1.5rem; }
}
@media (max-width: 768px) {
.tool-hero::before, .tool-hero::after { display: none; }
.data-table th, .data-table td { padding: 0.45rem 0.5rem; font-size: 0.78rem; }
.tool-hero-icon { display: none; }
.tool-hero { padding: 2rem 1.25rem 1.5rem; }
.tool-hero h1 { font-size: 1.55rem; margin-bottom: 0.4rem; }
.tool-hero .hero-subtitle { font-size: 0.95rem; }
.tool-hero .breadcrumb { margin-bottom: 0.6rem; font-size: 0.78rem; }
.tool-hero .meta { margin-top: 0.5rem; font-size: 0.78rem; }
.hero-badge { font-size: 0.7rem; padding: 0.2rem 0.7rem; margin-bottom: 0.6rem; }
.page-body { padding: 1.25rem 1rem 2.5rem; }
.card { padding: 1.25rem; }
.form-group { margin-bottom: 1rem; }
.form-group label { font-size: 0.88rem; margin-bottom: 0.3rem; }
.form-section-label { font-size: 0.72rem; margin-bottom: 0.75rem; }
.radio-group { gap: 0.35rem; }
.radio-group label { padding: 0.45rem 0.85rem; font-size: 0.85rem; }
.checkbox-group { gap: 0.4rem; }
.checkbox-group label { font-size: 0.88rem; gap: 0.5rem; }
.checkbox-group input[type="checkbox"] { width: 16px; height: 16px; }
.form-divider { margin: 1rem 0; }
select { font-size: 16px; padding: 0.6rem 2.5rem 0.6rem 0.75rem; }
.btn-calculate { font-size: 0.95rem; padding: 0.8rem; }
.total-cost-card { padding: 1.25rem; }
.total-cost-value { font-size: 2.4rem; }
.total-cost-label { font-size: 0.78rem; }
.total-cost-city { font-size: 0.82rem; }
.total-cost-disclaimer { font-size: 0.72rem; }
.breakdown-table { font-size: 0.85rem; }
.breakdown-table td { padding: 0.4rem 0; word-break: break-word; }
.comp-row-label { font-size: 0.82rem; }
.cta-affiliate { font-size: 0.85rem; padding: 0.7rem 0.9rem; flex-wrap: wrap; gap: 0.3rem; }
.tip-box { font-size: 0.82rem; padding: 0.85rem; }
.cost-list li { font-size: 0.82rem; padding: 0.35rem 0; }
.sidebar-card h2 { font-size: 0.92rem; margin-bottom: 0.75rem; }
.sidebar-card { margin-bottom: 1rem; }
.seo-content { margin-top: 2rem; overflow-wrap: break-word; word-wrap: break-word; }
.seo-content h2 { font-size: 1.2rem; margin-top: 1.75rem; margin-bottom: 0.6rem; }
.seo-content h3 { font-size: 1rem; margin-top: 1.25rem; }
.seo-content p { font-size: 0.92rem; }
}
@media (max-width: 480px) {
.tool-hero { padding: 1.5rem 1rem 1.25rem; }
.tool-hero h1 { font-size: 1.35rem; }
.tool-hero .hero-subtitle { font-size: 0.88rem; }
.page-body { padding: 1rem 0.85rem 2rem; }
.card { padding: 1rem; }
.radio-group { flex-direction: column; gap: 0.3rem; }
.radio-group label { padding: 0.5rem 0.9rem; font-size: 0.85rem; border-radius: 8px; }
.form-group { margin-bottom: 0.85rem; }
.total-cost-value { font-size: 2rem; }
}
@media (max-width: 380px) {
.tool-hero { padding: 1.25rem 0.75rem 1rem; }
.tool-hero h1 { font-size: 1.2rem; }
.card { padding: 0.85rem; }
.total-cost-value { font-size: 1.8rem; }
.page-body { padding: 0.85rem 0.7rem 2rem; }
}

/* Print */
</style>

<!-- HERO -->
<div class="tool-hero">
<div class="tool-hero-inner">
<nav class="breadcrumb" aria-label="Breadcrumb">
<a href="/">Home</a> &rsaquo;
<a href="/tools/">Free Expat Tools</a> &rsaquo;
<span>Cost of Living Calculator</span>
</nav>
<div class="tool-hero-content">
<div class="tool-hero-text">
<span class="hero-badge">Free Tool &bull; Updated March 2026</span>
<h1>Cost of Living Calculator Netherlands 2026</h1>
<p class="hero-subtitle">Estimate your monthly expenses in the Netherlands &mdash; from rent and groceries to health insurance and transport &mdash; by city and lifestyle.</p>
<div class="meta">Free &middot; No signup required &middot; By Sarah van den Berg</div>
</div>
<div class="tool-hero-icon" aria-hidden="true">
<svg viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="8" y="16" width="52" height="48" rx="4" stroke="currentColor" stroke-width="2.5"/>
<path d="M8 28h52" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
<path d="M20 40h8M20 52h8" stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity="0.7"/>
<path d="M36 40h16M36 52h10" stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
<circle cx="62" cy="20" r="12" fill="currentColor" opacity="0.15" stroke="currentColor" stroke-width="2.5"/>
<path d="M58 20h6M57 16.5c0-2 1.2-3 2.8-3s2.7.9 2.7 2.8" stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity="0.8"/>
<path d="M57 23.5h7" stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity="0.8"/>
</svg>
</div>
</div>
</div>
</div>

<!-- MAIN -->
<div class="page-body">
<div class="tool-grid">

<!-- FORM COLUMN -->
<div>
<div class="card" role="form" aria-label="Cost of living calculator form">

<span class="form-section-label">Your situation</span>

<!-- City -->
<div class="form-group">
<label for="citySelect">City</label>
<select id="citySelect" aria-label="Select your city">
<option value="amsterdam">Amsterdam</option>
<option value="rotterdam">Rotterdam</option>
<option value="the-hague">The Hague</option>
<option value="utrecht">Utrecht</option>
<option value="eindhoven">Eindhoven</option>
<option value="leiden">Leiden</option>
<option value="groningen">Groningen</option>
<option value="maastricht">Maastricht</option>
<option value="other">Other / Netherlands average</option>
</select>
</div>

<!-- Housing situation -->
<div class="form-group">
<label>Housing situation</label>
<div class="radio-group" role="radiogroup" aria-label="Housing situation">
<label>
<input type="radio" name="housing" value="rent1bed" checked>
Renting alone (1-bed)
</label>
<label>
<input type="radio" name="housing" value="rent2bed">
Renting with partner (2-bed)
</label>
<label>
<input type="radio" name="housing" value="shared">
Sharing a flat
</label>
<label>
<input type="radio" name="housing" value="mortgage">
Own home (mortgage)
</label>
</div>
</div>

<!-- Lifestyle -->
<div class="form-group">
<label>Lifestyle <span class="label-hint">(affects groceries, dining, and utilities estimates)</span></label>
<div class="radio-group" role="radiogroup" aria-label="Lifestyle">
<label>
<input type="radio" name="lifestyle" value="budget">
Budget-conscious
</label>
<label>
<input type="radio" name="lifestyle" value="avg" checked>
Average
</label>
<label>
<input type="radio" name="lifestyle" value="comfortable">
Comfortable
</label>
</div>
</div>

<hr class="form-divider">

<!-- Include checkboxes -->
<div class="form-group">
<label>Include in estimate</label>
<div class="checkbox-group" role="group" aria-label="Categories to include">
<label>
<input type="checkbox" id="chk-health" checked>
Health insurance
</label>
<label>
<input type="checkbox" id="chk-ov" checked>
Public transport (OV)
</label>
<label>
<input type="checkbox" id="chk-groceries" checked>
Groceries
</label>
<label>
<input type="checkbox" id="chk-dining" checked>
Dining out
</label>
<label>
<input type="checkbox" id="chk-gym">
Gym membership
</label>
<label>
<input type="checkbox" id="chk-phone" checked>
Phone &amp; internet
</label>
<label>
<input type="checkbox" id="chk-utilities" checked>
Utilities (gas/electric/water)
</label>
</div>
</div>

<button class="btn-calculate" onclick="calculate()" type="button">
Calculate My Monthly Budget &rarr;
</button>
</div>

<!-- RESULTS -->
<div id="result" aria-live="polite" aria-label="Calculation results">

<!-- Total cost -->
<div class="total-cost-card" id="totalCostCard">
<div class="total-cost-label">Estimated monthly cost</div>
<div class="total-cost-value" id="totalCostValue">&mdash;</div>
<div class="total-cost-city" id="totalCostCity"></div>
<div class="total-cost-disclaimer">Estimate only &mdash; actual costs vary. See breakdown below.</div>
</div>

<!-- Breakdown table -->
<div class="card breakdown-card" id="breakdownCard">
<h3>Monthly Cost Breakdown</h3>
<table class="breakdown-table" id="breakdownTable">
<tbody></tbody>
</table>
</div>

<!-- Amsterdam comparison (hidden if Amsterdam selected) -->
<div class="card comparison-card" id="comparisonCard" style="display:none;">
<h3>Comparison to Amsterdam</h3>
<div class="comparison-bars" id="comparisonBars"></div>
</div>

<!-- Tip box -->
<div class="tip-box" id="tipBox">
<strong>Check if this fits your salary</strong>
Use our <a href="/tools/housing-budget-checker/">Rent Affordability Calculator</a> to see how this monthly budget stacks up against your net income.
</div>

<!-- Affiliate CTAs -->
<div class="result-ctas card" id="ctaSection">
<h3>Useful next steps</h3>
<a href="/tools/health-insurance-wizard/" class="cta-affiliate secondary">
Compare health insurance options <span class="cta-arrow">&rarr;</span>
</a>
<a href="/tools/bank-account-chooser/" class="cta-affiliate secondary">
Find the right bank account <span class="cta-arrow">&rarr;</span>
</a>
<a href="/tools/housing-budget-checker/" class="cta-affiliate secondary">
Check housing affordability <span class="cta-arrow">&rarr;</span>
</a>
<a href="https://wise.com/invite/ihpc/willemt52" class="cta-affiliate accent" rel="sponsored" target="_blank">
Save on international transfers &mdash; Wise <span class="cta-arrow">&rarr;</span>
</a>
</div>
</div>

<!-- SEO CONTENT -->
<div class="seo-content">
<h2>What Does It Cost to Live in the Netherlands as an Expat?</h2>
<p>The Netherlands is one of Western Europe&rsquo;s most desirable destinations for expats, but it&rsquo;s not cheap. When I first moved to Amsterdam, I had a rough idea of what rent would cost &mdash; but I seriously underestimated everything else. Groceries, health insurance (mandatory!), OV-chipkaart for the trains, utilities. It all adds up faster than you expect.</p>
<p>The good news: the Netherlands is predictable. Costs are relatively transparent, prices are stable, and once you know the numbers, budgeting is straightforward. This calculator gives you a city-specific monthly estimate based on 2026 market data. It covers the core categories that matter most for expats.</p>

<h2>Average Monthly Cost of Living by Dutch City (2026)</h2>
<p>The biggest variable is always housing &mdash; and housing varies enormously by city. Everything else (groceries, transport, insurance) is much more consistent across the country. Here&rsquo;s how the major cities compare for a single person renting a one-bedroom apartment:</p>

<div class="table-scroll-wrapper">
<table class="data-table">
<thead>
<tr>
<th>City</th>
<th>Rent (1-bed)</th>
<th>Health ins.</th>
<th>OV monthly</th>
<th>Avg. groceries</th>
<th>Est. total</th>
</tr>
</thead>
<tbody>
<tr><td class="bold">Amsterdam</td><td>&euro;1,650</td><td>&euro;130</td><td>&euro;110</td><td>&euro;350</td><td class="bold">&euro;2,545+</td></tr>
<tr><td class="bold">Utrecht</td><td>&euro;1,350</td><td>&euro;130</td><td>&euro;100</td><td>&euro;330</td><td class="bold">&euro;2,210+</td></tr>
<tr><td class="bold">The Hague</td><td>&euro;1,250</td><td>&euro;130</td><td>&euro;100</td><td>&euro;320</td><td class="bold">&euro;2,100+</td></tr>
<tr><td class="bold">Rotterdam</td><td>&euro;1,250</td><td>&euro;130</td><td>&euro;100</td><td>&euro;320</td><td class="bold">&euro;2,100+</td></tr>
<tr><td class="bold">Leiden</td><td>&euro;1,225</td><td>&euro;130</td><td>&euro;95</td><td>&euro;320</td><td class="bold">&euro;2,070+</td></tr>
<tr><td class="bold">Eindhoven</td><td>&euro;1,150</td><td>&euro;130</td><td>&euro;95</td><td>&euro;300</td><td class="bold">&euro;1,975+</td></tr>
<tr><td class="bold">Groningen</td><td>&euro;1,050</td><td>&euro;130</td><td>&euro;90</td><td>&euro;290</td><td class="bold">&euro;1,860+</td></tr>
<tr><td class="bold">Maastricht</td><td>&euro;1,025</td><td>&euro;130</td><td>&euro;90</td><td>&euro;290</td><td class="bold">&euro;1,835+</td></tr>
</tbody>
</table>
</div>

<h3>Health Insurance &mdash; A Hidden Cost Many Expats Miss</h3>
<p>Health insurance (zorgverzekering) is mandatory for everyone living or working in the Netherlands, including expats. In 2026, the basic premium (basispremie) averages around &euro;130&ndash;140 per month depending on the insurer and excess (eigen risico) you choose. This is a fixed cost that you cannot avoid &mdash; budget for it from day one.</p>
<p>The government does offer a healthcare allowance (zorgtoeslag) if your income is below certain thresholds, which can partially offset this cost.</p>

<h3>Public Transport (OV) Costs</h3>
<p>The Netherlands has an excellent public transport network. Most expats use the OV-chipkaart for trains, trams, buses and metros. For regular commuters, monthly subscriptions range from &euro;90&ndash;110 depending on the city and how far you travel. If you work in a different city from where you live, your employer may reimburse travel costs &mdash; this is common in the Netherlands and worth negotiating into your package.</p>

<h3>Groceries: What to Expect</h3>
<p>Dutch supermarkets are good value by Western European standards. Albert Heijn is the most common (mid-range), Jumbo is slightly cheaper, and Aldi/Lidl are the budget options. A single person cooking at home can manage comfortably on &euro;250&ndash;350 per month. If you regularly shop at specialty stores or organic markets, budget &euro;400&ndash;450.</p>

<h3>Utilities in the Netherlands</h3>
<p>Dutch energy bills were volatile in recent years but have stabilised significantly in 2025&ndash;2026. Expect &euro;160&ndash;220 per month for gas, electricity, and water combined in a typical one-bedroom apartment. Note that some rentals (especially newer builds) include utilities in the rent &mdash; always check your contract.</p>

<h2>Tips for Keeping Costs Down as an Expat</h2>
<ul>
<li><strong>Choose the right city:</strong> Groningen and Maastricht can save you &euro;600&ndash;700/month compared to Amsterdam on rent alone. Both have strong expat communities.</li>
<li><strong>Compare health insurers:</strong> Premiums can differ by &euro;20&ndash;30/month for equivalent cover. Use our <a href="/tools/health-insurance-wizard/">Health Insurance Comparison</a> tool.</li>
<li><strong>Get a Wise account for international transfers:</strong> If you&rsquo;re sending money home or receiving foreign income, Wise is typically much cheaper than your Dutch bank. <a href="https://wise.com/invite/ihpc/willemt52" rel="sponsored">Open a Wise account here.</a></li>
<li><strong>Use your employer&rsquo;s travel reimbursement:</strong> Many Dutch employers offer &euro;0.23/km or a monthly OV pass. Don&rsquo;t leave this on the table.</li>
<li><strong>Cook at home during the week:</strong> Dutch restaurants are not cheap. Limiting dining out to weekends can save &euro;100&ndash;200/month.</li>
<li><strong>Shared housing is common:</strong> Especially in Amsterdam and Utrecht, sharing a flat is financially sensible and socially normal even for working professionals in their 30s.</li>
</ul>
</div>
</div>

<!-- SIDEBAR -->
<aside>
<div class="card sidebar-card">
<h2>Quick Reference Costs</h2>
<ul class="cost-list">
<li><span class="cl-label">Health insurance (basic)</span><span class="cl-val">&euro;130/mo</span></li>
<li><span class="cl-label">NS train subscription</span><span class="cl-val">&euro;90&ndash;120/mo</span></li>
<li><span class="cl-label">Internet (home)</span><span class="cl-val">&euro;40&ndash;55/mo</span></li>
<li><span class="cl-label">Mobile plan</span><span class="cl-val">&euro;15&ndash;30/mo</span></li>
<li><span class="cl-label">Utilities (gas/elec/water)</span><span class="cl-val">&euro;150&ndash;220/mo</span></li>
<li><span class="cl-label">Gym (basic)</span><span class="cl-val">&euro;25&ndash;45/mo</span></li>
<li><span class="cl-label">Groceries (1 person)</span><span class="cl-val">&euro;250&ndash;400/mo</span></li>
<li><span class="cl-label">Dining out (avg.)</span><span class="cl-val">&euro;12&ndash;25/meal</span></li>
<li><span class="cl-label">Coffee (caf&eacute;)</span><span class="cl-val">&euro;3.50&ndash;5</span></li>
<li><span class="cl-label">Cinema ticket</span><span class="cl-val">&euro;12&ndash;16</span></li>
</ul>
<p class="sidebar-note">Figures are 2026 estimates. <a href="/guides/finance/">Read more in the Finance Guide &rarr;</a></p>
</div>

<div class="card sidebar-card">
<h2>Related Tools</h2>
<ul class="cost-list">
<li><a href="/tools/housing-budget-checker/" style="color:var(--expat-primary);font-size:0.88rem;">Rent Affordability Calculator</a></li>
<li><a href="/tools/salary-checker/" style="color:var(--expat-primary);font-size:0.88rem;">Net Salary Calculator</a></li>
<li><a href="/tools/30-percent-ruling-calculator/" style="color:var(--expat-primary);font-size:0.88rem;">30% Ruling Calculator</a></li>
<li><a href="/tools/health-insurance-wizard/" style="color:var(--expat-primary);font-size:0.88rem;">Health Insurance Comparison</a></li>
<li><a href="/tools/bank-account-chooser/" style="color:var(--expat-primary);font-size:0.88rem;">Bank Account Comparison</a></li>
</ul>
</div>

<div class="card sidebar-card">
<h2>Save on Transfers</h2>
<p style="font-size:0.85rem;color:var(--expat-muted);margin-bottom:0.75rem;line-height:1.55;">Sending money home or receiving foreign income? Wise is significantly cheaper than Dutch banks for international transfers.</p>
<a href="https://wise.com/invite/ihpc/willemt52" rel="sponsored" target="_blank" class="cta-affiliate accent" style="margin-bottom:0;font-size:0.85rem;">
Open a Wise account <span class="cta-arrow">&rarr;</span>
</a>
</div>
</aside>
</div>
</div>

<script>
'use strict';

// ============================================================
// COST DATA — all figures in EUR/month, 2026 estimates
// ============================================================
var COST_DATA = {
amsterdam:   {
rent1bed: 1650, rent2bed: 2200, shared: 850, mortgage: 1400,
health: 130,
ov: 110,
groceriesBudget: 250, groceriesAvg: 350, groceriesComfortable: 450,
diningBudget: 50,  diningAvg: 150,  diningComfortable: 300,
gym: 40,
phone: 55,
utilitiesBudget: 150, utilitiesAvg: 200, utilitiesComfortable: 250
},
rotterdam:   {
rent1bed: 1250, rent2bed: 1700, shared: 650, mortgage: 1000,
health: 130,
ov: 100,
groceriesBudget: 230, groceriesAvg: 320, groceriesComfortable: 420,
diningBudget: 45,  diningAvg: 130,  diningComfortable: 250,
gym: 35,
phone: 55,
utilitiesBudget: 140, utilitiesAvg: 180, utilitiesComfortable: 220
},
'the-hague': {
rent1bed: 1250, rent2bed: 1700, shared: 650, mortgage: 1050,
health: 130,
ov: 100,
groceriesBudget: 230, groceriesAvg: 320, groceriesComfortable: 420,
diningBudget: 45,  diningAvg: 130,  diningComfortable: 250,
gym: 35,
phone: 55,
utilitiesBudget: 140, utilitiesAvg: 180, utilitiesComfortable: 220
},
utrecht:     {
rent1bed: 1350, rent2bed: 1800, shared: 700, mortgage: 1100,
health: 130,
ov: 100,
groceriesBudget: 240, groceriesAvg: 330, groceriesComfortable: 430,
diningBudget: 45,  diningAvg: 140,  diningComfortable: 270,
gym: 38,
phone: 55,
utilitiesBudget: 145, utilitiesAvg: 190, utilitiesComfortable: 230
},
eindhoven:   {
rent1bed: 1150, rent2bed: 1500, shared: 600, mortgage: 900,
health: 130,
ov: 95,
groceriesBudget: 220, groceriesAvg: 300, groceriesComfortable: 400,
diningBudget: 40,  diningAvg: 120,  diningComfortable: 220,
gym: 32,
phone: 55,
utilitiesBudget: 135, utilitiesAvg: 170, utilitiesComfortable: 210
},
leiden:      {
rent1bed: 1225, rent2bed: 1600, shared: 625, mortgage: 1000,
health: 130,
ov: 95,
groceriesBudget: 230, groceriesAvg: 320, groceriesComfortable: 420,
diningBudget: 45,  diningAvg: 130,  diningComfortable: 250,
gym: 35,
phone: 55,
utilitiesBudget: 140, utilitiesAvg: 180, utilitiesComfortable: 220
},
groningen:   {
rent1bed: 1050, rent2bed: 1400, shared: 550, mortgage: 800,
health: 130,
ov: 90,
groceriesBudget: 210, groceriesAvg: 290, groceriesComfortable: 380,
diningBudget: 35,  diningAvg: 100,  diningComfortable: 180,
gym: 30,
phone: 55,
utilitiesBudget: 130, utilitiesAvg: 160, utilitiesComfortable: 195
},
maastricht:  {
rent1bed: 1025, rent2bed: 1350, shared: 525, mortgage: 750,
health: 130,
ov: 90,
groceriesBudget: 210, groceriesAvg: 290, groceriesComfortable: 380,
diningBudget: 35,  diningAvg: 100,  diningComfortable: 180,
gym: 30,
phone: 55,
utilitiesBudget: 130, utilitiesAvg: 160, utilitiesComfortable: 195
}
};

// "Other" = average of all cities
(function buildOther() {
var cities = Object.keys(COST_DATA);
var keys = Object.keys(COST_DATA.amsterdam);
var avg = {};
keys.forEach(function(k) {
var sum = 0;
cities.forEach(function(c) { sum += COST_DATA[c][k]; });
avg[k] = Math.round(sum / cities.length);
});
COST_DATA['other'] = avg;
})();

var CITY_NAMES = {
amsterdam: 'Amsterdam', rotterdam: 'Rotterdam', 'the-hague': 'The Hague',
utrecht: 'Utrecht', eindhoven: 'Eindhoven', leiden: 'Leiden',
groningen: 'Groningen', maastricht: 'Maastricht', other: 'Netherlands (avg.)'
};

// ============================================================
// HELPERS
// ============================================================
function fmt(n) {
return '\u20ac' + Math.round(n).toLocaleString('nl-NL');
}

function checked(id) {
return document.getElementById(id).checked;
}

function radioVal(name) {
var el = document.querySelector('input[name="' + name + '"]:checked');
return el ? el.value : null;
}

// ============================================================
// CALCULATE
// ============================================================
function calculate() {
var city     = document.getElementById('citySelect').value;
var housing  = radioVal('housing');
var lifestyle = radioVal('lifestyle');
var d        = COST_DATA[city];
var cityName = CITY_NAMES[city];

// Build breakdown rows
var rows = [];
var total = 0;

// Housing (always included)
var rentKey = { rent1bed: 'rent1bed', rent2bed: 'rent2bed', shared: 'shared', mortgage: 'mortgage' }[housing];
var housingLabel = {
rent1bed: 'Rent (1-bed apartment)',
rent2bed: 'Rent (2-bed apartment)',
shared:   'Rent (shared flat, your share)',
mortgage: 'Mortgage (avg. monthly payment)'
}[housing];
var housingCost = d[rentKey];
rows.push({ label: housingLabel, amount: housingCost, always: true });
total += housingCost;

// Health insurance
if (checked('chk-health')) {
rows.push({ label: 'Health insurance (zorgverzekering)', amount: d.health });
total += d.health;
}

// OV
if (checked('chk-ov')) {
rows.push({ label: 'Public transport (OV monthly pass)', amount: d.ov });
total += d.ov;
}

// Groceries
if (checked('chk-groceries')) {
var grocKey = { budget: 'groceriesBudget', avg: 'groceriesAvg', comfortable: 'groceriesComfortable' }[lifestyle];
rows.push({ label: 'Groceries', amount: d[grocKey] });
total += d[grocKey];
}

// Dining out
if (checked('chk-dining')) {
var diningKey = { budget: 'diningBudget', avg: 'diningAvg', comfortable: 'diningComfortable' }[lifestyle];
rows.push({ label: 'Dining out / caf\u00e9s', amount: d[diningKey] });
total += d[diningKey];
}

// Gym
if (checked('chk-gym')) {
rows.push({ label: 'Gym membership', amount: d.gym });
total += d.gym;
}

// Phone/internet
if (checked('chk-phone')) {
rows.push({ label: 'Phone & internet (bundle)', amount: d.phone });
total += d.phone;
}

// Utilities
if (checked('chk-utilities')) {
var utilKey = { budget: 'utilitiesBudget', avg: 'utilitiesAvg', comfortable: 'utilitiesComfortable' }[lifestyle];
rows.push({ label: 'Utilities (gas/electric/water)', amount: d[utilKey] });
total += d[utilKey];
}

// ---- Render total ----
document.getElementById('totalCostValue').textContent = fmt(total);
document.getElementById('totalCostCity').textContent =
cityName + ' \u00b7 ' +
{ rent1bed: 'Single, 1-bed', rent2bed: 'With partner, 2-bed', shared: 'Shared flat', mortgage: 'Own home' }[housing] +
' \u00b7 ' +
{ budget: 'Budget lifestyle', avg: 'Average lifestyle', comfortable: 'Comfortable lifestyle' }[lifestyle];

// ---- Render breakdown table ----
var tbody = document.querySelector('#breakdownTable tbody');
tbody.innerHTML = '';
var maxAmt = Math.max.apply(null, rows.map(function(r){ return r.amount; }));
rows.forEach(function(row) {
var pct = Math.round((row.amount / total) * 100);
var barPct = Math.round((row.amount / maxAmt) * 100);
var tr = document.createElement('tr');
tr.innerHTML =
'<td class="label-cell">' +
row.label +
'<div class="breakdown-bar"><div class="breakdown-bar-fill" style="width:' + barPct + '%"></div></div>' +
'</td>' +
'<td>' + fmt(row.amount) + '<br><span style="font-size:0.75rem;font-weight:400;color:var(--expat-muted);">' + pct + '%</span></td>';
tbody.appendChild(tr);
});
// Total row
var totalTr = document.createElement('tr');
totalTr.className = 'total-row';
totalTr.innerHTML = '<td>Total monthly estimate</td><td>' + fmt(total) + '</td>';
tbody.appendChild(totalTr);

// ---- Render Amsterdam comparison ----
var compCard = document.getElementById('comparisonCard');
if (city !== 'amsterdam') {
compCard.style.display = '';
var amsData = COST_DATA['amsterdam'];
var amsTotal = 0;
// Replicate same selections for Amsterdam
amsTotal += amsData[rentKey];
if (checked('chk-health'))     amsTotal += amsData.health;
if (checked('chk-ov'))         amsTotal += amsData.ov;
if (checked('chk-groceries'))  { var gk = { budget: 'groceriesBudget', avg: 'groceriesAvg', comfortable: 'groceriesComfortable' }[lifestyle]; amsTotal += amsData[gk]; }
if (checked('chk-dining'))     { var dk2 = { budget: 'diningBudget', avg: 'diningAvg', comfortable: 'diningComfortable' }[lifestyle]; amsTotal += amsData[dk2]; }
if (checked('chk-gym'))        amsTotal += amsData.gym;
if (checked('chk-phone'))      amsTotal += amsData.phone;
if (checked('chk-utilities'))  { var uk = { budget: 'utilitiesBudget', avg: 'utilitiesAvg', comfortable: 'utilitiesComfortable' }[lifestyle]; amsTotal += amsData[uk]; }

var maxComp = Math.max(total, amsTotal);
var selPct  = Math.round((total / maxComp) * 100);
var amsPct  = Math.round((amsTotal / maxComp) * 100);

var diff = total - amsTotal;
var badgeClass = diff < 0 ? 'cheaper' : (diff > 0 ? 'pricier' : 'same');
var badgeText  = diff < 0
? fmt(Math.abs(diff)) + '/mo cheaper than Amsterdam'
: (diff > 0 ? fmt(diff) + '/mo more expensive than Amsterdam' : 'Same cost as Amsterdam');

document.getElementById('comparisonBars').innerHTML =
'<div>' +
'<div class="comp-row-label"><span class="comp-row-name">' + cityName + '</span><span class="comp-row-amount">' + fmt(total) + '/mo</span></div>' +
'<div class="comp-bar-track"><div class="comp-bar-fill selected" style="width:' + selPct + '%"></div></div>' +
'</div>' +
'<div>' +
'<div class="comp-row-label"><span class="comp-row-name">Amsterdam</span><span class="comp-row-amount">' + fmt(amsTotal) + '/mo</span></div>' +
'<div class="comp-bar-track"><div class="comp-bar-fill amsterdam" style="width:' + amsPct + '%"></div></div>' +
'</div>' +
'<span class="savings-badge ' + badgeClass + '">' + badgeText + '</span>';
} else {
compCard.style.display = 'none';
}

// ---- Show results ----
var result = document.getElementById('result');
result.style.display = 'block';
// Re-trigger animation
result.style.animation = 'none';
result.offsetHeight; // reflow
result.style.animation = '';

// Scroll into view
result.scrollIntoView({ behavior: 'smooth', block: 'start' });

// GA4 event
if (typeof gtag === 'function') {
gtag('event', 'calculator_used', {
event_category: 'tool',
event_label: 'cost_of_living_calculator',
city: city,
housing: housing,
lifestyle: lifestyle,
total: Math.round(total)
});
}
}
</script>
