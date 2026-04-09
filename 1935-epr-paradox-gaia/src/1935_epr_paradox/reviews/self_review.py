from gaia.cli._reviews import ReviewBundle, ClaimReview, StrategyReview

# Import knowledge objects and strategy objects
from ..motivation import (
    c_noncommuting_preclude,
    c_qm_assumes_complete,
    _ded_momentum_definite,
    _ded_position_indefinite,
    _ded_initial_dilemma,
)
from ..s2_two_particle import (
    c_individual_state_unmeasurable,
    c_complete_theory_possible,
    _infer_two_states,
    _ded_momentum_meas,
    _ded_position_meas,
    _infer_both_reality,
    _ded_pq_noncommute,
    _infer_negation_chain,
    _ded_qm_incomplete,
    _infer_objection,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ── Independent premises (3) ──
        ClaimReview(
            subject=c_noncommuting_preclude,
            prior=0.99,
            justification="Core result of QM: non-commuting operators preclude simultaneous "
            "definite values. Established by the uncertainty principle.",
        ),
        ClaimReview(
            subject=c_individual_state_unmeasurable,
            prior=0.95,
            justification="Standard QM: after interaction, individual states require measurement "
            "(wave packet reduction) to determine.",
        ),
        ClaimReview(
            subject=c_qm_assumes_complete,
            prior=0.85,
            justification="The Copenhagen interpretation assumes completeness, though this is "
            "precisely what EPR challenge. Moderately high prior as the prevailing orthodoxy in 1935.",
        ),
        # ── Orphaned claim ──
        ClaimReview(
            subject=c_complete_theory_possible,
            prior=0.7,
            justification="EPR express belief that a more complete theory is possible, but "
            "provide no argument beyond the incompleteness result. Article of faith.",
        ),
        # ── Section 1 strategies (all deductions, no review params needed) ──
        StrategyReview(
            subject=_ded_momentum_definite,
            justification="Strict mathematical derivation from eigenvalue equation.",
        ),
        StrategyReview(
            subject=_ded_position_indefinite,
            justification="Direct computation of probability distribution in momentum eigenstate.",
        ),
        StrategyReview(
            subject=_ded_initial_dilemma,
            justification="Logical consequence: if definite values existed, they'd be in the "
            "complete description and predictable. They're not, so one of the two "
            "alternatives must hold.",
        ),
        # ── Section 2 strategies ──
        StrategyReview(
            subject=_infer_two_states,
            conditional_probabilities=[0.1, 0.9],
            justification="If wave packet reduction is valid (standard QM), two different "
            "measurements give different states for II with high probability.",
        ),
        StrategyReview(
            subject=_ded_momentum_meas,
            justification="Direct algebraic substitution into the two-particle wave function.",
        ),
        StrategyReview(
            subject=_ded_position_meas,
            justification="Direct computation using Dirac delta function properties.",
        ),
        StrategyReview(
            subject=_infer_both_reality,
            conditional_probabilities=[0.05, 0.3, 0.5, 0.95],
            justification="If both measurements yield definite values, the criterion of reality "
            "makes both P and Q elements of reality with high probability. Main uncertainty: "
            "whether criterion applies to counterfactual predictions (one OR the other, not both).",
        ),
        StrategyReview(
            subject=_ded_pq_noncommute,
            justification="Standard canonical commutation relation.",
        ),
        StrategyReview(
            subject=_infer_negation_chain,
            conditional_probabilities=[0.01, 0.2, 0.4, 0.6, 0.3, 0.7, 0.8, 0.3,
                                       0.5, 0.7, 0.6, 0.9, 0.7, 0.8, 0.9, 0.98],
            justification="The logical chain from dilemma + completeness assumption + "
            "simultaneous reality + non-commutation → negation of (2). High conditional "
            "when all premises hold.",
        ),
        StrategyReview(
            subject=_ded_qm_incomplete,
            justification="Logical consequence: if negation of (1) implies negation of (2), "
            "and (1) and (2) are exhaustive alternatives, then (1) must be true.",
        ),
        StrategyReview(
            subject=_infer_objection,
            conditional_probabilities=[0.1, 0.9],
            justification="If both are elements of reality, the objection about simultaneity "
            "is weak because it makes reality depend on remote measurement. Strong "
            "philosophical argument.",
        ),
    ],
)
