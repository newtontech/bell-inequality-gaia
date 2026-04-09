"""Introduction and Formulation — EPR paradox motivates hidden variables; Bell's locality assumption."""

from gaia.lang import claim, setting

# ── EPR motivation for hidden variables ──

s_epr_motivation = setting(
    "The EPR paradox was advanced as an argument that QM could not be a complete "
    "theory but should be supplemented by additional variables. These additional "
    "variables were to restore to the theory causality and locality.",
    title="EPR motivation for hidden variables",
)

# ── Bohm-Aharonov example ──

s_bohm_aharonov_example = setting(
    "Consider a pair of spin one-half particles formed in the singlet spin state "
    "and moving freely in opposite directions. Measurements can be made on selected "
    "components of the spins $\\sigma_1$ and $\\sigma_2$ by Stern-Gerlach magnets. "
    "If measurement of the component $\\sigma_1 \\cdot \\hat{a}$ yields the value +1, "
    "then according to QM, measurement of $\\sigma_2 \\cdot \\hat{a}$ must yield -1.",
    title="Bohm-Aharonov spin singlet example",
)

# ── Locality hypothesis ──

c_locality_hypothesis = claim(
    "If the two measurements are made at places remote from one another, the "
    "orientation of one magnet does not influence the result obtained with the other. "
    "Since we can predict in advance the result of measuring any chosen component of "
    "$\\sigma_2$ by previously measuring the same component of $\\sigma_1$, the result "
    "of any such measurement must actually be predetermined.",
    title="Locality hypothesis: remote measurements are independent",
)

# ── Predetermination implies hidden variables ──

c_predetermination_implies_hidden_vars = claim(
    "Since the initial quantum mechanical wave function does not determine the result "
    "of an individual measurement, the predetermination implied by locality "
    "(@c_locality_hypothesis) requires the possibility of a more complete specification "
    "of the state by means of additional parameters $\\lambda$.",
    title="Predetermination under locality requires hidden variables",
)

# ── Hidden variable formalism ──

s_hidden_variable_formalism = setting(
    "Let $\\lambda$ denote hidden variable(s). The result $A$ of measuring "
    "$\\sigma_1 \\cdot \\hat{a}$ is determined by $\\hat{a}$ and $\\lambda$, and the "
    "result $B$ of measuring $\\sigma_2 \\cdot \\hat{b}$ is determined by $\\hat{b}$ "
    "and $\\lambda$:\n\n"
    "$$A(\\hat{a}, \\lambda) = \\pm 1, \\quad B(\\hat{b}, \\lambda) = \\pm 1$$\n\n"
    "The vital assumption is that result $B$ does not depend on $\\hat{a}$, nor $A$ "
    "on $\\hat{b}$.",
    title="Hidden variable formalism with locality",
)

# ── Expectation value in hidden variable theory ──

s_expectation_value = setting(
    "If $\\rho(\\lambda)$ is the probability distribution of $\\lambda$, then the "
    "expectation value of the product of the two components $\\sigma_1 \\cdot \\hat{a}$ "
    "and $\\sigma_2 \\cdot \\hat{b}$ is:\n\n"
    "$$P(\\hat{a}, \\hat{b}) = \\int d\\lambda \\, \\rho(\\lambda) \\, A(\\hat{a}, \\lambda) \\, B(\\hat{b}, \\lambda)$$",
    title="Expectation value in hidden variable theory",
)

# ── QM prediction for singlet state ──

c_qm_singlet_prediction = claim(
    "The quantum mechanical expectation value for the singlet state is:\n\n"
    "$$P(\\hat{a}, \\hat{b}) = -\\hat{a} \\cdot \\hat{b}$$\n\n"
    "Bell will show that this cannot be reproduced by any local hidden variable theory.",
    title="QM predicts $P = -\\hat{a} \\cdot \\hat{b}$ for singlet state",
)
