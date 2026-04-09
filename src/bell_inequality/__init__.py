"""Bell Inequality Gaia — EPR Paradox Formalization

Formalization of Einstein, Podolsky, and Rosen (1935):
"Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?"
Physical Review, 47, 777-780.
"""

from .motivation import *
from .s2_epr_argument import *

__all__ = [
    "c_qm_incomplete",
    "c_criterion_of_reality",
    "c_reality_independent_of_measurement",
    "c_complete_theory_possible",
    "c_p_and_q_simultaneous_reality",
    "c_initial_dilemma",
    "c_negation_1_implies_negation_2",
]
