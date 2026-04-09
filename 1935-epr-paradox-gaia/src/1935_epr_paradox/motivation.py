"""Section 1: Introduction — Distinction between objective reality and physical concepts, criterion of reality, and the initial dilemma."""

from gaia.lang import claim, setting, question, deduction, infer

# ── Background: distinction between objective reality and theory ──

s_objective_reality = setting(
    "There exists an objective reality independent of any theory. Physical concepts "
    "are intended to correspond with this objective reality.",
    title="Objective reality independent of theory",
)

# ── Two criteria for judging a physical theory ──

s_two_criteria = setting(
    "Two questions can be asked of any physical theory: (1) Is the theory correct? "
    "(2) Is the description given by the theory complete? Correctness is judged by "
    "agreement between conclusions and human experience (experiment and measurement).",
    title="Two criteria for judging a physical theory",
)

# ── Condition of completeness ──

s_completeness_condition = setting(
    "A necessary requirement for a complete theory: every element of the physical "
    "reality must have a counterpart in the physical theory. This is called the "
    "**condition of completeness**.",
    title="Condition of completeness",
)

# ── Criterion of reality ──

s_criterion_of_reality = setting(
    "If, without in any way disturbing a system, we can predict with certainty "
    "(i.e., with probability equal to unity) the value of a physical quantity, "
    "then there exists an element of physical reality corresponding to this "
    "physical quantity. This is regarded as a **sufficient** (not necessary) "
    "condition of reality, in agreement with both classical and quantum-mechanical "
    "ideas of reality.",
    title="Criterion of reality (sufficient condition)",
)

# ── Quantum mechanical state concept ──

s_qm_state_concept = setting(
    "In quantum mechanics, the state of a system is completely characterized by a "
    "wave function $\\Psi$, which is a function of the variables chosen to describe "
    "the system's behavior. Corresponding to each physically observable quantity $A$ "
    "there is an operator, designated by the same letter.",
    title="QM state and observable operators",
)

# ── Eigenvalue equation ──

s_eigenvalue_equation = setting(
    "If $\\Psi$ is an eigenfunction of the operator $A$, i.e., $A\\Psi = a\\Psi$ "
    "where $a$ is a number, then the physical quantity $A$ has with certainty the "
    "value $a$ whenever the particle is in the state given by $\\Psi$.",
    title="Eigenvalue equation and definite values",
)

# ── Single-particle illustration: momentum eigenstate ──

c_momentum_definite = claim(
    "For a particle in the momentum eigenstate "
    "$\\Psi = e^{(2\\pi i/h) p_0 x}$, the momentum has with certainty the value "
    "$p_0$. By the criterion of reality, the momentum of the particle in this state "
    "is real.",
    title="Momentum is definite (and real) in momentum eigenstate",
)

c_position_indefinite = claim(
    "For a particle in the momentum eigenstate $\\Psi = e^{(2\\pi i/h) p_0 x}$, "
    "all values of the coordinate are equally probable. A definite value of the "
    "coordinate is not predictable but may be obtained only by a direct measurement, "
    "which disturbs the particle and alters its state.",
    title="Position is indefinite in momentum eigenstate",
)

# ── QM consequence: non-commuting operators ──

c_noncommuting_preclude = claim(
    "In quantum mechanics, if the operators corresponding to two physical quantities "
    "$A$ and $B$ do not commute ($AB \\neq BA$), then the precise knowledge of one "
    "precludes such knowledge of the other. Any attempt to determine the latter "
    "experimentally will alter the state of the system and destroy the knowledge "
    "of the first.",
    title="Non-commuting operators preclude simultaneous knowledge",
)

# ── The initial dilemma ──

c_initial_dilemma = claim(
    "From the quantum-mechanical fact that non-commuting observables preclude "
    "simultaneous knowledge, it follows that either:\n\n"
    "(1) The quantum-mechanical description of reality given by the wave function "
    "is not complete, **or**\n\n"
    "(2) When the operators corresponding to two physical quantities do not commute, "
    "the two quantities cannot have simultaneous reality.\n\n"
    "For if both had simultaneous reality (and thus definite values), these values "
    "would enter into the complete description according to the condition of "
    "completeness, and would be predictable from the wave function. Since they are "
    "not, one of the two alternatives must hold.",
    title="The initial dilemma: (1) QM incomplete or (2) no simultaneous reality",
)

# ── QM usually assumes completeness ──

c_qm_assumes_complete = claim(
    "In quantum mechanics it is usually assumed that the wave function does contain "
    "a complete description of the physical reality of the system in the state to "
    "which it corresponds.",
    title="QM usually assumes wave functions give complete description",
)

# ── Preview of contradiction ──

q_completeness_contradiction = question(
    "Does the assumption that the wave function provides a complete description of "
    "physical reality, together with the criterion of reality, lead to a contradiction?",
    title="Does completeness assumption lead to contradiction?",
)

# ── Strategies (Pass 2: Connect) ──

_ded_momentum_definite = deduction(
    [c_noncommuting_preclude],
    c_momentum_definite,
    reason="The momentum eigenstate $\\Psi = e^{(2\\pi i/h)p_0 x}$ is an "
    "eigenfunction of the momentum operator with eigenvalue $p_0$ "
    "(@s_eigenvalue_equation). Therefore momentum is definite in this state, "
    "and by @s_criterion_of_reality, it is an element of physical reality.",
    background=[s_eigenvalue_equation, s_criterion_of_reality],
)

_ded_position_indefinite = deduction(
    [c_noncommuting_preclude],
    c_position_indefinite,
    reason="In the momentum eigenstate, the probability $P(a,b) = \\int_a^b |\\Psi|^2 dx = b - a$ "
    "is independent of position, so all coordinate values are equally probable. "
    "A definite value is obtainable only by measurement that disturbs the state.",
    background=[s_eigenvalue_equation, s_qm_state_concept],
)

_ded_initial_dilemma = deduction(
    [c_noncommuting_preclude],
    c_initial_dilemma,
    reason="If non-commuting quantities $A$ and $B$ had simultaneous reality "
    "(@c_noncommuting_preclude), their definite values would enter into the "
    "complete description per @s_completeness_condition and be predictable from "
    "the wave function. Since QM says they are not simultaneously predictable, "
    "either (1) QM is incomplete or (2) they lack simultaneous reality.",
    background=[s_completeness_condition],
)
