"""Section 3: Bohr's 1935 Reply to the EPR Argument

Nils Bohr responds to Einstein, Podolsky, and Rosen's (1935) argument that quantum
mechanics is incomplete. Bohr argues that the EPR "criterion of reality" contains
an essential ambiguity when applied to quantum phenomena. He introduces the principle
of complementarity: the measurement apparatus and the measured object form an
indivisible whole, and different experimental arrangements yield complementary
but mutually exclusive descriptions of reality.

Reference: Bohr, N. (1935) "Can Quantum-Mechanical Description of Physical Reality
be Considered Complete?" Physical Review, 48, 696-702.
"""

from gaia.lang import (
    claim, setting, deduction, abduction, noisy_and,
    contradiction, complement,
)
from .motivation import (
    c_criterion_of_reality,
    c_qm_assumes_complete,
    c_initial_dilemma,
)
from .s2_epr_argument import (
    c_no_interaction_no_disturbance,
    c_qm_incomplete,
    c_p_and_q_simultaneous_reality,
)

# ============================================================
# Settings — Bohr's conceptual framework
# ============================================================

s_slit_diffraction_example = setting(
    "In the single-slit diffraction example: when the diaphragm is rigidly fixed, "
    "the slit width $\\delta q$ defines the position uncertainty of the particle, "
    "and the momentum uncertainty $\\delta p$ is correlated to $\\delta q$ by "
    "Heisenberg's relation $\\delta q \\cdot \\delta p \\approx h$. When the "
    "diaphragm is movable, we can measure the momentum exchange, but lose precise "
    "knowledge of the slit position.",
    title="Slit diffraction: complementary arrangements",
)

# ============================================================
# Claims — Bohr's core arguments
# ============================================================

c_complementarity_principle = claim(
    "The principle of complementarity: quantum phenomena require a 'wholeness' of "
    "description that acknowledges the fundamental impossibility of separating the "
    "object under investigation from the measuring instruments. Different experimental "
    "arrangements yield complementary but mutually exclusive aspects of physical "
    "reality, such as precise position versus precise momentum.",
    title="Complementarity principle",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_object_apparatus_whole = claim(
    "In quantum mechanics, the interaction between object and measuring agencies is "
    "an inherent element of the phenomenon. The object and measuring apparatus form "
    "an indivisible whole — they cannot be treated as independently existing entities "
    "during measurement. This 'wholeness' is conditioned by the very existence of "
    "the quantum of action (Planck's constant).",
    title="Object-apparatus wholeness",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_quantum_of_action = claim(
    "The finite interaction between object and measuring agencies, conditioned by "
    "the existence of the quantum of action $h$ (Planck's constant), entails the "
    "impossibility of controlling the reaction of the object on the measuring instruments "
    "if those instruments are to serve their purpose. This necessitates a renunciation "
    "of the classical ideal of causality and a radical revision of our attitude "
    "toward physical reality.",
    title="Quantum of action and measurement interaction",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_position_momentum_complementarity = claim(
    "Position measurements and momentum measurements are complementary: a precise "
    "position measurement requires an apparatus rigidly fixed in space (allowing "
    "spatial coordination but uncontrollable momentum exchange), while a precise "
    "momentum measurement requires measuring the momentum transfer (allowing "
    "momentum prediction but uncontrollable spatial displacement). The two experimental "
    "arrangements are mutually exclusive.",
    title="Position-momentum complementarity in measurements",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_epr_criterion_ambiguous = claim(
    "The EPR criterion of reality — 'If, without in any way disturbing a system, "
    "we can predict with certainty the value of a physical quantity, then there "
    "exists an element of physical reality corresponding to this physical quantity' "
    "— contains an essential ambiguity when applied to quantum phenomena. The phrase "
    "'without in any way disturbing a system' is ill-defined because it ignores "
    "the fact that different measurement choices affect the very conditions that "
    "define the types of predictions possible for the system.",
    title="EPR criterion of reality is ambiguous for quantum phenomena",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_disturbance_concept_ill_defined = claim(
    "The concept of 'disturbance' in the EPR argument is ill-defined. While there "
    "is no question of a mechanical disturbance to system II during the final "
    "stage of the measuring procedure (when the systems are spatially separated), "
    "there remains the question of an influence on the very conditions that define "
    "the possible types of predictions regarding the future behavior of the system. "
    "The choice of measurement on system I determines which experimental arrangement "
    "is relevant, and thus affects the entire definition of the phenomenon.",
    title="The 'disturbance' concept in EPR is ill-defined",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_measurement_defines_conditions = claim(
    "The conditions of measurement constitute an inherent element of the description "
    "of any phenomenon to which the term 'physical reality' can be properly attached. "
    "These conditions are not a passive background but are definitively shaped by "
    "the choice of experimental arrangement. The 'freedom of choice' in which "
    "measurement to perform is not a freedom to choose between alternative realities, "
    "but a freedom to choose between mutually exclusive experimental arrangements.",
    title="Measurement conditions define the phenomenon",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_position_momentum_mutually_exclusive = claim(
    "Any experimental arrangement suited for the study of quantum phenomena involves "
    "a renunciation of one or the other of two complementary aspects of description: "
    "either the unambiguous use of space location (position) or the legitimate "
    "application of the conservation theorem of momentum. These arrangements are "
    "mutually exclusive — any attempt to simultaneously realize both would destroy "
    "the quantum phenomenon itself.",
    title="Position and momentum measurements are mutually exclusive",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_impossibility_not_ignorance = claim(
    "In quantum mechanics, we are not dealing with a mere ignorance of the value "
    "of certain physical quantities (as in classical statistical mechanics), but "
    "with the impossibility of defining these quantities in an unambiguous way "
    "independently of the experimental arrangement. The statistical character of "
    "quantum mechanics is therefore fundamental, not a sign of incompleteness.",
    title="QM uncertainty is impossibility, not ignorance",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_epr_two_particle_reinterpreted = claim(
    "The EPR two-particle arrangement, when properly analyzed, reveals the same "
    "complementarity structure as the single-slit case. When we measure the position "
    "of particle I (using a rigidly fixed diaphragm), we lose the possibility of "
    "applying momentum conservation to the entire system. When we measure the "
    "momentum of particle I (using a movable diaphragm), we lose the basis for "
    "position predictions regarding particle II. The choice of measurement on I "
    "determines the entire experimental context and thus the meaning of 'reality' "
    "for particle II.",
    title="EPR two-particle case exhibits complementarity",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_position_choice_destroys_momentum_basis = claim(
    "When we choose to measure the position of one of the two particles, we must "
    "establish a correlation between its behavior and an instrument rigidly fixed "
    "to the support defining the space frame. By allowing an essentially "
    "uncontrollable momentum to pass from the particle into this support, we cut "
    "ourselves off from any future possibility of applying the law of conservation "
    "of momentum — we lose our only basis for unambiguous application of the idea "
    "of momentum in predictions about the second particle.",
    title="Position measurement destroys momentum prediction basis",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_momentum_choice_destroys_position_basis = claim(
    "Conversely, when we choose to measure the momentum of one of the particles, "
    "the uncontrollable displacement inevitable in such a measurement destroys any "
    "possibility of deducing the position of the diaphragm relative to the rest "
    "of the apparatus. We thus have no basis whatever for predictions regarding "
    "the location (position) of the other particle.",
    title="Momentum measurement destroys position prediction basis",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_complementarity_rational_discrimination = claim(
    "What appears in EPR as an arbitrary picking out of different elements of "
    "physical reality is in fact a rational discrimination between essentially "
    "different experimental arrangements and procedures. Different arrangements "
    "are suited either for the unambiguous use of space location or for the "
    "legitimate application of momentum conservation. Any remaining appearance "
    "of arbitrariness concerns merely our freedom of handling the measuring "
    "instruments, which is characteristic of the very idea of experiment.",
    title="Complementarity as rational discrimination, not arbitrariness",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_qm_is_complete = claim(
    "The quantum-mechanical description of physical reality, far from being "
    "incomplete, may be characterized as a rational utilization of all possibilities "
    "of unambiguous interpretation of measurements, compatible with the finite "
    "and uncontrollable interaction between objects and measuring instruments in "
    "quantum theory. Within its scope, this description fulfills all rational "
    "demands of completeness. The wave function provides a complete description "
    "of what can be meaningfully said about a quantum system.",
    title="QM description IS complete (Bohr's conclusion)",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_wave_function_complete_interpretation = claim(
    "The wave function in quantum mechanics should not be interpreted as an "
    "incomplete representation of an underlying reality possessing definite "
    "values for all observables. Rather, it provides the complete mathematical "
    "expression for the totality of predictions that can be made about a system "
    "given a specific experimental arrangement. The 'incompleteness' alleged "
    "by EPR stems from applying classical concepts of reality beyond their "
    "domain of validity.",
    title="Wave function as complete predictive tool",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_statistical_nature_fundamental = claim(
    "The statistical nature of quantum mechanics is not a sign of incompleteness "
    "or a temporary expedient awaiting a more complete deterministic theory. "
    "This statistical character is fundamental and irreducible, arising from "
    "the very existence of the quantum of action and the wholeness of the "
    "quantum phenomenon. Comparisons between quantum mechanics and classical "
    "statistical mechanics are 'essentially irrelevant' to understanding this "
    "fundamental feature.",
    title="QM statistics are fundamental, not provisional",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_time_energy_complementarity = claim(
    "The complementarity between position and momentum measurements extends to "
    "time and energy measurements. Time measurements require clock-like mechanisms "
    "whose functioning is described classically, but any attempt to control the "
    "energy exchanged with these clocks would interfere with their use as time "
    "indicators. This entails a complementary relationship between detailed time "
    "accounts and energy conservation in atomic phenomena.",
    title="Time-energy complementarity",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_object_instrument_discrimination = claim(
    "A principal distinction between classical and quantum-mechanical description "
    "is the necessity of discriminating, in each experimental arrangement, between "
    "those parts of the physical system treated as measuring instruments and those "
    "constituting the objects under investigation. In classical physics this "
    "distinction does not affect the character of the description, but in quantum "
    "theory it is fundamental and indispensable.",
    title="Object-instrument discrimination is fundamental in QM",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_reality_revision_required = claim(
    "Quantum theory requires a radical revision of our attitude toward physical "
    "reality, comparable to the modification of ideas regarding absolute space "
    "and time brought about by general relativity theory. The dependence of "
    "measurement readings on the entire experimental context in quantum theory "
    "parallels the dependence of space-time measurements on the reference system "
    "in relativity.",
    title="QM requires revision of reality concept",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_mechanical_disturbance_vs_influence = claim(
    "The EPR argument correctly identifies that there is no mechanical disturbance "
    "to system II during the final stage of measurement (the systems are spatially "
    "separated). However, this misses the essential point: the choice of measurement "
    "on system I influences the very conditions that define what constitutes a "
    "valid physical description of system II. 'Influence on the conditions' is "
    "fundamentally different from 'mechanical disturbance', but no less real "
    "in its effect on what can be meaningfully said about reality.",
    title="Mechanical non-disturbance vs. influence on conditions",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_ambiguity_without_disturbing = claim(
    "The phrase 'without in any way disturbing a system' in the EPR criterion "
    "of reality is ambiguous when applied to quantum phenomena. While there may "
    "be no mechanical disturbance, the very possibility of making a prediction "
    "about system II depends on an experimental arrangement that affects the "
    "definition of physical quantities for system II. The 'way of disturbing' "
    "includes the choice of experimental context, not just mechanical interaction.",
    title="Ambiguity in 'without disturbing a system'",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

c_two_measurements_two_contexts = claim(
    "The two different measurements EPR describe (measuring position vs. momentum "
    "on system I) are not merely two different ways of gathering information about "
    "the same pre-existing reality. They represent two fundamentally different "
    "experimental contexts, each defining what 'reality' means for system II in "
    "a different way. The 'free choice' between measurements is a choice between "
    "mutually exclusive definitions of the physical situation, not between alternative "
    "views of a single definite situation.",
    title="Two measurements = two experimental contexts",
    metadata={"source": "artifacts/1935_bohr_reply/bohr_1935_reply_full_text.txt"},
)

# ============================================================
# Abduction alternatives — named for review sidecar
# ============================================================

alt_epr_preserves_classical_reality = claim(
    "EPR's argument correctly preserves the classical notion of physical reality: "
    "properties exist independently of measurement. The apparent contradictions "
    "with QM indicate that QM is incomplete, not that reality needs to be "
    "reconceptualized. A complete theory would recover classical realism.",
    title="Alternative: EPR's classical realism is correct",
)

alt_mechanical_isolation_sufficient = claim(
    "If two systems are mechanically isolated (no interaction), then any property "
    "of one system that can be inferred from measurements on the other must be "
    "an independent element of reality of the first system. The choice of "
    "measurement on the distant system cannot affect the local reality.",
    title="Alternative: Mechanical isolation guarantees independent reality",
)

# ============================================================
# Operators — logical contradictions
# ============================================================

# Contradiction 1: Bohr's claim that QM is complete vs. EPR's claim that QM is incomplete
_bohr_complete_vs_epr_incomplete = contradiction(
    c_qm_is_complete,
    c_qm_incomplete,
    reason="Bohr concludes that QM is complete (@c_qm_is_complete) while EPR "
    "conclude that QM is incomplete (@c_qm_incomplete). These are directly "
    "contradictory conclusions derived from different interpretations of the "
    "same formalism.",
)

# Contradiction 2: Bohr's claim that uncertainty is impossibility vs. EPR's
# simultaneous reality claim
_bohr_impossibility_vs_epr_simultaneous = contradiction(
    c_impossibility_not_ignorance,
    c_p_and_q_simultaneous_reality,
    reason="Bohr argues that position and momentum cannot be simultaneously defined "
    "as elements of reality (@c_impossibility_not_ignorance), directly "
    "contradicting EPR's conclusion that P and Q have simultaneous reality "
    "(@c_p_and_q_simultaneous_reality).",
)

# Contradiction 3: Bohr's ambiguity of 'disturbance' vs. EPR's no-disturbance claim
_bohr_disturbance_ambiguity_vs_epr_no_disturbance = contradiction(
    c_disturbance_concept_ill_defined,
    c_no_interaction_no_disturbance,
    reason="Bohr argues that the concept of 'disturbance' in EPR is ill-defined "
    "because it ignores the influence on measurement conditions "
    "(@c_disturbance_concept_ill_defined), while EPR claim there is no disturbance "
    "to system II (@c_no_interaction_no_disturbance).",
)

# ============================================================
# Strategies — reasoning connections
# ============================================================

# Strategy 1: From ambiguity of criterion to EPR argument failure
_strat_criterion_ambiguous_undermines_epr = deduction(
    [c_epr_criterion_ambiguous, c_ambiguity_without_disturbing],
    c_complementarity_rational_discrimination,
    reason="The EPR criterion of reality is ambiguous when applied to quantum "
    "phenomena (@c_epr_criterion_ambiguous), specifically in the phrase "
    "'without disturbing a system' (@c_ambiguity_without_disturbing). What EPR "
    "interpret as incompleteness is actually the rational discrimination between "
    "mutually exclusive experimental arrangements (@c_complementarity_rational_discrimination).",
)

# Strategy 2: Position and momentum as mutually exclusive arrangements
_strat_position_momentum_exclusive = deduction(
    [c_position_momentum_complementarity, c_object_apparatus_whole, c_quantum_of_action],
    c_position_momentum_mutually_exclusive,
    reason="Because of the quantum of action (@c_quantum_of_action) and the "
    "wholeness of object-apparatus interaction (@c_object_apparatus_whole), "
    "position and momentum measurements are complementary and mutually exclusive "
    "(@c_position_momentum_complementarity → @c_position_momentum_mutually_exclusive).",
)

# Strategy 3: Two-particle case shows complementarity, not simultaneous reality
_strat_two_particle_complementarity = noisy_and(
    [c_epr_two_particle_reinterpreted, c_position_choice_destroys_momentum_basis,
     c_momentum_choice_destroys_position_basis, c_complementarity_principle],
    c_two_measurements_two_contexts,
    reason="In the two-particle case, measuring position destroys the momentum "
    "prediction basis (@c_position_choice_destroys_momentum_basis), while measuring "
    "momentum destroys the position basis (@c_momentum_choice_destroys_position_basis). "
    "This shows that the two measurements define different experimental contexts "
    "(@c_two_measurements_two_contexts), reflecting the principle of complementarity "
    "(@c_complementarity_principle).",
    background=[c_object_apparatus_whole],
)

# Strategy 4: From mutual exclusivity to fundamental statistics
_strat_mutual_exclusivity_fundamental = deduction(
    [c_position_momentum_mutually_exclusive, c_impossibility_not_ignorance],
    c_statistical_nature_fundamental,
    reason="Position and momentum measurements are mutually exclusive "
    "(@c_position_momentum_mutually_exclusive), and this represents an impossibility "
    "of definition, not mere ignorance (@c_impossibility_not_ignorance). "
    "Therefore the statistical nature of QM is fundamental (@c_statistical_nature_fundamental).",
)

# Strategy 5: From fundamental statistics + wave function utility to completeness
_strat_completeness_argument = noisy_and(
    [c_statistical_nature_fundamental, c_wave_function_complete_interpretation,
     c_complementarity_rational_discrimination],
    c_qm_is_complete,
    reason="QM statistics are fundamental, not provisional "
    "(@c_statistical_nature_fundamental). The wave function provides complete "
    "predictive capacity given an experimental arrangement "
    "(@c_wave_function_complete_interpretation). The apparent arbitrariness "
    "is rational discrimination between arrangements "
    "(@c_complementarity_rational_discrimination). Therefore QM is complete "
    "within its scope (@c_qm_is_complete).",
)

# Strategy 6: Bohr's reinterpretation of EPR's no-disturbance claim
_strat_disturbance_reinterpretation = deduction(
    [c_mechanical_disturbance_vs_influence, c_measurement_defines_conditions,
     c_object_apparatus_whole],
    c_disturbance_concept_ill_defined,
    reason="While EPR are correct about no mechanical disturbance "
    "(@c_mechanical_disturbance_vs_influence), Bohr argues that measurement "
    "defines the conditions of the phenomenon (@c_measurement_defines_conditions) "
    "due to object-apparatus wholeness (@c_object_apparatus_whole). "
    "Therefore the 'disturbance' concept is ill-defined "
    "(@c_disturbance_concept_ill_defined).",
)

# Strategy 7: From wholeness to object-instrument discrimination
_strat_wholeness_discrimination = deduction(
    [c_object_apparatus_whole, c_quantum_of_action, c_epr_two_particle_reinterpreted],
    c_object_instrument_discrimination,
    reason="The wholeness of object-apparatus interaction (@c_object_apparatus_whole) "
    "conditioned by the quantum of action (@c_quantum_of_action), as illustrated "
    "in the two-particle case (@c_epr_two_particle_reinterpreted), requires "
    "discriminating between object and measuring instruments as a fundamental "
    "feature of quantum description (@c_object_instrument_discrimination).",
)

# Strategy 8: From complementarity to reality revision
_strat_reality_revision = deduction(
    [c_qm_is_complete, c_complementarity_rational_discrimination,
     c_mechanical_disturbance_vs_influence],
    c_reality_revision_required,
    reason="QM is complete within its scope (@c_qm_is_complete) despite requiring "
    "complementarity (@c_complementarity_rational_discrimination) and a distinction "
    "between mechanical disturbance and influence on conditions "
    "(@c_mechanical_disturbance_vs_influence). This situation is analogous to "
    "relativity theory and requires a revision of our concept of reality "
    "(@c_reality_revision_required).",
)

# Strategy 9: Alternative (EPR's classical realism) vs. Bohr's interpretation
_strat_alternative_classical_realism = abduction(
    observation=c_position_momentum_mutually_exclusive,
    hypothesis=c_reality_revision_required,
    alternative=alt_epr_preserves_classical_reality,
    reason="Bohr argues that the mutual exclusivity of position and momentum "
    "measurements (@c_position_momentum_mutually_exclusive) requires revising "
    "our concept of reality (@c_reality_revision_required). EPR would argue "
    "instead that this shows QM's incompleteness, preserving classical realism "
    "(@alt_epr_preserves_classical_reality). Bohr rejects this alternative "
    "by emphasizing the wholeness of quantum phenomena.",
    background=[c_complementarity_principle, c_object_apparatus_whole],
)

# Strategy 10: From mechanical isolation to reality judgment
_strat_isolation_reality = abduction(
    observation=c_no_interaction_no_disturbance,
    hypothesis=alt_mechanical_isolation_sufficient,
    alternative=c_mechanical_disturbance_vs_influence,
    reason="EPR argue that mechanical isolation of systems is sufficient to "
    "guarantee independent reality (@alt_mechanical_isolation_sufficient), based "
    "on the absence of interaction (@c_no_interaction_no_disturbance). Bohr "
    "counters that this ignores the influence on the conditions defining "
    "the phenomenon (@c_mechanical_disturbance_vs_influence), showing that "
    "mechanical isolation alone does not determine what constitutes 'reality' "
    "in quantum phenomena.",
    background=[c_object_apparatus_whole, c_measurement_defines_conditions],
)
