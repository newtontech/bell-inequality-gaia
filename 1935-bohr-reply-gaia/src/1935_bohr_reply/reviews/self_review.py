from gaia.cli._reviews import ReviewBundle, ClaimReview, StrategyReview

from ..motivation import (
    c_bohr_summarizes_epr,
    c_bohr_rejects_epr_conclusion,
    c_criterion_ambiguity,
)
from ..s2_complementarity import (
    c_position_measurement_loses_momentum,
    c_momentum_measurement_loses_position,
    c_object_instrument_distinction,
    _infer_mutual_exclusion,
    _ded_complementarity,
    _ded_bohr_counter,
    _infer_qm_rational,
    _infer_relativity,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ── Independent premises ──
        ClaimReview(
            subject=c_criterion_ambiguity,
            prior=0.7,
            justification="Bohr makes a valid point that 'without disturbing' is ambiguous: "
            "there is no mechanical disturbance but there is an influence on conditions. "
            "However, EPR's criterion was carefully worded for physical, not epistemic, "
            "disturbance. Moderate prior.",
        ),
        ClaimReview(
            subject=c_position_measurement_loses_momentum,
            prior=0.85,
            justification="Standard QM: position measurement introduces uncontrollable "
            "momentum transfer. Well-established through uncertainty principle.",
        ),
        ClaimReview(
            subject=c_momentum_measurement_loses_position,
            prior=0.85,
            justification="Standard QM: momentum measurement introduces uncontrollable "
            "displacement. Well-established through uncertainty principle.",
        ),
        ClaimReview(
            subject=c_object_instrument_distinction,
            prior=0.8,
            justification="The cut between object and measuring instrument is a key "
            "feature of the Copenhagen interpretation. Bohr's argument is coherent "
            "within his framework.",
        ),
        # ── Orphaned claims ──
        ClaimReview(
            subject=c_bohr_summarizes_epr,
            prior=0.9,
            justification="Accurate summary of the EPR prediction mechanism.",
        ),
        ClaimReview(
            subject=c_bohr_rejects_epr_conclusion,
            prior=0.6,
            justification="Bohr asserts EPR's argument does not undermine QM soundness, "
            "but this is his conclusion, not a demonstrated fact. The formalism is "
            "consistent, but whether it is complete remains contested.",
        ),
        # ── Strategies ──
        StrategyReview(
            subject=_infer_mutual_exclusion,
            conditional_probabilities=[0.05, 0.4, 0.5, 0.9],
            justification="If both measurements lose complementary information, mutual "
            "exclusion follows with high probability. The inference is reasonable within "
            "Bohr's framework.",
        ),
        StrategyReview(
            subject=_ded_complementarity,
            justification="Logical consequence of mutual exclusion: if procedures exclude "
            "each other, this provides room for new laws (complementarity).",
        ),
        StrategyReview(
            subject=_ded_bohr_counter,
            justification="Logical deduction: if the criterion is ambiguous and "
            "complementarity explains why, the EPR conclusion does not follow.",
        ),
        StrategyReview(
            subject=_infer_qm_rational,
            conditional_probabilities=[0.05, 0.4, 0.5, 0.9],
            justification="If complementarity and object-instrument distinction hold, "
            "QM is a rational description within its scope.",
        ),
        StrategyReview(
            subject=_infer_relativity,
            conditional_probabilities=[0.1, 0.8],
            justification="The analogy between complementarity and relativity is "
            "suggestive but not a formal proof.",
        ),
    ],
)
