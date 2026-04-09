from gaia.cli._reviews import ReviewBundle, ClaimReview, StrategyReview

from ..motivation import (
    c_locality_hypothesis,
    c_qm_singlet_prediction,
    c_predetermination_implies_hidden_vars,
)
from ..s3_illustration import (
    c_single_particle_hv_possible,
    c_verbal_features_reproducible,
    c_not_stationary_at_minimum,
    c_nonlocal_reproduces_qm,
)
from ..s4_contradiction import (
    c_crucial_experiments,
    _ded_perfect_anticorr,
    _ded_bell_inequality,
    _infer_qm_violates,
    _ded_bell_theorem,
    _ded_nonlocality,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ── Independent premises ──
        ClaimReview(
            subject=c_locality_hypothesis,
            prior=0.8,
            justification="Einstein's locality principle is deeply intuitive and was "
            "widely assumed. However, it is precisely this assumption that Bell's theorem "
            "will challenge. Moderately high prior as the working assumption.",
        ),
        ClaimReview(
            subject=c_qm_singlet_prediction,
            prior=0.95,
            justification="The QM prediction $P = -\\hat{a} \\cdot \\hat{b}$ for the "
            "singlet state is a well-established result derivable from standard QM.",
        ),
        # ── Orphaned claims ──
        ClaimReview(
            subject=c_single_particle_hv_possible,
            prior=0.95,
            justification="Bell's explicit construction proves this is possible.",
        ),
        ClaimReview(
            subject=c_verbal_features_reproducible,
            prior=0.9,
            justification="Bell gives an explicit model that reproduces these features.",
        ),
        ClaimReview(
            subject=c_not_stationary_at_minimum,
            prior=0.85,
            justification="Mathematical property of the model. Key insight leading to "
            "the main result.",
        ),
        ClaimReview(
            subject=c_nonlocal_reproduces_qm,
            prior=0.9,
            justification="If non-local dependence is allowed, reproduction is trivial. "
            "This is the point: locality is the constraint that makes it impossible.",
        ),
        ClaimReview(
            subject=c_predetermination_implies_hidden_vars,
            prior=0.75,
            justification="Logical consequence of locality + QM predictions, but the "
            "inference from 'predictable' to 'predetermined' is the key step EPR take.",
        ),
        ClaimReview(
            subject=c_crucial_experiments,
            prior=0.8,
            justification="Bohm-Aharonov type experiments with rapid setting changes "
            "are indeed crucial for closing the locality loophole.",
        ),
        # ── Strategies (all deductions except one infer) ──
        StrategyReview(
            subject=_ded_perfect_anticorr,
            justification="Mathematical necessity: $P = -1$ only when $A = -B$ a.e.",
        ),
        StrategyReview(
            subject=_ded_bell_inequality,
            justification="Algebraic manipulation of the integral form, using $|A| = 1$.",
        ),
        StrategyReview(
            subject=_infer_qm_violates,
            conditional_probabilities=[0.05, 0.4, 0.6, 0.95],
            justification="If both the inequality and QM prediction hold, violation "
            "follows with high probability. The specific angle choice makes the violation "
            "unambiguous.",
        ),
        StrategyReview(
            subject=_ded_bell_theorem,
            justification="Direct consequence: violation of the inequality means no local "
            "HV theory can match QM.",
        ),
        StrategyReview(
            subject=_ded_nonlocality,
            justification="Logical consequence of the theorem: any deterministic completion "
            "of QM must be non-local.",
        ),
    ],
)
