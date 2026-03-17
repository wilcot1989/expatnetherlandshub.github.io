"""
Dutch Income Tax Calculator 2026
================================
Open source by ExpatNetherlandsHub.com
https://expatnetherlandshub.com/tools/salary-checker/

Free to use, modify, and distribute.
Attribution appreciated: link to https://expatnetherlandshub.com

Tax brackets, rates, and deductions current as of March 2026.
"""

# ─────────────────────────────────────────────────────────────────────────────
# Dutch Income Tax Calculator 2026
# For expats and everyone else working in the Netherlands.
#
# GitHub: https://github.com/wilcot1989/dutch-tax-calculator
# Maintained by: ExpatNetherlandsHub.com
# ─────────────────────────────────────────────────────────────────────────────

from dataclasses import dataclass, field
from typing import Optional


# ─────────────────────────────────────────────────────────────────────────────
# 2026 Tax Constants
# Source: Belastingdienst (https://www.belastingdienst.nl)
# ─────────────────────────────────────────────────────────────────────────────

# Box 1 income tax brackets (loonbelasting / inkomstenbelasting Box 1)
TAX_BRACKET_1_RATE = 0.3697       # 36.97% on income up to the threshold
TAX_BRACKET_2_RATE = 0.4950       # 49.50% on income above the threshold
TAX_BRACKET_THRESHOLD = 76_817    # EUR — top of the first bracket

# Algemene heffingskorting (general tax credit)
# The maximum applies to income up to AHK_PHASE_IN_END.
# Above AHK_PHASE_OUT_START it is reduced at AHK_PHASE_OUT_RATE per EUR.
AHK_MAX = 3_362                   # EUR — maximum credit
AHK_PHASE_OUT_START = 24_813      # EUR — reduction starts above this income
AHK_PHASE_OUT_RATE = 0.06095      # 6.095% per EUR above phase-out start
AHK_MIN = 0                       # Credit cannot go below zero

# Arbeidskorting (employment tax credit)
# Builds up in two phases, then phases out above ARBKORTING_PHASE_OUT_START.
ARBKORTING_PHASE1_END = 10_741    # EUR
ARBKORTING_PHASE1_RATE = 0.08425  # 8.425%
ARBKORTING_PHASE2_END = 23_201    # EUR
ARBKORTING_PHASE2_RATE = 0.29861  # 29.861% on additional income in phase 2
ARBKORTING_MAX = 5_532            # EUR — maximum credit (reached at ~€39,958)
ARBKORTING_PHASE_OUT_START = 39_958
ARBKORTING_PHASE_OUT_RATE = 0.0651  # 6.51% per EUR above phase-out start
ARBKORTING_MIN = 0

# Zvw (Zorgverzekeringswet) — health insurance contribution paid by employer
# but relevant for self-employed / DGA; included here for completeness.
ZVW_RATE = 0.0532                 # 5.32%
ZVW_MAX_BASE = 71_628             # EUR — maximum grondslag

# Vakantiegeld (holiday allowance)
VAKANTIEGELD_RATE = 0.08          # 8% of gross annual salary (statutory minimum)

# ─────────────────────────────────────────────────────────────────────────────
# 30% Ruling Phase-Down
# Introduced 2024; the tax-free portion steps down over the 5-year period.
# ─────────────────────────────────────────────────────────────────────────────
RULING_PHASES = [
    (20, 0.30),  # Months  1–20: 30% of gross is tax-free
    (20, 0.20),  # Months 21–40: 20% of gross is tax-free
    (20, 0.10),  # Months 41–60: 10% of gross is tax-free
]


# ─────────────────────────────────────────────────────────────────────────────
# Data Classes
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class TaxResult:
    """
    Complete breakdown of Dutch income tax for a given salary.

    All monetary values are annual EUR amounts unless otherwise noted.
    """
    # ── Inputs ───────────────────────────────────────────────────────────────
    gross_annual: float
    has_30_percent_ruling: bool
    ruling_months_elapsed: int     # How far into the 60-month ruling period
    age: int

    # ── Salary components ────────────────────────────────────────────────────
    vakantiegeld: float = 0.0      # 8% holiday allowance (included in gross)
    base_salary: float = 0.0       # Gross minus vakantiegeld

    # ── 30% Ruling ───────────────────────────────────────────────────────────
    ruling_exempt_amount: float = 0.0   # Amount excluded from Box 1
    taxable_income: float = 0.0         # Gross minus ruling exemption

    # ── Box 1 Tax (before credits) ───────────────────────────────────────────
    tax_bracket_1: float = 0.0     # Tax on income in bracket 1
    tax_bracket_2: float = 0.0     # Tax on income in bracket 2
    gross_tax: float = 0.0         # Sum of bracket taxes

    # ── Tax Credits ──────────────────────────────────────────────────────────
    algemene_heffingskorting: float = 0.0
    arbeidskorting: float = 0.0
    total_credits: float = 0.0

    # ── Final Tax & Social Contributions ────────────────────────────────────
    net_tax: float = 0.0           # gross_tax minus credits (min 0)
    zvw_bijdrage: float = 0.0      # ZVW health contribution
    total_deductions: float = 0.0  # net_tax + zvw_bijdrage

    # ── Net Results ──────────────────────────────────────────────────────────
    net_annual: float = 0.0
    net_monthly: float = 0.0        # Net annual / 12

    # ── Effective Rates ──────────────────────────────────────────────────────
    effective_tax_rate: float = 0.0      # net_tax / gross_annual
    effective_total_rate: float = 0.0    # total_deductions / gross_annual

    def summary(self) -> str:
        """Return a human-readable summary of the tax calculation."""
        ruling_label = ""
        if self.has_30_percent_ruling:
            phase_pct = _ruling_exempt_fraction(self.ruling_months_elapsed) * 100
            ruling_label = f"  30% Ruling phase:       {phase_pct:.0f}% exempt\n"
            ruling_label += f"  30% Ruling exemption:   € {self.ruling_exempt_amount:>10,.2f}\n"

        lines = [
            "=" * 50,
            "  Dutch Income Tax 2026 — Calculation Summary",
            "=" * 50,
            f"  Gross annual salary:     € {self.gross_annual:>10,.2f}",
            f"  of which vakantiegeld:   € {self.vakantiegeld:>10,.2f}  (8%)",
            ruling_label.rstrip() if ruling_label else "",
            f"  Taxable income (Box 1):  € {self.taxable_income:>10,.2f}",
            "",
            "  ── Box 1 Tax ──────────────────────────────",
            f"  Bracket 1 (36.97%):      € {self.tax_bracket_1:>10,.2f}",
            f"  Bracket 2 (49.50%):      € {self.tax_bracket_2:>10,.2f}",
            f"  Gross tax:               € {self.gross_tax:>10,.2f}",
            "",
            "  ── Tax Credits ────────────────────────────",
            f"  Alg. heffingskorting:    € {self.algemene_heffingskorting:>10,.2f}",
            f"  Arbeidskorting:          € {self.arbeidskorting:>10,.2f}",
            f"  Total credits:           € {self.total_credits:>10,.2f}",
            "",
            "  ── Deductions ─────────────────────────────",
            f"  Net income tax:          € {self.net_tax:>10,.2f}",
            f"  ZVW bijdrage (5.32%):    € {self.zvw_bijdrage:>10,.2f}",
            f"  Total deductions:        € {self.total_deductions:>10,.2f}",
            "",
            "  ── Net Salary ─────────────────────────────",
            f"  Net annual:              € {self.net_annual:>10,.2f}",
            f"  Net monthly:             € {self.net_monthly:>10,.2f}",
            "",
            f"  Effective tax rate:      {self.effective_tax_rate * 100:>9.1f}%",
            f"  Effective total rate:    {self.effective_total_rate * 100:>9.1f}%",
            "=" * 50,
        ]
        return "\n".join(line for line in lines if line is not None)


# ─────────────────────────────────────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────────────────────────────────────

def _ruling_exempt_fraction(months_elapsed: int) -> float:
    """
    Return the tax-free fraction under the 30% ruling for a given position
    in the 60-month period.

    Parameters
    ----------
    months_elapsed : int
        How many months of the ruling period have already been used (0–60).
        0 means the ruling just started (first phase applies).

    Returns
    -------
    float
        0.30, 0.20, 0.10, or 0.0 depending on the phase.
    """
    if months_elapsed < 0:
        raise ValueError("months_elapsed cannot be negative.")
    cumulative = 0
    for duration, fraction in RULING_PHASES:
        cumulative += duration
        if months_elapsed < cumulative:
            return fraction
    return 0.0  # Ruling period has expired


def _calculate_ahk(taxable_income: float) -> float:
    """
    Calculate the algemene heffingskorting (general tax credit) for 2026.

    The credit is AHK_MAX for lower incomes and phases out linearly above
    AHK_PHASE_OUT_START at a rate of AHK_PHASE_OUT_RATE per EUR.

    Parameters
    ----------
    taxable_income : float
        The Box 1 taxable income.

    Returns
    -------
    float
        The algemene heffingskorting, capped between 0 and AHK_MAX.
    """
    if taxable_income <= AHK_PHASE_OUT_START:
        return AHK_MAX
    reduction = (taxable_income - AHK_PHASE_OUT_START) * AHK_PHASE_OUT_RATE
    return max(AHK_MIN, AHK_MAX - reduction)


def _calculate_arbeidskorting(taxable_income: float) -> float:
    """
    Calculate the arbeidskorting (employment tax credit) for 2026.

    The credit builds up in two phases for lower incomes, reaches a maximum,
    then phases out linearly above ARBKORTING_PHASE_OUT_START.

    Parameters
    ----------
    taxable_income : float
        The Box 1 taxable income (generally: gross employment income).

    Returns
    -------
    float
        The arbeidskorting, capped between 0 and ARBKORTING_MAX.
    """
    if taxable_income <= 0:
        return 0.0

    # Build-up phase 1
    if taxable_income <= ARBKORTING_PHASE1_END:
        credit = taxable_income * ARBKORTING_PHASE1_RATE
    # Build-up phase 2
    elif taxable_income <= ARBKORTING_PHASE2_END:
        credit = (ARBKORTING_PHASE1_END * ARBKORTING_PHASE1_RATE
                  + (taxable_income - ARBKORTING_PHASE1_END) * ARBKORTING_PHASE2_RATE)
    else:
        # Maximum is reached at approximately €39,958; cap it
        credit = ARBKORTING_MAX

    credit = min(credit, ARBKORTING_MAX)

    # Phase-out above ARBKORTING_PHASE_OUT_START
    if taxable_income > ARBKORTING_PHASE_OUT_START:
        reduction = (taxable_income - ARBKORTING_PHASE_OUT_START) * ARBKORTING_PHASE_OUT_RATE
        credit = max(ARBKORTING_MIN, credit - reduction)

    return credit


def _calculate_box1_tax(taxable_income: float) -> tuple[float, float, float]:
    """
    Calculate the raw Box 1 income tax (before applying tax credits).

    Parameters
    ----------
    taxable_income : float
        Income taxable in Box 1.

    Returns
    -------
    tuple[float, float, float]
        (tax_bracket_1, tax_bracket_2, gross_tax)
    """
    if taxable_income <= 0:
        return 0.0, 0.0, 0.0

    bracket_1_income = min(taxable_income, TAX_BRACKET_THRESHOLD)
    bracket_2_income = max(0.0, taxable_income - TAX_BRACKET_THRESHOLD)

    tax_1 = bracket_1_income * TAX_BRACKET_1_RATE
    tax_2 = bracket_2_income * TAX_BRACKET_2_RATE

    return tax_1, tax_2, tax_1 + tax_2


def _calculate_zvw(gross_salary: float) -> float:
    """
    Calculate the ZVW (Zorgverzekeringswet) income-related contribution.

    For employees this is typically paid by the employer (werkgeversheffing),
    but it is relevant to DGA / freelancers and is shown here for full
    cost-of-employment transparency.

    Parameters
    ----------
    gross_salary : float
        Gross annual salary.

    Returns
    -------
    float
        ZVW contribution amount.
    """
    base = min(gross_salary, ZVW_MAX_BASE)
    return base * ZVW_RATE


# ─────────────────────────────────────────────────────────────────────────────
# Main Calculator Function
# ─────────────────────────────────────────────────────────────────────────────

def calculate_dutch_tax(
    gross_annual: float,
    has_30_percent_ruling: bool = False,
    ruling_months_elapsed: int = 0,
    age: int = 35,
    vakantiegeld_included: bool = True,
) -> TaxResult:
    """
    Calculate Dutch income tax (Box 1) for 2026.

    Parameters
    ----------
    gross_annual : float
        Annual gross salary in EUR, **including** the 8% vakantiegeld unless
        vakantiegeld_included is False (in which case it is added automatically).
    has_30_percent_ruling : bool
        Whether the employee has been granted the 30% ruling (expatregeling).
    ruling_months_elapsed : int
        Number of months already used in the 60-month 30% ruling period.
        0 = just started (full 30% applies), 20 = second phase (20%), etc.
    age : int
        Employee age. Currently used for informational purposes; AOW
        (state pension) premium exceptions for 65+ are not yet modelled.
    vakantiegeld_included : bool
        If True (default), gross_annual is assumed to already include the 8%
        vakantiegeld. If False, vakantiegeld is added on top of gross_annual.

    Returns
    -------
    TaxResult
        A dataclass with the full tax breakdown. Call .summary() for a
        formatted printout.

    Examples
    --------
    >>> result = calculate_dutch_tax(60_000)
    >>> print(result.summary())

    >>> result = calculate_dutch_tax(80_000, has_30_percent_ruling=True, ruling_months_elapsed=0)
    >>> print(f"Net monthly: €{result.net_monthly:,.2f}")
    """
    if gross_annual < 0:
        raise ValueError("gross_annual must be non-negative.")
    if not (0 <= ruling_months_elapsed <= 60):
        raise ValueError("ruling_months_elapsed must be between 0 and 60.")
    if age < 0:
        raise ValueError("age must be non-negative.")

    # ── Step 1: Vakantiegeld ─────────────────────────────────────────────────
    # Standard Dutch employment contracts include 8% holiday pay.
    # If the gross already includes it, we decompose it; otherwise we add it.
    if vakantiegeld_included:
        # gross = base * 1.08  →  base = gross / 1.08
        base_salary = gross_annual / (1 + VAKANTIEGELD_RATE)
        vakantiegeld = gross_annual - base_salary
    else:
        base_salary = gross_annual
        vakantiegeld = gross_annual * VAKANTIEGELD_RATE
        gross_annual = base_salary + vakantiegeld

    # ── Step 2: 30% Ruling Exemption ────────────────────────────────────────
    # The 30% ruling allows a portion of the gross salary to be paid as a
    # tax-free expense reimbursement. The fraction steps down over 5 years.
    ruling_exempt_amount = 0.0
    if has_30_percent_ruling:
        fraction = _ruling_exempt_fraction(ruling_months_elapsed)
        ruling_exempt_amount = gross_annual * fraction

    taxable_income = gross_annual - ruling_exempt_amount

    # ── Step 3: Box 1 Tax ────────────────────────────────────────────────────
    tax_bracket_1, tax_bracket_2, gross_tax = _calculate_box1_tax(taxable_income)

    # ── Step 4: Tax Credits ──────────────────────────────────────────────────
    # Credits are applied against the Box 1 tax. They are calculated on the
    # taxable income (post-ruling, pre-credit).
    ahk = _calculate_ahk(taxable_income)
    arbkorting = _calculate_arbeidskorting(taxable_income)
    total_credits = ahk + arbkorting

    # ── Step 5: Net Tax ──────────────────────────────────────────────────────
    net_tax = max(0.0, gross_tax - total_credits)

    # ── Step 6: ZVW Bijdrage ─────────────────────────────────────────────────
    # For employed individuals, the employer pays the ZVW contribution
    # (werkgeversheffing ZVW). It is shown here as a cost-of-employment figure.
    # Self-employed individuals pay the nominale premie directly.
    zvw_bijdrage = _calculate_zvw(gross_annual)

    # ── Step 7: Net Salary ───────────────────────────────────────────────────
    total_deductions = net_tax + zvw_bijdrage
    net_annual = gross_annual - total_deductions
    net_monthly = net_annual / 12

    # ── Step 8: Effective Rates ──────────────────────────────────────────────
    effective_tax_rate = net_tax / gross_annual if gross_annual > 0 else 0.0
    effective_total_rate = total_deductions / gross_annual if gross_annual > 0 else 0.0

    return TaxResult(
        gross_annual=gross_annual,
        has_30_percent_ruling=has_30_percent_ruling,
        ruling_months_elapsed=ruling_months_elapsed,
        age=age,
        vakantiegeld=vakantiegeld,
        base_salary=base_salary,
        ruling_exempt_amount=ruling_exempt_amount,
        taxable_income=taxable_income,
        tax_bracket_1=tax_bracket_1,
        tax_bracket_2=tax_bracket_2,
        gross_tax=gross_tax,
        algemene_heffingskorting=ahk,
        arbeidskorting=arbkorting,
        total_credits=total_credits,
        net_tax=net_tax,
        zvw_bijdrage=zvw_bijdrage,
        total_deductions=total_deductions,
        net_annual=net_annual,
        net_monthly=net_monthly,
        effective_tax_rate=effective_tax_rate,
        effective_total_rate=effective_total_rate,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Command-Line Interface
# ─────────────────────────────────────────────────────────────────────────────

def _parse_args():
    """Parse command-line arguments."""
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Dutch Income Tax Calculator 2026\n"
            "Open source by ExpatNetherlandsHub.com\n"
            "https://expatnetherlandshub.com/tools/salary-checker/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "gross_salary",
        type=float,
        help="Gross annual salary in EUR (including vakantiegeld by default).",
    )
    parser.add_argument(
        "--ruling",
        action="store_true",
        default=False,
        help="Apply the 30%% ruling (expatregeling).",
    )
    parser.add_argument(
        "--ruling-months",
        type=int,
        default=0,
        dest="ruling_months",
        metavar="N",
        help=(
            "Months already elapsed in the 60-month ruling period "
            "(0=first phase 30%%, 20=second phase 20%%, 40=third phase 10%%)."
        ),
    )
    parser.add_argument(
        "--age",
        type=int,
        default=35,
        help="Employee age (default: 35).",
    )
    parser.add_argument(
        "--no-vakantiegeld",
        action="store_true",
        default=False,
        dest="no_vakantiegeld",
        help="Treat gross salary as base salary (vakantiegeld added on top).",
    )
    return parser.parse_args()


# ─────────────────────────────────────────────────────────────────────────────
# Demo / Self-Test
# ─────────────────────────────────────────────────────────────────────────────

def _run_demo():
    """
    Run a small demo with representative salary levels.

    Useful for a quick sanity check. Expected approximate results for 2026:

    €40,000 (no ruling)  → ~€28,700 net / year   (~€2,392/month)
    €60,000 (no ruling)  → ~€40,000 net / year   (~€3,333/month)
    €80,000 (no ruling)  → ~€49,200 net / year   (~€4,100/month)
    €60,000 (30% ruling) → ~€46,400 net / year   (~€3,867/month)
    """
    scenarios = [
        {"gross_annual": 40_000, "has_30_percent_ruling": False, "label": "€40,000 — no ruling"},
        {"gross_annual": 60_000, "has_30_percent_ruling": False, "label": "€60,000 — no ruling"},
        {"gross_annual": 80_000, "has_30_percent_ruling": False, "label": "€80,000 — no ruling"},
        {
            "gross_annual": 60_000,
            "has_30_percent_ruling": True,
            "ruling_months_elapsed": 0,
            "label": "€60,000 — 30% ruling (phase 1)",
        },
        {
            "gross_annual": 60_000,
            "has_30_percent_ruling": True,
            "ruling_months_elapsed": 20,
            "label": "€60,000 — 20% ruling (phase 2)",
        },
    ]

    for scenario in scenarios:
        label = scenario.pop("label")
        print(f"\n{'─' * 50}")
        print(f"  Scenario: {label}")
        result = calculate_dutch_tax(**scenario)
        print(result.summary())


# ─────────────────────────────────────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    # If no arguments given, run demo
    if len(sys.argv) == 1:
        _run_demo()
        print(
            "\nFor an interactive salary calculator, visit:\n"
            "https://expatnetherlandshub.com/tools/salary-checker/\n"
        )
    else:
        args = _parse_args()
        result = calculate_dutch_tax(
            gross_annual=args.gross_salary,
            has_30_percent_ruling=args.ruling,
            ruling_months_elapsed=args.ruling_months,
            age=args.age,
            vakantiegeld_included=not args.no_vakantiegeld,
        )
        print(result.summary())
        print(
            "\nFor an interactive salary calculator, visit:\n"
            "https://expatnetherlandshub.com/tools/salary-checker/\n"
        )
