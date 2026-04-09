"""Section 2: Two-Particle Argument — Wave packet reduction, the EPR thought experiment, and the conclusion that QM is incomplete."""

from gaia.lang import claim, setting, deduction, infer

# ── Two-system setup ──

s_two_system_setup = setting(
    "Two systems, I and II, are permitted to interact from time $t=0$ to $t=T$, "
    "after which there is no longer any interaction between them. The states of "
    "both systems before $t=0$ are known, and the state of the combined system "
    "I+II at any subsequent time can be calculated via Schrödinger's equation. "
    "Let $\\Psi(x_1, x_2)$ designate the wave function of the combined system for "
    "any $t > T$.",
    title="Two-system interaction setup",
)

# ── Cannot calculate individual states without measurement ──

c_individual_state_unmeasurable = claim(
    "After the interaction period, the state in which either system is left cannot "
    "be calculated from the combined wave function alone. According to quantum "
    "mechanics, this can be done only with the help of further measurements, by "
    "a process known as the **reduction of the wave packet**.",
    title="Individual post-interaction states require measurement",
)

# ── Wave packet reduction: measurement of A ──

s_wave_packet_reduction = setting(
    "Let $a_1, a_2, a_3, \\ldots$ be the eigenvalues of some physical quantity $A$ "
    "pertaining to system I, with eigenfunctions $u_1(x_1), u_2(x_1), \\ldots$. "
    "The combined wave function can be expanded as:\n\n"
    "$$\\Psi(x_1, x_2) = \\sum_n \\psi_n(x_2) u_n(x_1)$$\n\n"
    "If quantity $A$ is measured on system I and found to have value $a_k$, then "
    "system I is left in state $u_k(x_1)$ and system II is left in state "
    "$\\psi_k(x_2)$.",
    title="Wave packet reduction for measurement of A",
)

# ── Alternative measurement of B gives different state for II ──

s_alternative_measurement = setting(
    "If instead of $A$, another quantity $B$ with eigenvalues $b_1, b_2, \\ldots$ "
    "and eigenfunctions $v_1(x_1), v_2(x_1), \\ldots$ is chosen, the combined "
    "wave function has an alternative expansion:\n\n"
    "$$\\Psi(x_1, x_2) = \\sum_s \\phi_s(x_2) v_s(x_1)$$\n\n"
    "If $B$ is measured on system I and found to have value $b_r$, then system II "
    "is left in state $\\phi_r(x_2)$.",
    title="Alternative expansion for measurement of B",
)

# ── Two different wave functions for same reality ──

c_two_states_for_same_reality = claim(
    "As a consequence of two different measurements performed upon system I, "
    "system II may be left in states with two different wave functions "
    "(e.g., $\\psi_k$ and $\\phi_r$). Since at the time of measurement the two "
    "systems no longer interact, no real change can take place in system II in "
    "consequence of anything done to system I. Thus it is possible to assign two "
    "different wave functions to the same reality (system II after the interaction).",
    title="Two different wave functions assigned to the same reality",
)

# ── Specific example: two particles, position and momentum ──

s_two_particle_specific = setting(
    "Consider two particles with combined wave function:\n\n"
    "$$\\Psi(x_1, x_2) = \\int_{-\\infty}^{\\infty} e^{(2\\pi i/h)(x_1 - x_2 + x_0)p} dp$$\n\n"
    "where $x_0$ is some constant. If $A$ is the momentum of particle 1, its "
    "eigenfunctions are $u_p(x_1) = e^{(2\\pi i/h)px_1}$ with eigenvalue $p$. "
    "If $B$ is the position of particle 1, its eigenfunctions are delta functions "
    "$\\delta(x_1 - x)$ with eigenvalue $x$.",
    title="Specific two-particle example with position and momentum",
)

# ── Measuring momentum of particle 1 → momentum of particle 2 ──

c_measure_momentum = claim(
    "Measuring the momentum of particle 1 yields a definite value $p$. After "
    "measurement, particle 2 is left in the state "
    "$\\psi_p(x_2) = e^{-(2\\pi i/h)(x_2 - x_0)p}$, which is an eigenfunction "
    "of the momentum operator $P = (h/2\\pi i)\\partial/\\partial x_2$ with "
    "eigenvalue $-p$. Thus the momentum of particle 2 has the definite value $-p$.",
    title="Measuring momentum of particle 1 gives momentum of particle 2",
)

# ── Measuring position of particle 1 → position of particle 2 ──

c_measure_position = claim(
    "Measuring the position of particle 1 yields a definite value $x$. After "
    "measurement, particle 2 is left in the state $\\phi_x(x_2) = h\\delta(x - x_2 + x_0)$, "
    "which is an eigenfunction of the position operator $Q = x_2$ with eigenvalue "
    "$x + x_0$. Thus the position of particle 2 has the definite value $x + x_0$.",
    title="Measuring position of particle 1 gives position of particle 2",
)

# ── Both P and Q are elements of reality for system II ──

c_both_elements_of_reality = claim(
    "By measuring either the momentum or position of particle 1, we are in a "
    "position to predict with certainty, and without in any way disturbing particle 2, "
    "either the value of its momentum $P$ (namely $-p$) or the value of its position "
    "$Q$ (namely $x + x_0$). In accordance with the criterion of reality "
    "(@s_criterion_of_reality), in the first case $P$ is an element of reality, "
    "and in the second case $Q$ is an element of reality. Since both wave functions "
    "belong to the same reality (particle 2 after interaction), both $P$ and $Q$ "
    "are elements of reality for system II.",
    title="Both momentum and position are elements of reality for system II",
)

# ── P and Q do not commute ──

c_pq_noncommuting = claim(
    "The momentum operator $P = (h/2\\pi i)\\partial/\\partial x_2$ and the position "
    "operator $Q = x_2$ do not commute: $PQ - QP = h/2\\pi i \\neq 0$.",
    title="Momentum and position operators do not commute",
)

# ── Negation of (1) leads to negation of (2) ──

c_negation_1_implies_negation_2 = claim(
    "Previously it was shown (@c_initial_dilemma) that either (1) the QM description "
    "is not complete, or (2) non-commuting quantities cannot have simultaneous reality. "
    "Starting with the assumption that the wave function does give a complete "
    "description of physical reality (@c_qm_assumes_complete), we arrived at the "
    "conclusion that two physical quantities with non-commuting operators ($P$ and $Q$) "
    "can have simultaneous reality (@c_both_elements_of_reality). Thus the negation "
    "of (1) leads to the negation of the only other alternative (2).",
    title="Negation of (1) implies negation of (2)",
)

# ── Final conclusion ──

c_qm_incomplete = claim(
    "The quantum-mechanical description of physical reality given by wave functions "
    "is not complete.",
    title="Final conclusion: QM description is incomplete",
)

# ── Anticipated objection ──

c_anticipated_objection = claim(
    "One could object to the conclusion on the grounds that the criterion of reality "
    "is not sufficiently restrictive. If one insists that two or more physical "
    "quantities can be regarded as simultaneous elements of reality only when they "
    "can be simultaneously measured or predicted, then since only one of $P$ or $Q$ "
    "(not both simultaneously) can be predicted, they would not be simultaneously real. "
    "However, this makes the reality of $P$ and $Q$ depend upon the process of "
    "measurement carried out on the first system, which does not disturb the second "
    "system in any way. No reasonable definition of reality could be expected to "
    "permit this.",
    title="Anticipated objection: reality should not depend on remote measurement",
)

# ── Open question ──

c_complete_theory_possible = claim(
    "While the wave function does not provide a complete description of physical "
    "reality, the question of whether or not such a description exists is left open. "
    "EPR believe, however, that such a theory is possible.",
    title="A more complete theory may be possible",
)

# ── Import premises from Section 1 ──

from .motivation import (
    s_completeness_condition,
    s_criterion_of_reality,
    s_qm_state_concept,
    c_initial_dilemma,
    c_qm_assumes_complete,
)

# ── Strategies (Pass 2: Connect) ──

# Wave packet reduction → two different states for II
_infer_two_states = infer(
    [c_individual_state_unmeasurable],
    c_two_states_for_same_reality,
    reason="According to the QM process of wave packet reduction "
    "(@c_individual_state_unmeasurable), measuring $A$ on system I leaves II in "
    "state $\\psi_k$, while measuring $B$ leaves II in state $\\phi_r$. Since the "
    "two systems no longer interact (@s_two_system_setup), no real change occurs "
    "in II. Thus two different wave functions describe the same reality.",
    background=[s_wave_packet_reduction, s_alternative_measurement, s_two_system_setup],
)

# Momentum measurement → definite momentum for particle 2
_ded_momentum_meas = deduction(
    [c_two_states_for_same_reality],
    c_measure_momentum,
    reason="Substituting $A$ = momentum of particle 1 into the general wave packet "
    "reduction (@s_wave_packet_reduction), the expansion in eigenfunctions of "
    "momentum yields $\\psi_p(x_2) = e^{-(2\\pi i/h)(x_2 - x_0)p}$, which is "
    "an eigenfunction of the momentum operator for particle 2 with eigenvalue $-p$.",
    background=[s_two_particle_specific, s_wave_packet_reduction],
)

# Position measurement → definite position for particle 2
_ded_position_meas = deduction(
    [c_two_states_for_same_reality],
    c_measure_position,
    reason="Substituting $B$ = position of particle 1 into the alternative expansion "
    "(@s_alternative_measurement), the expansion in position eigenfunctions yields "
    "$\\phi_x(x_2) = h\\delta(x - x_2 + x_0)$, which is an eigenfunction of the "
    "position operator for particle 2 with eigenvalue $x + x_0$.",
    background=[s_two_particle_specific, s_alternative_measurement],
)

# Both P and Q are elements of reality for system II
_infer_both_reality = infer(
    [c_measure_momentum, c_measure_position],
    c_both_elements_of_reality,
    reason="Measuring momentum of particle 1 predicts with certainty the momentum of "
    "particle 2 (@c_measure_momentum) without disturbing it. By @s_criterion_of_reality, "
    "this makes momentum an element of reality for particle 2. Similarly, measuring "
    "position of particle 1 predicts with certainty the position of particle 2 "
    "(@c_measure_position) without disturbing it, making position an element of reality. "
    "Since both predictions refer to the same particle 2 (after interaction), both $P$ "
    "and $Q$ are simultaneously elements of reality for system II.",
    background=[s_criterion_of_reality],
)

# P and Q do not commute
_ded_pq_noncommute = deduction(
    [c_measure_momentum, c_measure_position],
    c_pq_noncommuting,
    reason="The momentum operator $P = (h/2\\pi i)\\partial/\\partial x_2$ and "
    "position operator $Q = x_2$ satisfy $PQ - QP = h/2\\pi i \\neq 0$, a standard "
    "result of the canonical commutation relation.",
)

# Negation of (1) leads to negation of (2)
_infer_negation_chain = infer(
    [c_initial_dilemma, c_qm_assumes_complete, c_both_elements_of_reality, c_pq_noncommuting],
    c_negation_1_implies_negation_2,
    reason="The initial dilemma (@c_initial_dilemma) states: either (1) QM is incomplete "
    "or (2) non-commuting quantities lack simultaneous reality. Assuming QM is complete "
    "(@c_qm_assumes_complete, i.e., negating (1)), the two-particle argument shows "
    "non-commuting $P$ and $Q$ (@c_pq_noncommuting) have simultaneous reality "
    "(@c_both_elements_of_reality), which negates (2). Thus negation of (1) implies "
    "negation of (2).",
)

# Final conclusion: QM is incomplete
_ded_qm_incomplete = deduction(
    [c_negation_1_implies_negation_2],
    c_qm_incomplete,
    reason="The argument shows that assuming completeness (negating (1)) leads to the "
    "negation of (2), i.e., non-commuting quantities CAN have simultaneous reality. "
    "But (2) was the only alternative to (1) in the initial dilemma. Since assuming "
    "the negation of (1) leads to a contradiction with the dilemma structure, (1) "
    "must hold: the QM description of reality is not complete.",
)

# Anticipated objection: no reasonable definition allows this
_infer_objection = infer(
    [c_both_elements_of_reality],
    c_anticipated_objection,
    reason="The objection that $P$ and $Q$ are not simultaneously real because they "
    "cannot be simultaneously predicted would make reality depend on a measurement "
    "performed on a spatially separated system that does not disturb system II. "
    "EPR argue no reasonable definition of reality could permit this.",
    background=[s_criterion_of_reality, s_two_system_setup],
)
