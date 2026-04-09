"""Section 1: EPR Setup — Completeness, Criterion of Reality, and the Initial Dilemma

Einstein, Podolsky, and Rosen (1935) begin by distinguishing objective reality from
physical concepts, then propose a criterion of reality and a condition of completeness.
Using a single-particle illustration, they derive the initial dilemma: either quantum
mechanics is incomplete, or non-commuting physical quantities cannot have simultaneous reality.

Reference: Einstein, Podolsky, Rosen (1935) Phys. Rev. 47, 777-780.
"""

from gaia.lang import claim, setting, question, contradiction

# ============================================================
# Settings — definitions and formal setups
# ============================================================

s_objective_reality = setting(
    "There is a distinction between the objective reality, which is independent of any theory, "
    "and the physical concepts with which the theory operates. These concepts are intended to "
    "correspond with the objective reality.",
    title="Objective reality vs. physical concepts",
)

s_completeness_condition = setting(
    "A necessary condition for a complete physical theory: every element of the physical "
    "reality must have a counterpart in the physical theory. EPR call this the *condition of completeness*.",
    title="Condition of completeness",
)

s_wave_function_state = setting(
    "In quantum mechanics, the state of a system is completely characterized by the wave function "
    "$\\psi$, which is a function of the variables chosen to describe the system's behavior.",
    title="Wave function as complete state description",
)

s_observable_operator = setting(
    "Corresponding to each physically observable quantity $A$ in quantum mechanics, there is "
    "a Hermitian operator (designated by the same letter). If $\\psi$ is an eigenfunction "
    "of operator $A$, i.e., $A\\psi = a\\psi$ where $a$ is a number, then the physical quantity "
    "$A$ has with certainty the value $a$.",
    title="Observable-operator correspondence",
)

s_momentum_operator = setting(
    "The operator corresponding to the momentum of a single particle is "
    "$p = (h/2\\pi i)\\,\\partial/\\partial x$, where $h$ is Planck's constant "
    "and $x$ is the position variable.",
    title="Momentum operator",
)

s_position_operator = setting(
    "The operator corresponding to the position (coordinate) of a single particle is "
    "the operator of multiplication by the independent variable $x$.",
    title="Position operator",
)

s_noncommuting_definition = setting(
    "Two operators $A$ and $B$ do not commute when $AB \\neq BA$. "
    "The position operator $x$ and momentum operator $p$ satisfy the canonical commutation "
    "relation $xp - px = h/(2\\pi i)$.",
    title="Non-commuting operators definition",
)

# ============================================================
# Questions
# ============================================================

q_completeness = question(
    "Can the quantum-mechanical description of physical reality be considered complete?",
    title="EPR's central question",
)

q_elements_of_reality = question(
    "What are the elements of the physical reality?",
    title="Elements of reality",
)

# ============================================================
# Claims — propositions from Section 1
# ============================================================

c_criterion_of_reality = claim(
    "EPR Criterion of Reality: If, without in any way disturbing a system, we can predict "
    "with certainty (i.e., with probability equal to unity) the value of a physical quantity, "
    "then there exists an element of physical reality corresponding to this physical quantity. "
    "This criterion is sufficient (not necessary) for reality, and is in agreement with both "
    "classical and quantum-mechanical ideas of reality.",
    title="EPR criterion of reality",
)

c_correctness_judged = claim(
    "The correctness of a physical theory is judged by the degree of agreement between "
    "the conclusions of the theory and human experience (experiment and measurement).",
    title="Theory correctness criterion",
)

c_momentum_eigenstate_definite = claim(
    "For a single particle in the momentum eigenstate $\\psi = \\exp(2\\pi i/h)\\,p_0 x$, "
    "where $p_0$ is a constant, the momentum $p$ has the definite value $p_0$. "
    "This follows because $p\\psi = p_0\\psi$ (eigenfunction equation). "
    "By the EPR criterion of reality, the momentum is an element of reality in this state.",
    title="Momentum is definite in momentum eigenstate",
    metadata={"source": "artifacts/1935_einstein_epr/epr_1935_full_text.txt, Eqs. 2-4"},
)

c_position_indefinite_in_momentum_state = claim(
    "For a single particle in the momentum eigenstate $\\psi = \\exp(2\\pi i/h)\\,p_0 x$, "
    "the probability that a measurement of the coordinate (position) gives a result between "
    "$a$ and $b$ is $P(a,b) = \\int_a^b |\\psi|^2 dx = (b - a)$, which is independent of $a$. "
    "Thus all values of the coordinate are equally probable: no definite value of the coordinate "
    "is predictable. A definite value can only be obtained by direct measurement, which disturbs "
    "the particle and alters its state away from the momentum eigenstate.",
    title="Position is indefinite in momentum eigenstate",
    metadata={"source": "artifacts/1935_einstein_epr/epr_1935_full_text.txt, Eq. 6"},
)

c_known_momentum_no_position_reality = claim(
    "The usual conclusion in quantum mechanics is that when the momentum of a particle is known, "
    "its coordinate (position) has no physical reality — i.e., the position is not an element "
    "of reality when the particle is in a momentum eigenstate.",
    title="QM conclusion: known momentum excludes position reality",
)

c_noncommuting_precludes_simultaneous = claim(
    "In quantum mechanics, if the operators corresponding to two physical quantities $A$ and $B$ "
    "do not commute ($AB \\neq BA$), then precise knowledge of one precludes precise knowledge "
    "of the other. Furthermore, any attempt to determine the latter experimentally will alter the "
    "state of the system in such a way as to destroy the knowledge of the first.",
    title="Non-commuting quantities preclude simultaneous knowledge",
)

c_initial_dilemma = claim(
    "Either (1) the quantum-mechanical description of reality given by the wave function "
    "is not complete, or (2) when the operators corresponding to two physical quantities do not "
    "commute, the two quantities cannot have simultaneous reality. "
    "Proof: If both had simultaneous reality (and thus definite values), these values would enter "
    "into the complete description per the condition of completeness. If the wave function provided "
    "such a complete description, it would contain these values and they would be predictable. "
    "Since they are not predictable, at least one of the two alternatives must hold.",
    title="EPR initial dilemma: incomplete or no simultaneous reality",
)

c_qm_assumes_complete = claim(
    "In quantum mechanics it is usually assumed that the wave function does contain a complete "
    "description of the physical reality of the system in the state to which it corresponds. "
    "This assumption appears reasonable because the information obtainable from a wave function "
    "seems to correspond exactly to what can be measured without altering the state of the system.",
    title="QM assumption: wave function is complete",
)

c_completeness_plus_reality_contradiction = claim(
    "The assumption that the wave function gives a complete description of physical reality, "
    "together with the EPR criterion of reality, leads to a contradiction. "
    "EPR state they will show this in Section 2 using a two-particle argument.",
    title="Completeness assumption + reality criterion → contradiction (promised)",
)

# Note: The initial dilemma is a valid logical disjunction from QM's formalism.
# It is NOT contradictory to c_qm_assumes_complete — both can be true if
# non-commuting quantities cannot have simultaneous reality (horn 2 of the dilemma).
# The real contradiction is in s2_epr_argument.py between simultaneous reality
# and the non-commuting exclusion principle.
