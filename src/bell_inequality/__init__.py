"""Bell Inequality Gaia — EPR Paradox and Bohr's Reply Formalization

Formalization of the 1935 EPR-Bohr debate:

- Einstein, Podolsky, and Rosen (1935): "Can Quantum-Mechanical Description
  of Physical Reality Be Considered Complete?" Physical Review, 47, 777-780.

- Bohr, N. (1935): "Can Quantum-Mechanical Description of Physical Reality
  be Considered Complete?" Physical Review, 48, 696-702.
"""

from .motivation import *
from .s2_epr_argument import *
from .s3_bohr_reply import *

__all__ = [
    # From motivation.py
    "c_criterion_of_reality",
    "c_initial_dilemma",
    "c_qm_assumes_complete",
    # From s2_epr_argument.py
    "c_qm_incomplete",
    "c_reality_independent_of_measurement",
    "c_complete_theory_possible",
    "c_p_and_q_simultaneous_reality",
    "c_negation_1_implies_negation_2",
    "c_no_interaction_no_disturbance",
    # From s3_bohr_reply.py
    "c_qm_is_complete",
    "c_epr_criterion_ambiguous",
    "c_disturbance_concept_ill_defined",
    "c_complementarity_rational_discrimination",
    "c_impossibility_not_ignorance",
    "c_position_momentum_mutually_exclusive",
    "c_statistical_nature_fundamental",
    "c_mechanical_disturbance_vs_influence",
    "c_object_instrument_discrimination",
    "c_reality_revision_required",
]
