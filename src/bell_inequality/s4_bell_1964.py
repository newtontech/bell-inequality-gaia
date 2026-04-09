"""Section 4: Bell's 1964 Theorem

John Stewart Bell's 1964 paper "On the Einstein Podolsky Rosen Paradox" demonstrates
that any local hidden-variable theory must satisfy certain statistical constraints
(inequalities) that quantum mechanics violates. This transforms the EPR-Bohr
philosophical debate into an experimentally testable question.

The key insight: locality + hidden variables → Bell's inequality. QM predictions
violate this inequality. Therefore, no local hidden-variable theory can reproduce
all QM predictions.

Reference: Bell, J.S. (1964) "On the Einstein Podolsky Rosen Paradox" Physics 1, 195-200.
"""

from gaia.lang import (
    claim, setting, deduction, abduction, noisy_and,
    contradiction, complement,
)
from .motivation import (
    c_criterion_of_reality,
)
from .s2_epr_argument import (
    c_qm_incomplete, c_p_and_q_simultaneous_reality,
    c_no_interaction_no_disturbance,
)
from .s3_bohr_reply import (
    c_qm_is_complete,
)

# ============================================================
# Settings — Bell's conceptual framework
# ============================================================

s_singlet_spin_state = setting(
    "Consider a pair of spin-1/2 particles formed in the singlet spin state and moving "
    "freely in opposite directions. The singlet state is $\\frac{1}{\\sqrt{2}}(|\\uparrow\\downarrow\\rangle - "
    "|\\downarrow\\uparrow\\rangle)$, which is rotationally invariant. Measurements can be "
    "made using Stern-Gerlach magnets on selected components of the spins $\\vec{\\sigma}_1 \\cdot \\vec{a}$ "
    "and $\\vec{\\sigma}_2 \\cdot \\vec{b}$, where $\\vec{a}$ and $\\vec{b}$ are unit vectors specifying "
    "the measurement directions.",
    title="Singlet state and spin measurements",
)

s_locality_assumption_bell = setting(
    "Bell's locality assumption: the result of a measurement on one system is unaffected "
    "by operations on a distant system with which it has interacted in the past. Formally, "
    "if $A$ is the result of measuring $\\vec{\\sigma}_1 \\cdot \\vec{a}$ and $B$ is the result "
    "of measuring $\\vec{\\sigma}_2 \\cdot \\vec{b}$, then $A$ depends only on $\\vec{a}$ and the "
    "hidden variable $\\lambda$, while $B$ depends only on $\\vec{b}$ and $\\lambda$. The result "
    "$B$ does not depend on $\\vec{a}$, nor $A$ on $\\vec{b}$.",
    title="Bell locality assumption",
)

s_hidden_variable_formalism = setting(
    "A hidden variable theory posits that the quantum mechanical wave function does not "
    "provide a complete description of physical reality. Let $\\lambda$ denote a set of "
    "additional parameters (hidden variables) that more completely specify the state of "
    "the system. These parameters have a probability distribution $\\rho(\\lambda)$, and "
    "the results of measurements are functions $A(\\vec{a}, \\lambda)$ and $B(\\vec{b}, \\lambda)$ "
    "that take values $\\pm 1$. The expectation value of the product $\\vec{\\sigma}_1 \\cdot \\vec{a}$ "
    "and $\\vec{\\sigma}_2 \\cdot \\vec{b}$ is $P(\\vec{a}, \\vec{b}) = \\int d\\lambda \\rho(\\lambda) A(\\vec{a}, \\lambda) B(\\vec{b}, \\lambda)$.",
    title="Hidden variable formalism",
)

s_qm_correlation_singlet = setting(
    "In quantum mechanics, the expectation value of the product $\\vec{\\sigma}_1 \\cdot \\vec{a}$ "
    "and $\\vec{\\sigma}_2 \\cdot \\vec{b}$ for the singlet state is $E_{QM}(\\vec{a}, \\vec{b}) = -\\vec{a} \\cdot \\vec{b} = -\\cos\\theta$, "
    "where $\\theta$ is the angle between measurement directions $\\vec{a}$ and $\\vec{b}$. "
    "This correlation function attains its minimum value of $-1$ when $\\vec{a} = \\vec{b}$ (parallel measurements).",
    title="Quantum mechanical correlation function",
)

# ============================================================
# Claims — Bell's core argument
# ============================================================

c_epr_motivation_hidden_variables = claim(
    "The EPR paradox was advanced as an argument that quantum mechanics could not be "
    "a complete theory but should be supplemented by additional variables (hidden variables). "
    "These additional variables were intended to restore to the theory causality and locality.",
    title="EPR motivates hidden variables",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_locality_creates_difficulty = claim(
    "It is the requirement of locality — or more precisely that the result of a measurement "
    "on one system be unaffected by operations on a distant system with which it has "
    "interacted in the past — that creates the essential difficulty for hidden variable "
    "theories attempting to reproduce quantum mechanics.",
    title="Locality is the essential difficulty",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_nonlocal_hidden_variable_exists = claim(
    "A hidden variable interpretation of elementary quantum theory has been explicitly "
    "constructed (Bohm 1952). That particular interpretation has a grossly non-local structure. "
    "This is characteristic, according to Bell's result, of any such theory which reproduces "
    "exactly the quantum mechanical predictions.",
    title="Explicit nonlocal hidden variable theory exists",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_singlet_perfect_anticorrelation = claim(
    "In the singlet spin state, if measurement of the component $\\vec{\\sigma}_1 \\cdot \\vec{a}$ "
    "yields the value $+1$, then according to quantum mechanics, measurement of $\\vec{\\sigma}_2 \\cdot \\vec{a}$ "
    "must yield the value $-1$, and vice versa. This perfect anticorrelation holds for any "
    "measurement direction $\\vec{a}$.",
    title="Perfect anticorrelation in singlet state",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_locality_implies_predetermination = claim(
    "Given the locality assumption (that the orientation of one magnet does not influence "
    "the result obtained with the other), and the fact that we can predict in advance the "
    "result of measuring any chosen component of particle 2 by previously measuring the "
    "same component of particle 1, it follows that the result of any such measurement must "
    "actually be predetermined. Since the initial quantum mechanical wave function does not "
    "determine the result of an individual measurement, this predetermination implies the "
    "possibility of a more complete specification of the state via hidden variables $\\lambda$.",
    title="Locality implies predetermination",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_hidden_variables_complete_specification = claim(
    "Let the more complete specification be effected by means of parameters $\\lambda$. "
    "Whether $\\lambda$ denotes a single variable or a set, or even a set of functions, "
    "and whether the variables are discrete or continuous, is a matter of indifference "
    "for the mathematical formulation. The result $A$ of measuring $\\vec{\\sigma}_1 \\cdot \\vec{a}$ "
    "is determined by $\\vec{a}$ and $\\lambda$, and the result $B$ of measuring $\\vec{\\sigma}_2 \\cdot \\vec{b}$ "
    "is determined by $\\vec{b}$ and $\\lambda$.",
    title="Hidden variables as complete specification",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_locality_constraint_formal = claim(
    "The vital locality assumption is that the result $B$ for particle 2 does not depend "
    "on the setting $\\vec{a}$ of the magnet for particle 1, nor $A$ on $\\vec{b}$. "
    "Formally, $A = A(\\vec{a}, \\lambda)$ and $B = B(\\vec{b}, \\lambda)$, with no "
    "cross-dependence: $\\partial B / \\partial \\vec{a} = 0$ and $\\partial A / \\partial \\vec{b} = 0$.",
    title="Formal locality constraint",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_local_hidden_correlation_form = claim(
    "For any local hidden variable theory, the expectation value of the product "
    "$\\vec{\\sigma}_1 \\cdot \\vec{a}$ and $\\vec{\\sigma}_2 \\cdot \\vec{b}$ must take the form "
    "$P(\\vec{a}, \\vec{b}) = \\int d\\lambda \\rho(\\lambda) A(\\vec{a}, \\lambda) B(\\vec{b}, \\lambda)$, "
    "where $\\rho(\\lambda)$ is the probability distribution of hidden variables and "
    "$A, B \\in \\{\\pm 1\\}$.",
    title="Local hidden correlation form",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_bell_inequality = claim(
    "For any local hidden variable theory, the correlation function $P(\\vec{a}, \\vec{b})$ "
    "must satisfy the constraint $|P(\\vec{a}, \\vec{b}) - P(\\vec{a}, \\vec{c})| \\leq 1 + P(\\vec{b}, \\vec{c})$ "
    "for all unit vectors $\\vec{a}, \\vec{b}, \\vec{c}$. This constraint follows from the "
    "locality assumption and the fact that measurement outcomes are bounded ($\\pm 1$). "
    "Equivalently, in its CHSH form: $|P(\\vec{a}, \\vec{b}) - P(\\vec{a}, \\vec{b}')| + "
    "|P(\\vec{a}', \\vec{b}) + P(\\vec{a}', \\vec{b}')| \\leq 2$.",
    title="Bell's inequality for local hidden variables",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_qm_correlation_function = claim(
    "Quantum mechanics predicts for the singlet state that the correlation function is "
    "$E_{QM}(\\vec{a}, \\vec{b}) = -\\vec{a} \\cdot \\vec{b} = -\\cos\\theta$, where $\\theta$ is "
    "the angle between measurement directions. This correlation function is smooth, "
    "stationary at its minimum value of $-1$ when $\\vec{a} = \\vec{b}$, and varies continuously "
    "as a function of the angle between measurements.",
    title="QM correlation: $E = -\\vec{a} \\cdot \\vec{b}$",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_local_theory_nonstationary = claim(
    "For any local hidden variable theory of the form $P(\\vec{a}, \\vec{b}) = \\int d\\lambda \\rho(\\lambda) "
    "A(\\vec{a}, \\lambda) B(\\vec{b}, \\lambda)$, the correlation function cannot be stationary "
    "at the minimum value $-1$. This is because reaching $P(\\vec{a}, \\vec{a}) = -1$ for all "
    "$\\vec{a}$ would require $A(\\vec{a}, \\lambda) = -B(\\vec{a}, \\lambda)$ almost everywhere, which "
    "implies the correlation varies linearly with the angle difference for small angles, not "
    "quadratically as the QM prediction does.",
    title="Local theories give non-stationary correlations",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_qm_violates_bell_inequality = claim(
    "The quantum mechanical correlation function $E_{QM}(\\vec{a}, \\vec{b}) = -\\vec{a} \\cdot \\vec{b}$ "
    "violates Bell's inequality for certain choices of measurement directions. For example, "
    "with coplanar vectors where $\\vec{a} \\cdot \\vec{c} = 0$ and $\\vec{a} \\cdot \\vec{b} = "
    "\\vec{b} \\cdot \\vec{c} = 1/\\sqrt{2}$, QM gives $P(\\vec{a}, \\vec{b}) = P(\\vec{b}, \\vec{c}) = -1/\\sqrt{2}$ "
    "and $P(\\vec{a}, \\vec{c}) = 0$, so the left side of the inequality $|P(\\vec{a}, \\vec{b}) - P(\\vec{a}, \\vec{c})| = "
    "$\\sqrt{2} \\approx 1.414$ while the right side $1 + P(\\vec{b}, \\vec{c}) = 1 - 1/\\sqrt{2} \\approx 0.586$. "
    "Since $1.414 > 0.586$, the inequality is violated.",
    title="QM violates Bell's inequality",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_local_hv_incompatible_with_qm = claim(
    "The quantum mechanical expectation value cannot be represented, either accurately "
    "or arbitrarily closely, in the local hidden variable form $P(\\vec{a}, \\vec{b}) = \\int d\\lambda "
    "\\rho(\\lambda) A(\\vec{a}, \\lambda) B(\\vec{b}, \\lambda)$. This is Bell's main result: "
    "no local hidden variable theory can reproduce all the statistical predictions of "
    "quantum mechanics for the singlet state.",
    title="Local HV incompatible with QM statistics",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_approximation_impossible = claim(
    "Even if we relax the requirement of exact agreement and only require that the local "
    "hidden variable theory approximate the quantum mechanical predictions to within "
    "some small error $\\epsilon$, Bell shows that $\\epsilon$ cannot be made arbitrarily small. "
    "For the optimal configuration of measurement directions, the difference between QM "
    "and any local hidden variable theory is bounded below by a finite amount.",
    title="No local HV theory can approximate QM arbitrarily closely",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_locality_lorentz_invariance_conflict = claim(
    "In a theory in which parameters are added to quantum mechanics to determine the results "
    "of individual measurements without changing the statistical predictions, there must be "
    "a mechanism whereby the setting of one measuring device can influence the reading of "
    "another instrument, however remote. Moreover, the signal involved must propagate "
    "instantaneously, so that such a theory could not be Lorentz invariant. Any hidden "
    "variable theory that reproduces QM predictions must be nonlocal.",
    title="Reproducing QM requires instantaneous nonlocality",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_bell_result_generalizes = claim(
    "Bell's result is not limited to spin-1/2 particles. The theorem can be extended to "
    "any quantum systems with state spaces of dimensionality greater than 2 by considering "
    "two-dimensional subspaces and defining, in their direct product, operators formally "
    "analogous to the spin operators. For at least one quantum mechanical state (the 'singlet' "
    "state in the combined subspaces), the statistical predictions of quantum mechanics "
    "are incompatible with separable predetermination.",
    title="Bell's theorem generalizes beyond spin",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_time_varying_settings_crucial = claim(
    "If quantum mechanical predictions have limited validity and apply only to experiments "
    "in which the settings of the instruments are made sufficiently in advance to allow "
    "them to reach some mutual rapport by exchange of signals with velocity less than or "
    "equal to that of light, then local hidden variable theories might be viable. Experiments "
    "in which the settings are changed during the flight of the particles (as proposed by "
    "Bohm and Aharonov) are therefore crucial for testing Bell's inequality.",
    title="Time-varying settings are crucial for tests",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

c_bell_theorem = claim(
    "Bell's theorem: No local hidden-variable theory can reproduce all the statistical "
    "predictions of quantum mechanics. This is not a philosophical argument but a "
    "mathematical result: any theory satisfying locality and determinism (via hidden "
    "variables) must satisfy Bell's inequality, while quantum mechanics predicts "
    "violations of this inequality. The question is therefore experimentally testable.",
    title="Bell's theorem: local HV theories cannot reproduce QM",
    metadata={"source": "artifacts/1964_bell_inequality/bell_1964_full_text.txt"},
)

# ============================================================
# Abduction alternatives — named for review sidecar
# ============================================================

alt_locality_violates_qm = claim(
    "Quantum mechanics might itself be nonlocal, allowing instantaneous correlations "
    "between separated measurements without any hidden variables. The apparent violations "
    "of Bell's inequality would then reflect a genuine nonlocality in nature, not an "
    "incompleteness of QM. This is the orthodox Copenhagen position extended to acknowledge "
    "quantum nonlocality.",
    title="Alternative: QM itself is fundamentally nonlocal",
)

alt_superdeterminism = claim(
    "The apparent freedom to choose measurement settings might be illusory. If the hidden "
    "variables $\\lambda$ also determine the choice of measurement directions (the 'free will' "
    "or 'no-conspiracy' assumption fails), then Bell's derivation would not apply. This "
    "superdeterministic scenario would allow a local hidden variable theory to reproduce "
    "QM predictions without nonlocality.",
    title="Alternative: Superdeterminism (measurement settings correlated with $\\lambda$)",
)

alt_retrocausality = claim(
    "The hidden variables might influence events backwards in time, allowing measurement "
    "settings to be correlated with particle properties without requiring faster-than-light "
    "influence. A retrocausal theory could potentially reproduce QM correlations while "
    "maintaining a form of locality in spacetime.",
    title="Alternative: Retrocausal hidden variables",
)

# ============================================================
# Operators — logical contradictions
# ============================================================

# Contradiction: Local hidden variable theories must satisfy Bell's inequality,
# but QM violates it
_qm_violates_bell = contradiction(
    c_local_hv_incompatible_with_qm,
    c_bell_inequality,
    reason="Bell's inequality (@c_bell_inequality) is a necessary condition for any "
    "local hidden variable theory. QM predictions violate this inequality "
    "(@c_local_hv_incompatible_with_qm, @c_qm_violates_bell_inequality). Therefore "
    "QM cannot be described by any local hidden variable theory.",
)

# Contradiction: Locality (no instantaneous influence) vs. QM predictions
# (which require nonlocality or hidden variables that conflict with locality)
_locality_vs_qm_predictions = contradiction(
    c_locality_constraint_formal,
    c_locality_lorentz_invariance_conflict,
    reason="The locality constraint (@c_locality_constraint_formal) prohibits instantaneous "
    "influence between distant measurements. However, any theory reproducing QM predictions "
    "must have such instantaneous influence (@c_locality_lorentz_invariance_conflict), "
    "violating the locality requirement.",
)

# ============================================================
# Strategies — reasoning connections
# ============================================================

# Strategy 1: From EPR argument to hidden variable motivation
_strat_epr_to_hv = abduction(
    observation=c_qm_incomplete,
    hypothesis=c_epr_motivation_hidden_variables,
    alternative=c_qm_is_complete,
    reason="EPR argue that QM is incomplete (@c_qm_incomplete), which motivates the search "
    "for additional variables (hidden variables) that would restore causality and locality "
    "(@c_epr_motivation_hidden_variables). Bohr's response is that QM is complete "
    "(@c_qm_is_complete).",
)

# Strategy 2: Singlet anticorrelation + locality → predetermination
_strat_locality_to_predetermination = deduction(
    [c_singlet_perfect_anticorrelation, c_locality_constraint_formal],
    c_locality_implies_predetermination,
    reason="In the singlet state, measuring particle 1 predicts the result of measuring "
    "particle 2 (@c_singlet_perfect_anticorrelation). If locality holds (the result at 2 "
    "doesn't depend on the setting at 1, @c_locality_constraint_formal), then the result "
    "at 2 must be predetermined. Since the wave function doesn't determine individual "
    "results, this requires hidden variables (@c_locality_implies_predetermination).",
)

# Strategy 3: Predetermination → hidden variable formalism
_strat_predetermination_to_hv_formalism = deduction(
    [c_locality_implies_predetermination],
    c_hidden_variables_complete_specification,
    reason="If measurement results are predetermined despite the wave function not "
    "specifying them (@c_locality_implies_predetermination), then a more complete "
    "specification via hidden variables $\\lambda$ must exist (@c_hidden_variables_complete_specification).",
)

# Strategy 4: Hidden variables + locality → Bell inequality form
_strat_hv_locality_to_bell_form = deduction(
    [c_hidden_variables_complete_specification, c_locality_constraint_formal],
    c_local_hidden_correlation_form,
    reason="Hidden variables specify complete state (@c_hidden_variables_complete_specification). "
    "Locality means outcomes depend only on local settings and $\\lambda$ "
    "(@c_locality_constraint_formal). Therefore the correlation must take the local "
    "form $P(\\vec{a}, \\vec{b}) = \\int d\\lambda \\rho(\\lambda) A(\\vec{a}, \\lambda) B(\\vec{b}, \\lambda)$ "
    "(@c_local_hidden_correlation_form).",
)

# Strategy 5: Local form → Bell inequality
_strat_local_form_to_inequality = deduction(
    [c_local_hidden_correlation_form],
    c_bell_inequality,
    reason="From the mathematical structure of the local hidden variable correlation form "
    "(@c_local_hidden_correlation_form), bounded measurement outcomes ($\\pm 1$) imply "
    "Bell's inequality $|P(\\vec{a}, \\vec{b}) - P(\\vec{a}, \\vec{c})| \\leq 1 + P(\\vec{b}, \\vec{c})$ "
    "for all measurement directions (@c_bell_inequality).",
)

# Strategy 6: QM formalism → correlation prediction
_strat_qm_to_correlation = deduction(
    [c_singlet_perfect_anticorrelation],
    c_qm_correlation_function,
    reason="The singlet state formalism plus standard quantum mechanical rules for calculating "
    "expectation values yields the correlation function $E_{QM}(\\vec{a}, \\vec{b}) = -\\vec{a} \\cdot \\vec{b}$. "
    "Starting from perfect anticorrelation (@c_singlet_perfect_anticorrelation), QM formalism "
    "predicts the correlation varies smoothly as the cosine of the angle between measurement directions "
    "(@c_qm_correlation_function).",
    background=[s_singlet_spin_state, s_qm_correlation_singlet],
)

# Strategy 7: Local theories give wrong functional form
_strat_local_theories_nonstationary = deduction(
    [c_local_hidden_correlation_form, c_bell_inequality],
    c_local_theory_nonstationary,
    reason="Any local hidden variable theory must satisfy Bell's inequality "
    "(@c_bell_inequality). The QM correlation $-\\vec{a} \\cdot \\vec{b}$ is stationary at "
    "its minimum, but functions satisfying Bell's inequality cannot be stationary "
    "at -1 (@c_local_theory_nonstationary).",
)

# Strategy 8: QM prediction vs. Bell inequality (numerical comparison)
_strat_qm_violates_inequality = abduction(
    observation=c_qm_violates_bell_inequality,
    hypothesis=c_local_hv_incompatible_with_qm,
    alternative=alt_locality_violates_qm,
    reason="The QM correlation function violates Bell's inequality for specific angle choices "
    "(@c_qm_violates_bell_inequality). This means either (1) local hidden variables cannot reproduce QM "
    "(@c_local_hv_incompatible_with_qm) or (2) QM itself is nonlocal (@alt_locality_violates_qm).",
    background=[c_bell_inequality, c_qm_correlation_function],
)

# Strategy 9: Main theorem — local HV incompatible with QM
_strat_main_theorem = deduction(
    [c_local_hidden_correlation_form, c_bell_inequality, c_qm_correlation_function,
     c_qm_violates_bell_inequality],
    c_bell_theorem,
    reason="Local hidden variable theories produce correlations of a specific form "
    "(@c_local_hidden_correlation_form) that must satisfy Bell's inequality "
    "(@c_bell_inequality). QM predicts a different correlation (@c_qm_correlation_function) "
    "that violates this inequality (@c_qm_violates_bell_inequality). Therefore "
    "no local hidden variable theory can reproduce all QM predictions (@c_bell_theorem).",
)

# Strategy 10: Implications for locality and Lorentz invariance
_strat_locality_lorentz_implication = deduction(
    [c_bell_theorem, c_local_hv_incompatible_with_qm],
    c_locality_lorentz_invariance_conflict,
    reason="Since local hidden variables cannot reproduce QM (@c_bell_theorem, "
    "@c_local_hv_incompatible_with_qm), any theory that adds hidden variables to QM "
    "must include nonlocal influences. These influences propagate instantaneously, "
    "violating Lorentz invariance (@c_locality_lorentz_invariance_conflict).",
)

# Strategy 11: The locality assumption as the essential difficulty
_strat_locality_essential = noisy_and(
    [c_bell_theorem, c_locality_lorentz_invariance_conflict],
    c_locality_creates_difficulty,
    reason="Any theory preserving locality cannot reproduce QM (@c_bell_theorem), while any "
    "theory reproducing QM requires instantaneous nonlocality (@c_locality_lorentz_invariance_conflict). "
    "This shows that locality is the essential difficulty that makes local hidden variable "
    "theories incompatible with QM (@c_locality_creates_difficulty).",
)

# Strategy 12: Approximation is impossible
_strat_approximation_impossible = deduction(
    [c_bell_inequality, c_qm_violates_bell_inequality],
    c_approximation_impossible,
    reason="Bell's inequality is not just violated but violated by a finite margin "
    "(@c_qm_violates_bell_inequality). Therefore no local hidden variable theory can "
    "approximate QM predictions arbitrarily closely — there is a fundamental lower bound "
    "on the discrepancy (@c_approximation_impossible).",
)

# Strategy 13: Alternative explanation — superdeterminism
_strat_superdeterminism_alternative = abduction(
    observation=c_bell_theorem,
    hypothesis=alt_superdeterminism,
    alternative=c_local_hv_incompatible_with_qm,
    reason="Bell's theorem assumes that measurement settings can be chosen independently "
    "of the hidden variables $\\lambda$. If this assumption fails (settings and $\\lambda$ "
    "are correlated), then a local hidden variable theory could potentially reproduce QM "
    "(@alt_superdeterminism). This is the 'superdeterminism' loophole.",
    background=[c_locality_constraint_formal],
)

# Strategy 14: Alternative explanation — retrocausality
_strat_retrocausality_alternative = abduction(
    observation=c_bell_theorem,
    hypothesis=alt_retrocausality,
    alternative=c_local_hv_incompatible_with_qm,
    reason="If hidden variables can influence events backwards in time, measurement settings "
    "could be correlated with particle properties without requiring superluminal influence "
    "(@alt_retrocausality). This offers another potential way around Bell's theorem, "
    "though it radically changes our conception of causality.",
)

# Strategy 15: Generalization beyond spin-1/2
_strat_generalization = deduction(
    [c_bell_theorem],
    c_bell_result_generalizes,
    reason="Bell's proof for spin-1/2 particles can be extended to any quantum system "
    "by considering two-dimensional subspaces. The incompatibility between locality and "
    "QM predictions is therefore general, not specific to the spin case (@c_bell_result_generalizes).",
)

# Strategy 16: Experimental implications — time-varying settings
_strat_experimental_implications = deduction(
    [c_locality_lorentz_invariance_conflict, c_bell_theorem],
    c_time_varying_settings_crucial,
    reason="Since any hidden variable theory reproducing QM requires instantaneous influence "
    "(@c_locality_lorentz_invariance_conflict), experiments where measurement settings are "
    "changed during particle flight are crucial (@c_time_varying_settings_crucial). Such "
    "experiments would prevent any light-speed signal from communicating settings between "
    "measurements, closing the 'locality' loophole.",
)
