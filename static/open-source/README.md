# Dutch Tax Calculator 2026 🇳🇱

Free, open-source Python calculator for Dutch income tax (Box 1).
Built for expats and locals by [ExpatNetherlandsHub.com](https://expatnetherlandshub.com).

---

## Features

- **2026 tax brackets** — 36.97% and 49.50% (Box 1)
- **30% ruling support** — flat 30% exemption across the 60-month period, with the Balkenendenorm salary cap applied
- **Algemene heffingskorting** — general tax credit with phase-out
- **Arbeidskorting** — employment tax credit with build-up and phase-out
- **ZVW bijdrage** — health insurance contribution (5.32%, capped at €71,628)
- **Vakantiegeld** — 8% holiday allowance correctly handled in gross/net split
- Clean dataclass output with a formatted summary
- CLI interface — pipe it into scripts or use interactively

---

## Quick Start

**No dependencies. Requires Python 3.10+.**

```bash
# Run the built-in demo (5 representative salary levels)
python dutch-tax-calculator.py

# Single salary calculation
python dutch-tax-calculator.py 60000

# With the 30% ruling
python dutch-tax-calculator.py 80000 --ruling

# 30% ruling, 20 months already used (same 30% rate — no step-down exists)
python dutch-tax-calculator.py 80000 --ruling --ruling-months 20

# Full options
python dutch-tax-calculator.py 90000 --ruling --ruling-months 0 --age 34
```

---

## Example Output

```
==================================================
  Dutch Income Tax 2026 — Calculation Summary
==================================================
  Gross annual salary:     €  60,000.00
  of which vakantiegeld:   €   4,444.44  (8%)
  Taxable income (Box 1):  €  60,000.00

  ── Box 1 Tax ──────────────────────────────
  Bracket 1 (36.97%):      €  22,182.00
  Bracket 2 (49.50%):      €       0.00
  Gross tax:               €  22,182.00

  ── Tax Credits ────────────────────────────
  Alg. heffingskorting:    €   1,210.18
  Arbeidskorting:          €   4,225.00
  Total credits:           €   5,435.18

  ── Deductions ─────────────────────────────
  Net income tax:          €  16,746.82
  ZVW bijdrage (5.32%):    €   3,192.00
  Total deductions:        €  19,938.82

  ── Net Salary ─────────────────────────────
  Net annual:              €  40,061.18
  Net monthly:             €   3,338.43

  Effective tax rate:            27.9%
  Effective total rate:          33.2%
==================================================
```

---

## Use as a Library

```python
from dutch_tax_calculator import calculate_dutch_tax

# Basic calculation
result = calculate_dutch_tax(60_000)
print(f"Net monthly: €{result.net_monthly:,.2f}")

# With the 30% ruling
result = calculate_dutch_tax(
    gross_annual=90_000,
    has_30_percent_ruling=True,
    ruling_months_elapsed=0,
    age=32,
)
print(result.summary())

# Access individual fields
print(f"Income tax:        €{result.net_tax:,.2f}")
print(f"ZVW bijdrage:      €{result.zvw_bijdrage:,.2f}")
print(f"Heffingskorting:   €{result.algemene_heffingskorting:,.2f}")
print(f"Arbeidskorting:    €{result.arbeidskorting:,.2f}")
print(f"Effective rate:    {result.effective_total_rate * 100:.1f}%")
```

---

## API Reference

### `calculate_dutch_tax(gross_annual, ...)`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `gross_annual` | `float` | required | Annual gross salary in EUR (including vakantiegeld by default) |
| `has_30_percent_ruling` | `bool` | `False` | Whether the 30% ruling applies |
| `ruling_months_elapsed` | `int` | `0` | Months already used in the 60-month period (the rate is a flat 30% throughout; past 60 the ruling has expired) |
| `age` | `int` | `35` | Employee age |
| `vakantiegeld_included` | `bool` | `True` | If `False`, 8% vakantiegeld is added on top of `gross_annual` |

Returns a `TaxResult` dataclass. Call `.summary()` for formatted output.

### `TaxResult` fields

| Field | Description |
|-------|-------------|
| `gross_annual` | Annual gross salary (including vakantiegeld) |
| `vakantiegeld` | 8% holiday allowance component |
| `taxable_income` | Gross minus 30% ruling exemption |
| `gross_tax` | Box 1 tax before credits |
| `algemene_heffingskorting` | General tax credit applied |
| `arbeidskorting` | Employment tax credit applied |
| `net_tax` | Final income tax after credits |
| `zvw_bijdrage` | ZVW health contribution |
| `net_annual` | Take-home annual salary |
| `net_monthly` | Take-home monthly salary |
| `effective_tax_rate` | `net_tax / gross_annual` |
| `effective_total_rate` | `(net_tax + zvw) / gross_annual` |

---

## 30% Ruling Percentage

The tax-free reimbursement is a **flat 30% of gross salary for every month** of the
60-month period in 2025 and 2026. The 30/20/10 step-down that was legislated in the
2024 Tax Plan was repealed in the 2025 Tax Plan before it ever took effect, so it is
not part of Dutch law and this calculator does not model it.

| Period | Months elapsed | Tax-free fraction |
|--------|---------------|-------------------|
| Ruling running (2025–2026) | 0–60 months | 30% of gross |
| Ruling expired | over 60 months | 0% |

Two further rules are relevant:

- **From 1 January 2027** the maximum drops to **27%**, unless the ruling was already
  being applied to the salary on or before 31 December 2023 (transitional protection
  at 30%). Rulings first applied in 2024 move to 27% on the current salary norm;
  rulings first applied from 2025 move to 27% under a higher salary norm.
- **Salary cap (Balkenendenorm, 2026):** the allowance is calculated on salary up to
  €262,000, so the tax-free amount never exceeds €78,600 per year.

Use `--ruling-months` on the CLI or `ruling_months_elapsed` in the API to model where
you are in the 60-month period (it determines whether the ruling still applies at all).

---

## Limitations & Disclaimer

This calculator covers the most common scenario: an **employee receiving a standard
Dutch employment salary**. It does **not** cover:

- Box 2 (substantial interest) or Box 3 (savings/investments)
- Self-employed / ZZP deductions (zelfstandigenaftrek, MKB-winstvrijstelling)
- Pension contributions (pre-tax)
- Partner/toeslagen (rent, childcare, healthcare allowances)
- AOW exemption for people over 67
- Inkomensafhankelijke bijdrage ZVW for DGA

**Always verify with a Dutch tax advisor (belastingadviseur) or the Belastingdienst
for your personal situation.**

---

## Full Online Version

For an interactive calculator with more features, visit:

**[ExpatNetherlandsHub Salary Calculator](https://expatnetherlandshub.com/tools/salary-checker/)**

---

## Other Free Expat Tools

- [30% Ruling Calculator](https://expatnetherlandshub.com/tools/30-percent-ruling-calculator/)
- [Cost of Living Calculator](https://expatnetherlandshub.com/tools/cost-of-living-calculator/)
- [Health Insurance Comparison](https://expatnetherlandshub.com/tools/health-insurance-wizard/)

All tools are free. No signup required.

---

## Contributing

Pull requests welcome. Please keep the constants in sync with the official
[Belastingdienst tarievenoverzicht](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/overzicht_tarieven_en_schijven/).

If you add features (Box 3, toeslagen, pension), open a PR — contributions
are merged under MIT.

---

## License

MIT License — free to use, modify, and distribute.

Attribution to [ExpatNetherlandsHub.com](https://expatnetherlandshub.com) is appreciated
but not required.

---

*Tax rates current as of March 2026. Maintained by [ExpatNetherlandsHub.com](https://expatnetherlandshub.com).*
