---
title: "Free Expat Checklists & Templates"
description: "Download free printable checklists for moving to the Netherlands. BSN registration, first 30 days, tax return, leaving NL — all in one place."
featured_image: "/images/categories/legal.svg"
type: "page"
layout: "single"
---

<style>
/* ============================================================
   DOWNLOADS PAGE — SCREEN STYLES
   ============================================================ */
.dl-hero {
  background: linear-gradient(135deg, var(--expat-primary-dark) 0%, var(--expat-primary) 50%, #2D9B6A 100%);
  color: #fff;
  padding: 3rem 1.5rem 2.5rem;
  position: relative;
  overflow: hidden;
}
.dl-hero::before {
  content: '';
  position: absolute;
  top: -50%; right: -20%;
  width: 500px; height: 500px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(232,131,42,0.12) 0%, transparent 70%);
  pointer-events: none;
}
.dl-hero-inner { max-width: 1100px; margin: 0 auto; position: relative; z-index: 1; }
.dl-hero .breadcrumb, .dl-hero .breadcrumb a { color: rgba(255,255,255,0.7); font-size: 0.875rem; }
.dl-hero .breadcrumb a:hover { color: #fff; }
.dl-hero h1 { font-size: 2.2rem; margin: 0.75rem 0 0.75rem; color: #fff; }
.dl-hero-desc { font-size: 1.1rem; color: rgba(255,255,255,.85); max-width: 680px; margin-bottom: 1.5rem; }
.dl-hero-badge {
  display: inline-block;
  background: rgba(232,131,42,0.2);
  border: 1px solid rgba(232,131,42,0.5);
  color: #F5A623;
  padding: 0.35rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 1rem;
}
.dl-hero-meta { color: rgba(255,255,255,0.7); font-size: 0.85rem; }

.dl-main { max-width: 1100px; margin: 0 auto; padding: 3rem 1.5rem 4rem; }

/* Quick-nav TOC */
.dl-toc {
  background: var(--expat-card);
  border: 1px solid var(--expat-border);
  border-radius: 14px;
  padding: 1.5rem 2rem;
  margin-bottom: 3rem;
}
.dl-toc h2 { font-size: 1rem; text-transform: uppercase; letter-spacing: 0.07em; color: var(--expat-primary); margin: 0 0 0.75rem; font-weight: 700; }
.dl-toc-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.3rem 2rem;
}
.dl-toc a {
  color: var(--expat-primary-dark);
  text-decoration: none;
  font-size: 0.9rem;
  padding: 0.2rem 0;
  border-bottom: 1px solid var(--expat-border);
  display: block;
}
.dl-toc a:hover { color: var(--expat-primary); text-decoration: underline; }

/* Individual checklist card */
.checklist-card {
  border: 1px solid var(--expat-border);
  border-radius: 16px;
  background: var(--expat-card);
  margin-bottom: 2.5rem;
  overflow: hidden;
  page-break-inside: avoid;
}
.checklist-card-header {
  background: var(--expat-primary-dark);
  color: #fff;
  padding: 1.25rem 1.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.checklist-card-header-left { display: flex; align-items: center; gap: 0.85rem; }
.checklist-num {
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.25);
  border-radius: 8px;
  width: 36px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.85rem; font-weight: 700;
  flex-shrink: 0;
}
.checklist-card-header h2 {
  margin: 0;
  font-size: 1.15rem;
  color: #fff;
  font-weight: 700;
}
.btn-print {
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.35);
  color: #fff;
  padding: 0.45rem 1rem;
  border-radius: 8px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: background 0.15s;
  display: flex; align-items: center; gap: 0.4rem;
}
.btn-print:hover { background: rgba(255,255,255,0.25); }
.btn-print svg { width: 15px; height: 15px; flex-shrink: 0; }

.checklist-body { padding: 1.5rem 1.75rem; }

/* Sections within a checklist */
.cl-section { margin-bottom: 1.5rem; }
.cl-section:last-child { margin-bottom: 0; }
.cl-section-title {
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--expat-primary);
  margin-bottom: 0.6rem;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid var(--expat-primary);
  display: inline-block;
}

/* Checkbox items */
.cl-items { list-style: none; margin: 0; padding: 0; }
.cl-items li {
  display: flex;
  align-items: flex-start;
  gap: 0.7rem;
  padding: 0.45rem 0;
  border-bottom: 1px solid var(--expat-border);
  font-size: 0.925rem;
  color: var(--expat-text);
  line-height: 1.45;
}
.cl-items li:last-child { border-bottom: none; }
.cl-check {
  display: inline-block;
  width: 20px; height: 20px;
  border: 2px solid var(--expat-primary);
  border-radius: 4px;
  flex-shrink: 0;
  margin-top: 1px;
  background: #fff;
}
.cl-note {
  font-size: 0.8rem;
  color: var(--expat-muted);
  margin-top: 0.2rem;
}
.cl-warning {
  background: #FEF9C3;
  border-left: 3px solid #CA8A04;
  border-radius: 0 6px 6px 0;
  padding: 0.6rem 0.9rem;
  font-size: 0.875rem;
  color: #713F12;
  margin: 0.75rem 0;
}
.cl-affiliate-box {
  background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
  border: 1px solid #86EFAC;
  border-radius: 10px;
  padding: 0.9rem 1.1rem;
  margin: 1rem 0 0.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.cl-affiliate-box .aff-text { font-size: 0.875rem; color: #166534; }
.cl-affiliate-box .aff-text strong { display: block; margin-bottom: 0.2rem; }
.cl-affiliate-box .aff-cta {
  background: #16A34A;
  color: #fff;
  text-decoration: none;
  padding: 0.4rem 0.9rem;
  border-radius: 7px;
  font-size: 0.82rem;
  font-weight: 700;
  white-space: nowrap;
  flex-shrink: 0;
}
.cl-affiliate-box .aff-cta:hover { background: #15803D; text-decoration: none; }

/* Footer of each card */
.checklist-footer {
  border-top: 1px solid var(--expat-border);
  padding: 0.9rem 1.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  font-size: 0.82rem;
  color: var(--expat-muted);
  background: var(--expat-bg);
}
.checklist-footer a { color: var(--expat-primary); text-decoration: underline; }
.checklist-source { font-weight: 600; }

/* Share section at bottom of page */
.share-box {
  background: var(--expat-card);
  border: 1px solid var(--expat-border);
  border-radius: 16px;
  padding: 2rem;
  margin-top: 2rem;
}
.share-box h2 { font-size: 1.4rem; color: var(--expat-primary-dark); margin-top: 0; }
.share-url {
  background: var(--expat-bg);
  border: 1px solid var(--expat-border);
  border-radius: 8px;
  padding: 0.7rem 1rem;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  color: var(--expat-text);
  margin: 0.75rem 0;
  word-break: break-all;
}

/* ============================================================
   PRINT STYLES
   ============================================================ */
@media print {
  /* Hide everything except checklist cards */
  .dl-hero,
  .dl-toc,
  .share-box,
  header, nav, footer,
  .site-header, .site-footer,
  .sidebar, .related-posts,
  .btn-print,
  .cl-affiliate-box .aff-cta {
    display: none !important;
  }

  body { font-size: 11pt; color: #000; background: #fff; }
  .dl-main { padding: 0; max-width: 100%; }

  .checklist-card {
    border: 1pt solid #ccc;
    border-radius: 0;
    margin-bottom: 1.5rem;
    page-break-inside: avoid;
    break-inside: avoid;
  }
  .checklist-card-header {
    background: #1B4D3E !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    color: #fff !important;
    padding: 0.75rem 1rem;
  }
  .checklist-card-header h2 { font-size: 12pt; }
  .checklist-num { display: none; }
  .checklist-body { padding: 0.75rem 1rem; }
  .cl-check {
    border: 1.5pt solid #1B4D3E;
    border-radius: 2px;
    background: #fff;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .cl-section-title { color: #1B4D3E !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .cl-affiliate-box { border: 1pt solid #ccc; background: #f9f9f9 !important; }
  .checklist-footer {
    background: #f9f9f9 !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    border-top: 1pt solid #ccc;
  }

  /* Page footer with URL */
  @page {
    margin: 1.5cm 1.5cm 2.5cm;
  }
  body::after {
    content: 'Source: expatnetherlandshub.com/downloads/ — Free printable checklists for expats in the Netherlands';
    display: block;
    position: fixed;
    bottom: 0.5cm;
    left: 1.5cm;
    right: 1.5cm;
    font-size: 8pt;
    color: #666;
    border-top: 0.5pt solid #ccc;
    padding-top: 0.3cm;
    text-align: center;
  }
}

@media (max-width: 768px) {
  .dl-hero h1 { font-size: 1.6rem; }
  .dl-toc-grid { grid-template-columns: 1fr; }
  .checklist-card-header { flex-direction: column; align-items: flex-start; }
  .cl-affiliate-box { flex-direction: column; align-items: flex-start; }
}
</style>

<script>
function printChecklist(id) {
  // Temporarily hide all other checklist cards, then print
  var allCards = document.querySelectorAll('.checklist-card');
  var targetCard = document.getElementById(id);
  var hidden = [];
  allCards.forEach(function(card) {
    if (card !== targetCard) {
      card.style.display = 'none';
      hidden.push(card);
    }
  });
  var toc = document.querySelector('.dl-toc');
  var share = document.querySelector('.share-box');
  if (toc) toc.style.display = 'none';
  if (share) share.style.display = 'none';
  window.print();
  // Restore
  hidden.forEach(function(card) { card.style.display = ''; });
  if (toc) toc.style.display = '';
  if (share) share.style.display = '';
}
</script>

<section class="dl-hero">
<div class="dl-hero-inner">
<nav class="breadcrumb" aria-label="Breadcrumb">
<a href="/">Home</a> &rsaquo; <span>Free Downloads</span>
</nav>
<div class="dl-hero-badge">Free &bull; Printable &bull; Updated March 2026</div>
<h1>Free Expat Checklists &amp; Templates</h1>
<p class="dl-hero-desc">Download free printable checklists for moving to the Netherlands. BSN registration, first 30 days, tax return, leaving NL — all in one place.</p>
<p class="dl-hero-meta">8 checklists &middot; Print-ready &middot; No sign-up required &middot; By Sarah van den Berg</p>
</div>
</section>

<div class="dl-main">

<div class="dl-toc">
<h2>Jump to a checklist</h2>
<div class="dl-toc-grid">
<a href="#moving-checklist">1. Moving to the Netherlands</a>
<a href="#bsn-checklist">2. BSN Registration</a>
<a href="#health-insurance-checklist">3. Health Insurance Setup</a>
<a href="#tax-return-checklist">4. Dutch Tax Return</a>
<a href="#thirty-percent-checklist">5. 30% Ruling Application</a>
<a href="#leaving-checklist">6. Leaving the Netherlands</a>
<a href="#bank-account-checklist">7. Opening a Bank Account</a>
<a href="#housing-checklist">8. Housing Search</a>
</div>
</div>

<!-- ==========================================
     CHECKLIST 1 — MOVING TO THE NETHERLANDS
     ========================================== -->
<div class="checklist-card" id="moving-checklist">
<div class="checklist-card-header">
<div class="checklist-card-header-left">
<div class="checklist-num">01</div>
<h2>Moving to the Netherlands Checklist</h2>
</div>
<button class="btn-print" onclick="printChecklist('moving-checklist')">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
Print this checklist
</button>
</div>
<div class="checklist-body">

<div class="cl-section">
<div class="cl-section-title">Before you leave</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Get apostilles on key documents (birth certificate, marriage certificate, diplomas) — takes 2–8 weeks depending on country<div class="cl-note">Most countries issue apostilles through their Ministry of Foreign Affairs or designated authority</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Arrange temporary or permanent housing in the Netherlands<div class="cl-note">You need a registered address to get your BSN — hotel addresses generally not accepted</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Arrange travel insurance to cover the gap before Dutch health insurance kicks in</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Book return flight or have onward travel if required for entry</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Notify your home country bank of your move (international card access)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Gather certified copies of your employment contract, rental contract, and passport</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Research your municipality (gemeente) and their BSN appointment process<div class="cl-note">Amsterdam, Rotterdam, and The Hague have different booking systems and wait times</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Arrange pet import paperwork if applicable (EU health certificate, rabies vaccine, microchip)</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">First week after arrival</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Register at your gemeente and receive your BSN number<div class="cl-note">Book the appointment before you arrive if possible — some cities have 2–4 week waits</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Open a Dutch bank account (or set up Wise for the interim period)<div class="cl-note">You need your BSN for most Dutch bank accounts, but Wise works without one</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Contact your employer's HR to confirm payroll registration with Dutch tax authority (Belastingdienst)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Get a Dutch SIM card or plan (KPN, Odido, Lebara)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Register with a GP (huisarts) — walk in or call the practice directly<div class="cl-note">Many practices are full; register as early as possible</div></span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">First month</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Apply for DigiD (takes 1–2 weeks; activation code arrives by post)<div class="cl-note">You need DigiD for taxes, the IND portal, pension overview, and healthcare declarations</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Take out Dutch health insurance (zorgverzekering) within 4 months of registration
<div class="cl-warning">⚠ If you miss the 4-month window, you are still required to be insured from your registration date and will owe backdated premiums with a surcharge</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Apply for zorgtoeslag (healthcare benefit) at toeslagen.nl if your income qualifies</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Set up a Dutch bank account if you haven't already (ING, ABN AMRO, Rabobank, Bunq)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Apply for the 30% ruling with your employer if eligible<div class="cl-note">Both you and your employer must submit the application; you cannot apply alone</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Arrange home contents insurance (inboedelverzekering) and liability insurance (aansprakelijkheidsverzekering)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Notify your home country: cancel or redirect mail, update address with tax authority, pension, and bank</span></li>
</ul>
</div>

</div>
<div class="checklist-footer">
<span class="checklist-source">Source: <a href="https://expatnetherlandshub.com/downloads/">expatnetherlandshub.com/downloads/</a></span>
<span>Full guide: <a href="/guides/legal/first-30-days-netherlands-expat-checklist-2026/">First 30 Days in the Netherlands →</a></span>
<span>To save as PDF: Ctrl+P &rarr; Save as PDF</span>
</div>
</div>

<!-- ==========================================
     CHECKLIST 2 — BSN REGISTRATION
     ========================================== -->
<div class="checklist-card" id="bsn-checklist">
<div class="checklist-card-header">
<div class="checklist-card-header-left">
<div class="checklist-num">02</div>
<h2>BSN Registration Checklist</h2>
</div>
<button class="btn-print" onclick="printChecklist('bsn-checklist')">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
Print this checklist
</button>
</div>
<div class="checklist-body">

<div class="cl-section">
<div class="cl-section-title">Documents to prepare</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Valid passport or national ID (original, not a copy)<div class="cl-note">EU citizens can use a national ID card; non-EU citizens must use a passport</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Original birth certificate (plus an apostille if issued outside the EU)<div class="cl-note">Some municipalities accept a certified copy; call ahead to confirm</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Rental contract or proof of address at a Dutch address<div class="cl-note">Your name must appear on the contract or have a landlord declaration (verhuurdersverklaring)</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Marriage certificate if applicable (apostilled if issued outside the EU)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Work permit or employment contract (some municipalities ask for this)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Completed municipality registration form (varies per city; download from gemeente website)</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Booking your appointment</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Find your municipality's appointment portal (gemeente.nl, amsterdam.nl, denhaag.nl, etc.)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Book as early as possible — ideally before you arrive<div class="cl-note">Amsterdam and The Hague often have 3–6 week waits during peak periods (September–October)</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Note your appointment reference and confirm appointment by email/SMS reminder</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check if your gemeente requires a specific form to be downloaded and completed in advance</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>If your city has a Expat Center (Amsterdam, The Hague, Eindhoven), check if you qualify — they often have faster appointments</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">At the gemeente appointment</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Bring all original documents (not photocopies)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Arrive 10 minutes early; bring the appointment confirmation</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Ask for written confirmation of your BSN on the spot if possible<div class="cl-note">Some municipalities give you a print-out; others send your BSN by post within 5 working days</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Ask about DigiD registration at the same appointment if available</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Note the date of your official registration — this is the start date for your 4-month health insurance window</span></li>
</ul>
</div>

</div>
<div class="checklist-footer">
<span class="checklist-source">Source: <a href="https://expatnetherlandshub.com/downloads/">expatnetherlandshub.com/downloads/</a></span>
<span>Full guide: <a href="/guides/legal/bsn-registration-guide-2026/">BSN Registration Guide →</a></span>
<span>To save as PDF: Ctrl+P &rarr; Save as PDF</span>
</div>
</div>

<!-- ==========================================
     CHECKLIST 3 — HEALTH INSURANCE
     ========================================== -->
<div class="checklist-card" id="health-insurance-checklist">
<div class="checklist-card-header">
<div class="checklist-card-header-left">
<div class="checklist-num">03</div>
<h2>Health Insurance Setup Checklist</h2>
</div>
<button class="btn-print" onclick="printChecklist('health-insurance-checklist')">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
Print this checklist
</button>
</div>
<div class="checklist-body">

<div class="cl-section">
<div class="cl-section-title">Understand your deadline</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Note your BSN registration date — your 4-month insurance window starts then
<div class="cl-warning">⚠ Critical deadline: You must have Dutch health insurance within 4 months of registering in the Netherlands. Missing this means backdated premiums plus a surcharge from the CAK.</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check whether you are exempt (EU cross-border workers, certain diplomats, and long-stay students under an international plan sometimes qualify)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Confirm your employment start date with HR — your employer may have insurance from day one</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Compare and choose a policy</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Decide on your eigen risico (own risk / deductible): €385 minimum in 2026, up to €885 voluntary<div class="cl-note">Higher own risk = lower monthly premium, but you pay more out of pocket if you use care</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Decide whether you need aanvullende verzekering (supplementary insurance) for dental, physio, or glasses</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check if English-language support matters to you (Zilveren Kruis, CZ, and ONVZ all offer English)</span></li>
</ul>
<div class="cl-affiliate-box">
<div class="aff-text">
<strong>Compare all Dutch health insurers side by side</strong>
Independer is the Netherlands' largest comparison platform — free, takes 10 minutes, shows exact premiums for your age and preferred own risk.
</div>
<a href="https://go.expatnetherlandshub.com/independer-zorg?ref=/downloads/" rel="nofollow noopener sponsored" target="_blank" class="aff-cta">Compare on Independer →</a>
</div>
</div>

<div class="cl-section">
<div class="cl-section-title">Documents needed to enrol</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>BSN number (required by all Dutch insurers)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Dutch home address</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Dutch bank account IBAN for direct debit<div class="cl-note">Some insurers accept a foreign IBAN temporarily; Wise works here if you don't have a Dutch account yet</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Date of birth and passport number</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Preferred GP (huisarts) if choosing a managed-care (zorgmodel) policy</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">After you sign up</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Save your insurance card (verzekeringskaart) — you need it at doctors and pharmacies</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Apply for zorgtoeslag (monthly healthcare benefit) at toeslagen.nl if you are eligible<div class="cl-note">In 2026, single people earning under ~€37,000 may qualify; couples up to ~€47,000</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Register with a GP (huisarts) near your home address</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Cancel any international or home-country health insurance that overlaps</span></li>
</ul>
</div>

</div>
<div class="checklist-footer">
<span class="checklist-source">Source: <a href="https://expatnetherlandshub.com/downloads/">expatnetherlandshub.com/downloads/</a></span>
<span>Full guide: <a href="/guides/health/dutch-health-insurance-guide-expats-2026/">Dutch Health Insurance Guide →</a></span>
<span>To save as PDF: Ctrl+P &rarr; Save as PDF</span>
</div>
</div>

<!-- ==========================================
     CHECKLIST 4 — DUTCH TAX RETURN
     ========================================== -->
<div class="checklist-card" id="tax-return-checklist">
<div class="checklist-card-header">
<div class="checklist-card-header-left">
<div class="checklist-num">04</div>
<h2>Dutch Tax Return Checklist</h2>
</div>
<button class="btn-print" onclick="printChecklist('tax-return-checklist')">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
Print this checklist
</button>
</div>
<div class="checklist-body">

<div class="cl-section">
<div class="cl-section-title">Key deadlines</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span><strong>1 May</strong> — standard deadline to file your aangifte inkomstenbelasting (income tax return) online via belastingdienst.nl
<div class="cl-warning">⚠ If you can't file by 1 May, request an extension before the deadline. Extensions are usually granted automatically for 6 months.</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>1 July</strong> — extended deadline if you request one in time</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>M-form:</strong> If you arrived or left the Netherlands during the tax year, use the M-form (Migration form) — this has a separate process and a different deadline (typically end of June)</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Before you start: what you need</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>DigiD login with SMS authentication activated<div class="cl-note">Without DigiD you cannot file online; apply at digid.nl if you don't have one</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Jaaropgave (annual salary statement) from every employer — typically sent by February<div class="cl-note">If you changed jobs mid-year, you need a jaaropgave from each employer</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>WOZ-waarde (property valuation) if you own property — gemeente sends this by post in January/February</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Mortgage annual statement (hypotheekopgave) showing interest paid — from your bank or mortgage provider</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Annual bank statements or January 1 balances for all accounts (Box 3 savings)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Dividend statements if you hold shares or have a Box 2 (substantial interest) situation</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Healthcare invoice total (for the eigen risico deductible you paid)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Pension statement (pensioenoverzicht) from mijnpensioenoverzicht.nl</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>30% ruling approval letter if applicable — shows your tax-free allowance and the correct taxable salary</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Potential deductions to check</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Mortgage interest deduction (hypotheekrenteaftrek) — only for your primary residence</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Alimony payments (partneralimentatie)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Study costs (if paid out of pocket and not reimbursed) — check current rules as these have been restricted</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Gifts to recognised charities (giftenaftrek) over €60 or 1% of income, up to 10% of income</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Specific healthcare costs not reimbursed by insurance (limited circumstances)</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">After filing</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Keep confirmation and the filing reference number</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Wait for the voorlopige aanslag (provisional assessment) — Belastingdienst sends this within a few weeks</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check the final aanslag (definitive assessment) and verify figures match your filing</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>If you disagree with the assessment: file a bezwaar (objection) within 6 weeks of the date on the letter</span></li>
</ul>
</div>

</div>
<div class="checklist-footer">
<span class="checklist-source">Source: <a href="https://expatnetherlandshub.com/downloads/">expatnetherlandshub.com/downloads/</a></span>
<span>Full guide: <a href="/guides/finance/dutch-tax-return-checklist-expats-2026/">Dutch Tax Return Guide for Expats →</a></span>
<span>To save as PDF: Ctrl+P &rarr; Save as PDF</span>
</div>
</div>

<!-- ==========================================
     CHECKLIST 5 — 30% RULING
     ========================================== -->
<div class="checklist-card" id="thirty-percent-checklist">
<div class="checklist-card-header">
<div class="checklist-card-header-left">
<div class="checklist-num">05</div>
<h2>30% Ruling Application Checklist</h2>
</div>
<button class="btn-print" onclick="printChecklist('thirty-percent-checklist')">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
Print this checklist
</button>
</div>
<div class="checklist-body">

<div class="cl-section">
<div class="cl-section-title">Eligibility requirements — confirm all apply</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>You are recruited from abroad (not already living in the Netherlands)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>You have a specific expertise that is scarce in the Dutch labour market</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Your taxable salary (after the 30% exclusion) meets the minimum threshold:
  <div class="cl-note">2026 threshold: €46,107 gross/year (taxable after ruling). Under 30 with a qualifying master's degree: €35,048. Adjust upwards — your actual salary must be ~€65,867 or ~€50,069 respectively.</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>You lived more than 150 km from the Dutch border for 16 of the 24 months before your start date<div class="cl-note">This is the "distance criterion" — it disqualifies people who lived in Belgium, Luxembourg, or near the German/French border</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Your employer is a Dutch payroll entity (registered with Belastingdienst)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>This is your first time applying (or you meet the recalculation rules for prior Dutch work)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>You submit within 4 months of your Dutch employment start date
  <div class="cl-warning">⚠ Apply within 4 months of your Dutch contract start date. If you miss this window, the ruling can only start from the date of application — you lose the backdated benefit.</div></span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Steps for your employer</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>HR or payroll team submits the application to Belastingdienst on your behalf (the employee cannot apply alone)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Employer completes form "Verzoek loonheffingen 30%-regeling" (available at belastingdienst.nl)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Employer signs and submits the form — you both sign</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Wait for the "beschikking" (ruling letter) — typically 4–10 weeks</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Once approved, employer applies the ruling to payroll starting from the approval date (or retroactively if within the window)</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Documents to gather</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Employment contract showing Dutch salary and start date</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Proof of previous foreign address (utility bills, registration document from prior country)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Copies of relevant diplomas or credentials demonstrating scarcity</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Passport copy</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>BSN number (once received from gemeente)</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">2026 step-down schedule (new rulings from 2024 onward)</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Months 1–20:</strong> 30% of your salary is tax-free</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Months 21–40:</strong> 20% of your salary is tax-free</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Months 41–60:</strong> 10% of your salary is tax-free</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Maximum ruling duration: 5 years (previous time in NL within last 25 years is subtracted)</span></li>
</ul>
</div>

</div>
<div class="checklist-footer">
<span class="checklist-source">Source: <a href="https://expatnetherlandshub.com/downloads/">expatnetherlandshub.com/downloads/</a></span>
<span>Full guide: <a href="/guides/finance/30-percent-ruling-eligibility-guide-2026/">30% Ruling Eligibility Guide →</a></span>
<span>To save as PDF: Ctrl+P &rarr; Save as PDF</span>
</div>
</div>

<!-- ==========================================
     CHECKLIST 6 — LEAVING THE NETHERLANDS
     ========================================== -->
<div class="checklist-card" id="leaving-checklist">
<div class="checklist-card-header">
<div class="checklist-card-header-left">
<div class="checklist-num">06</div>
<h2>Leaving the Netherlands Checklist</h2>
</div>
<button class="btn-print" onclick="printChecklist('leaving-checklist')">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
Print this checklist
</button>
</div>
<div class="checklist-body">

<div class="cl-section">
<div class="cl-section-title">3 months before you leave</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Notify your employer of your leaving date and start your notice period (opzegtermijn)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check your rental contract notice period (usually 1 month; some contracts require 2–3 months)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Arrange your move: shipping company, temporary storage, or selling furniture</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Contact Belastingdienst if you have an ongoing voorlopige teruggaaf (provisional refund) to stop it</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check your pension situation: request a value statement (waardeoverzicht) from your pension fund and check transfer or continuation options</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Cancel subscriptions with notice periods: gym, streaming, mobile plan, internet</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">1 month before you leave</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Deregister at your gemeente (uitschrijven) — this officially ends your Dutch residency<div class="cl-note">You can deregister up to 5 days before your actual departure date</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Cancel Dutch health insurance — it ends automatically on your deregistration date, but notify your insurer</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>File or arrange filing for your final Dutch tax return (M-form for the year of departure)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Request a final jaaropgave from your employer at the end of your employment</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Notify the IND if you are on a residence permit (they should be informed of departure)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Return any leased equipment from work</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Get a deposit refund from your landlord — document the apartment's condition with photos</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Final week</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Download your banking history and statements before closing or switching accounts<div class="cl-note">Dutch banks often send final statements by post — update your forwarding address first</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Set up mail forwarding with PostNL (doorsturen service) for 3–12 months</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Update your address with Belastingdienst to your new address abroad (or a trusted contact in NL)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Notify your Dutch bank of your new address; consider keeping the account open for any final refunds</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Take your BSN note — you may need it for the M-form tax return after you leave</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Cancel DigiD or update your contact details to your new address</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Collect final pay and holiday allowance (vakantiegeld) from employer</span></li>
</ul>
</div>

</div>
<div class="checklist-footer">
<span class="checklist-source">Source: <a href="https://expatnetherlandshub.com/downloads/">expatnetherlandshub.com/downloads/</a></span>
<span>Full guide: <a href="/guides/legal/dutch-deregistration-leaving-checklist-2026/">Leaving the Netherlands Guide →</a></span>
<span>To save as PDF: Ctrl+P &rarr; Save as PDF</span>
</div>
</div>

<!-- ==========================================
     CHECKLIST 7 — BANK ACCOUNT
     ========================================== -->
<div class="checklist-card" id="bank-account-checklist">
<div class="checklist-card-header">
<div class="checklist-card-header-left">
<div class="checklist-num">07</div>
<h2>Opening a Bank Account Checklist</h2>
</div>
<button class="btn-print" onclick="printChecklist('bank-account-checklist')">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
Print this checklist
</button>
</div>
<div class="checklist-body">

<div class="cl-section">
<div class="cl-section-title">Before you can open a Dutch bank account</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>BSN number — required by all major Dutch banks (ING, ABN AMRO, Rabobank, SNS)<div class="cl-note">Without a BSN, your options are Bunq (accepts foreign address), or Wise (no BSN needed at all)</div></span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Dutch home address registered at gemeente</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Valid passport or ID card</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Dutch phone number (for SMS verification)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Email address</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Interim option: open a Wise account first</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Wise gives you a multi-currency account with an IBAN — usable immediately, no BSN required</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Good for receiving your first salary while waiting for your Dutch bank account</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Works with most Dutch landlords, health insurers, and employers for initial payments</span></li>
</ul>
<div class="cl-affiliate-box">
<div class="aff-text">
<strong>Wise — multi-currency account, works from day one</strong>
No BSN required, holds 40+ currencies, Dutch IBAN available, low international transfer fees.
</div>
<a href="https://go.expatnetherlandshub.com/wise?ref=/downloads/" rel="nofollow noopener sponsored" target="_blank" class="aff-cta">Open a Wise account →</a>
</div>
</div>

<div class="cl-section">
<div class="cl-section-title">Choose a Dutch bank</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span><strong>ING:</strong> English app, widely accepted, easy account opening online</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>ABN AMRO:</strong> Strong English support, good for expats and internationals; Expat Banking package available</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Rabobank:</strong> Good rural and mid-city coverage; English support is more limited</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Bunq:</strong> Dutch fintech, fully English, opens without BSN initially, very expat-friendly</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>N26 / Revolut:</strong> European neobanks — convenient but not always accepted by all Dutch systems<div class="cl-note">Some landlords and pension funds only accept Dutch IBANs (NLxx XXXX). Always confirm acceptability first.</div></span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">After opening your account</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Activate your debit card and iDEAL (the Dutch online payment system)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Set up salary payment with your employer's HR using your new IBAN</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Set up automatic payments (machtigingen) for rent, health insurance, and utilities</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Register for your bank's app and enable push notifications for transactions</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Share your Dutch IBAN with Belastingdienst for any tax refunds</span></li>
</ul>
</div>

</div>
<div class="checklist-footer">
<span class="checklist-source">Source: <a href="https://expatnetherlandshub.com/downloads/">expatnetherlandshub.com/downloads/</a></span>
<span>Full guide: <a href="/guides/finance/how-to-open-bank-account-netherlands-2026/">How to Open a Bank Account in the Netherlands →</a></span>
<span>To save as PDF: Ctrl+P &rarr; Save as PDF</span>
</div>
</div>

<!-- ==========================================
     CHECKLIST 8 — HOUSING SEARCH
     ========================================== -->
<div class="checklist-card" id="housing-checklist">
<div class="checklist-card-header">
<div class="checklist-card-header-left">
<div class="checklist-num">08</div>
<h2>Housing Search Checklist</h2>
</div>
<button class="btn-print" onclick="printChecklist('housing-checklist')">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
Print this checklist
</button>
</div>
<div class="checklist-body">

<div class="cl-section">
<div class="cl-section-title">Set your budget first</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Calculate your maximum rent: Dutch standard is that rent should not exceed 1/3 of your gross monthly salary</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Factor in servicekosten (service charges), which are added on top of the base rent for apartments</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Budget for the deposit (waarborgsom): typically 1–2 months' rent, paid upfront</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check if you qualify for huurtoeslag (rent benefit): single people earning under ~€31,750/year may qualify for social housing; private sector has no income cap for benefit</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Use the <a href="/tools/housing-budget-checker/">Rent Affordability Calculator</a> to know exactly what you can afford</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Where to search</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Funda.nl</strong> — the main listings platform; most agents post here</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Pararius.nl</strong> — strong for international listings, English interface</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Kamernet.nl</strong> — good for rooms, student housing, and shared flats</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Facebook Groups</strong> — "Amsterdam Housing", "Expats in The Hague Housing" — fast-moving, mix of scams and legitimate listings</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span><strong>Expat Center / relocation agency</strong> — if your employer offers a relocation package, ask HR to activate it</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Set up email alerts on Funda and Pararius for your criteria — good apartments in Amsterdam and The Hague go within 24–48 hours</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Scam red flags — walk away if you see these</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Landlord is "abroad" and sends keys by post after you wire a deposit</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Price is significantly below market rate for the location</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Payment requested via cryptocurrency, Western Union, or WhatsApp only</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>No physical viewing possible before signing the contract</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Urgency pressure: "someone else is offering today — decide now"</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Landlord's identity cannot be verified against the Kadaster (land registry) ownership records</span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Documents landlords typically want from you</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Passport or ID copy</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Employment contract or proof of income (3 recent payslips)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Employer's statement (werkgeversverklaring) confirming your employment and salary</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Bank statements for the last 3 months</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>References from previous landlords if available</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>BSN number (required once you register in the Netherlands)<div class="cl-note">Some landlords accept a letter confirming BSN is in process if you haven't registered yet</div></span></li>
</ul>
</div>

<div class="cl-section">
<div class="cl-section-title">Before signing the rental contract</div>
<ul class="cl-items">
<li><span class="cl-check" aria-hidden="true"></span><span>Read the entire contract — if it's in Dutch and you don't read Dutch, get a translated copy or have it reviewed</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check the notice period (opzegtermijn) and any break clauses</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Confirm what is included in the servicekosten (hot water, heating, building maintenance?)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Do a thorough inspection and document all existing damage with photos before moving in</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Confirm the deposit goes into a separate account (not into the landlord's personal account)</span></li>
<li><span class="cl-check" aria-hidden="true"></span><span>Check Huurcommissie rules: if your rent is in the social sector range, you may have rent protection rights</span></li>
</ul>
</div>

</div>
<div class="checklist-footer">
<span class="checklist-source">Source: <a href="https://expatnetherlandshub.com/downloads/">expatnetherlandshub.com/downloads/</a></span>
<span>Full guide: <a href="/guides/housing/finding-housing-netherlands-expats-2026/">Finding Housing in the Netherlands →</a></span>
<span>To save as PDF: Ctrl+P &rarr; Save as PDF</span>
</div>
</div>

<!-- ==========================================
     SHARE SECTION
     ========================================== -->
<div class="share-box">
<h2>Share These Checklists</h2>
<p>These checklists are free to use and share. If you find them helpful, we'd appreciate a link back to this page:</p>
<div class="share-url">https://expatnetherlandshub.com/downloads/</div>
<p>Expat bloggers, relocation services, and HR departments: feel free to link to or embed these checklists on your own website.</p>
<p>Each checklist is printable as a PDF via your browser (Ctrl+P &rarr; Save as PDF on Windows/Linux, Cmd+P on Mac). The print layout hides navigation and shows only the checklist content, with our URL in the footer so people can always find the original source.</p>
<p>Questions or suggestions for new checklists? <a href="/about/">Get in touch</a>.</p>
</div>

</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Free Expat Checklists & Templates",
  "description": "Download free printable checklists for moving to the Netherlands. BSN registration, first 30 days, tax return, leaving NL — all in one place.",
  "url": "https://expatnetherlandshub.com/downloads/",
  "publisher": {
    "@type": "Organization",
    "name": "Expat Netherlands Hub",
    "url": "https://expatnetherlandshub.com"
  },
  "mainEntity": {
    "@type": "ItemList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Moving to the Netherlands Checklist", "url": "https://expatnetherlandshub.com/downloads/#moving-checklist" },
      { "@type": "ListItem", "position": 2, "name": "BSN Registration Checklist", "url": "https://expatnetherlandshub.com/downloads/#bsn-checklist" },
      { "@type": "ListItem", "position": 3, "name": "Health Insurance Setup Checklist", "url": "https://expatnetherlandshub.com/downloads/#health-insurance-checklist" },
      { "@type": "ListItem", "position": 4, "name": "Dutch Tax Return Checklist", "url": "https://expatnetherlandshub.com/downloads/#tax-return-checklist" },
      { "@type": "ListItem", "position": 5, "name": "30% Ruling Application Checklist", "url": "https://expatnetherlandshub.com/downloads/#thirty-percent-checklist" },
      { "@type": "ListItem", "position": 6, "name": "Leaving the Netherlands Checklist", "url": "https://expatnetherlandshub.com/downloads/#leaving-checklist" },
      { "@type": "ListItem", "position": 7, "name": "Opening a Bank Account Checklist", "url": "https://expatnetherlandshub.com/downloads/#bank-account-checklist" },
      { "@type": "ListItem", "position": 8, "name": "Housing Search Checklist", "url": "https://expatnetherlandshub.com/downloads/#housing-checklist" }
    ]
  }
}
</script>
