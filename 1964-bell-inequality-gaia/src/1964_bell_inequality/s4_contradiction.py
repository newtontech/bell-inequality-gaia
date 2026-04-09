"""Contradiction — The main result: local hidden variables cannot reproduce QM correlations."""

from gaia.lang import claim, setting, deduction, infer

from .motivation import (
    s_hidden_variable_formalism,
    s_expectation_value,
    s_bohm_aharonov_example,
    c_qm_singlet_prediction,
    c_locality_hypothesis,
)

# ── Step 1: P reaches -1 only when A(a,λ) = -B(a,λ) ──

c_perfect_anticorrelation_condition = claim(
    "$P(\\hat{a}, \\hat{b})$ in the form (2) can reach $-1$ at $\\hat{a} = \\hat{b}$ "
    "only if\n\n"
    "$$A(\\hat{a}, \\lambda) = -B(\\hat{a}, \\lambda)$$\n\n"
    "except at a set of points $\\lambda$ of zero probability.",
    title="Perfect anti-correlation condition: $A = -B$ at same direction",
)

# ── Step 2: Rewrite P using anti-correlation ──

s_rewritten_expectation = setting(
    "Using the anti-correlation condition, $P(\\hat{a}, \\hat{b})$ can be rewritten as:\n\n"
    "$$P(\\hat{a}, \\hat{b}) = -\\int d\\lambda \\, \\rho(\\lambda) \\, A(\\hat{a}, \\lambda) \\, A(\\hat{b}, \\lambda)$$",
    title="Rewritten expectation value using anti-correlation",
)

# ── Step 3: Key inequality ──

c_bell_key_inequality = claim(
    "For any unit vectors $\\hat{a}$, $\\hat{b}$, $\\hat{c}$:\n\n"
    "$$1 + P(\\hat{b}, \\hat{c}) \\geq |P(\\hat{a}, \\hat{b}) - P(\\hat{a}, \\hat{c})|$$\n\n"
    "This follows from:\n"
    "$P(\\hat{a}, \\hat{b}) - P(\\hat{a}, \\hat{c}) = -\\int d\\lambda \\, \\rho(\\lambda) \\, "
    "[A(\\hat{a}, \\lambda)A(\\hat{b}, \\lambda) - A(\\hat{a}, \\lambda)A(\\hat{c}, \\lambda)]$\n"
    "$= -\\int d\\lambda \\, \\rho(\\lambda) \\, A(\\hat{a}, \\lambda)A(\\hat{b}, \\lambda) "
    "[1 - A(\\hat{b}, \\lambda)A(\\hat{c}, \\lambda)]$\n\n"
    "Since $|A| = 1$, the integrand is bounded by $[1 - A(\\hat{b}, \\lambda)A(\\hat{c}, \\lambda)]$, "
    "giving the inequality.",
    title="Bell's key inequality (original 1964 form)",
)

# ── Step 4: QM violates the inequality ──

c_qm_violates_inequality = claim(
    "The QM prediction $P(\\hat{a}, \\hat{b}) = -\\hat{a} \\cdot \\hat{b}$ violates "
    "the inequality for certain angle choices. For example, take "
    "$\\hat{a} \\cdot \\hat{c} = 0$ and $\\hat{a} \\cdot \\hat{b} = \\hat{b} \\cdot \\hat{c} = 1/\\sqrt{2}$ "
    "(i.e., angles of 90 degrees and 45 degrees). Then:\n\n"
    "- LHS: $1 + P(\\hat{b}, \\hat{c}) = 1 - \\hat{b} \\cdot \\hat{c} = 1 - 1/\\sqrt{2} \\approx 0.293$\n"
    "- RHS: $|P(\\hat{a}, \\hat{b}) - P(\\hat{a}, \\hat{c})| = |{-\\hat{a} \\cdot \\hat{b} + \\hat{a} \\cdot \\hat{c}}| = |{-1/\\sqrt{2} + 0}| = 1/\\sqrt{2} \\approx 0.707$\n\n"
    "Since $0.293 < 0.707$, the inequality is violated.",
    title="QM prediction violates Bell's inequality",
)

# ── The main theorem ──

c_bell_theorem = claim(
    "The quantum mechanical expectation value for the singlet state "
    "$P(\\hat{a}, \\hat{b}) = -\\hat{a} \\cdot \\hat{b}$ cannot be represented, either "
    "accurately or arbitrarily closely, in the local hidden variable form. "
    "Nor can the QM correlation be arbitrarily closely approximated by such a form.",
    title="Bell's theorem: local hidden variables cannot reproduce QM correlations",
)

# ── Conclusion: non-locality ──

c_nonlocality_conclusion = claim(
    "In a theory in which parameters are added to QM to determine the results of "
    "individual measurements, without changing the statistical predictions, there "
    "must be a mechanism whereby the setting of one measuring device can influence "
    "the reading of another instrument, however remote. Moreover, the signal involved "
    "must propagate instantaneously, so that such a theory could not be Lorentz invariant.",
    title="Conclusion: any hidden variable theory reproducing QM must be non-local",
)

# ── Crucial experiments ──

c_crucial_experiments = claim(
    "Experiments of the type proposed by Bohm and Aharonov, in which the settings "
    "are changed during the flight of the particles, are crucial for testing whether "
    "QM predictions hold when the settings cannot reach mutual rapport by exchange "
    "of signals with velocity less than or equal to that of light.",
    title="Crucial experiments: settings changed during particle flight",
)

# ── Strategies ──

_ded_perfect_anticorr = deduction(
    [c_locality_hypothesis],
    c_perfect_anticorrelation_condition,
    reason="If locality holds (@c_locality_hypothesis), the expectation value can "
    "reach $-1$ at $\\hat{a} = \\hat{b}$ only when $A(\\hat{a}, \\lambda) = -B(\\hat{a}, \\lambda)$ "
    "almost everywhere, since $|A| = |B| = 1$ and $\\rho$ is normalized.",
    background=[s_hidden_variable_formalism, s_expectation_value],
)

_ded_bell_inequality = deduction(
    [c_perfect_anticorrelation_condition],
    c_bell_key_inequality,
    reason="Using the rewritten form $P(\\hat{a}, \\hat{b}) = -\\int \\rho A(\\hat{a})A(\\hat{b})$ "
    "from @c_perfect_anticorrelation_condition, and the algebraic identity "
    "$A(\\hat{a})A(\\hat{b}) - A(\\hat{a})A(\\hat{c}) = A(\\hat{a})A(\\hat{b})(1 - A(\\hat{b})A(\\hat{c}))$, "
    "the bound $|A| \\leq 1$ gives the inequality.",
    background=[s_rewritten_expectation],
)

_infer_qm_violates = infer(
    [c_bell_key_inequality, c_qm_singlet_prediction],
    c_qm_violates_inequality,
    reason="The inequality (@c_bell_key_inequality) must hold for all local HV theories. "
    "The QM prediction (@c_qm_singlet_prediction) gives specific values that can be "
    "checked: for $\\hat{a} \\cdot \\hat{c} = 0$, $\\hat{a} \\cdot \\hat{b} = \\hat{b} \\cdot \\hat{c} = 1/\\sqrt{2}$, "
    "the inequality fails ($0.293 < 0.707$).",
)

_ded_bell_theorem = deduction(
    [c_qm_violates_inequality],
    c_bell_theorem,
    reason="Since the inequality (which all local HV theories must satisfy) is violated "
    "by the QM prediction, no local hidden variable theory can reproduce QM correlations. "
    "The approximation argument further shows even approximate reproduction is impossible.",
)

_ded_nonlocality = deduction(
    [c_bell_theorem],
    c_nonlocality_conclusion,
    reason="If QM statistics are correct and no local HV theory can reproduce them, "
    "then any deterministic underpinning must involve non-local influence. "
    "Instantaneous influence is required, violating Lorentz invariance.",
)
