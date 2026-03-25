---
title: "Which Dutch City Is Right for You? — Free Quiz"
description: "Answer 7 quick questions and find out which Dutch city matches your lifestyle, budget, and priorities. Free interactive quiz for expats moving to the Netherlands."
type: "tools"
layout: "single"
featured_image: "/images/categories/cities.svg"
---

<script type="application/ld+json">
{
"@context": "https://schema.org",
"@type": "WebApplication",
"name": "Which Dutch City Is Right for You? Quiz",
"url": "https://expatnetherlandshub.com/tools/city-quiz/",
"description": "Answer 7 questions and find out which Dutch city matches your lifestyle, budget, and priorities. Free quiz for expats moving to the Netherlands.",
"applicationCategory": "LifestyleApplication",
"operatingSystem": "All",
"offers": {
"@type": "Offer",
"price": "0",
"priceCurrency": "EUR"
},
"publisher": {
"@type": "Organization",
"name": "ExpatNetherlandsHub",
"url": "https://expatnetherlandshub.com"
}
}
</script>

<style>
/* ============================================================
  VARIABLES
============================================================ */
:root {
  --green:       #1B6B4A;
  --green-dark:  #134D36;
  --green-light: #E8F5EF;
  --orange:      #E8832A;
  --orange-light:#FEF3E8;
  --text:        #1A2332;
  --muted:       #6B7280;
  --border:      #E5E9EE;
  --card:        #FFFFFF;
  --radius:      14px;
  --radius-sm:   10px;
  --shadow:      0 2px 12px rgba(0,0,0,0.07);
  --shadow-lg:   0 8px 32px rgba(0,0,0,0.12);
}

/* ============================================================
  HERO
============================================================ */
.quiz-hero {
  background:
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Ccircle cx='40' cy='40' r='1.5' fill='%23ffffff' opacity='0.07'/%3E%3Ccircle cx='0' cy='0' r='1' fill='%23ffffff' opacity='0.05'/%3E%3Ccircle cx='80' cy='0' r='1' fill='%23ffffff' opacity='0.05'/%3E%3Ccircle cx='0' cy='80' r='1' fill='%23ffffff' opacity='0.05'/%3E%3Ccircle cx='80' cy='80' r='1' fill='%23ffffff' opacity='0.05'/%3E%3Cpath d='M0 40h80M40 0v80' stroke='%23ffffff' stroke-width='0.3' opacity='0.04'/%3E%3C/svg%3E"),
    linear-gradient(135deg, #134D36 0%, #1B6B4A 55%, #2D9B6A 100%);
  color: #fff;
  padding: 3rem 1.5rem 2.5rem;
  position: relative;
  overflow: hidden;
}
.quiz-hero::before {
  content: '';
  position: absolute;
  top: -50%; right: -15%;
  width: 500px; height: 500px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(232,131,42,0.13) 0%, transparent 70%);
  pointer-events: none;
}
.quiz-hero::after {
  content: '';
  position: absolute;
  bottom: -40%; left: -10%;
  width: 400px; height: 400px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(45,155,106,0.15) 0%, transparent 70%);
  pointer-events: none;
}
.quiz-hero-inner {
  max-width: 760px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  text-align: center;
}
.quiz-hero-badge {
  display: inline-block;
  background: rgba(232,131,42,0.2);
  border: 1px solid rgba(232,131,42,0.5);
  color: #F5A623;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 0.3rem 0.9rem;
  border-radius: 20px;
  margin-bottom: 1rem;
}
.quiz-hero h1 {
  font-size: 2.1rem;
  font-weight: 800;
  color: #fff;
  margin: 0 0 0.6rem;
  letter-spacing: -0.02em;
  line-height: 1.2;
}
.quiz-hero-sub {
  color: rgba(255,255,255,0.85);
  font-size: 1.05rem;
  margin: 0 auto 0.8rem;
  max-width: 560px;
}
.quiz-hero-meta {
  color: rgba(255,255,255,0.6);
  font-size: 0.82rem;
}
.quiz-hero-icon {
  font-size: 3.5rem;
  margin-bottom: 1rem;
  line-height: 1;
}

/* ============================================================
  BREADCRUMB
============================================================ */
.quiz-breadcrumb {
  font-size: 0.83rem;
  color: var(--muted);
  margin-bottom: 1.5rem;
}
.quiz-breadcrumb a {
  color: var(--muted);
  text-decoration: none;
}
.quiz-breadcrumb a:hover { color: var(--green); }

/* ============================================================
  LAYOUT
============================================================ */
.quiz-body {
  max-width: 760px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem 5rem;
}

/* ============================================================
  CARD
============================================================ */
.quiz-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 2rem;
  margin-bottom: 1.5rem;
}

/* ============================================================
  PROGRESS
============================================================ */
.progress-wrap {
  margin-bottom: 2rem;
}
.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.6rem;
}
.progress-label {
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--muted);
}
.progress-count {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--green);
}
.progress-bar-track {
  height: 6px;
  background: var(--border);
  border-radius: 99px;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--green) 0%, #2D9B6A 100%);
  border-radius: 99px;
  transition: width 0.4s ease;
}

/* ============================================================
  QUESTION
============================================================ */
.question-block {
  display: none;
  animation: fadeSlideIn 0.35s ease both;
}
.question-block.active {
  display: block;
}
@keyframes fadeSlideIn {
  from { opacity: 0; transform: translateY(14px); }
  to   { opacity: 1; transform: translateY(0); }
}
.question-number {
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--orange);
  margin-bottom: 0.5rem;
}
.question-text {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--text);
  margin: 0 0 0.3rem;
  line-height: 1.3;
  font-family: 'DM Sans', sans-serif;
}
.question-hint {
  font-size: 0.88rem;
  color: var(--muted);
  margin-bottom: 1.5rem;
}

/* ============================================================
  OPTIONS
============================================================ */
.options-grid {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.option-btn {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding: 0.9rem 1.2rem;
  border: 2px solid var(--border);
  border-radius: var(--radius-sm);
  background: #fff;
  cursor: pointer;
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--text);
  text-align: left;
  transition: border-color 0.15s, background 0.15s, box-shadow 0.15s;
  font-family: inherit;
  width: 100%;
}
.option-btn:hover {
  border-color: var(--green);
  background: var(--green-light);
  box-shadow: 0 2px 8px rgba(27,107,74,0.1);
}
.option-btn.selected {
  border-color: var(--green);
  background: var(--green-light);
  color: var(--green-dark);
  box-shadow: 0 2px 8px rgba(27,107,74,0.15);
}
.option-btn.selected .option-check {
  background: var(--green);
  border-color: var(--green);
}
.option-btn.selected .option-check::after {
  opacity: 1;
}
.option-check {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid var(--border);
  flex-shrink: 0;
  position: relative;
  transition: all 0.15s;
}
.option-check::after {
  content: '';
  position: absolute;
  top: 4px; left: 4px;
  width: 10px; height: 10px;
  border-radius: 50%;
  background: #fff;
  opacity: 0;
  transition: opacity 0.15s;
}
.option-emoji {
  font-size: 1.2rem;
  flex-shrink: 0;
}
.option-label {
  flex: 1;
  line-height: 1.3;
}
.option-sub {
  display: block;
  font-size: 0.8rem;
  color: var(--muted);
  font-weight: 400;
  margin-top: 0.15rem;
}

/* ============================================================
  NAVIGATION
============================================================ */
.quiz-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1.75rem;
  gap: 1rem;
}
.btn-back {
  padding: 0.7rem 1.4rem;
  border: 2px solid var(--border);
  border-radius: var(--radius-sm);
  background: #fff;
  color: var(--muted);
  font-size: 0.92rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
  font-family: inherit;
}
.btn-back:hover {
  border-color: var(--green);
  color: var(--green);
}
.btn-back:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}
.btn-next {
  padding: 0.8rem 2rem;
  background: var(--green);
  color: #fff;
  border: none;
  border-radius: var(--radius-sm);
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s, transform 0.1s;
  font-family: inherit;
  letter-spacing: 0.01em;
}
.btn-next:hover { background: var(--green-dark); }
.btn-next:active { transform: scale(0.98); }
.btn-next:disabled {
  background: #CBD5E1;
  cursor: not-allowed;
}

/* ============================================================
  RESULTS
============================================================ */
#quiz-results {
  display: none;
}
.results-header {
  text-align: center;
  margin-bottom: 2rem;
}
.results-celebrate {
  font-size: 3rem;
  margin-bottom: 0.5rem;
}
.results-title {
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--text);
  margin: 0 0 0.4rem;
  font-family: 'DM Sans', sans-serif;
}
.results-sub {
  color: var(--muted);
  font-size: 0.95rem;
}

/* City result cards */
.city-result {
  border: 2px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  margin-bottom: 1.25rem;
  transition: box-shadow 0.2s;
}
.city-result:hover {
  box-shadow: var(--shadow-lg);
}
.city-result.rank-1 {
  border-color: var(--green);
}
.city-result.rank-2 {
  border-color: #D1E9DC;
}
.city-result.rank-3 {
  border-color: var(--border);
}
.city-result-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.2rem 1.5rem;
  background: #FAFBFC;
  border-bottom: 1px solid var(--border);
}
.city-result.rank-1 .city-result-header {
  background: var(--green-light);
}
.city-rank-badge {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1rem;
  flex-shrink: 0;
  font-family: 'DM Sans', sans-serif;
}
.rank-1 .city-rank-badge {
  background: var(--green);
  color: #fff;
}
.rank-2 .city-rank-badge {
  background: #2D9B6A;
  color: #fff;
}
.rank-3 .city-rank-badge {
  background: #6B7280;
  color: #fff;
}
.city-result-name {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--text);
  font-family: 'DM Sans', sans-serif;
  margin: 0;
}
.city-result-tagline {
  font-size: 0.85rem;
  color: var(--muted);
  margin: 0.1rem 0 0;
}
.city-match-score {
  margin-left: auto;
  text-align: right;
  flex-shrink: 0;
}
.city-match-pct {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--green);
  font-family: 'DM Sans', sans-serif;
  line-height: 1;
}
.city-match-label {
  font-size: 0.72rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.city-result-body {
  padding: 1.25rem 1.5rem;
}
.city-why {
  font-size: 0.9rem;
  color: var(--text);
  margin-bottom: 1rem;
  line-height: 1.55;
}
.city-why strong {
  color: var(--green-dark);
}
.city-quick-facts {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.1rem;
}
.city-fact-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.3rem 0.75rem;
  background: var(--green-light);
  color: var(--green-dark);
  border-radius: 99px;
  font-size: 0.8rem;
  font-weight: 600;
}
.city-links {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.city-link-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.6rem 1.1rem;
  border-radius: var(--radius-sm);
  font-size: 0.87rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.15s;
}
.city-link-btn.primary {
  background: var(--green);
  color: #fff;
}
.city-link-btn.primary:hover {
  background: var(--green-dark);
}
.city-link-btn.secondary {
  background: var(--orange-light);
  color: var(--orange);
  border: 1px solid rgba(232,131,42,0.3);
}
.city-link-btn.secondary:hover {
  background: rgba(232,131,42,0.2);
}

/* Share */
.share-card {
  background: linear-gradient(135deg, var(--green-light) 0%, #fff 100%);
  border: 2px solid #D1E9DC;
  border-radius: var(--radius);
  padding: 1.75rem;
  text-align: center;
  margin-top: 1.75rem;
}
.share-title {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--text);
  margin: 0 0 0.3rem;
  font-family: 'DM Sans', sans-serif;
}
.share-sub {
  font-size: 0.88rem;
  color: var(--muted);
  margin-bottom: 1.1rem;
}
.btn-share {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.8rem;
  background: var(--orange);
  color: #fff;
  border: none;
  border-radius: var(--radius-sm);
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  font-family: inherit;
  transition: background 0.15s, transform 0.1s;
  margin-right: 0.5rem;
  margin-bottom: 0.5rem;
}
.btn-share:hover { background: #CC6F1F; }
.btn-share:active { transform: scale(0.98); }
.btn-retake {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.8rem;
  background: #fff;
  color: var(--green);
  border: 2px solid var(--green);
  border-radius: var(--radius-sm);
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.15s;
  margin-bottom: 0.5rem;
}
.btn-retake:hover {
  background: var(--green-light);
}
.share-copied {
  display: none;
  font-size: 0.85rem;
  color: var(--green);
  font-weight: 600;
  margin-top: 0.75rem;
}
.share-copied.visible {
  display: block;
}

/* ============================================================
  ABOUT SECTION
============================================================ */
.about-section {
  margin-top: 3rem;
}
.about-section h2 {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--text);
  margin: 0 0 0.75rem;
  font-family: 'DM Sans', sans-serif;
}
.about-section p {
  font-size: 0.92rem;
  color: #374151;
  line-height: 1.65;
  margin-bottom: 1rem;
}
.cities-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.5rem;
}
.city-chip {
  display: inline-block;
  padding: 0.25rem 0.7rem;
  background: var(--green-light);
  color: var(--green-dark);
  border-radius: 99px;
  font-size: 0.8rem;
  font-weight: 600;
  text-decoration: none;
}
.city-chip:hover {
  background: #D1E9DC;
}

/* ============================================================
  RESPONSIVE
============================================================ */
@media (max-width: 600px) {
  .quiz-hero h1 { font-size: 1.55rem; }
  .quiz-card { padding: 1.35rem; }
  .question-text { font-size: 1.1rem; }
  .city-result-header { padding: 1rem; }
  .city-result-body { padding: 1rem; }
  .city-links { flex-direction: column; }
  .city-link-btn { justify-content: center; }
  .city-match-pct { font-size: 1.1rem; }
  .quiz-hero { padding: 2.2rem 1.2rem 2rem; }
}
</style>

<!-- HERO -->
<div class="quiz-hero">
  <div class="quiz-hero-inner">
    <div class="quiz-hero-icon">🇳🇱</div>
    <div class="quiz-hero-badge">Free Quiz — Takes 2 Minutes</div>
    <h1>Which Dutch City Is Right for You?</h1>
    <p class="quiz-hero-sub">Answer 7 questions about your budget, lifestyle, and priorities — we'll match you to the perfect Dutch city.</p>
    <p class="quiz-hero-meta">18 cities covered &nbsp;·&nbsp; No sign-up needed &nbsp;·&nbsp; Instantly shareable result</p>
  </div>
</div>

<!-- BODY -->
<div class="quiz-body">

  <div class="quiz-breadcrumb">
    <a href="/">Home</a> &rsaquo;
    <a href="/tools/">Tools</a> &rsaquo;
    Dutch City Quiz
  </div>

  <!-- QUIZ CARD -->
  <div class="quiz-card" id="quiz-container">

    <!-- Progress -->
    <div class="progress-wrap">
      <div class="progress-header">
        <span class="progress-label">Your Progress</span>
        <span class="progress-count" id="progress-count">Question 1 of 7</span>
      </div>
      <div class="progress-bar-track">
        <div class="progress-bar-fill" id="progress-bar" style="width: 14%"></div>
      </div>
    </div>

    <!-- Q1: Budget -->
    <div class="question-block active" id="q1">
      <div class="question-number">Question 1 — Budget</div>
      <h2 class="question-text">What's your monthly rent budget?</h2>
      <p class="question-hint">Think about what you can realistically spend on an apartment or room.</p>
      <div class="options-grid">
        <button class="option-btn" data-q="1" data-v="budget_low">
          <span class="option-check"></span>
          <span class="option-emoji">💰</span>
          <span class="option-label">
            Under €1,000
            <span class="option-sub">Student or very budget-conscious — shared housing is likely</span>
          </span>
        </button>
        <button class="option-btn" data-q="1" data-v="budget_mid">
          <span class="option-check"></span>
          <span class="option-emoji">💶</span>
          <span class="option-label">
            €1,000 – €1,500
            <span class="option-sub">Solid budget — studio or small apartment is possible in many cities</span>
          </span>
        </button>
        <button class="option-btn" data-q="1" data-v="budget_high">
          <span class="option-check"></span>
          <span class="option-emoji">💳</span>
          <span class="option-label">
            €1,500 – €2,000
            <span class="option-sub">Comfortable — a real apartment in most cities, including bigger ones</span>
          </span>
        </button>
        <button class="option-btn" data-q="1" data-v="budget_top">
          <span class="option-check"></span>
          <span class="option-emoji">🏠</span>
          <span class="option-label">
            Over €2,000
            <span class="option-sub">Premium — you can live well anywhere, including central Amsterdam</span>
          </span>
        </button>
      </div>
    </div>

    <!-- Q2: Work style -->
    <div class="question-block" id="q2">
      <div class="question-number">Question 2 — Work Style</div>
      <h2 class="question-text">How do you work?</h2>
      <p class="question-hint">Your work situation shapes which city makes the most practical sense.</p>
      <div class="options-grid">
        <button class="option-btn" data-q="2" data-v="work_office">
          <span class="option-check"></span>
          <span class="option-emoji">🏢</span>
          <span class="option-label">
            Office job in a major city
            <span class="option-sub">I need to be close to corporate headquarters or a financial hub</span>
          </span>
        </button>
        <button class="option-btn" data-q="2" data-v="work_tech">
          <span class="option-check"></span>
          <span class="option-emoji">⚙️</span>
          <span class="option-label">
            Tech, engineering, or design
            <span class="option-sub">I work in the innovation economy — ASML, Philips, startups</span>
          </span>
        </button>
        <button class="option-btn" data-q="2" data-v="work_remote">
          <span class="option-check"></span>
          <span class="option-emoji">🌐</span>
          <span class="option-label">
            Remote or freelance
            <span class="option-sub">Location-independent — I just need fast internet and good quality of life</span>
          </span>
        </button>
        <button class="option-btn" data-q="2" data-v="work_academia">
          <span class="option-check"></span>
          <span class="option-emoji">🎓</span>
          <span class="option-label">
            University, research, or academia
            <span class="option-sub">I'm a student or researcher at a Dutch university</span>
          </span>
        </button>
      </div>
    </div>

    <!-- Q3: Social life -->
    <div class="question-block" id="q3">
      <div class="question-number">Question 3 — Social Life</div>
      <h2 class="question-text">What kind of social scene matters most to you?</h2>
      <p class="question-hint">Be honest — your social energy will shape how happy you are day-to-day.</p>
      <div class="options-grid">
        <button class="option-btn" data-q="3" data-v="social_international">
          <span class="option-check"></span>
          <span class="option-emoji">🌍</span>
          <span class="option-label">
            Big international expat community
            <span class="option-sub">I want to meet people from everywhere and feel at home quickly</span>
          </span>
        </button>
        <button class="option-btn" data-q="3" data-v="social_gezellig">
          <span class="option-check"></span>
          <span class="option-emoji">☕</span>
          <span class="option-label">
            Cozy, local Dutch culture (gezellig)
            <span class="option-sub">I want to integrate, find neighbourhood cafes, and live like a local</span>
          </span>
        </button>
        <button class="option-btn" data-q="3" data-v="social_nightlife">
          <span class="option-check"></span>
          <span class="option-emoji">🎉</span>
          <span class="option-label">
            Active nightlife and events
            <span class="option-sub">Bars, clubs, festivals, cultural events — I want to be in the middle of it</span>
          </span>
        </button>
        <button class="option-btn" data-q="3" data-v="social_family">
          <span class="option-check"></span>
          <span class="option-emoji">👨‍👩‍👧</span>
          <span class="option-label">
            Family-friendly and safe
            <span class="option-sub">Good schools, parks, quiet neighbourhoods — I'm here with a family</span>
          </span>
        </button>
      </div>
    </div>

    <!-- Q4: Nature -->
    <div class="question-block" id="q4">
      <div class="question-number">Question 4 — Nature</div>
      <h2 class="question-text">How important is access to nature?</h2>
      <p class="question-hint">The Netherlands is flat, but some cities are much greener than others.</p>
      <div class="options-grid">
        <button class="option-btn" data-q="4" data-v="nature_high">
          <span class="option-check"></span>
          <span class="option-emoji">🌲</span>
          <span class="option-label">
            Very important — I need forests, hills, or beach nearby
            <span class="option-sub">Weekend walks and cycling through nature are non-negotiable for me</span>
          </span>
        </button>
        <button class="option-btn" data-q="4" data-v="nature_mid">
          <span class="option-check"></span>
          <span class="option-emoji">🌳</span>
          <span class="option-label">
            Somewhat — nice parks and green spaces are enough
            <span class="option-sub">I appreciate green areas but don't need wilderness on my doorstep</span>
          </span>
        </button>
        <button class="option-btn" data-q="4" data-v="nature_low">
          <span class="option-check"></span>
          <span class="option-emoji">🏙️</span>
          <span class="option-label">
            Not really — I'm a city person
            <span class="option-sub">Streets, culture, restaurants, and urban energy is what I'm after</span>
          </span>
        </button>
      </div>
    </div>

    <!-- Q5: Commute -->
    <div class="question-block" id="q5">
      <div class="question-number">Question 5 — Commute</div>
      <h2 class="question-text">Do you need to commute to Amsterdam?</h2>
      <p class="question-hint">Amsterdam is the biggest job hub. Proximity matters if you work there.</p>
      <div class="options-grid">
        <button class="option-btn" data-q="5" data-v="commute_daily">
          <span class="option-check"></span>
          <span class="option-emoji">🚆</span>
          <span class="option-label">
            Yes, daily or nearly daily
            <span class="option-sub">I need to be within 30–45 minutes of Amsterdam by train</span>
          </span>
        </button>
        <button class="option-btn" data-q="5" data-v="commute_sometimes">
          <span class="option-check"></span>
          <span class="option-emoji">🚉</span>
          <span class="option-label">
            Sometimes — a few times a week is fine
            <span class="option-sub">An hour by train is acceptable a couple of days per week</span>
          </span>
        </button>
        <button class="option-btn" data-q="5" data-v="commute_no">
          <span class="option-check"></span>
          <span class="option-emoji">🏡</span>
          <span class="option-label">
            No — I don't commute to Amsterdam at all
            <span class="option-sub">My work is local, remote, or in another city entirely</span>
          </span>
        </button>
      </div>
    </div>

    <!-- Q6: Language -->
    <div class="question-block" id="q6">
      <div class="question-number">Question 6 — Language</div>
      <h2 class="question-text">How is your Dutch?</h2>
      <p class="question-hint">English is widely spoken in the Netherlands, but it varies by city.</p>
      <div class="options-grid">
        <button class="option-btn" data-q="6" data-v="lang_english">
          <span class="option-check"></span>
          <span class="option-emoji">🇬🇧</span>
          <span class="option-label">
            English only — I don't speak Dutch
            <span class="option-sub">I need a city where I can handle daily life entirely in English</span>
          </span>
        </button>
        <button class="option-btn" data-q="6" data-v="lang_learning">
          <span class="option-check"></span>
          <span class="option-emoji">📚</span>
          <span class="option-label">
            I'm learning Dutch
            <span class="option-sub">Basic Dutch, happy to practice — but I still need English as backup</span>
          </span>
        </button>
        <button class="option-btn" data-q="6" data-v="lang_dutch">
          <span class="option-check"></span>
          <span class="option-emoji">🇳🇱</span>
          <span class="option-label">
            I speak Dutch (or I will soon)
            <span class="option-sub">Language isn't a limiting factor — smaller Dutch cities are fine</span>
          </span>
        </button>
      </div>
    </div>

    <!-- Q7: Vibe -->
    <div class="question-block" id="q7">
      <div class="question-number">Question 7 — Your Vibe</div>
      <h2 class="question-text">Which of these best describes you?</h2>
      <p class="question-hint">Last question — this one really narrows it down.</p>
      <div class="options-grid">
        <button class="option-btn" data-q="7" data-v="vibe_cosmopolitan">
          <span class="option-check"></span>
          <span class="option-emoji">🌆</span>
          <span class="option-label">
            Cosmopolitan and international
            <span class="option-sub">I want world-class museums, international restaurants, global connections</span>
          </span>
        </button>
        <button class="option-btn" data-q="7" data-v="vibe_creative">
          <span class="option-check"></span>
          <span class="option-emoji">🎨</span>
          <span class="option-label">
            Creative and alternative
            <span class="option-sub">Street art, architecture, start-up culture, and unconventional spaces</span>
          </span>
        </button>
        <button class="option-btn" data-q="7" data-v="vibe_academic">
          <span class="option-check"></span>
          <span class="option-emoji">🔬</span>
          <span class="option-label">
            Academic and intellectual
            <span class="option-sub">Bookshops, lectures, cycling to the library, thoughtful conversations</span>
          </span>
        </button>
        <button class="option-btn" data-q="7" data-v="vibe_relaxed">
          <span class="option-check"></span>
          <span class="option-emoji">☀️</span>
          <span class="option-label">
            Relaxed with a southern charm
            <span class="option-sub">Good food, slower pace, café terraces, Burgundian lifestyle</span>
          </span>
        </button>
        <button class="option-btn" data-q="7" data-v="vibe_practical">
          <span class="option-check"></span>
          <span class="option-emoji">⚡</span>
          <span class="option-label">
            Practical and no-nonsense
            <span class="option-sub">Good infrastructure, efficient city, easy cycling, get things done</span>
          </span>
        </button>
      </div>
    </div>

    <!-- Navigation -->
    <div class="quiz-nav">
      <button class="btn-back" id="btn-back" disabled>← Back</button>
      <button class="btn-next" id="btn-next" disabled>Next question →</button>
    </div>

  </div><!-- /quiz-card -->

  <!-- RESULTS -->
  <div id="quiz-results">
    <div class="quiz-card">
      <div class="results-header">
        <div class="results-celebrate">🎉</div>
        <h2 class="results-title" id="results-title">Your top Dutch cities</h2>
        <p class="results-sub" id="results-sub">Based on your answers, here are the cities that suit you best.</p>
      </div>
      <div id="results-list"></div>
    </div>

    <div class="share-card">
      <div class="share-title">Share your result</div>
      <p class="share-sub">Know someone else deciding where to live in the Netherlands? Send them the quiz.</p>
      <button class="btn-share" id="btn-share">📋 Copy &amp; Share Result</button>
      <button class="btn-retake" id="btn-retake">↩ Retake Quiz</button>
      <div class="share-copied" id="share-copied">✓ Copied to clipboard! Paste it anywhere.</div>
    </div>
  </div>

  <!-- ABOUT -->
  <div class="about-section">
    <h2>About This Quiz</h2>
    <p>This quiz was designed by the ExpatNetherlandsHub team to help expats moving to the Netherlands narrow down which city actually fits their life — not just the one they've heard of. We cover 18 Dutch cities across 7 key dimensions: budget, work, social life, nature, commute needs, language, and personal vibe.</p>
    <p>The Netherlands has a city for every type of expat. Budget-conscious students thrive in Groningen and Enschede. Tech professionals love Eindhoven and Delft. Amsterdam is the obvious international choice, but Rotterdam, Utrecht, and Haarlem often turn out to be better fits for people who want real quality of life without the Amsterdam price tag.</p>
    <p>Explore all 18 cities we cover:</p>
    <div class="cities-grid">
      <a class="city-chip" href="/cities/amsterdam/">Amsterdam</a>
      <a class="city-chip" href="/cities/rotterdam/">Rotterdam</a>
      <a class="city-chip" href="/cities/the-hague/">Den Haag</a>
      <a class="city-chip" href="/cities/utrecht/">Utrecht</a>
      <a class="city-chip" href="/cities/eindhoven/">Eindhoven</a>
      <a class="city-chip" href="/cities/groningen/">Groningen</a>
      <a class="city-chip" href="/cities/haarlem/">Haarlem</a>
      <a class="city-chip" href="/cities/leiden/">Leiden</a>
      <a class="city-chip" href="/cities/maastricht/">Maastricht</a>
      <a class="city-chip" href="/cities/delft/">Delft</a>
      <a class="city-chip" href="/cities/breda/">Breda</a>
      <a class="city-chip" href="/cities/den-bosch/">Den Bosch</a>
      <a class="city-chip" href="/cities/nijmegen/">Nijmegen</a>
      <a class="city-chip" href="/cities/tilburg/">Tilburg</a>
      <a class="city-chip" href="/cities/almere/">Almere</a>
      <a class="city-chip" href="/cities/arnhem/">Arnhem</a>
      <a class="city-chip" href="/cities/amstelveen/">Amstelveen</a>
      <a class="city-chip" href="/cities/enschede/">Enschede</a>
    </div>
  </div>

</div><!-- /quiz-body -->

<script>
(function () {
  'use strict';

  /* ============================================================
    CITY DATA
  ============================================================ */
  const CITIES = {
    amsterdam: {
      name: 'Amsterdam',
      tagline: 'The international capital — buzzing, global, and endlessly diverse',
      facts: ['Best English support', 'Huge expat community', 'Top cultural scene', 'Highest rents'],
      citySlug: 'amsterdam',
      movingSlug: 'moving-to-amsterdam-guide-2026',
    },
    rotterdam: {
      name: 'Rotterdam',
      tagline: 'Bold, modern, and creative — the city that reinvented itself',
      facts: ['Lower rents than Amsterdam', 'Amazing architecture', 'Strong harbour culture', 'Great nightlife'],
      citySlug: 'rotterdam',
      movingSlug: 'moving-to-rotterdam-guide-2026',
    },
    denhaag: {
      name: 'Den Haag',
      tagline: 'Diplomatic hub with beaches — international yet surprisingly affordable',
      facts: ['Many embassies & NGOs', 'Beach 10 min away', 'Strong English support', 'The Hague International School'],
      citySlug: 'the-hague',
      movingSlug: 'moving-to-the-hague-guide-2026',
    },
    utrecht: {
      name: 'Utrecht',
      tagline: 'The perfect Dutch city — central, manageable, and wonderfully liveable',
      facts: ['Central location', 'Strong job market', 'University city', 'Family-friendly'],
      citySlug: 'utrecht',
      movingSlug: 'moving-to-utrecht-guide-2026',
    },
    eindhoven: {
      name: 'Eindhoven',
      tagline: 'Design and tech capital — ASML, Philips, and an international spirit',
      facts: ['Top tech ecosystem', 'Surprising English support', 'Affordable rents', 'Design scene'],
      citySlug: 'eindhoven',
      movingSlug: 'moving-to-eindhoven-guide-2026',
    },
    groningen: {
      name: 'Groningen',
      tagline: 'The student city of the north — young, vibrant, and very affordable',
      facts: ['Cheapest rents', 'Huge student population', 'Excellent nightlife', 'Strong cycling culture'],
      citySlug: 'groningen',
      movingSlug: 'moving-to-groningen-guide-2026',
    },
    haarlem: {
      name: 'Haarlem',
      tagline: 'Amsterdam\'s charming neighbour — canals, beach, and quick train access',
      facts: ['15 min to Amsterdam', 'Beach nearby', 'Beautiful old city', 'Family favourite'],
      citySlug: 'haarlem',
      movingSlug: 'moving-to-haarlem-guide-2026',
    },
    leiden: {
      name: 'Leiden',
      tagline: 'Historic university city — academic, compact, and close to Amsterdam and Den Haag',
      facts: ['Oldest Dutch university', 'Great location', 'Charming canals', 'Research hub'],
      citySlug: 'leiden',
      movingSlug: 'moving-to-leiden-expat-guide-2026',
    },
    maastricht: {
      name: 'Maastricht',
      tagline: 'Southern charm — Burgundian lifestyle, architecture, and European flair',
      facts: ['Warmest weather', 'Café culture', 'Belgium/Germany day trips', 'Art & history'],
      citySlug: 'maastricht',
      movingSlug: 'moving-to-maastricht-expat-guide-2026',
    },
    delft: {
      name: 'Delft',
      tagline: 'Compact, beautiful, and home to the Netherlands\' top technical university',
      facts: ['TU Delft campus', 'Picture-perfect canals', '10 min to Den Haag', 'Engineering hub'],
      citySlug: 'delft',
      movingSlug: 'moving-to-delft-guide-2026',
    },
    breda: {
      name: 'Breda',
      tagline: 'Southern warmth with a laid-back energy and growing creative scene',
      facts: ['Relaxed atmosphere', 'Good rents', 'Accessible south', 'Café culture'],
      citySlug: 'breda',
      movingSlug: 'moving-to-breda-guide-2026',
    },
    denbosch: {
      name: '\'s-Hertogenbosch (Den Bosch)',
      tagline: 'Charming medieval city with a love of good food and the easy southern life',
      facts: ['Bourgondische sfeer', 'Carnival capital', 'Affordable', 'Beautiful centre'],
      citySlug: 'den-bosch',
      movingSlug: 'moving-to-den-bosch-guide-2026',
    },
    nijmegen: {
      name: 'Nijmegen',
      tagline: 'Oldest city in the Netherlands — academic, green, and underrated',
      facts: ['Radboud University', 'Hilly terrain (unique!)', 'Affordable', 'Lively student scene'],
      citySlug: 'nijmegen',
      movingSlug: 'moving-to-nijmegen-guide-2026',
    },
    tilburg: {
      name: 'Tilburg',
      tagline: 'Unpretentious, affordable, and growing fast — a hidden gem of the south',
      facts: ['Very affordable rents', 'Strong music scene', 'Tilburg University', 'Growing city'],
      citySlug: 'tilburg',
      movingSlug: 'moving-to-tilburg-guide-2026',
    },
    almere: {
      name: 'Almere',
      tagline: 'Modern and affordable — just 20 minutes from Amsterdam by train',
      facts: ['20 min to Amsterdam', 'Newest Dutch city', 'Very affordable', 'Family-friendly'],
      citySlug: 'almere',
      movingSlug: null,
    },
    arnhem: {
      name: 'Arnhem',
      tagline: 'Green and culturally rich — gateway to the Veluwe nature reserve',
      facts: ['Veluwe on the doorstep', 'Fashion industry hub', 'Affordable', 'Green city'],
      citySlug: 'arnhem',
      movingSlug: 'moving-to-arnhem-guide-2026',
    },
    amstelveen: {
      name: 'Amstelveen',
      tagline: 'Suburban Amsterdam with great schools and the largest Japanese community in NL',
      facts: ['15 min to Amsterdam', 'Top international schools', 'Green & quiet', 'Family favourite'],
      citySlug: 'amstelveen',
      movingSlug: null,
    },
    enschede: {
      name: 'Enschede',
      tagline: 'University of Twente city — affordable, green, and close to Germany',
      facts: ['Lowest rents in NL', 'University of Twente', 'Near Germany', 'Lots of nature'],
      citySlug: 'enschede',
      movingSlug: 'moving-to-enschede-guide-2026',
    },
  };

  /* ============================================================
    SCORING RULES
    Each answer adds points to specific city keys.
  ============================================================ */
  const SCORING = {
    // Q1 — Budget
    budget_low: {
      groningen: 5, enschede: 5, tilburg: 4, nijmegen: 3, arnhem: 3,
      almere: 2, breda: 2, denbosch: 2,
    },
    budget_mid: {
      rotterdam: 5, utrecht: 5, eindhoven: 5, nijmegen: 4, arnhem: 4,
      tilburg: 4, groningen: 3, leiden: 3, delft: 3, breda: 3,
      denbosch: 3, almere: 4,
    },
    budget_high: {
      amsterdam: 4, denhaag: 5, haarlem: 4, leiden: 3, delft: 3,
      rotterdam: 3, utrecht: 4, amstelveen: 3,
    },
    budget_top: {
      amsterdam: 5, denhaag: 4, haarlem: 3, amstelveen: 2,
    },

    // Q2 — Work style
    work_office: {
      amsterdam: 5, rotterdam: 4, denhaag: 4, utrecht: 3,
    },
    work_tech: {
      eindhoven: 6, delft: 5, amsterdam: 3, rotterdam: 2, utrecht: 2,
    },
    work_remote: {
      groningen: 3, enschede: 3, tilburg: 3, nijmegen: 3, arnhem: 3,
      maastricht: 3, breda: 3, denbosch: 3, leiden: 2, delft: 2,
      haarlem: 2, almere: 2,
    },
    work_academia: {
      leiden: 6, delft: 5, groningen: 5, nijmegen: 5, enschede: 4,
      utrecht: 3, amsterdam: 2, eindhoven: 3,
    },

    // Q3 — Social life
    social_international: {
      amsterdam: 6, denhaag: 5, eindhoven: 4, rotterdam: 3, leiden: 2, delft: 2,
    },
    social_gezellig: {
      maastricht: 6, nijmegen: 5, haarlem: 5, tilburg: 4, denbosch: 4,
      breda: 4, leiden: 3, groningen: 3, arnhem: 3,
    },
    social_nightlife: {
      amsterdam: 6, rotterdam: 5, groningen: 5, utrecht: 3, eindhoven: 2,
    },
    social_family: {
      amstelveen: 6, haarlem: 5, utrecht: 5, almere: 4, leiden: 4,
      delft: 3, breda: 3,
    },

    // Q4 — Nature
    nature_high: {
      arnhem: 6, maastricht: 5, haarlem: 4, nijmegen: 4, groningen: 3,
      enschede: 4, breda: 3, denbosch: 3, leiden: 3,
    },
    nature_mid: {
      utrecht: 4, leiden: 4, delft: 4, amstelveen: 3, almere: 3,
      tilburg: 3, rotterdam: 2, groningen: 2,
    },
    nature_low: {
      amsterdam: 4, rotterdam: 4, denhaag: 3, eindhoven: 2,
    },

    // Q5 — Commute
    commute_daily: {
      haarlem: 6, amstelveen: 6, utrecht: 5, almere: 5,
    },
    commute_sometimes: {
      leiden: 5, delft: 5, rotterdam: 4, denhaag: 4, haarlem: 3,
    },
    commute_no: {
      groningen: 2, enschede: 2, maastricht: 2, tilburg: 2, eindhoven: 2,
      arnhem: 2, nijmegen: 2, breda: 2, denbosch: 2,
    },

    // Q6 — Language
    lang_english: {
      amsterdam: 5, denhaag: 4, eindhoven: 4, rotterdam: 3, leiden: 2,
      delft: 2, haarlem: 2, amstelveen: 3,
    },
    lang_learning: {
      amsterdam: 3, denhaag: 3, eindhoven: 3, rotterdam: 3, utrecht: 3,
      groningen: 2, haarlem: 2, leiden: 2,
    },
    lang_dutch: {
      groningen: 2, enschede: 2, tilburg: 2, nijmegen: 2, arnhem: 2,
      maastricht: 2, breda: 2, denbosch: 2, almere: 2,
    },

    // Q7 — Vibe
    vibe_cosmopolitan: {
      amsterdam: 6, denhaag: 4, rotterdam: 3, leiden: 2,
    },
    vibe_creative: {
      rotterdam: 6, amsterdam: 4, arnhem: 4, tilburg: 3, eindhoven: 3,
      nijmegen: 2,
    },
    vibe_academic: {
      leiden: 6, delft: 6, groningen: 5, nijmegen: 5, enschede: 4,
      utrecht: 3, amsterdam: 2,
    },
    vibe_relaxed: {
      maastricht: 6, denbosch: 5, breda: 5, nijmegen: 4, arnhem: 3,
      tilburg: 3,
    },
    vibe_practical: {
      utrecht: 6, eindhoven: 5, almere: 4, rotterdam: 3, haarlem: 3,
      amstelveen: 3,
    },
  };

  /* ============================================================
    "WHY" REASON GENERATOR
    Returns a personalised reason string based on answers.
  ============================================================ */
  function generateWhy(cityKey, answers) {
    const city = CITIES[cityKey];
    const reasons = [];
    const v = answers; // {1: 'budget_mid', 2: 'work_tech', ...}

    // Budget reason
    if (v[1] === 'budget_low' && ['groningen','enschede','tilburg','nijmegen'].includes(cityKey)) {
      reasons.push('rents here are among the lowest in the Netherlands, making your budget go much further');
    } else if (v[1] === 'budget_top' && cityKey === 'amsterdam') {
      reasons.push('with your budget, you can live well in central Amsterdam without compromise');
    } else if (v[1] === 'budget_mid' && ['rotterdam','utrecht','eindhoven'].includes(cityKey)) {
      reasons.push('your budget fits comfortably here — a proper apartment is achievable');
    }

    // Work reason
    if (v[2] === 'work_tech' && ['eindhoven','delft'].includes(cityKey)) {
      reasons.push(cityKey === 'eindhoven'
        ? 'Eindhoven is the Netherlands\' tech and innovation capital — ASML, Philips, and hundreds of startups are based here'
        : 'Delft is home to TU Delft and a dense cluster of engineering and tech companies');
    }
    if (v[2] === 'work_academia' && ['leiden','delft','groningen','nijmegen','enschede'].includes(cityKey)) {
      reasons.push('the university here is one of the best in the Netherlands for your field');
    }
    if (v[2] === 'work_office' && ['amsterdam','rotterdam','denhaag'].includes(cityKey)) {
      reasons.push('major corporate employers, law firms, and financial institutions are based here');
    }
    if (v[2] === 'work_remote') {
      reasons.push('as a remote worker, you benefit from lower rents and a higher quality of life here without sacrificing connectivity');
    }

    // Social reason
    if (v[3] === 'social_international' && ['amsterdam','denhaag','eindhoven'].includes(cityKey)) {
      reasons.push('the expat and international community here is huge — making friends and feeling at home is noticeably easier');
    }
    if (v[3] === 'social_gezellig' && ['maastricht','nijmegen','haarlem','tilburg'].includes(cityKey)) {
      reasons.push('this city has exactly the cozy, neighbourhood-feel Dutch culture that makes expats fall in love with the Netherlands');
    }
    if (v[3] === 'social_nightlife' && ['amsterdam','rotterdam','groningen'].includes(cityKey)) {
      reasons.push('the nightlife and cultural events scene here is genuinely excellent by Dutch standards');
    }
    if (v[3] === 'social_family' && ['amstelveen','haarlem','utrecht','almere'].includes(cityKey)) {
      reasons.push('international families consistently rate this city very highly for schools, safety, and family life');
    }

    // Nature reason
    if (v[4] === 'nature_high' && ['arnhem','maastricht','haarlem','nijmegen'].includes(cityKey)) {
      reasons.push(cityKey === 'arnhem'
        ? 'the Veluwe — the Netherlands\' largest nature reserve — starts right on the city\'s edge'
        : cityKey === 'maastricht'
        ? 'the Limburg hills and river landscapes around Maastricht are genuinely beautiful and unique in the Netherlands'
        : cityKey === 'haarlem'
        ? 'the North Sea beach is a 15-minute bike ride from the centre'
        : 'Nijmegen has unusual hills for the Netherlands and borders the Gelderse Poort nature area');
    }

    // Commute reason
    if (v[5] === 'commute_daily' && ['haarlem','amstelveen','utrecht','almere'].includes(cityKey)) {
      reasons.push(cityKey === 'haarlem' || cityKey === 'amstelveen'
        ? 'you\'re within 15–20 minutes of Amsterdam Centraal by train or metro — a very easy daily commute'
        : cityKey === 'utrecht'
        ? 'Utrecht Centraal is just 26 minutes from Amsterdam — one of the best commuter connections in the country'
        : 'Almere is only 20 minutes from Amsterdam by train, and rents are dramatically lower');
    }

    // Language reason
    if (v[6] === 'lang_english' && ['amsterdam','denhaag','eindhoven'].includes(cityKey)) {
      reasons.push('English is genuinely a first language here — you can open a bank account, see a doctor, and do your shopping entirely in English without any difficulty');
    }

    // Vibe reason
    if (v[7] === 'vibe_cosmopolitan' && cityKey === 'amsterdam') {
      reasons.push('Amsterdam is one of the most international cities in Europe — world-class museums, Michelin-starred restaurants, and a genuinely global social scene');
    }
    if (v[7] === 'vibe_creative' && cityKey === 'rotterdam') {
      reasons.push('Rotterdam is the most architecturally adventurous city in the Netherlands, with a world-renowned design scene and an anything-goes creative energy');
    }
    if (v[7] === 'vibe_relaxed' && ['maastricht','denbosch','breda'].includes(cityKey)) {
      reasons.push('the Burgundian lifestyle here — long café lunches, great food, easy pace — is unlike anything you\'ll find in the Randstad');
    }
    if (v[7] === 'vibe_practical' && cityKey === 'utrecht') {
      reasons.push('Utrecht is the most efficiently designed major Dutch city — everything works, the cycling infrastructure is superb, and almost nothing is unnecessarily complicated');
    }

    // Fallback if we have no reasons
    if (reasons.length === 0) {
      reasons.push('your combination of priorities aligns well with what this city has to offer');
    }

    // Build sentence
    const name = city.name;
    const combined = reasons.slice(0, 2).join(', and ');
    return `<strong>${name}</strong> suits you because ${combined}.`;
  }

  /* ============================================================
    QUIZ STATE
  ============================================================ */
  let currentQ = 1;
  const TOTAL_Q = 7;
  const answers = {};

  /* ============================================================
    DOM REFS
  ============================================================ */
  const progressBar   = document.getElementById('progress-bar');
  const progressCount = document.getElementById('progress-count');
  const btnBack       = document.getElementById('btn-back');
  const btnNext       = document.getElementById('btn-next');
  const quizContainer = document.getElementById('quiz-container');
  const quizResults   = document.getElementById('quiz-results');
  const resultsList   = document.getElementById('results-list');
  const btnShare      = document.getElementById('btn-share');
  const btnRetake     = document.getElementById('btn-retake');
  const shareCopied   = document.getElementById('share-copied');

  /* ============================================================
    OPTION CLICK HANDLER
  ============================================================ */
  document.querySelectorAll('.option-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const q = this.dataset.q;
      const v = this.dataset.v;

      // Deselect siblings
      document.querySelectorAll('.option-btn[data-q="' + q + '"]').forEach(function (b) {
        b.classList.remove('selected');
      });

      // Select this one
      this.classList.add('selected');
      answers[parseInt(q, 10)] = v;

      // Enable next
      btnNext.disabled = false;

      // Auto-advance after short delay for better UX
      setTimeout(function () {
        if (answers[parseInt(q, 10)] === v) {
          handleNext();
        }
      }, 350);
    });
  });

  /* ============================================================
    NAVIGATION
  ============================================================ */
  btnNext.addEventListener('click', handleNext);
  btnBack.addEventListener('click', handleBack);

  function handleNext() {
    if (!answers[currentQ]) return;

    if (currentQ < TOTAL_Q) {
      goToQuestion(currentQ + 1);
    } else {
      showResults();
    }
  }

  function handleBack() {
    if (currentQ > 1) {
      goToQuestion(currentQ - 1);
    }
  }

  function goToQuestion(n) {
    document.getElementById('q' + currentQ).classList.remove('active');
    currentQ = n;
    document.getElementById('q' + currentQ).classList.add('active');
    updateProgress();
    updateNav();
  }

  function updateProgress() {
    var pct = Math.round((currentQ / TOTAL_Q) * 100);
    progressBar.style.width = pct + '%';
    progressCount.textContent = 'Question ' + currentQ + ' of ' + TOTAL_Q;
  }

  function updateNav() {
    btnBack.disabled = (currentQ === 1);
    btnNext.disabled = !answers[currentQ];

    if (currentQ === TOTAL_Q) {
      btnNext.textContent = answers[currentQ] ? 'See My Results →' : 'See My Results →';
    } else {
      btnNext.textContent = 'Next question →';
    }
  }

  /* ============================================================
    CALCULATE SCORES
  ============================================================ */
  function calculateScores() {
    var scores = {};

    // Initialise all cities
    Object.keys(CITIES).forEach(function (key) {
      scores[key] = 0;
    });

    // Add points for each answer
    Object.keys(answers).forEach(function (q) {
      var val = answers[q];
      if (SCORING[val]) {
        Object.keys(SCORING[val]).forEach(function (city) {
          scores[city] = (scores[city] || 0) + SCORING[val][city];
        });
      }
    });

    return scores;
  }

  function getTopCities(scores, n) {
    return Object.keys(scores)
      .sort(function (a, b) { return scores[b] - scores[a]; })
      .slice(0, n);
  }

  /* ============================================================
    SHOW RESULTS
  ============================================================ */
  function showResults() {
    progressBar.style.width = '100%';
    progressCount.textContent = 'Complete!';

    var scores = calculateScores();
    var top = getTopCities(scores, 3);
    var maxScore = scores[top[0]] || 1;

    // Update heading
    var winner = CITIES[top[0]];
    document.getElementById('results-title').textContent =
      'Your #1 match: ' + winner.name + '!';
    document.getElementById('results-sub').textContent =
      'Here are your top 3 Dutch cities based on your answers.';

    // Build result cards
    var html = '';
    var rankLabels = ['1', '2', '3'];

    top.forEach(function (cityKey, i) {
      var city = CITIES[cityKey];
      var score = scores[cityKey];
      var pct = Math.round((score / maxScore) * 100);
      var rank = i + 1;

      var factsHtml = city.facts.map(function (f) {
        return '<span class="city-fact-tag">✓ ' + f + '</span>';
      }).join('');

      var cityUrl = '/cities/' + city.citySlug + '/';
      var movingUrl = city.movingSlug
        ? '/guides/housing/' + city.movingSlug + '/'
        : null;

      var linksHtml = '<a class="city-link-btn primary" href="' + cityUrl + '">Explore ' + city.name + ' →</a>';
      if (movingUrl) {
        linksHtml += '<a class="city-link-btn secondary" href="' + movingUrl + '">Moving guide</a>';
      }

      var whyText = generateWhy(cityKey, answers);

      html += '<div class="city-result rank-' + rank + '">'
        + '<div class="city-result-header">'
        + '<div class="city-rank-badge">' + rankLabels[i] + '</div>'
        + '<div>'
        + '<div class="city-result-name">' + city.name + '</div>'
        + '<div class="city-result-tagline">' + city.tagline + '</div>'
        + '</div>'
        + '<div class="city-match-score">'
        + '<div class="city-match-pct">' + pct + '%</div>'
        + '<div class="city-match-label">match</div>'
        + '</div>'
        + '</div>'
        + '<div class="city-result-body">'
        + '<p class="city-why">' + whyText + '</p>'
        + '<div class="city-quick-facts">' + factsHtml + '</div>'
        + '<div class="city-links">' + linksHtml + '</div>'
        + '</div>'
        + '</div>';
    });

    resultsList.innerHTML = html;

    // Hide quiz card, show results
    quizContainer.style.display = 'none';
    quizResults.style.display = 'block';

    // Scroll to top of results
    quizResults.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  /* ============================================================
    SHARE
  ============================================================ */
  btnShare.addEventListener('click', function () {
    var scores = calculateScores();
    var top = getTopCities(scores, 1);
    var winnerName = CITIES[top[0]].name;
    var text = 'I took the ExpatNetherlandsHub city quiz and got ' + winnerName + '! \uD83C\uDDF3\uD83C\uDDF1 Which Dutch city is right for YOU? Take it: https://expatnetherlandshub.com/tools/city-quiz/';

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        showCopied();
      }).catch(function () {
        fallbackCopy(text);
      });
    } else {
      fallbackCopy(text);
    }
  });

  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    try { document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
    showCopied();
  }

  function showCopied() {
    shareCopied.classList.add('visible');
    btnShare.textContent = '✓ Copied!';
    setTimeout(function () {
      shareCopied.classList.remove('visible');
      btnShare.innerHTML = '\uD83D\uDCCB Copy &amp; Share Result';
    }, 3000);
  }

  /* ============================================================
    RETAKE
  ============================================================ */
  btnRetake.addEventListener('click', function () {
    // Reset state
    Object.keys(answers).forEach(function (k) { delete answers[k]; });
    currentQ = 1;

    // Deselect all options
    document.querySelectorAll('.option-btn').forEach(function (b) {
      b.classList.remove('selected');
    });

    // Reset UI
    progressBar.style.width = '14%';
    progressCount.textContent = 'Question 1 of 7';
    btnBack.disabled = true;
    btnNext.disabled = true;
    btnNext.textContent = 'Next question →';

    // Show question 1
    document.querySelectorAll('.question-block').forEach(function (b) {
      b.classList.remove('active');
    });
    document.getElementById('q1').classList.add('active');

    // Swap views
    quizResults.style.display = 'none';
    quizContainer.style.display = 'block';

    // Scroll to top
    quizContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

})();
</script>

<h2>Related Guides</h2>
<ul>
  <li><a href="/guides/housing/best-cities-netherlands-expats-2026/">Best Cities for Expats in the Netherlands</a> — detailed comparison of all major Dutch cities for international residents</li>
  <li><a href="/guides/housing/finding-housing-netherlands-expats-2026/">Finding Housing in the Netherlands</a> — practical guide to the Dutch rental and buying market</li>
  <li><a href="/guides/housing/cost-of-living-netherlands-2026/">Cost of Living in the Netherlands</a> — what to expect for rent, groceries, transport, and more</li>
</ul>
