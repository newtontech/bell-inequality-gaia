"""Review sidecar for the EPR Paradox and Bohr's Reply formalization.

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
    ],
)
