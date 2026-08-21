---
title: "Open Source: Dutch Tax Calculator 2026 (Python)"
description: "Free, open-source Python calculator for Dutch income tax (Box 1) with 30% ruling, tax credits and holiday allowance. No dependencies, MIT-style free use."
date: 2026-08-21
lastmod: 2026-08-21
url: /open-source/
affiliate: false
---

> **Quick answer:** we publish a free, open-source **Dutch income tax calculator** in Python — 2026 brackets, 30% ruling with the salary cap, general and employment tax credits, ZVW contribution and holiday allowance. No dependencies, Python 3.10+. Download it below, use and modify it freely; a link back to this site is appreciated.

## Download

- **[dutch-tax-calculator.py](/open-source/dutch-tax-calculator.py)** — the calculator (single file, no dependencies)
- **[README.md](/open-source/README.md)** — features, quick start and examples

## What it calculates

The calculator covers Box 1 income tax for 2026: the 36.97% and 49.50% brackets, the **30% ruling** (flat exemption across the 60-month period, Balkenendenorm cap applied), *algemene heffingskorting* and *arbeidskorting* with their phase-outs, the ZVW health-insurance contribution and the 8% *vakantiegeld* gross/net split. Output is a clean summary you can pipe into scripts.

```bash
# Run the built-in demo (5 salary levels)
python dutch-tax-calculator.py

# Single salary
python dutch-tax-calculator.py 60000
```

Prefer a no-code version? The same logic powers our [salary checker](/tools/salary-checker/) and the [salary comparison tool](/salary-comparison/).

## License and attribution

Free to use, modify and distribute — commercially too. Attribution is appreciated: a link to expatnetherlandshub.com. Tax rates and thresholds are current as of March 2026; always verify against the [Belastingdienst](https://www.belastingdienst.nl/) for decisions that matter.

*No rights can be derived from this calculator or its output.*
