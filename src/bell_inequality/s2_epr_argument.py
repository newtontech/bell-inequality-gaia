"""Section 2: The EPR Two-Particle Argument

EPR construct a two-particle system that interacts then separates. By measuring different
physical quantities on particle I, one can predict with certainty — without disturbing
particle II — either its momentum or its position. Since momentum and position correspond
to non-commuting operators, both are elements of reality for particle II. This contradicts
the alternative (2) from the initial dilemma, forcing the conclusion that quantum mechanics
is incomplete.

Reference: Einstein, Podolsky, Rosen (1935) Phys. Rev. 47, 779-780.
"""

from gaia.lang import (
    claim, setting, deduction, abduction, noisy_and,
    contradiction, complement,
)
from .motivation import (
    c_criterion_of_reality,
    c_initial_dilemma,
    c_qm_assumes_complete,
    c_noncommuting_precludes_simultaneous,
    s_completeness_condition,
    s_noncommuting_definition,
)

# ============================================================
# Settings — formal setup for two-particle system
# ============================================================

s_two_systems = setting(
    "Two systems, I and II, interact from time $t = 0$ to $t = T$, after which there is "
    "no longer any interaction between them. The states of both systems before $t = 0$ are known.",
    title="Two-system interaction setup",
)

s_schrodinger_evolution = setting(
    "Given the initial states and the interaction, one can calculate via Schrödinger's equation "
    "the state of the combined system I+II at any subsequent time $t > T$. Let $\\Psi$ designate "
    "the corresponding wave function. However, the individual state of either system after "
    "interaction can only be determined via further measurements (wave packet reduction).",
    title="Schrödinger evolution of combined system",
)

s_wave_packet_reduction_obs_a = setting(
    "For a physical quantity $A$ of system I with eigenvalues $a_1, a_2, \\ldots$ and "
    "eigenfunctions $u_1(x_1), u_2(x_1), \\ldots$, the combined wave function can be expanded as "
    "$\\Psi(x_1, x_2) = \\sum_n \\phi_n(x_2)\\,u_n(x_1)$. If $A$ is measured and yields $a_k$, "
    "then after measurement system I is in state $u_k(x_1)$ and system II is in state $\\phi_k(x_2)$. "
    "This is the process of wave packet reduction.",
    title="Wave packet reduction (observable A)",
)

s_wave_packet_reduction_obs_b = setting(
    "For a different physical quantity $B$ of system I with eigenvalues $b_1, b_2, \\ldots$ and "
    "eigenfunctions $v_1(x_1), v_2(x_1), \\ldots$, the same wave function can be expanded as "
    "$\\Psi(x_1, x_2) = \\sum_s \\psi_s(x_2)\\,v_s(x_1)$. If $B$ is measured and yields $b_r$, "
    "then after measurement system I is in state $v_r(x_1)$ and system II is in state $\\psi_r(x_2)$.",
    title="Wave packet reduction (observable B)",
)

s_two_particle_wavefunction = setting(
    "For the concrete two-particle example, the combined wave function is "
    "$\\Psi(x_1, x_2) = \\int_{-\\infty}^{\\infty} \\exp\\left[\\frac{2\\pi i}{h}(x_1 - x_2 + x_0)p\\right] dp$, "
    "where $x_0$ is a constant.",
    title="Two-particle wave function",
)

# ============================================================
# Claims — the core argument
# ============================================================

c_two_measurements_two_states = claim(
    "As a consequence of two different measurements performed upon system I "
    "(measuring observable $A$ or observable $B$), the second system II may be left in states "
    "with two different wave functions ($\\phi_k$ from measuring $A$, or $\\psi_s$ from measuring $B$).",
    title="Two measurements yield two different wave functions for system II",
    metadata={"source": "artifacts/1935_einstein_epr/epr_1935_full_text.txt"},
)

c_no_interaction_no_disturbance = claim(
    "Since at the time of measurement ($t > T$) the two systems no longer interact, "
    "no real change can take place in system II as a consequence of anything that may be "
    "done to system I. This is a statement of the absence of interaction between the two systems.",
    title="No disturbance to system II from measurement on I",
    metadata={"source": "artifacts/1935_einstein_epr/epr_1935_full_text.txt"},
)

c_two_wavefunctions_same_reality = claim(
    "It is possible to assign two different wave functions ($\\phi_k$ and $\\psi_s$) to the same "
    "reality — namely, system II after the interaction with system I. This follows because "
    "the choice of which wave function describes system II depends on which measurement is "
    "performed on system I, but system II is not disturbed by that measurement.",
    title="Two wave functions describe the same reality",
)

c_momentum_prediction = claim(
    "In the two-particle example, if the momentum $p$ of particle I is measured "
    "(where $p$ is the eigenvalue), then particle II is left in the eigenfunction "
    "$\\phi_p(x_2) = \\exp[-(2\\pi i/h)(x_2 - x_0)p]$, which is the eigenfunction of the "
    "momentum operator $P = (h/2\\pi i)\\,\\partial/\\partial x_2$ corresponding to eigenvalue $-p$. "
    "Thus, measuring momentum $p$ on particle I allows predicting with certainty that particle II "
    "has momentum $-p$.",
    title="Measuring momentum of I predicts momentum of II",
    metadata={"source": "artifacts/1935_einstein_epr/epr_1935_full_text.txt, Eqs. 10-13"},
)

c_position_prediction = claim(
    "In the two-particle example, if the position (coordinate) $x$ of particle I is measured "
    "(eigenvalue $x$), then particle II is left in the eigenfunction "
    "$\\psi_x(x_2) = h\\,\\delta(x_2 - x + x_0)$, where $\\delta$ is the Dirac delta function, "
    "corresponding to the eigenvalue $x + x_0$ of the position operator $Q = x_2$ of particle II. "
    "Thus, measuring position $x$ on particle I allows predicting with certainty that particle II "
    "has position $x + x_0$.",
    title="Measuring position of I predicts position of II",
    metadata={"source": "artifacts/1935_einstein_epr/epr_1935_full_text.txt, Eqs. 14-16"},
)

c_pq_noncommuting = claim(
    "The momentum operator $P = (h/2\\pi i)\\,\\partial/\\partial x_2$ and position operator "
    "$Q = x_2$ for particle II do not commute: $PQ - QP = h/(2\\pi i) \\neq 0$. "
    "Thus the wave functions $\\phi_k$ and $\\psi_s$ obtained from different measurements on "
    "particle I are eigenfunctions of two non-commuting operators.",
    title="P and Q for particle II are non-commuting",
    metadata={"source": "artifacts/1935_einstein_epr/epr_1935_full_text.txt, Eq. 17"},
)

c_predict_both_without_disturbance = claim(
    "By measuring either observable $A$ or observable $B$ on system I, we are in a position "
    "to predict with certainty, and without in any way disturbing system II, either the value "
    "of the quantity $P$ (i.e., momentum $-p$) or the value of the quantity $Q$ (i.e., position "
    "$x + x_0$) for system II.",
    title="Both P and Q predictable without disturbing II",
    metadata={"source": "artifacts/1935_einstein_epr/epr_1935_full_text.txt"},
)

c_p_element_of_reality = claim(
    "Since we can predict with certainty the value of $P$ (momentum $-p$) for system II "
    "without disturbing it — by measuring the momentum of particle I — the quantity $P$ "
    "must be considered an element of reality for system II, in accordance with the "
    "EPR criterion of reality.",
    title="P (momentum) is an element of reality for II",
)

c_q_element_of_reality = claim(
    "Since we can predict with certainty the value of $Q$ (position $x + x_0$) for system II "
    "without disturbing it — by measuring the position of particle I — the quantity $Q$ "
    "must be considered an element of reality for system II, in accordance with the "
    "EPR criterion of reality.",
    title="Q (position) is an element of reality for II",
)

c_p_and_q_simultaneous_reality = claim(
    "Both $P$ (momentum) and $Q$ (position) for particle II are simultaneous elements of "
    "reality, because both wave functions $\\phi_k$ and $\\psi_s$ belong to the same reality "
    "(particle II after interaction). Despite $P$ and $Q$ having non-commuting operators "
    "($PQ - QP \\neq 0$), both quantities have definite values that can be predicted without "
    "disturbing the system.",
    title="P and Q have simultaneous reality",
)

c_negation_1_implies_negation_2 = claim(
    "Starting from the assumption that the wave function gives a complete description of "
    "physical reality (negation of alternative (1) in the initial dilemma), EPR arrive at "
    "the conclusion that two physical quantities with non-commuting operators CAN have "
    "simultaneous reality — which contradicts alternative (2) in the initial dilemma. "
    "Thus the negation of (1) leads to the negation of (2): if QM is complete, then "
    "non-commuting quantities must have simultaneous reality, contradicting the initial dilemma.",
    title="Negation of (1) implies negation of (2)",
)

c_qm_incomplete = claim(
    "The quantum-mechanical description of physical reality given by wave functions is not "
    "complete. This conclusion is forced because assuming completeness leads to the conclusion "
    "that non-commuting quantities have simultaneous reality, contradicting one horn of the "
    "initial dilemma. Since the assumption of completeness contradicts the logical structure "
    "derived from QM's own formalism, QM must be incomplete.",
    title="QM description is incomplete (EPR conclusion)",
)

c_reality_independent_of_measurement = claim(
    "The reality of quantities $P$ and $Q$ for system II should not depend upon the process "
    "of measurement carried out on system I, which does not disturb system II in any way. "
    "No reasonable definition of reality could be expected to permit this dependence.",
    title="Reality cannot depend on distant measurement",
)

c_complete_theory_possible = claim(
    "While EPR have shown that the wave function does not provide a complete description "
    "of physical reality, they left open the question of whether such a description exists. "
    "They believe that such a more complete theory is possible.",
    title="A complete theory may exist (EPR belief)",
)

# ============================================================
# Abduction alternatives — named for review sidecar
# ============================================================

alt_momentum_formal_not_real = claim(
    "The predictability of particle II's momentum from a measurement on particle I "
    "is merely a formal mathematical property of the wave function, not evidence of "
    "a pre-existing element of reality in particle II. The correlation arises from "
    "the measurement process on system I, not from an independent property of system II.",
    title="Alternative: momentum predictability is formal, not real",
)

alt_position_formal_not_real = claim(
    "The predictability of particle II's position from a measurement on particle I "
    "is a consequence of the entangled wave function, not evidence of an independent "
    "element of reality. The definite position value only becomes meaningful upon "
    "measurement of system I.",
    title="Alternative: position predictability is formal, not real",
)

# ============================================================
# Operators — logical constraints
# ============================================================

# P and Q having simultaneous reality contradicts the claim that non-commuting quantities
# cannot have simultaneous reality. This is the core contradiction that drives the argument.
_simultaneous_reality_vs_noncommuting = contradiction(
    c_p_and_q_simultaneous_reality,
    c_noncommuting_precludes_simultaneous,
    reason="EPR show P and Q (non-commuting) have simultaneous reality, contradicting the "
    "QM principle that non-commuting quantities cannot simultaneously be real.",
)

# ============================================================
# Strategies — reasoning connections (Pass 2)
# ============================================================

# Strategy 1: From momentum prediction + no disturbance → P is element of reality
_strat_p_reality = abduction(
    observation=c_momentum_prediction,
    hypothesis=c_p_element_of_reality,
    alternative=alt_momentum_formal_not_real,
    reason="By measuring momentum $p$ on particle I, we can predict with certainty that "
    "particle II has momentum $-p$ (@c_momentum_prediction), without any disturbance to "
    "particle II (@c_no_interaction_no_disturbance). By the EPR criterion of reality "
    "(@c_criterion_of_reality), this makes $P$ an element of reality for II.",
    background=[c_criterion_of_reality, c_no_interaction_no_disturbance],
)

# Strategy 2: From position prediction + no disturbance → Q is element of reality
_strat_q_reality = abduction(
    observation=c_position_prediction,
    hypothesis=c_q_element_of_reality,
    alternative=alt_position_formal_not_real,
    reason="By measuring position $x$ on particle I, we can predict with certainty that "
    "particle II has position $x + x_0$ (@c_position_prediction), without any disturbance "
    "to particle II (@c_no_interaction_no_disturbance). By the EPR criterion of reality "
    "(@c_criterion_of_reality), this makes $Q$ an element of reality for II.",
    background=[c_criterion_of_reality, c_no_interaction_no_disturbance],
)

# Strategy 3: Both P and Q are elements of reality → simultaneous reality
_strat_simultaneous = noisy_and(
    [c_p_element_of_reality, c_q_element_of_reality, c_pq_noncommuting, c_two_wavefunctions_same_reality],
    c_p_and_q_simultaneous_reality,
    reason="Both $P$ (@c_p_element_of_reality) and $Q$ (@c_q_element_of_reality) are elements "
    "of reality for system II. Despite their operators being non-commuting (@c_pq_noncommuting), "
    "both wave functions belong to the same reality (@c_two_wavefunctions_same_reality). "
    "Therefore $P$ and $Q$ have simultaneous reality.",
    background=[s_noncommuting_definition],
)

# Strategy 4: Negation of (1) implies negation of (2)
_strat_negation_chain = deduction(
    [c_qm_assumes_complete, c_p_and_q_simultaneous_reality, c_initial_dilemma],
    c_negation_1_implies_negation_2,
    reason="Assuming QM is complete (@c_qm_assumes_complete), and given that non-commuting "
    "quantities $P$ and $Q$ have simultaneous reality (@c_p_and_q_simultaneous_reality), "
    "this contradicts alternative (2) of the initial dilemma (@c_initial_dilemma) which states "
    "that non-commuting quantities cannot have simultaneous reality. Thus negating (1) leads "
    "to negating (2).",
    background=[s_completeness_condition],
)

# Strategy 5: The final conclusion — QM is incomplete
_strat_qm_incomplete = deduction(
    [c_negation_1_implies_negation_2, c_initial_dilemma],
    c_qm_incomplete,
    reason="The initial dilemma (@c_initial_dilemma) states: (1) QM is incomplete, or (2) "
    "non-commuting quantities cannot have simultaneous reality. Since negating (1) forces "
    "negating (2) (@c_negation_1_implies_negation_2), and both alternatives cannot be "
    "simultaneously false (they are the only two options), alternative (1) must hold: "
    "QM is incomplete.",
)

# Strategy 6: Reality independence argument
_strat_reality_independent = noisy_and(
    [c_no_interaction_no_disturbance, c_predict_both_without_disturbance],
    c_reality_independent_of_measurement,
    reason="Since measurement on system I does not disturb system II "
    "(@c_no_interaction_no_disturbance), and both quantities can be predicted "
    "(@c_predict_both_without_disturbance), it would be unreasonable for the reality "
    "of $P$ and $Q$ to depend on which measurement is chosen on the distant system I.",
)

# Strategy 7: Two wave functions for the same reality
_strat_two_wf_same_reality = noisy_and(
    [c_two_measurements_two_states, c_no_interaction_no_disturbance],
    c_two_wavefunctions_same_reality,
    reason="Two different measurements on system I produce two different wave functions "
    "for system II (@c_two_measurements_two_states). Since system II is not disturbed "
    "(@c_no_interaction_no_disturbance), both wave functions must describe the same "
    "physical reality.",
)

# Strategy 8: From specific predictions to the general claim about predictability
_strat_predict_both = deduction(
    [c_momentum_prediction, c_position_prediction, c_no_interaction_no_disturbance],
    c_predict_both_without_disturbance,
    reason="Measuring momentum on I predicts momentum of II (@c_momentum_prediction), "
    "and measuring position on I predicts position of II (@c_position_prediction). "
    "Neither measurement disturbs II (@c_no_interaction_no_disturbance). Therefore both "
    "$P$ and $Q$ can be predicted with certainty without disturbing II.",
)

# Exported conclusions are listed in __init__.py __all__
