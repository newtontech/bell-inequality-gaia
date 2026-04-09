"""Bell Inequality Gaia — EPR Paradox to Bell's Theorem

Formalization of the historical development from EPR (1935) through
Bell's Theorem (1964) to modern loophole-free Bell tests:

- Einstein, Podolsky, and Rosen (1935): "Can Quantum-Mechanical Description
  of Physical Reality Be Considered Complete?" Physical Review, 47, 777-780.

- Bohr, N. (1935): "Can Quantum-Mechanical Description of Physical Reality
  be Considered Complete?" Physical Review, 48, 696-702.

- Bell, J.S. (1964): "On the Einstein Podolsky Rosen Paradox" Physics 1, 195-200.

- Clauser, Horne, Shimony, and Holt (1969): "Proposed Experiment to Test Local
  Hidden-Variable Theories" Physical Review Letters, 23, 880-884.
"""

from .motivation import *
from .s2_epr_argument import *
from .s3_bohr_reply import *
from .s4_bell_1964 import *
from .s5_chsh_1969 import *

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
    # From s4_bell_1964.py
    "c_epr_motivation_hidden_variables",
    "c_locality_creates_difficulty",
    "c_nonlocal_hidden_variable_exists",
    "c_singlet_perfect_anticorrelation",
    "c_locality_implies_predetermination",
    "c_hidden_variables_complete_specification",
    "c_locality_constraint_formal",
    "c_local_hidden_correlation_form",
    "c_bell_inequality",
    "c_qm_correlation_function",
    "c_local_theory_nonstationary",
    "c_qm_violates_bell_inequality",
    "c_local_hv_incompatible_with_qm",
    "c_approximation_impossible",
    "c_locality_lorentz_invariance_conflict",
    "c_bell_result_generalizes",
    "c_time_varying_settings_crucial",
    "c_bell_theorem",
    # From s5_chsh_1969.py
    "c_chsh_particle_pair_setup",
    "c_chsh_locality_assumption",
    "c_chsh_two_settings_claim",
    "c_chsh_emergence_interpretation",
    "c_chsh_calcium_source",
    "c_chsh_generalizes_bell",
    "c_chsh_avoids_perfect_correlation",
    "c_chsh_inequality_form",
    "c_chsh_standard_form",
    "c_chsh_experimental_prediction",
    "c_qm_predicts_violation_chsh",
    "c_chsh_optimal_angles",
    "c_chsh_detector_efficiency_requirement",
    "c_chsh_efficiency_angle_tradeoff",
    "c_chsh_detection_assumption",
    "c_chsh_two_relative_orientations",
    "c_wu_shaknov_inadequate",
    "c_kocher_commins_inadequate",
    "c_chsh_proposed_experiment",
    "c_chsh_tsirelson_bound",
    "c_chsh_experimental_consequence",
    "c_chsh_general_beyond_photons",
    "c_chsh_detection_loophole",
]
