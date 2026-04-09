"""Complementarity — Measurement arrangements and the mutual exclusion of experimental procedures."""

from gaia.lang import claim, setting, deduction, infer

from .motivation import (
    s_bohr_aim,
    c_bohr_summarizes_epr,
    c_bohr_rejects_epr_conclusion,
    c_criterion_ambiguity,
    c_bohr_conclusion,
)

# ── Single-particle example: slit in a diaphragm ──

s_slit_example = setting(
    "A particle passes through a slit in a diaphragm. If the diaphragm is rigidly "
    "fixed to a support defining the space frame, the momentum exchanged between "
    "particle and diaphragm passes into the common support, and we have voluntarily "
    "cut ourselves off from any possibility of taking these reactions into account "
    "separately in predictions. This arrangement is suited for position measurements "
    "but precludes accurate momentum determination.",
    title="Single-particle slit: fixed diaphragm → position measurement",
)

s_slit_momentum = setting(
    "Alternatively, if the diaphragm is not rigidly connected with the other parts, "
    "it is possible in principle to measure its momentum with any desired accuracy "
    "before and after the passage of the particle, and thus to predict the momentum "
    "of the particle after it has passed through the slit. But the diaphragm can then "
    "no longer serve as a position measuring instrument — its position relative to "
    "the rest of the apparatus becomes uncertain.",
    title="Single-particle slit: free diaphragm → momentum measurement",
)

# ── Core complementarity claim ──

c_mutually_exclusive_procedures = claim(
    "In the phenomena concerned we are not dealing with an incomplete description "
    "characterized by arbitrary picking out of different elements of physical reality "
    "at the cost of sacrificing other such elements, but with a rational discrimination "
    "between essentially different experimental arrangements and procedures which are "
    "suited either for an unambiguous use of the idea of space location, or for a "
    "legitimate application of the conservation theorem of momentum. These procedures "
    "are mutually exclusive.",
    title="Position and momentum procedures are mutually exclusive, not incomplete",
)

# ── The EPR two-particle case through Bohr's lens ──

s_epr_two_particle_bohr = setting(
    "Bohr considers the same two-particle state as EPR, which can be produced by a "
    "rigid diaphragm with two parallel slits, through each of which one particle "
    "with given initial momentum passes. If the diaphragm's momentum is measured "
    "before and after, we know the sum of the momenta components and the difference "
    "of their initial positional coordinates. A subsequent measurement of either "
    "position or momentum of one particle determines the corresponding quantity "
    "of the other.",
    title="Bohr's two-particle arrangement with diaphragm",
)

# ── Position measurement on one particle ──

c_position_measurement_loses_momentum = claim(
    "To measure the position of one of the particles means establishing a correlation "
    "between its behavior and some instrument rigidly fixed to the support defining "
    "the space frame. By allowing an essentially uncontrollable momentum to pass from "
    "the first particle into the support, we have cut ourselves off from any future "
    "possibility of applying the law of conservation of momentum to the system "
    "consisting of the diaphragm and the two particles, and therefore have lost our "
    "only basis for an unambiguous application of the idea of momentum in predictions "
    "regarding the behavior of the second particle.",
    title="Position measurement on particle 1 loses momentum prediction for particle 2",
)

# ── Momentum measurement on one particle ──

c_momentum_measurement_loses_position = claim(
    "If we choose to measure the momentum of one of the particles, we lose through "
    "the uncontrollable displacement inevitable in such a measurement any possibility "
    "of deducing from the behavior of this particle the position of the diaphragm "
    "relative to the rest of the apparatus, and have thus no basis whatever for "
    "predictions regarding the location of the other particle.",
    title="Momentum measurement on particle 1 loses position prediction for particle 2",
)

# ── Complementarity principle ──

c_complementarity_principle = claim(
    "It is only the mutual exclusion of any two experimental procedures, permitting "
    "the unambiguous definition of complementary physical quantities, which provides "
    "room for new physical laws, the coexistence of which might at first sight appear "
    "irreconcilable with the basic principles of science. This entirely new situation "
    "is what the notion of complementarity aims at characterizing.",
    title="The complementarity principle: mutual exclusion of procedures",
)

# ── Object-instrument distinction ──

c_object_instrument_distinction = claim(
    "The necessity of discriminating in each experimental arrangement between those "
    "parts of the physical system considered which are to be treated as measuring "
    "instruments and those which constitute the objects under investigation forms "
    "a principal distinction between classical and quantum-mechanical description. "
    "In quantum theory this distinction has its root in the indispensable use of "
    "classical concepts in the interpretation of all proper measurements.",
    title="Object-instrument distinction is fundamental in QM",
)

# ── QM description is rational and complete within its scope ──

c_qm_rational_within_scope = claim(
    "Quantum-mechanical description may be characterized as a rational utilization "
    "of all possibilities of unambiguous interpretation of measurements, compatible "
    "with the finite and uncontrollable interaction between the objects and the "
    "measuring instruments in the field of quantum theory.",
    title="QM is a rational utilization of all measurement possibilities",
)

# ── Relativity analogy ──

c_relativity_analogy = claim(
    "The situation in quantum theory presents striking analogies with general "
    "relativity. The singular position of measuring instruments in the account of "
    "quantum phenomena appears closely analogous to the necessity in relativity "
    "theory of upholding an ordinary description of all measuring processes. "
    "Both involve a radical revision of our attitude regarding physical reality.",
    title="Analogy between complementarity and relativity",
)

# ── Strategies (Pass 2: Connect) ──

_infer_mutual_exclusion = infer(
    [c_position_measurement_loses_momentum, c_momentum_measurement_loses_position],
    c_mutually_exclusive_procedures,
    reason="Position measurement on particle 1 loses momentum basis for particle 2 "
    "(@c_position_measurement_loses_momentum), while momentum measurement on particle 1 "
    "loses position basis for particle 2 (@c_momentum_measurement_loses_position). "
    "These are not different aspects of the same incomplete description, but "
    "discriminations between essentially different experimental arrangements.",
    background=[s_slit_example, s_slit_momentum, s_epr_two_particle_bohr],
)

_ded_complementarity = deduction(
    [c_mutually_exclusive_procedures],
    c_complementarity_principle,
    reason="If position and momentum procedures are mutually exclusive "
    "(@c_mutually_exclusive_procedures), this mutual exclusion is not a deficiency "
    "but provides room for new physical laws. The notion of complementarity "
    "characterizes this entirely new situation.",
)

_ded_bohr_counter = deduction(
    [c_criterion_ambiguity, c_complementarity_principle],
    c_bohr_conclusion,
    reason="Since the EPR criterion contains an ambiguity about 'without disturbing' "
    "(@c_criterion_ambiguity) — measurement conditions, not the system itself, are "
    "influenced — and complementarity explains this as a feature of QM "
    "(@c_complementarity_principle), the EPR argumentation does not justify "
    "the conclusion that QM is incomplete.",
)

_infer_qm_rational = infer(
    [c_complementarity_principle, c_object_instrument_distinction],
    c_qm_rational_within_scope,
    reason="The complementarity principle (@c_complementarity_principle) shows that "
    "mutually exclusive procedures are not a deficiency but a rational feature. "
    "Combined with the object-instrument distinction "
    "(@c_object_instrument_distinction), QM is a rational utilization of all "
    "measurement possibilities within its scope.",
)

_infer_relativity = infer(
    [c_object_instrument_distinction],
    c_relativity_analogy,
    reason="The singular position of measuring instruments in QM "
    "(@c_object_instrument_distinction) parallels the role of reference frames in "
    "relativity. Both require upholding classical measurement descriptions while "
    "introducing fundamentally new physical laws.",
)
