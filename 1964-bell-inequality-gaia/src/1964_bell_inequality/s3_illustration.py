"""Illustration — Single-particle hidden variables are possible; reproducing some QM features is easy."""

from gaia.lang import claim, setting, deduction

from .motivation import (
    s_hidden_variable_formalism,
    s_expectation_value,
    s_bohm_aharonov_example,
)

# ── Single particle hidden variables are unproblematic ──

c_single_particle_hv_possible = claim(
    "For a single spin-half particle in a pure spin state with polarization $\\hat{p}$, "
    "it is straightforward to give a hidden variable account. Using a unit vector "
    "$\\lambda$ with uniform probability distribution over the hemisphere "
    "$\\lambda \\cdot \\hat{p} > 0$, and defining the measurement result as "
    "$A(\\hat{a}, \\lambda) = \\text{sign}(\\lambda \\cdot \\hat{a}')$ where $\\hat{a}'$ "
    "is obtained from $\\hat{a}$ by rotation towards $\\hat{p}$, the expectation value "
    "$\\langle A \\rangle = -\\hat{a} \\cdot \\hat{p}$ is reproduced exactly.",
    title="Single-particle hidden variables can reproduce QM statistics",
)

# ── Verbal features can be reproduced ──

c_verbal_features_reproducible = claim(
    "The commonly discussed features of the singlet correlation — perfect anti-correlation "
    "when $\\hat{a} = \\hat{b}$, and expectation value depending only on the angle between "
    "$\\hat{a}$ and $\\hat{b}$ — can be reproduced by a hidden variable model. For example, "
    "taking $\\lambda$ as a unit vector with uniform distribution over all directions and "
    "defining $A = -\\text{sign}(\\lambda \\cdot \\hat{a})$, $B = \\text{sign}(\\lambda \\cdot \\hat{b})$ "
    "gives $P(\\hat{a}, \\hat{b}) = -1 + (2/\\pi)\\theta$ where $\\theta$ is the angle between "
    "$\\hat{a}$ and $\\hat{b}$.",
    title="Verbal features of singlet correlation are reproducible by hidden variables",
)

# ── But the function is not stationary at minimum ──

c_not_stationary_at_minimum = claim(
    "Unlike the QM correlation $P = -\\hat{a} \\cdot \\hat{b}$, the hidden variable "
    "correlation $P = -1 + (2/\\pi)\\theta$ is not stationary at the minimum value $-1$ "
    "(at $\\theta = 0$). This is characteristic of functions of the local hidden variable "
    "form (2), and will be the key to the contradiction.",
    title="Hidden variable correlations are not stationary at the minimum",
)

# ── Non-local dependence reproduces QM ──

c_nonlocal_reproduces_qm = claim(
    "If the results $A$ and $B$ are allowed to depend on both $\\hat{a}$ and $\\hat{b}$ "
    "(i.e., non-local dependence), the QM correlation can be reproduced. However, for "
    "given values of the hidden variables, the results of measurements with one magnet "
    "then depend on the setting of the distant magnet, which is exactly what we wish to avoid.",
    title="Non-local hidden variables can reproduce QM correlations",
)

# ── Strategies ──
# c_single_particle_hv_possible, c_verbal_features_reproducible, c_not_stationary_at_minimum,
# and c_nonlocal_reproduces_qm are standalone observations/illustrations.
# No strategies needed — they are independent premises (assigned priors in review).
