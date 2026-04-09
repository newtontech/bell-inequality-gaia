"""Review sidecar for EPR, Bohr, Bell, and CHSH formalization.

Formalization of the historical chain from EPR (1935) through Bell's Theorem (1964)
to the CHSH inequality (1969) that enabled experimental tests.

Priors are assigned to independent (leaf) premises. Derived claims get
uninformative priors (0.5) from the inference engine.
"""

from gaia.review import ReviewBundle, review_claim, review_strategy

from ..motivation import (
    c_criterion_of_reality,
    c_initial_dilemma,
    c_qm_assumes_complete,
    c_noncommuting_precludes_simultaneous,
    c_completeness_plus_reality_contradiction,
    c_correctness_judged,
    c_momentum_eigenstate_definite,
    c_position_indefinite_in_momentum_state,
    c_known_momentum_no_position_reality,
)
from ..s2_epr_argument import (
    c_two_measurements_two_states,
    c_no_interaction_no_disturbance,
    c_momentum_prediction,
    c_position_prediction,
    c_pq_noncommuting,
    c_p_element_of_reality,
    c_q_element_of_reality,
    c_p_and_q_simultaneous_reality,
    c_predict_both_without_disturbance,
    c_two_wavefunctions_same_reality,
    c_negation_1_implies_negation_2,
    c_qm_incomplete,
    c_reality_independent_of_measurement,
    c_complete_theory_possible,
    alt_momentum_formal_not_real,
    alt_position_formal_not_real,
    _strat_p_reality,
    _strat_q_reality,
    _strat_simultaneous,
    _strat_negation_chain,
    _strat_qm_incomplete,
    _strat_reality_independent,
    _strat_two_wf_same_reality,
    _strat_predict_both,
)
from ..s3_bohr_reply import (
    # Settings
    s_slit_diffraction_example,
    # Core claims
    c_complementarity_principle,
    c_object_apparatus_whole,
    c_quantum_of_action,
    c_position_momentum_complementarity,
    c_time_energy_complementarity,
    c_epr_criterion_ambiguous,
    c_disturbance_concept_ill_defined,
    c_measurement_defines_conditions,
    c_position_momentum_mutually_exclusive,
    c_impossibility_not_ignorance,
    c_epr_two_particle_reinterpreted,
    c_position_choice_destroys_momentum_basis,
    c_momentum_choice_destroys_position_basis,
    c_complementarity_rational_discrimination,
    c_qm_is_complete,
    c_wave_function_complete_interpretation,
    c_statistical_nature_fundamental,
    c_time_energy_complementarity,
    c_object_instrument_discrimination,
    c_reality_revision_required,
    c_mechanical_disturbance_vs_influence,
    c_ambiguity_without_disturbing,
    c_two_measurements_two_contexts,
    # Alternatives
    alt_epr_preserves_classical_reality,
    alt_mechanical_isolation_sufficient,
    # Contradictions
    _bohr_complete_vs_epr_incomplete,
    _bohr_impossibility_vs_epr_simultaneous,
    _bohr_disturbance_ambiguity_vs_epr_no_disturbance,
    # Strategies
    _strat_criterion_ambiguous_undermines_epr,
    _strat_position_momentum_exclusive,
    _strat_two_particle_complementarity,
    _strat_mutual_exclusivity_fundamental,
    _strat_completeness_argument,
    _strat_disturbance_reinterpretation,
    _strat_wholeness_discrimination,
    _strat_reality_revision,
    _strat_alternative_classical_realism,
    _strat_isolation_reality,
)
from ..s4_bell_1964 import (
    # Settings
    s_singlet_spin_state,
    s_locality_assumption_bell,
    s_hidden_variable_formalism,
    s_qm_correlation_singlet,
    # Core claims
    c_epr_motivation_hidden_variables,
    c_locality_creates_difficulty,
    c_nonlocal_hidden_variable_exists,
    c_singlet_perfect_anticorrelation,
    c_locality_implies_predetermination,
    c_hidden_variables_complete_specification,
    c_locality_constraint_formal,
    c_local_hidden_correlation_form,
    c_bell_inequality,
    c_qm_correlation_function,
    c_local_theory_nonstationary,
    c_qm_violates_bell_inequality,
    c_local_hv_incompatible_with_qm,
    c_approximation_impossible,
    c_locality_lorentz_invariance_conflict,
    c_bell_result_generalizes,
    c_time_varying_settings_crucial,
    c_bell_theorem,
    # Alternatives
    alt_locality_violates_qm,
    alt_superdeterminism,
    alt_retrocausality,
    # Contradictions
    _qm_violates_bell,
    _locality_vs_qm_predictions,
    # Strategies
    _strat_epr_to_hv,
    _strat_locality_to_predetermination,
    _strat_predetermination_to_hv_formalism,
    _strat_hv_locality_to_bell_form,
    _strat_local_form_to_inequality,
    _strat_qm_to_correlation,
    _strat_local_theories_nonstationary,
    _strat_qm_violates_inequality,
    _strat_main_theorem,
    _strat_locality_lorentz_implication,
    _strat_locality_essential,
    _strat_approximation_impossible,
    _strat_superdeterminism_alternative,
    _strat_retrocausality_alternative,
    _strat_generalization,
    _strat_experimental_implications,
)
from ..s5_chsh_1969 import (
    # Settings
    s_chsh_particle_setup,
    s_chsh_locality_formalism,
    s_chsh_two_settings_per_side,
    s_chsh_emergence_correlation,
    s_chsh_calcium_cascade,
    # Core claims
    c_chsh_particle_pair_setup,
    c_chsh_locality_assumption,
    c_chsh_two_settings_claim,
    c_chsh_emergence_interpretation,
    c_chsh_calcium_source,
    c_chsh_generalizes_bell,
    c_chsh_avoids_perfect_correlation,
    c_chsh_inequality_form,
    c_chsh_standard_form,
    c_chsh_experimental_prediction,
    c_qm_predicts_violation_chsh,
    c_chsh_optimal_angles,
    c_chsh_detector_efficiency_requirement,
    c_chsh_efficiency_angle_tradeoff,
    c_chsh_detection_assumption,
    c_chsh_two_relative_orientations,
    c_wu_shaknov_inadequate,
    c_kocher_commins_inadequate,
    c_chsh_proposed_experiment,
    c_chsh_tsirelson_bound,
    c_chsh_experimental_consequence,
    c_chsh_general_beyond_photons,
    c_chsh_detection_loophole,
    # Alternatives
    alt_chsh_detector_conspiracy,
    alt_chsh_superdeterminism_settings,
    # Contradictions
    _chsh_qm_contradiction,
    _chsh_local_hv_contradiction,
    # Strategies
    _strat_bell_to_chsh_motivation,
    _strat_chsh_setup_formalism,
    _strat_two_settings_to_chsh,
    _strat_experimental_simplification,
    _strat_experimental_prediction_form,
    _strat_qm_to_chsh_violation,
    _strat_optimal_angles_derivation,
    _strat_efficiency_requirements,
    _strat_efficiency_angle_tradeoff,
    _strat_two_orientations_sufficient,
    _strat_previous_experiments_inadequate,
    _strat_tsirelson_bound,
    _strat_experimental_locality_test,
    _strat_generality_beyond_photons,
    _strat_detection_loophole,
    _strat_superdeterminism_chsh,
    _strat_chsh_main_theorem,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ============================================================
        # Leaf premises — priors (from motivation.py and s2_epr_argument.py)
        # ============================================================

        # QM assumption: the wave function is a complete description
        # This is the orthodox QM position, widely held in 1935.
        # Prior reflects the pre-Bell consensus: most physicists accepted this.
        review_claim(
            c_qm_assumes_complete,
            prior=0.70,
            judgment="supporting",
            justification="The completeness assumption was the standard QM position in 1935. "
            "Bohr, Heisenberg, and the Copenhagen school strongly endorsed it.",
        ),

        # EPR initial dilemma: either incomplete or no simultaneous reality
        # This is a valid logical disjunction from QM's own formalism.
        review_claim(
            c_initial_dilemma,
            prior=0.85,
            judgment="supporting",
            justification="The dilemma follows rigorously from QM's formalism: if both non-commuting "
            "quantities had simultaneous definite values, they'd be in the wave function and predictable. "
            "Since they're not, at least one alternative must hold.",
        ),

        # Non-commuting quantities preclude simultaneous knowledge
        # This is a core theorem of QM (Heisenberg uncertainty).
        review_claim(
            c_noncommuting_precludes_simultaneous,
            prior=0.90,
            judgment="supporting",
            justification="This is a well-established consequence of the non-commutativity of "
            "operators in QM, directly related to the Heisenberg uncertainty principle.",
        ),

        # Two different measurements yield two different wave functions for system II
        # This follows directly from wave packet reduction applied to different observables.
        review_claim(
            c_two_measurements_two_states,
            prior=0.90,
            judgment="supporting",
            justification="Direct consequence of expanding the same wave function in two "
            "different eigenbases and applying wave packet reduction.",
        ),

        # No disturbance to system II from measurement on I (locality)
        # This is the key physical assumption: the systems are separated.
        review_claim(
            c_no_interaction_no_disturbance,
            prior=0.60,
            judgment="tentative",
            justification="This is EPR's locality assumption — that spatially separated systems "
            "cannot instantaneously affect each other. Bohr challenges this by arguing that "
            "'disturbance' includes influence on experimental conditions. Bell's theorem (1964) "
            "later showed this assumption is testable and experiments suggest quantum correlations "
            "violate it.",
        ),

        # Momentum prediction: measuring p of I → II has momentum -p
        # This is a mathematical result from the specific wave function.
        review_claim(
            c_momentum_prediction,
            prior=0.90,
            judgment="supporting",
            justification="Straightforward calculation from the two-particle wave function "
            "and the momentum eigenfunction expansion. Mathematically rigorous.",
        ),

        # Position prediction: measuring x of I → II has position x + x_0
        # Mathematical result from the same wave function.
        review_claim(
            c_position_prediction,
            prior=0.90,
            judgment="supporting",
            justification="Straightforward calculation using the Dirac delta function "
            "eigenstate expansion. Mathematically rigorous.",
        ),

        # P and Q are non-commuting for particle II
        # This is the canonical commutation relation.
        review_claim(
            c_pq_noncommuting,
            prior=0.95,
            judgment="supporting",
            justification="The canonical commutation relation [P, Q] = h/(2πi) is a "
            "fundamental result of quantum mechanics.",
        ),

        # Abduction alternative: momentum predictability is merely formal
        # Bohr's response would essentially argue this.
        review_claim(
            alt_momentum_formal_not_real,
            prior=0.40,
            judgment="tentative",
            justification="This represents the Copenhagen interpretation's response: "
            "the correlation is a property of the entangled state, not evidence of a "
            "pre-existing element of reality. Bohr's argument supports this view.",
        ),

        # Abduction alternative: position predictability is merely formal
        # Same as above for position.
        review_claim(
            alt_position_formal_not_real,
            prior=0.40,
            judgment="tentative",
            justification="Same reasoning as the momentum alternative. The Copenhagen "
            "response, articulated by Bohr, would deny independent reality but "
            "emphasizes that this reflects the wholeness of quantum phenomena.",
        ),

        # ============================================================
        # Orphaned / background-only claims — priors required by engine
        # ============================================================

        # EPR criterion of reality — background-only but needs prior
        review_claim(
            c_criterion_of_reality,
            prior=0.70,
            judgment="tentative",
            justification="A reasonable sufficient condition for reality in classical contexts. "
            "Bohr argues it becomes ambiguous for quantum phenomena. Moderate prior reflecting "
            "the controversy.",
        ),

        # Theory correctness criterion — context, not in reasoning chain
        review_claim(
            c_correctness_judged,
            prior=0.95,
            judgment="supporting",
            justification="Standard epistemological principle: theories are judged by "
            "experimental agreement.",
        ),

        # Momentum is definite in momentum eigenstate — illustration
        review_claim(
            c_momentum_eigenstate_definite,
            prior=0.90,
            judgment="supporting",
            justification="Direct consequence of the eigenfunction equation. "
            "Uncontroversial within QM.",
        ),

        # Position indefinite in momentum eigenstate — illustration
        review_claim(
            c_position_indefinite_in_momentum_state,
            prior=0.90,
            judgment="supporting",
            justification="Standard QM result: uniform probability distribution "
            "over all positions in a momentum eigenstate.",
        ),

        # QM conclusion: known momentum excludes position reality
        review_claim(
            c_known_momentum_no_position_reality,
            prior=0.60,
            judgment="tentative",
            justification="This is the usual QM conclusion but it is precisely what "
            "EPR challenge. Moderate prior reflecting QM's standard position.",
        ),

        # Completeness + reality → contradiction (promised in §1)
        review_claim(
            c_completeness_plus_reality_contradiction,
            prior=0.70,
            judgment="tentative",
            justification="EPR promise to show this in §2. The contradiction is "
            "demonstrated via the two-particle argument.",
        ),

        # A complete theory may exist — EPR's belief
        review_claim(
            c_complete_theory_possible,
            prior=0.40,
            judgment="tentative",
            justification="EPR express belief but provide no argument. This is "
            "the hidden variables hypothesis. No evidence in this paper. Bell's theorem "
            "later severely constrained such theories.",
        ),

        # ============================================================
        # Leaf premises — priors from s3_bohr_reply.py (Bohr's arguments)
        # ============================================================

        # Complementarity principle
        review_claim(
            c_complementarity_principle,
            prior=0.75,
            judgment="supporting",
            justification="The central principle of the Copenhagen interpretation. "
            "Well-established as a consistent framework for QM, though controversial "
            "among realists.",
        ),

        # Object-apparatus wholeness
        review_claim(
            c_object_apparatus_whole,
            prior=0.70,
            judgment="supporting",
            justification="A key feature of Bohr's interpretation. Captures the insight "
            "that measurement context matters fundamentally in QM.",
        ),

        # Quantum of action conditions measurement interaction
        review_claim(
            c_quantum_of_action,
            prior=0.85,
            judgment="supporting",
            justification="Planck's constant h sets the scale of quantum effects. "
            "The uncontrollability principle is well-established.",
        ),

        # Position-momentum complementarity in measurements
        review_claim(
            c_position_momentum_complementarity,
            prior=0.80,
            judgment="supporting",
            justification="Standard QM: different experimental arrangements are needed "
            "for precise position vs. precise momentum measurements.",
        ),

        # EPR criterion is ambiguous for quantum phenomena
        review_claim(
            c_epr_criterion_ambiguous,
            prior=0.70,
            judgment="supporting",
            justification="Bohr's key critique. The phrase 'without disturbing' ignores "
            "the influence of experimental context. A strong philosophical argument.",
        ),

        # Disturbance concept is ill-defined
        review_claim(
            c_disturbance_concept_ill_defined,
            prior=0.70,
            judgment="supporting",
            justification="Bohr correctly identifies that EPR use 'disturbance' in a "
            "narrow mechanical sense. The broader concept of 'influence on conditions' "
            "is necessary.",
        ),

        # Measurement conditions define the phenomenon
        review_claim(
            c_measurement_defines_conditions,
            prior=0.75,
            judgment="supporting",
            justification="A core principle of the Copenhagen interpretation. The "
            "experimental arrangement is an inherent part of the quantum phenomenon.",
        ),

        # Impossibility, not ignorance
        review_claim(
            c_impossibility_not_ignorance,
            prior=0.70,
            judgment="supporting",
            justification="Distinguishes quantum from classical statistics. Bell's "
            "theorem later provided strong support for this view.",
        ),

        # Position and momentum are mutually exclusive
        review_claim(
            c_position_momentum_mutually_exclusive,
            prior=0.85,
            judgment="supporting",
            justification="Directly related to the uncertainty principle. Well-established "
            "in QM formalism and experiment.",
        ),

        # EPR two-particle case exhibits complementarity
        review_claim(
            c_epr_two_particle_reinterpreted,
            prior=0.70,
            judgment="tentative",
            justification="Bohr's reinterpretation of the EPR setup. Logically consistent "
            "but requires accepting the wholeness of quantum phenomena.",
        ),

        # Position measurement destroys momentum basis
        review_claim(
            c_position_choice_destroys_momentum_basis,
            prior=0.80,
            judgment="supporting",
            justification="Bohr's detailed analysis of the experimental setup. The "
            "momentum exchange with the fixed support is uncontrollable.",
        ),

        # Momentum measurement destroys position basis
        review_claim(
            c_momentum_choice_destroys_position_basis,
            prior=0.80,
            judgment="supporting",
            justification="Symmetric to the position case. The uncontrollable displacement "
            "in momentum measurements is a standard QM effect.",
        ),

        # Complementarity as rational discrimination
        review_claim(
            c_complementarity_rational_discrimination,
            prior=0.70,
            judgment="tentative",
            justification="Bohr's defense against charges of arbitrariness. Persuasive "
            "if one accepts the wholeness of quantum phenomena.",
        ),

        # Wave function as complete predictive tool
        review_claim(
            c_wave_function_complete_interpretation,
            prior=0.65,
            judgment="tentative",
            justification="Bohr's instrumentalist interpretation of the wave function. "
            "Controversial among realists but consistent with Copenhagen.",
        ),

        # Statistical nature is fundamental
        review_claim(
            c_statistical_nature_fundamental,
            prior=0.65,
            judgment="tentative",
            justification="Bohr's key claim. Bell's theorem and Aspect's experiments "
            "later provided strong support for this Copenhagen position.",
        ),

        # Object-instrument discrimination is fundamental
        review_claim(
            c_object_instrument_discrimination,
            prior=0.70,
            judgment="supporting",
            justification="Bohr correctly identifies a key difference between classical "
            "and quantum descriptions.",
        ),

        # QM requires revision of reality concept
        review_claim(
            c_reality_revision_required,
            prior=0.60,
            judgment="tentative",
            justification="Bohr's philosophical conclusion. Reasonable if one accepts "
            "his arguments, but controversial among realists.",
        ),

        # Mechanical disturbance vs. influence distinction
        review_claim(
            c_mechanical_disturbance_vs_influence,
            prior=0.70,
            judgment="supporting",
            justification="Bohr's key conceptual move. Distinguishing mechanical interaction "
            "from influence on experimental conditions is crucial.",
        ),

        # Ambiguity in 'without disturbing a system'
        review_claim(
            c_ambiguity_without_disturbing,
            prior=0.70,
            judgment="supporting",
            justification="Elaborates on the ambiguity of EPR's criterion. The 'way of "
            "disturbing' includes the choice of experimental context.",
        ),

        # Two measurements = two experimental contexts
        review_claim(
            c_two_measurements_two_contexts,
            prior=0.70,
            judgment="tentative",
            justification="Bohr's reinterpretation of the EPR choice. Persuasive if "
            "one accepts complementarity.",
        ),

        # Time-energy complementarity
        review_claim(
            c_time_energy_complementarity,
            prior=0.75,
            judgment="supporting",
            justification="Standard QM result: the time-energy uncertainty relation is "
            "well-established, though its interpretation is more subtle than position-momentum.",
        ),

        # ============================================================
        # Alternatives from Bohr's module
        # ============================================================

        # Alternative: EPR's classical realism is correct
        review_claim(
            alt_epr_preserves_classical_reality,
            prior=0.40,
            judgment="tentative",
            justification="Represents the realist alternative to Bohr's interpretation. "
            "Einstein's position. Bell's theorem severely constrains local hidden "
            "variable theories of this type.",
        ),

        # Alternative: Mechanical isolation guarantees independent reality
        review_claim(
            alt_mechanical_isolation_sufficient,
            prior=0.50,
            judgment="neutral",
            justification="Represents a strong locality assumption. EPR's argument "
            "relies on this, but Bell's theorem and subsequent experiments suggest "
            "it may be violated in quantum mechanics.",
        ),

        # ============================================================
        # Strategy reviews — conditional probabilities (from EPR module)
        # ============================================================

        # Strategy 1: Momentum prediction → P is element of reality (abduction)
        # The abduction is strong: certainty prediction + no disturbance
        review_strategy(
            _strat_p_reality,
            judgment="formalized",
            justification="The EPR criterion of reality directly applies: certain prediction "
            "without disturbance implies element of reality. The alternative (formal correlation) "
            "requires abandoning locality or the criterion itself.",
        ),

        # Strategy 2: Position prediction → Q is element of reality (abduction)
        review_strategy(
            _strat_q_reality,
            judgment="formalized",
            justification="Symmetric to the momentum case. The same criterion applies "
            "with equal force.",
        ),

        # Strategy 3: P and Q both real → simultaneous reality (noisy_and)
        # 4 premises: moderate multiplicative effect
        review_strategy(
            _strat_simultaneous,
            conditional_probability=0.80,
            judgment="formalized",
            justification="The key step. Both P and Q being individually elements of reality "
            "strongly supports their simultaneous reality, but the argument depends on the "
            "same reality condition. The 4-premise AND gate introduces some uncertainty.",
        ),

        # Strategy 4: Negation of (1) → negation of (2) (deduction)
        # This is a logical syllogism: if complete, then simultaneous reality exists,
        # which contradicts (2). Pure deduction.
        review_strategy(
            _strat_negation_chain,
            judgment="formalized",
            justification="Pure logical deduction: assuming completeness forces the conclusion "
            "that non-commuting quantities have simultaneous reality, contradicting the "
            "second horn of the dilemma.",
        ),

        # Strategy 5: QM is incomplete (deduction)
        # Since negation of (1) forces negation of (2), and both can't be false,
        # (1) must hold.
        review_strategy(
            _strat_qm_incomplete,
            judgment="formalized",
            justification="The logical conclusion of the EPR argument. If the two alternatives "
            "are exhaustive and negating one forces negating the other, the first must hold.",
        ),

        # Strategy 6: Reality independence (noisy_and)
        review_strategy(
            _strat_reality_independent,
            conditional_probability=0.85,
            judgment="formalized",
            justification="The philosophical force of the argument: it would be unreasonable "
            "for distant measurement choice to determine local reality.",
        ),

        # Strategy 7: Two wave functions same reality (noisy_and)
        review_strategy(
            _strat_two_wf_same_reality,
            conditional_probability=0.85,
            judgment="formalized",
            justification="Combines the two-measurement result with the no-disturbance "
            "condition to conclude both wave functions describe the same reality.",
        ),

        # Strategy 8: Both P and Q predictable (deduction)
        review_strategy(
            _strat_predict_both,
            judgment="formalized",
            justification="Direct logical combination of the two prediction claims "
            "with the no-disturbance condition.",
        ),

        # ============================================================
        # Strategy reviews — from Bohr's module
        # ============================================================

        # Strategy 1: Criterion ambiguity undermines EPR
        review_strategy(
            _strat_criterion_ambiguous_undermines_epr,
            judgment="formalized",
            justification="Bohr's core argument against EPR. If the criterion of reality "
            "is ambiguous (@c_epr_criterion_ambiguous), then EPR's conclusion doesn't follow. "
            "The strength depends on accepting Bohr's interpretation of 'disturbance'.",
        ),

        # Strategy 2: Position-momentum mutual exclusivity
        review_strategy(
            _strat_position_momentum_exclusive,
            judgment="formalized",
            justification="Strong argument from the quantum of action and object-apparatus "
            "wholeness. This is a well-established feature of QM.",
        ),

        # Strategy 3: Two-particle complementarity
        review_strategy(
            _strat_two_particle_complementarity,
            conditional_probability=0.75,
            judgment="formalized",
            justification="Bohr's detailed analysis shows the EPR setup exhibits the same "
            "complementarity structure as single-particle measurements. Persuasive if "
            "one accepts the wholeness of quantum phenomena.",
        ),

        # Strategy 4: Mutual exclusivity → fundamental statistics
        review_strategy(
            _strat_mutual_exclusivity_fundamental,
            judgment="formalized",
            justification="Strong deductive link. If measurements are mutually exclusive "
            "(@c_position_momentum_mutually_exclusive) and this represents impossibility "
            "not ignorance (@c_impossibility_not_ignorance), then statistics are fundamental.",
        ),

        # Strategy 5: Completeness argument
        review_strategy(
            _strat_completeness_argument,
            conditional_probability=0.70,
            judgment="formalized",
            justification="Bohr's argument for QM completeness. Combines multiple premises. "
            "The conclusion is strong within the Copenhagen framework but controversial "
            "among realists.",
        ),

        # Strategy 6: Disturbance reinterpretation
        review_strategy(
            _strat_disturbance_reinterpretation,
            judgment="formalized",
            justification="Bohr's key move against EPR. While EPR are correct about no "
            "mechanical disturbance, Bohr shows this doesn't imply independent reality. "
            "Strong argument if one accepts wholeness.",
        ),

        # Strategy 7: Wholeness → discrimination
        review_strategy(
            _strat_wholeness_discrimination,
            judgment="formalized",
            justification="Clear deduction from wholeness and quantum of action. The "
            "object-instrument distinction is indeed fundamental to Bohr's interpretation.",
        ),

        # Strategy 8: Reality revision
        review_strategy(
            _strat_reality_revision,
            judgment="formalized",
            justification="Bohr's philosophical conclusion. The analogy to relativity is "
            "apt but the conclusion is controversial. Depends on accepting complementarity.",
        ),

        # Strategy 9: Alternative classical realism
        review_strategy(
            _strat_alternative_classical_realism,
            judgment="formalized",
            justification="Bohr considers and rejects the classical realist alternative. "
            "The strength of his rejection depends on accepting wholeness and complementarity. "
            "Bell's theorem later supported Bohr's position.",
        ),

        # Strategy 10: Isolation and reality
        review_strategy(
            _strat_isolation_reality,
            judgment="formalized",
            justification="EPR argue from mechanical isolation to independent reality. "
            "Bohr counters that this ignores experimental context. The debate hinges on "
            "the meaning of 'reality' in QM.",
        ),

        # ============================================================
        # Leaf premises — priors from s4_bell_1964.py (Bell's theorem)
        # ============================================================

        # EPR motivates hidden variables
        review_claim(
            c_epr_motivation_hidden_variables,
            prior=0.70,
            judgment="supporting",
            justification="Accurate historical statement: EPR argued QM is incomplete and "
            "additional variables could restore causality and locality. Bell's paper responds "
            "directly to this motivation.",
        ),

        # Locality creates the essential difficulty
        review_claim(
            c_locality_creates_difficulty,
            prior=0.85,
            judgment="supporting",
            justification="Bell correctly identifies locality as the key constraint that makes "
            "hidden variable theories incompatible with QM predictions. This is the core insight.",
        ),

        # Nonlocal hidden variable theory exists (Bohm 1952)
        review_claim(
            c_nonlocal_hidden_variable_exists,
            prior=0.90,
            judgment="supporting",
            justification="David Bohm's 1952 hidden variable theory is explicitly constructed "
            "and demonstrably nonlocal. This is a historical fact and key motivation for Bell's work.",
        ),

        # Singlet state perfect anticorrelation
        review_claim(
            c_singlet_perfect_anticorrelation,
            prior=0.95,
            judgment="supporting",
            justification="Standard QM result for the singlet state. Measuring spin along the "
            "same direction on both particles always gives opposite results. Mathematically proven.",
        ),

        # Singlet spin state definition
        review_claim(
            s_singlet_spin_state,
            prior=0.95,
            judgment="supporting",
            justification="Standard quantum mechanical definition of the singlet state. "
            "The formalism is uncontroversial.",
        ),

        # QM correlation function
        review_claim(
            s_qm_correlation_singlet,
            prior=0.95,
            judgment="supporting",
            justification="The QM prediction E(a,b) = -a·b is a standard calculation. "
            "Experimentally verified in countless tests.",
        ),

        # Bell locality assumption
        review_claim(
            s_locality_assumption_bell,
            prior=0.70,
            judgment="tentative",
            justification="This is the key assumption that Bell tests. It represents Einstein's "
            "separability principle. Moderate prior because the whole point is to test it experimentally.",
        ),

        # Hidden variable formalism
        review_claim(
            s_hidden_variable_formalism,
            prior=0.70,
            judgment="tentative",
            justification="This is a formal framework for hidden variable theories. The "
            "assumption that such theories exist is what Bell's theorem tests.",
        ),

        # QM correlation function claim
        review_claim(
            c_qm_correlation_function,
            prior=0.95,
            judgment="supporting",
            justification="Direct calculation from the singlet state formalism. The cosine "
            "dependence on angle is a central QM prediction, well-verified experimentally.",
        ),

        # Locality implies predetermination
        review_claim(
            c_locality_implies_predetermination,
            prior=0.75,
            judgment="supporting",
            justification="Bell's logical inference: given perfect anticorrelation (@c_singlet_perfect_anticorrelation) "
            "and locality (setting at 1 doesn't affect result at 2), the result at 2 must be "
            "predetermined. This is the EPR-Bell argument structure.",
        ),

        # Hidden variables as complete specification
        review_claim(
            c_hidden_variables_complete_specification,
            prior=0.65,
            judgment="tentative",
            justification="The formal definition of hidden variables. The prior reflects that "
            "this is a theoretical construct whose physical meaning is debated.",
        ),

        # Formal locality constraint
        review_claim(
            c_locality_constraint_formal,
            prior=0.75,
            judgment="supporting",
            justification="The mathematical expression of Bell's locality assumption. "
            "The constraint that outcomes depend only on local settings and λ is clear.",
        ),

        # Local hidden correlation form
        review_claim(
            c_local_hidden_correlation_form,
            prior=0.85,
            judgment="supporting",
            justification="This is the mathematical consequence of the locality constraint. "
            "If outcomes depend only on local variables, the correlation must take this form.",
        ),

        # Bell inequality (mathematical theorem)
        review_claim(
            c_bell_inequality,
            prior=0.95,
            judgment="supporting",
            justification="Bell's inequality is a mathematical theorem derived from the "
            "local hidden variable form. The derivation is rigorous and uncontroversial.",
        ),

        # Local theories give non-stationary correlations
        review_claim(
            c_local_theory_nonstationary,
            prior=0.85,
            judgment="supporting",
            justification="Mathematical result: functions satisfying Bell's inequality "
            "cannot be stationary at -1. This contrasts with the smooth QM correlation.",
        ),

        # QM violates Bell's inequality
        review_claim(
            c_qm_violates_bell_inequality,
            prior=0.95,
            judgment="supporting",
            justification="Both the mathematical claim (for specific angles) and its "
            "experimental verification (Aspect, Zeilinger, Weihs, etc.) are extremely well-established.",
        ),

        # Local HV incompatible with QM (Bell's main result)
        review_claim(
            c_local_hv_incompatible_with_qm,
            prior=0.90,
            judgment="supporting",
            justification="Bell's main theorem. Mathematical proof that no local hidden "
            "variable theory can reproduce all QM predictions. Overwhelmingly supported by experiment.",
        ),

        # Approximation impossible
        review_claim(
            c_approximation_impossible,
            prior=0.85,
            judgment="supporting",
            justification="Bell's argument that even approximate agreement fails for local "
            "hidden variables. The violation is not a small effect but significant.",
        ),

        # Locality-Lorentz invariance conflict
        review_claim(
            c_locality_lorentz_invariance_conflict,
            prior=0.80,
            judgment="supporting",
            justification="Bell's conclusion: any hidden variable theory reproducing QM must "
            "have instantaneous nonlocality, violating Lorentz invariance. This is a direct "
            "consequence of his theorem.",
        ),

        # Bell result generalizes
        review_claim(
            c_bell_result_generalizes,
            prior=0.85,
            judgment="supporting",
            justification="Bell correctly notes that the theorem extends beyond spin-1/2 "
            "to any quantum system with two-dimensional subspaces.",
        ),

        # Time-varying settings crucial
        review_claim(
            c_time_varying_settings_crucial,
            prior=0.85,
            judgment="supporting",
            justification="Bell's insight about the need for experiments with settings changed "
            "during particle flight. This is exactly what modern loophole-free tests do.",
        ),

        # Bell's theorem (main conclusion)
        review_claim(
            c_bell_theorem,
            prior=0.90,
            judgment="supporting",
            justification="The central result: no local hidden variable theory can reproduce "
            "all QM predictions. Mathematical theorem plus extensive experimental verification.",
        ),

        # ============================================================
        # Alternatives from Bell's module
        # ============================================================

        # Alternative: QM itself is nonlocal
        review_claim(
            alt_locality_violates_qm,
            prior=0.60,
            judgment="tentative",
            justification="One response to Bell's theorem: accept that QM is inherently nonlocal. "
            "This is the view of many physicists after Bell. Moderate prior reflecting the "
            "ongoing debate about the meaning of quantum nonlocality.",
        ),

        # Alternative: Superdeterminism
        review_claim(
            alt_superdeterminism,
            prior=0.25,
            judgment="tentative",
            justification="Superdeterminism rejects the 'free choice' or 'no-conspiracy' assumption. "
            "Low prior because it undermines scientific methodology and has no independent support, "
            "but it remains a logical possibility.",
        ),

        # Alternative: Retrocausality
        review_claim(
            alt_retrocausality,
            prior=0.30,
            judgment="tentative",
            justification="Retrocausal theories offer another way around Bell's theorem. "
            "Low to moderate prior: mathematically possible but requires radical revisions "
            "to our concept of causality with little empirical support.",
        ),

        # ============================================================
        # Strategy reviews — from Bell's module
        # ============================================================

        # Strategy 1: EPR to hidden variables
        review_strategy(
            _strat_epr_to_hv,
            judgment="formalized",
            justification="EPR's incompleteness argument (@c_qm_incomplete) directly motivates "
            "the search for hidden variables (@c_epr_motivation_hidden_variables). Bohr's "
            "alternative is that QM is complete (@c_qm_is_complete).",
        ),

        # Strategy 2: Locality to predetermination
        review_strategy(
            _strat_locality_to_predetermination,
            judgment="formalized",
            justification="Bell's key inference: perfect anticorrelation (@c_singlet_perfect_anticorrelation) "
            "plus locality (@c_locality_constraint_formal) implies predetermination "
            "(@c_locality_implies_predetermination). This is the EPR-Bell argument structure.",
        ),

        # Strategy 3: Predetermination to HV formalism
        review_strategy(
            _strat_predetermination_to_hv_formalism,
            judgment="formalized",
            justification="If results are predetermined despite the wave function not specifying "
            "them (@c_locality_implies_predetermination), then hidden variables must exist "
            "(@c_hidden_variables_complete_specification). Direct logical step.",
        ),

        # Strategy 4: HV + locality → Bell form
        review_strategy(
            _strat_hv_locality_to_bell_form,
            judgment="formalized",
            justification="Hidden variables (@c_hidden_variables_complete_specification) plus "
            "locality (@c_locality_constraint_formal) mathematically imply the local "
            "correlation form (@c_local_hidden_correlation_form). Pure deduction.",
        ),

        # Strategy 5: Local form → Bell inequality
        review_strategy(
            _strat_local_form_to_inequality,
            judgment="formalized",
            justification="The mathematical derivation of Bell's inequality (@c_bell_inequality) "
            "from the local hidden variable form (@c_local_hidden_correlation_form). "
            "Rigorous mathematical proof.",
        ),

        # Strategy 6: QM formalism → correlation
        review_strategy(
            _strat_qm_to_correlation,
            judgment="formalized",
            justification="Standard QM calculation: singlet state (@s_singlet_spin_state) "
            "yields correlation -a·b (@c_qm_correlation_function). Uncontroversial.",
        ),

        # Strategy 7: Local theories non-stationary
        review_strategy(
            _strat_local_theories_nonstationary,
            judgment="formalized",
            justification="Mathematical property: functions satisfying Bell's inequality "
            "(@c_bell_inequality) cannot be stationary at -1, unlike the QM prediction. "
            "This is key to Bell's argument.",
        ),

        # Strategy 8: QM violates Bell's inequality
        review_strategy(
            _strat_qm_violates_inequality,
            judgment="formalized",
            justification="The heart of Bell's theorem: QM predictions (@c_qm_correlation_function) "
            "violate Bell's inequality (@c_qm_violates_bell_inequality). Therefore local "
            "hidden variables cannot reproduce QM (@c_local_hv_incompatible_with_qm). "
            "The alternative is QM nonlocality (@alt_locality_violates_qm). "
            "Extremely well-supported by experiment.",
        ),

        # Strategy 9: Main theorem
        review_strategy(
            _strat_main_theorem,
            judgment="formalized",
            justification="Synthesizes the entire argument: local form (@c_local_hidden_correlation_form) → "
            "Bell inequality (@c_bell_inequality) → QM violation (@c_qm_violates_bell_inequality) → "
            "incompatibility (@c_bell_theorem). Bell's main result.",
        ),

        # Strategy 10: Locality-Lorentz implications
        review_strategy(
            _strat_locality_lorentz_implication,
            judgment="formalized",
            justification="Since local HV cannot work (@c_bell_theorem), any HV theory that "
            "reproduces QM must be nonlocal. This nonlocality implies instantaneous influence "
            "and Lorentz invariance violation (@c_locality_lorentz_invariance_conflict). "
            "Important implication of Bell's theorem.",
        ),

        # Strategy 11: Locality as essential difficulty
        review_strategy(
            _strat_locality_essential,
            conditional_probability=0.85,
            judgment="formalized",
            justification="Synthesizes Bell's insight: locality is the essential difficulty "
            "(@c_locality_creates_difficulty). You can have locality (and lose QM agreement) "
            "or QM agreement (and lose locality), but not both.",
        ),

        # Strategy 12: Approximation impossible
        review_strategy(
            _strat_approximation_impossible,
            judgment="formalized",
            justification="The violation of Bell's inequality is not a small effect that can "
            "be fixed by approximation. There's a fundamental gap (@c_approximation_impossible). "
            "Important for understanding why Bell's theorem is robust.",
        ),

        # Strategy 13: Superdeterminism alternative
        review_strategy(
            _strat_superdeterminism_alternative,
            judgment="formalized",
            justification="Bell's theorem assumes settings can be chosen independently of λ. "
            "If this fails (superdeterminism, @alt_superdeterminism), local HV could work. "
            "Low prior because this undermines scientific methodology.",
        ),

        # Strategy 14: Retrocausality alternative
        review_strategy(
            _strat_retrocausality_alternative,
            judgment="formalized",
            justification="Retrocausal theories (@alt_retrocausality) offer another loophole. "
            "Allow backwards-in-time influence instead of nonlocality. Mathematically possible "
            "but philosophically radical.",
        ),

        # Strategy 15: Generalization beyond spin
        review_strategy(
            _strat_generalization,
            judgment="formalized",
            justification="Bell correctly notes the theorem generalizes beyond spin-1/2 "
            "(@c_bell_result_generalizes). Any system with appropriate subspaces exhibits "
            "the same incompatibility.",
        ),

        # Strategy 16: Experimental implications
        review_strategy(
            _strat_experimental_implications,
            judgment="formalized",
            justification="Bell identifies the crucial experimental test: change settings during "
            "particle flight (@c_time_varying_settings_crucial). This prevents light-speed "
            "communication. Exactly what modern loophole-free tests do.",
        ),

        # ============================================================
        # Leaf premises — priors from s5_chsh_1969.py (CHSH inequality)
        # ============================================================

        # CHSH particle setup
        review_claim(
            c_chsh_particle_pair_setup,
            prior=0.95,
            judgment="supporting",
            justification="Standard description of a two-particle correlation experiment. "
            "The formalism is uncontroversial.",
        ),

        # CHSH locality formalism
        review_claim(
            c_chsh_locality_assumption,
            prior=0.75,
            judgment="tentative",
            justification="The locality assumption is what Bell's theorem tests. This "
            "formalization is clear and represents the local hidden variable position.",
        ),

        # CHSH two settings per side
        review_claim(
            c_chsh_two_settings_claim,
            prior=0.95,
            judgment="supporting",
            justification="This is a description of the experimental setup. The CHSH "
            "configuration uses two measurement settings on each side.",
        ),

        # Emergence correlation for photons
        review_claim(
            c_chsh_emergence_interpretation,
            prior=0.80,
            judgment="supporting",
            justification="A reasonable approach to photon polarization experiments. "
            "Interpreting +1 as emergence from the polarizer is standard.",
        ),

        # Calcium cascade source
        review_claim(
            c_chsh_calcium_source,
            prior=0.95,
            judgment="supporting",
            justification="The 6S₀-4³P₁-4S₀ cascade in calcium is a well-established "
            "source of polarization-entangled photon pairs. Historically accurate.",
        ),

        # CHSH generalizes Bell
        review_claim(
            c_chsh_generalizes_bell,
            prior=0.90,
            judgment="supporting",
            justification="Accurate historical and mathematical statement. CHSH removes "
            "Bell's perfect correlation requirement, making experimental tests feasible.",
        ),

        # CHSH avoids perfect correlation
        review_claim(
            c_chsh_avoids_perfect_correlation,
            prior=0.90,
            judgment="supporting",
            justification="Key innovation of CHSH: they assume P(b', b) = 1 - ε rather "
            "than perfect correlation. This makes the inequality experimentally testable.",
        ),

        # CHSH inequality in general form
        review_claim(
            c_chsh_inequality_form,
            prior=0.95,
            judgment="supporting",
            justification="Mathematical theorem derived from local hidden variable assumptions. "
            "The derivation is rigorous.",
        ),

        # CHSH standard form |S| ≤ 2
        review_claim(
            c_chsh_standard_form,
            prior=0.95,
            judgment="supporting",
            justification="The standard form of the CHSH inequality. Mathematically proven "
            "consequence of local hidden variables.",
        ),

        # CHSH experimental prediction form
        review_claim(
            c_chsh_experimental_prediction,
            prior=0.85,
            judgment="supporting",
            justification="Translation of the CHSH inequality into experimental counting rates. "
            "The derivation is sound.",
        ),

        # QM predicts violation of CHSH
        review_claim(
            c_qm_predicts_violation_chsh,
            prior=0.95,
            judgment="supporting",
            justification="Standard QM calculation for the calcium cascade. The prediction "
            "S = 2√2 is well-established and experimentally verified.",
        ),

        # CHSH optimal angles
        review_claim(
            c_chsh_optimal_angles,
            prior=0.95,
            judgment="supporting",
            justification="Mathematical result: for E = -cos(θ), the maximum of S occurs "
            "at the specified angles. The calculation is straightforward.",
        ),

        # Detector efficiency requirements
        review_claim(
            c_chsh_detector_efficiency_requirement,
            prior=0.90,
            judgment="supporting",
            justification="CHSH correctly identify that efficient detectors are needed. "
            "The threshold condition is mathematically derived.",
        ),

        # Efficiency-angle tradeoff
        review_claim(
            c_chsh_efficiency_angle_tradeoff,
            prior=0.90,
            judgment="supporting",
            justification="The trade-off between polarizer efficiency and collection angle "
            "is a physical constraint. The relationship F₁(θ)F₂(θ) > 1/2 is derived.",
        ),

        # CHSH detection assumption
        review_claim(
            c_chsh_detection_assumption,
            prior=0.60,
            judgment="tentative",
            justification="This assumption is necessary for the experimental prediction but "
            "creates the 'detection loophole'. Moderate prior reflecting this caveat.",
        ),

        # Only two orientations needed
        review_claim(
            c_chsh_two_relative_orientations,
            prior=0.95,
            judgment="supporting",
            justification="Mathematical observation: the four angles in CHSH correspond "
            "to two relative orientations. Correct.",
        ),

        # Wu-Shaknov inadequate
        review_claim(
            c_wu_shaknov_inadequate,
            prior=0.85,
            judgment="supporting",
            justification="CHSH correctly note that Compton polarimeters cannot provide "
            "a decisive test. The physics argument is sound.",
        ),

        # Kocher-Commins inadequate
        review_claim(
            c_kocher_commins_inadequate,
            prior=0.90,
            judgment="supporting",
            justification="Accurate assessment: the Kocher-Commins experiment measured only "
            "at 0° and 90°, insufficient for CHSH.",
        ),

        # CHSH proposed experiment
        review_claim(
            c_chsh_proposed_experiment,
            prior=0.90,
            judgment="supporting",
            justification="The proposal to extend Kocher-Commins with measurements at "
            "22.5° and 67.5° is sound and historically significant.",
        ),

        # Tsirelson's bound
        review_claim(
            c_chsh_tsirelson_bound,
            prior=0.95,
            judgment="supporting",
            justification="S = 2√2 is the maximum QM value for CHSH. This is Tsirelson's "
            "bound, a fundamental result in quantum information.",
        ),

        # CHSH experimental consequence
        review_claim(
            c_chsh_experimental_consequence,
            prior=0.90,
            judgment="supporting",
            justification="Correct: CHSH transforms the philosophical debate into an "
            "experimental test. If S > 2, local hidden variables are ruled out.",
        ),

        # CHSH general beyond photons
        review_claim(
            c_chsh_general_beyond_photons,
            prior=0.90,
            judgment="supporting",
            justification="Correct: CHSH applies to any two-level quantum system, not "
            "just photons. The inequality is very general.",
        ),

        # CHSH detection loophole
        review_claim(
            c_chsh_detection_loophole,
            prior=0.75,
            judgment="supporting",
            justification="Correct identification of the detection loophole. The assumption "
            "that emergence probability is setting-independent is testable but non-trivial.",
        ),

        # ============================================================
        # Alternatives from CHSH's module
        # ============================================================

        # Alternative: Detector conspiracy
        review_claim(
            alt_chsh_detector_conspiracy,
            prior=0.30,
            judgment="tentative",
            justification="The detector conspiracy loophole. Low prior because it would "
            "require fine-tuned correlation between hidden variables and detector response. "
            "Possible but implausible.",
        ),

        # Alternative: CHSH with superdeterminism
        review_claim(
            alt_chsh_superdeterminism_settings,
            prior=0.25,
            judgment="tentative",
            justification="Superdeterminism applied to CHSH. Low prior for the same "
            "reasons as in Bell's theorem: it undermines scientific methodology.",
        ),

        # ============================================================
        # Strategy reviews — from CHSH's module
        # ============================================================

        # Strategy 1: Bell to CHSH motivation
        review_strategy(
            _strat_bell_to_chsh_motivation,
            judgment="formalized",
            justification="Bell's theorem (@c_bell_theorem) requires perfect correlation "
            "for experimental test (@c_bell_inequality). CHSH removes this requirement "
            "(@c_chsh_generalizes_bell), making experiments feasible.",
        ),

        # Strategy 2: CHSH setup formalism
        review_strategy(
            _strat_chsh_setup_formalism,
            judgment="formalized",
            justification="The CHSH particle setup (@c_chsh_particle_pair_setup) with locality "
            "(@c_chsh_locality_assumption) yields an inequality without perfect correlation "
            "requirement (@c_chsh_avoids_perfect_correlation).",
        ),

        # Strategy 3: Two settings to CHSH
        review_strategy(
            _strat_two_settings_to_chsh,
            judgment="formalized",
            justification="Two settings per side (@c_chsh_two_settings_claim) plus "
            "relaxed perfect correlation (@c_chsh_avoids_perfect_correlation) yields "
            "the CHSH inequality (@c_chsh_inequality_form).",
        ),

        # Strategy 4: Experimental simplification
        review_strategy(
            _strat_experimental_simplification,
            judgment="formalized",
            justification="With constant detection rates and the detection assumption "
            "(@c_chsh_detection_assumption), the general CHSH inequality "
            "(@c_chsh_inequality_form) simplifies to |S| ≤ 2 (@c_chsh_standard_form).",
        ),

        # Strategy 5: Experimental prediction form
        review_strategy(
            _strat_experimental_prediction_form,
            judgment="formalized",
            justification="The standard CHSH inequality (@c_chsh_standard_form) is expressed "
            "in terms of counting rates using the emergence correlation framework "
            "(@c_chsh_emergence_interpretation), yielding testable predictions "
            "(@c_chsh_experimental_prediction).",
        ),

        # Strategy 6: QM to CHSH violation
        review_strategy(
            _strat_qm_to_chsh_violation,
            judgment="formalized",
            justification="QM correlation (@c_qm_correlation_function) for the calcium "
            "cascade (@c_chsh_calcium_source) predicts violation of CHSH with S = 2√2 "
            "(@c_qm_predicts_violation_chsh, @c_chsh_tsirelson_bound).",
        ),

        # Strategy 7: Optimal angles derivation
        review_strategy(
            _strat_optimal_angles_derivation,
            judgment="formalized",
            justification="Maximizing S = E(a,b) - E(a,b') + E(a',b) + E(a',b') with "
            "E = -cos(θ) (@c_qm_correlation_function) yields optimal angles "
            "a=0°, a'=45°, b=22.5°, b'=67.5° (@c_chsh_optimal_angles).",
        ),

        # Strategy 8: Efficiency requirements
        review_strategy(
            _strat_efficiency_requirements,
            judgment="formalized",
            justification="QM predicts CHSH violation (@c_qm_predicts_violation_chsh) but "
            "the experimental test (@c_chsh_experimental_prediction) requires minimum "
            "detector efficiency and polarizer quality (@c_chsh_detector_efficiency_requirement).",
        ),

        # Strategy 9: Efficiency-angle tradeoff
        review_strategy(
            _strat_efficiency_angle_tradeoff,
            judgment="formalized",
            justification="The detector efficiency requirement (@c_chsh_detector_efficiency_requirement) "
            "implies a trade-off: for given efficiency, there's an upper limit on "
            "collection angle θ, and vice versa (@c_chsh_efficiency_angle_tradeoff).",
        ),

        # Strategy 10: Two orientations sufficient
        review_strategy(
            _strat_two_orientations_sufficient,
            judgment="formalized",
            justification="The optimal CHSH angles (@c_chsh_optimal_angles) correspond "
            "to only two relative orientations: 22.5° and 67.5°. An experiment need "
            "only measure at these two orientations (@c_chsh_two_relative_orientations).",
        ),

        # Strategy 11: Previous experiments inadequate
        review_strategy(
            _strat_previous_experiments_inadequate,
            judgment="formalized",
            justification="Previous experiments (Wu-Shaknov, Kocher-Commins) were "
            "inadequate (@c_wu_shaknov_inadequate, @c_kocher_commins_inadequate). "
            "CHSH proposed extending Kocher-Commins to include 22.5° and 67.5° measurements "
            "(@c_chsh_proposed_experiment).",
        ),

        # Strategy 12: Tsirelson bound
        review_strategy(
            _strat_tsirelson_bound,
            judgment="formalized",
            justification="QM predicts S = 2√2 at optimal angles "
            "(@c_qm_predicts_violation_chsh, @c_chsh_optimal_angles). This is the "
            "maximum QM value, Tsirelson's bound (@c_chsh_tsirelson_bound).",
        ),

        # Strategy 13: Experimental locality test
        review_strategy(
            _strat_experimental_locality_test,
            judgment="formalized",
            justification="The CHSH inequality (@c_chsh_standard_form) and its QM violation "
            "(@c_qm_predicts_violation_chsh) create an experimental test: if S > 2, "
            "local hidden variables are ruled out; if S ≤ 2, they remain viable "
            "(@c_chsh_experimental_consequence).",
        ),

        # Strategy 14: Generality beyond photons
        review_strategy(
            _strat_generality_beyond_photons,
            judgment="formalized",
            justification="CHSH requires only two settings and two outcomes per side "
            "(@c_chsh_particle_pair_setup, @c_chsh_standard_form), not photon-specific "
            "properties. Therefore it applies to various two-level systems "
            "(@c_chsh_general_beyond_photons).",
        ),

        # Strategy 15: Detection loophole
        review_strategy(
            _strat_detection_loophole,
            judgment="formalized",
            justification="The CHSH derivation requires setting-independent emergence "
            "probability (@c_chsh_detection_assumption). If this fails—e.g., if hidden "
            "variables affect emergence in a setting-dependent way—local hidden variables "
            "could potentially reproduce QM violations (@alt_chsh_detector_conspiracy). "
            "This is the detection loophole (@c_chsh_detection_loophole).",
        ),

        # Strategy 16: Superdeterminism CHSH
        review_strategy(
            _strat_superdeterminism_chsh,
            judgment="formalized",
            justification="CHSH assumes settings can be chosen independently of λ. "
            "If settings and λ are correlated (superdeterminism), the derivation "
            "doesn't apply (@alt_chsh_superdeterminism_settings), offering a "
            "potential loophole around the experimental consequences "
            "(@c_chsh_experimental_consequence).",
        ),

        # Strategy 17: CHSH main theorem
        review_strategy(
            _strat_chsh_main_theorem,
            judgment="formalized",
            justification="Local hidden variables must satisfy |S| ≤ 2 "
            "(@c_chsh_standard_form). QM predicts S = 2√2 at optimal settings "
            "(@c_qm_predicts_violation_chsh, @c_chsh_tsirelson_bound). This "
            "contradiction creates an experimental test (@c_chsh_experimental_consequence).",
        ),
    ],
)
