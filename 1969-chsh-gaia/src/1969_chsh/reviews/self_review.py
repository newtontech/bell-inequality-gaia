from gaia.cli._reviews import ReviewBundle, ClaimReview, StrategyReview

from .. import (
    c_chsh_locality,
    c_qm_photon_prediction,
    c_existing_experiments_insufficient,
    _ded_chsh_inequality,
    _infer_qm_violates,
    _ded_decisive,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        ClaimReview(
            subject=c_chsh_locality,
            prior=0.8,
            justification="Same locality assumption as Bell 1964, now stated for "
            "general binary-outcome experiments. Reasonable but unproven.",
        ),
        ClaimReview(
            subject=c_qm_photon_prediction,
            prior=0.9,
            justification="Standard QM calculation for atomic cascade photons.",
        ),
        ClaimReview(
            subject=c_existing_experiments_insufficient,
            prior=0.85,
            justification="Valid analysis: Wu-Shaknov used Compton scattering (weak "
            "polarization index), Kocher-Commins only measured 0 and 90 degrees.",
        ),
        StrategyReview(
            subject=_ded_chsh_inequality,
            justification="Mathematical derivation from locality assumption, generalizing "
            "Bell's original proof to allow imperfect correlation.",
        ),
        StrategyReview(
            subject=_infer_qm_violates,
            conditional_probabilities=[0.05, 0.3, 0.6, 0.95],
            justification="If both the inequality and QM prediction hold, violation follows "
            "at specific angles with high probability.",
        ),
        StrategyReview(
            subject=_ded_decisive,
            justification="Logical consequence: if QM violates the inequality at realizable "
            "settings, a measurement provides a decisive test.",
        ),
    ],
)
