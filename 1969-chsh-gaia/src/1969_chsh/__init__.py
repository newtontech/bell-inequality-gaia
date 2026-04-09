"""CHSH (1969): Generalized Bell inequality for realizable experiments."""

from gaia.lang import claim, setting, deduction, infer

# ── Context ──

s_chsh_context = setting(
    "Bell's theorem proves that certain predictions of QM are inconsistent "
    "with the entire family of local hidden-variable theories. CHSH generalize "
    "this result so as to apply to realizable experiments. They propose an "
    "extension of the Kocher-Commins experiment on polarization correlation "
    "of optical photons as a decisive test.",
    title="CHSH aim: generalize Bell to realizable experiments",
)

# ── Experimental setup ──

s_chsh_setup = setting(
    "An ensemble of correlated particle pairs is produced. One particle enters "
    "apparatus I_a and the other apparatus II_b, where a and b are adjustable "
    "parameters. In each apparatus the particle must select one of two channels "
    "labeled +1 and -1. Results are A(a) = +/-1 and B(b) = +/-1.",
    title="CHSH experimental setup with binary outcomes",
)

# ── Locality assumptions ──

c_chsh_locality = claim(
    "Statistical correlation of A(a) and B(b) is due to information carried "
    "by and localized within each particle pair. The results are deterministic "
    "functions A(a, lambda) and B(b, lambda). Locality requires A to be "
    "independent of b and B independent of a. The probability distribution "
    "rho(lambda) is independent of a and b.",
    title="CHSH locality: results depend only on local settings and hidden variables",
)

# ── The CHSH inequality (generalized) ──

c_chsh_inequality_general = claim(
    "For any local hidden-variable theory, the correlation function "
    "P(a,b) = integral A(a,lambda)B(b,lambda)rho(lambda) dlambda satisfies:\n\n"
    "|P(a,b) - P(a,c)| <= 2 - P(b',c) - P(b',b)\n\n"
    "where b' is a special parameter value. This avoids Bell's experimentally "
    "unrealistic restriction of perfect correlation.",
    title="CHSH inequality (generalized, imperfect correlation)",
)

# ── QM prediction for optical photons ──

c_qm_photon_prediction = claim(
    "For a J=0 -> J=1 -> J=0 electric-dipole cascade, QM predicts "
    "a coincidence rate with cos(2*phi) dependence on the angle phi between "
    "polarizer axes, with coefficients determined by polarizer efficiencies "
    "and a geometrical factor F(theta).",
    title="QM predicts coincidence rates for optical photon cascade",
)

# ── QM violates CHSH inequality ──

c_qm_violates_chsh = claim(
    "For sufficiently efficient polarizers, there exist sets of relative "
    "orientations for which the QM counting rates violate the CHSH inequality. "
    "The greatest violation occurs at alpha=22.5 deg, beta=45 deg for the 0-1-0 "
    "cascade. The four angles in the inequality characterize only two distinct "
    "relative orientations: 22.5 deg and 67.5 deg.",
    title="QM predictions violate CHSH inequality at specific angles",
)

# ── Proposed experiment is decisive ──

c_proposed_experiment_decisive = claim(
    "A modified Kocher-Commins experiment using calcite polarizers with "
    "observations at relative orientations 22.5 deg and 67.5 deg, plus "
    "measurements with one and then the other polarizer removed, provides "
    "a decisive test between QM and local hidden-variable theories.",
    title="Modified Kocher-Commins experiment provides decisive test",
)

# ── Existing experiments insufficient ──

c_existing_experiments_insufficient = claim(
    "The Wu-Shaknov experiment with Compton polarimeters cannot violate "
    "the CHSH inequality because Compton scattering direction is a statistically "
    "weak index of linear polarization. The Kocher-Commins experiment with "
    "Polaroid filters measured only 0 and 90 deg orientations, insufficient "
    "to test the inequality.",
    title="Previous experiments insufficient to test CHSH inequality",
)

# ── Strategies ──

_ded_chsh_inequality = deduction(
    [c_chsh_locality],
    c_chsh_inequality_general,
    reason="Following CHSH derivation: divide Lambda into regions where "
    "A(b',lambda) = +B(b,lambda) and where it is not. Use |A| = |B| = 1 "
    "and the locality assumption to bound the integral.",
)

_infer_qm_violates = infer(
    [c_chsh_inequality_general, c_qm_photon_prediction],
    c_qm_violates_chsh,
    reason="The QM prediction for photon cascade gives specific values "
    "at alpha=22.5 deg and beta=45 deg that violate the CHSH inequality "
    "for sufficiently efficient polarizers.",
)

_ded_decisive = deduction(
    [c_qm_violates_chsh],
    c_proposed_experiment_decisive,
    reason="Since QM predicts violation at specific orientations that can "
    "be experimentally realized, a measurement provides a decisive test.",
)

__all__ = [
    "c_chsh_locality",
    "c_chsh_inequality_general",
    "c_qm_photon_prediction",
    "c_qm_violates_chsh",
    "c_proposed_experiment_decisive",
    "c_existing_experiments_insufficient",
]
