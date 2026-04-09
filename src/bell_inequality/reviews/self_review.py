"""Review sidecar for the EPR Paradox formalization.

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

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ============================================================
        # Leaf premises — priors
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
            prior=0.70,
            judgment="supporting",
            justification="This is EPR's locality assumption — that spatially separated systems "
            "cannot instantaneously affect each other. While intuitively compelling in 1935, "
            "Bell's theorem (1964) later showed this assumption is testable and the experiments "
            "suggest quantum correlations violate it.",
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
            prior=0.30,
            judgment="tentative",
            justification="This represents the Copenhagen interpretation's likely response: "
            "the correlation is a property of the entangled state, not evidence of a "
            "pre-existing element of reality. However, EPR's locality argument makes this "
            "position difficult to maintain without abandoning locality.",
        ),

        # Abduction alternative: position predictability is merely formal
        # Same as above for position.
        review_claim(
            alt_position_formal_not_real,
            prior=0.30,
            judgment="tentative",
            justification="Same reasoning as the momentum alternative. The Copenhagen "
            "response would deny independent reality but struggles with the no-disturbance condition.",
        ),

        # ============================================================
        # Orphaned / background-only claims — priors required by engine
        # ============================================================

        # EPR criterion of reality — background-only but needs prior
        review_claim(
            c_criterion_of_reality,
            prior=0.75,
            judgment="supporting",
            justification="A reasonable sufficient condition for reality. It is consistent "
            "with both classical and QM ideas of reality, though not exhaustive.",
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
            prior=0.50,
            judgment="neutral",
            justification="EPR express belief but provide no argument. This is "
            "the hidden variables hypothesis. No evidence in this paper.",
        ),

        # ============================================================
        # Strategy reviews — conditional probabilities
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
    ],
)
