"""Section 5: CHSH 1969 Inequality

Clauser, Horne, Shimony, and Holt's 1969 paper "Proposed Experiment to Test Local
Hidden-Variable Theories" generalizes Bell's theorem to apply to realizable experiments.
The key result is the CHSH inequality |S| ≤ 2, where S = E(a,b) - E(a,b') + E(a',b) + E(a',b'),
and the quantum mechanical prediction S = 2√2 for maximally entangled states.

The CHSH form is more experimentally practical than Bell's original inequality because
it doesn't require perfect correlation (detector efficiency = 1), making it applicable
to real experiments with photon polarization.

Reference: Clauser, J.F., Horne, M.A., Shimony, A., and Holt, R.A. (1969)
"Proposed Experiment to Test Local Hidden-Variable Theories" Physical Review Letters, 23, 880-884.
"""

from gaia.lang import (
    claim, setting, deduction, abduction, noisy_and,
    contradiction, complement,
)
from .s4_bell_1964 import (
    c_bell_inequality,
    c_qm_correlation_function,
    c_bell_theorem,
    c_local_hv_incompatible_with_qm,
    s_locality_assumption_bell,
    s_hidden_variable_formalism,
)

# ============================================================
# Settings — CHSH experimental setup
# ============================================================

s_chsh_particle_setup = setting(
    "Consider an ensemble of correlated pairs of particles moving so that one enters "
    "apparatus I and the other apparatus II. The apparatus parameters a and b are "
    "adjustable and represent measurement settings (e.g., polarizer orientations). "
    "In each apparatus, a particle must select one of two channels labeled +1 and -1. "
    "The results are A(a) and B(b), each equal to +1 or -1 according to which channel "
    "is selected.",
    title="CHSH correlated particle setup",
)

s_chsh_locality_formalism = setting(
    "The statistical correlation of A(a) and B(b) is due to information carried by "
    "and localized within each particle. At some time in the past, the particles "
    "constituting one pair were in contact and communicated regarding this information. "
    "The information is part of a set of hidden variables, denoted collectively by λ. "
    "The measurement results are deterministic functions A(a, λ) and B(b, λ). "
    "Locality requires A(a, λ) to be independent of b and B(b, λ) to be independent of a.",
    title="CHSH locality and hidden variable formalism",
)

s_chsh_two_settings_per_side = setting(
    "The CHSH setup allows two possible measurement settings on each side: a and a' "
    "for apparatus I, and b and b' for apparatus II. This four-setting configuration "
    "allows construction of the combined correlation quantity S = E(a,b) - E(a,b') + "
    "E(a',b) + E(a',b').",
    title="Two measurement settings per side",
)

s_chsh_emergence_correlation = setting(
    "For optical photon experiments, A(a) = +1 and B(b) = +1 are interpreted as "
    "emergence from polarizers, while -1 denotes non-emergence. The correlation "
    "function P(a, b) = ∫ A(a, λ)B(b, λ)ρ(λ)dλ is an emergence correlation function. "
    "An additional assumption is needed: if a pair of photons emerges from the filters, "
    "the probability of their joint detection is independent of a and b.",
    title="Emergence correlation for photon experiments",
)

s_chsh_calcium_cascade = setting(
    "The proposed experiment uses photon pairs emitted in the 6S₀-4³P₁-4S₀ cascade "
    "of calcium (a J=0→1→0 electric-dipole cascade). The two photons are in the "
    "visible spectrum, allowing the use of Polaroid-type filters. The correlation "
    "between photon polarizations in this cascade provides a test of the CHSH inequality.",
    title="Calcium atomic cascade photon source",
)

# ============================================================
# Claims — CHSH core argument
# ============================================================

c_chsh_particle_pair_setup = claim(
    "The CHSH experiment considers an ensemble of correlated particle pairs where "
    "one particle enters apparatus I and the other enters apparatus II. Each apparatus "
    "has adjustable parameters (measurement settings) and each particle selects one "
    "of two output channels labeled +1 and -1.",
    title="CHSH particle pair setup description",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_locality_assumption = claim(
    "The CHSH derivation assumes locality: the result A of measuring on particle 1 "
    "depends only on the local setting a and hidden variable λ, not on the distant "
    "setting b. Similarly, result B for particle 2 depends only on b and λ, not on a.",
    title="CHSH locality assumption",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_two_settings_claim = claim(
    "The CHSH configuration uses two measurement settings on each side: a and a' for "
    "apparatus I, and b and b' for apparatus II. This allows construction of the "
    "four-term correlation quantity S = E(a,b) - E(a,b') + E(a',b) + E(a',b').",
    title="Two measurement settings per side for CHSH",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_emergence_interpretation = claim(
    "For photon experiments, the outcomes A(a) = +1 and B(b) = +1 are interpreted as "
    "emergence from polarizers, while -1 denotes non-emergence. The correlation function "
    "measures the correlation of emergence events.",
    title="Emergence interpretation for photon experiments",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_calcium_source = claim(
    "The proposed CHSH experiment uses photon pairs from the calcium 6S₀-4³P₁-4S₀ cascade, "
    "a J=0→1→0 electric-dipole cascade producing visible photons suitable for "
    "polarization correlation measurements with polarizing filters.",
    title="Calcium cascade photon source for CHSH",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_generalizes_bell = claim(
    "Bell's 1964 theorem is generalized to apply to realizable experiments. "
    "Bell's original derivation required perfect correlation (detector efficiency = 1), "
    "which is experimentally unrealistic. The CHSH inequality applies even with "
    "imperfect detectors and finite efficiency.",
    title="CHSH generalizes Bell to realizable experiments",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_avoids_perfect_correlation = claim(
    "The CHSH derivation avoids Bell's experimentally unrealistic restriction that "
    "for some pair of parameters b and b' there is perfect correlation (i.e., the "
    "correlation function equals -1). Instead, CHSH assumes P(b', b) = 1 - ε where "
    "ε is close to but not equal to zero, allowing for experimental imperfections.",
    title="CHSH avoids perfect correlation requirement",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_inequality_form = claim(
    "The CHSH inequality states that for any local hidden variable theory, "
    "|P(a, b) - P(a, c)| ≤ 2 + P(b', b) - P(b', c), where P denotes the correlation "
    "function. When P(a, b) depends only on the parameter difference (e.g., rotational "
    "symmetry), this becomes |P(φ) - P(φ + η)| ≤ 2 + P(γ) - P(γ + η), where φ = a - b, "
    "η = c - b, and γ = b' - b.",
    title="CHSH inequality in general form",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_standard_form = claim(
    "In its most commonly used form, the CHSH inequality is written as |S| ≤ 2, "
    "where S = E(a, b) - E(a, b') + E(a', b) + E(a', b'). Here E denotes the "
    "expectation value of the product of measurement outcomes. This form applies "
    "when the experiment is designed such that single-particle detection rates "
    "are constants independent of the measurement settings.",
    title="CHSH inequality |S| ≤ 2",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_experimental_prediction = claim(
    "For realizable apparatus with photon polarization measurements, the CHSH inequality "
    "can be expressed in terms of coincidence counting rates: |R(α)/R₀ - R(α+β)/R₀| ≤ "
    "2 + R₁(γ)/R₀ - R₁(γ+β)/R₀, where R(α) is the coincidence rate with polarizers at "
    "relative angle α, R₀ is the rate with both polarizers removed, and R₁(γ) is the "
    "rate with one polarizer at angle γ.",
    title="CHSH inequality in experimental counting rates",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_qm_predicts_violation_chsh = claim(
    "Quantum mechanics predicts violation of the CHSH inequality for the proposed "
    "experiment. For a 0-1-0 electric-dipole cascade (like the calcium cascade), the "
    "maximum violation occurs at specific angles: α = 22.5°, β = 45°, and γ = 157.5°. "
    "The quantum mechanical correlation function predicts S = 2√2 ≈ 2.828 for maximally "
    "entangled states at optimal angles.",
    title="QM predicts violation: S = 2√2",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_optimal_angles = claim(
    "For maximally violating the CHSH inequality with quantum mechanics, the optimal "
    "measurement settings are: a = 0°, a' = 45°, b = 22.5°, b' = 67.5° (or any equivalent "
    "rotationally equivalent set). At these angles, quantum mechanics predicts S = "
    "E(0°, 22.5°) - E(0°, 67.5°) + E(45°, 22.5°) + E(45°, 67.5°) = -cos(22.5°) + cos(67.5°) "
    "- cos(22.5°) - cos(22.5°) = 2√2.",
    title="Optimal angles for CHSH violation",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_detector_efficiency_requirement = claim(
    "For the CHSH experiment to provide a decisive test of local hidden variable theories, "
    "the detector efficiency and polarizer quality must satisfy a threshold condition. "
    "Using calcite polarizers with efficiency ε_M ≈ 0.92 (uncoated) or ε_M ≈ 0.95 "
    "(with anti-reflection coating), and appropriate collection half-angle θ, the "
    "inequality can be violated by quantum mechanical predictions.",
    title="Detector efficiency requirements for CHSH test",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_efficiency_angle_tradeoff = claim(
    "There is a trade-off between polarizer efficiency ε_M and detector half-angle θ. "
    "For given ε_M, there is an upper limit on θ that allows violation of the CHSH "
    "inequality. Similarly, for given θ, there is a lower limit on ε_M. This relationship "
    "is expressed by the condition F₁(θ)F₂(θ) > 1/2, where F₁ and F₂ are efficiency "
    "functions of the half-angle.",
    title="Efficiency-angle tradeoff for decisive test",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_detection_assumption = claim(
    "The CHSH derivation requires an additional assumption for experimental predictions: "
    "that if a pair of photons emerges from the filters, the probability of their joint "
    "detection is independent of the polarizer orientations a and b. This assumption "
    "translates the emergence correlation function into predictions about coincidence "
    "counting rates.",
    title="Detection assumption for CHSH experiment",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_two_relative_orientations = claim(
    "The CHSH test requires measurement at only two distinct relative orientations of "
    "the polarizers: 22.5° and 67.5°. The four angles that appear in the inequality "
    "(α, α+β, γ, γ+β) correspond to just these two relative orientations. This "
    "simplification makes the experiment more practical to implement.",
    title="Only two polarizer orientations needed",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_wu_shaknov_inadequate = claim(
    "The Wu-Shaknov experiment on polarization correlation of 0.5-MeV gamma rays from "
    "positronium annihilation cannot provide a decisive test of the CHSH inequality. "
    "Although the polarization state is suitable, the high energy requires Compton "
    "polarimeters, and no binary decision partitioning of the Compton scattering sphere "
    "can yield a correlation that violates the CHSH inequality.",
    title="Wu-Shaknov experiment inadequate for CHSH test",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_kocher_commins_inadequate = claim(
    "The Kocher-Commins experiment on polarization correlation of photon pairs from "
    "the calcium 6S₀-4³P₁-4S₀ cascade did not provide a decisive test because their "
    "polarizers were not highly efficient and were placed only at relative orientations "
    "of 0° and 90°, which is insufficient to test the CHSH inequality. The CHSH proposal "
    "extends this experiment to include measurements at 22.5° and 67.5°.",
    title="Kocher-Commins experiment incomplete",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_proposed_experiment = claim(
    "A decisive test of local hidden variable theories can be obtained by modifying "
    "the Kocher-Commins experiment to include observations at two appropriate relative "
    "orientations (22.5° and 67.5°) and with each polarizer removed in turn. For "
    "realizable apparatus with sufficiently efficient polarizers and detectors, quantum "
    "mechanics predicts violation of inequality (2b), the CHSH inequality.",
    title="Proposed CHSH experiment with calcium cascade",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_tsirelson_bound = claim(
    "The maximum quantum mechanical value of S = 2√2 is known as Tsirelson's bound. "
    "This represents the maximum violation of the CHSH inequality possible in quantum "
    "mechanics. No quantum state can give S > 2√2, and this maximum is achieved "
    "by maximally entangled states such as the singlet state at optimal measurement angles.",
    title="Tsirelson's bound: maximum QM violation S = 2√2",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_experimental_consequence = claim(
    "The CHSH inequality transforms the philosophical debate between Einstein and Bohr "
    "into a concrete experimental test. If experiments show S > 2 (as quantum mechanics "
    "predicts with S = 2√2 at optimal settings), then local hidden variable theories "
    "are ruled out. If S ≤ 2 in all experiments, local hidden variables remain viable.",
    title="CHSH enables experimental test of locality",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_general_beyond_photons = claim(
    "The CHSH inequality is not limited to photon polarization experiments. It applies "
    "to any system with two measurement settings per side and two outcomes per measurement, "
    "including spin-1/2 particles, atomic states, and other two-level quantum systems. "
    "The essential requirement is the ability to measure correlated properties at "
    "multiple settings on each side.",
    title="CHSH applies to various two-level systems",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

c_chsh_detection_loophole = claim(
    "The detection assumption in CHSH—that joint detection probability is independent "
    "of polarizer settings—creates a potential loophole. If hidden variables affect "
    "which photons emerge from the polarizers in a way correlated with the settings, "
    "the inequality derivation may not apply to the actual experimental counting rates. "
    "This is known as the detection or 'fair sampling' loophole.",
    title="Detection loophole in CHSH derivation",
    metadata={"source": "artifacts/1969_clauser_chsh/chsh_1969_full_text.txt"},
)

# ============================================================
# Abduction alternatives — named for review sidecar
# ============================================================

alt_chsh_detector_conspiracy = claim(
    "A conspiracy between the hidden variables and detector efficiencies could allow "
    "a local hidden variable theory to reproduce CHSH violations. If the distribution "
    "of hidden variables when photons emerge from polarizers differs systematically "
    "from the overall distribution, the detection assumption fails and local hidden "
    "variables could potentially match QM predictions.",
    title="Alternative: Detector efficiency conspiracy",
)

alt_chsh_superdeterminism_settings = claim(
    "Superdeterminism—the correlation of hidden variables with measurement settings—could "
    "allow local hidden variables to violate the CHSH inequality bound. If the choice "
    "of which measurements to perform (a, a', b, b') is not independent of λ, then "
    "the derivation does not apply.",
    title="Alternative: CHSH with superdeterministic settings",
)

# ============================================================
# Operators — logical contradictions
# ============================================================

# Contradiction: CHSH inequality (|S| ≤ 2) vs. QM prediction (S = 2√2)
_chsh_qm_contradiction = contradiction(
    c_chsh_standard_form,
    c_qm_predicts_violation_chsh,
    reason="The CHSH inequality requires |S| ≤ 2 for any local hidden variable "
    "theory. Quantum mechanics predicts S = 2√2 ≈ 2.828 for maximally entangled "
    "states at optimal angles. Since 2.828 > 2, QM violates the CHSH bound.",
)

# Contradiction: Local HV theories (must satisfy CHSH) vs. QM (violates it)
_chsh_local_hv_contradiction = contradiction(
    c_chsh_standard_form,
    c_chsh_tsirelson_bound,
    reason="Local hidden variable theories must satisfy |S| ≤ 2. Quantum mechanics "
    "predicts a maximum of S = 2√2. The contradiction shows that QM cannot be "
    "described by any local hidden variable theory.",
)

# ============================================================
# Strategies — reasoning connections
# ============================================================

# Strategy 1: Bell's theorem motivates experimental generalization
_strat_bell_to_chsh_motivation = deduction(
    [c_bell_theorem, c_bell_inequality],
    c_chsh_generalizes_bell,
    reason="Bell's theorem shows that local hidden variables cannot reproduce QM, "
    "but the experimental test requires perfect correlation. CHSH generalizes Bell "
    "to avoid this requirement, making experimental tests feasible.",
    background=[c_chsh_avoids_perfect_correlation],
)

# Strategy 2: CHSH setup → locality + hidden variables
_strat_chsh_setup_formalism = deduction(
    [c_chsh_particle_pair_setup, c_chsh_locality_assumption],
    c_chsh_avoids_perfect_correlation,
    reason="The CHSH particle setup with locality allows derivation of an inequality "
    "that doesn't require perfect correlation.",
    background=[s_locality_assumption_bell, s_hidden_variable_formalism],
)

# Strategy 3: Two settings per side → CHSH form
_strat_two_settings_to_chsh = deduction(
    [c_chsh_two_settings_claim, c_chsh_avoids_perfect_correlation],
    c_chsh_inequality_form,
    reason="Having two measurement settings on each side allows construction of the "
    "four-term combination. Combined with the relaxed perfect correlation requirement, "
    "this yields the CHSH inequality in general form.",
)

# Strategy 4: Experimental simplification → standard CHSH form
_strat_experimental_simplification = deduction(
    [c_chsh_inequality_form, c_chsh_detection_assumption],
    c_chsh_standard_form,
    reason="When single-particle detection rates are constant and the detection "
    "assumption holds, the general CHSH inequality simplifies to the standard form |S| ≤ 2.",
)

# Strategy 5: Experimental prediction form
_strat_experimental_prediction_form = deduction(
    [c_chsh_standard_form, c_chsh_emergence_interpretation],
    c_chsh_experimental_prediction,
    reason="The standard CHSH inequality can be expressed in terms of experimental "
    "counting rates using the emergence correlation framework. This yields the testable "
    "prediction in terms of R(α), R₀, and R₁(γ).",
    background=[s_chsh_emergence_correlation],
)

# Strategy 6: QM calculation → CHSH violation prediction
_strat_qm_to_chsh_violation = deduction(
    [c_qm_correlation_function, c_chsh_calcium_source],
    c_qm_predicts_violation_chsh,
    reason="The quantum mechanical correlation function E = -cos(θ) applied to the "
    "calcium cascade setup predicts violation of the CHSH inequality at specific "
    "angles. The maximum violation is S = 2√2.",
    background=[c_chsh_tsirelson_bound, s_chsh_calcium_cascade],
)

# Strategy 7: Optimal angles calculation
_strat_optimal_angles_derivation = deduction(
    [c_qm_correlation_function, c_chsh_standard_form],
    c_chsh_optimal_angles,
    reason="To maximize the CHSH parameter S = E(a,b) - E(a,b') + E(a',b) + E(a',b') "
    "subject to the QM prediction E = -cos(θ), we find optimal angles a=0°, a'=45°, "
    "b=22.5°, b'=67.5°. At these angles, S = 2√2.",
)

# Strategy 8: Efficiency requirements for decisive test
_strat_efficiency_requirements = deduction(
    [c_qm_predicts_violation_chsh, c_chsh_experimental_prediction],
    c_chsh_detector_efficiency_requirement,
    reason="Since QM predicts CHSH violation but the experimental prediction depends on "
    "counting rates, there are minimum requirements on detector efficiency and polarizer "
    "quality for a decisive test.",
)

# Strategy 9: Efficiency-angle tradeoff
_strat_efficiency_angle_tradeoff = deduction(
    [c_chsh_detector_efficiency_requirement],
    c_chsh_efficiency_angle_tradeoff,
    reason="The detector efficiency requirement creates a trade-off between polarizer "
    "efficiency and collection half-angle. For given efficiency, there's an upper limit "
    "on θ, and vice versa.",
)

# Strategy 10: Two orientations sufficient
_strat_two_orientations_sufficient = deduction(
    [c_chsh_optimal_angles, c_chsh_experimental_prediction],
    c_chsh_two_relative_orientations,
    reason="The optimal CHSH angles correspond to only two distinct relative orientations: "
    "22.5° and 67.5°. Therefore, an experiment need only measure at these two orientations "
    "to test the inequality.",
)

# Strategy 11: Previous experiments inadequate
_strat_previous_experiments_inadequate = deduction(
    [c_wu_shaknov_inadequate, c_kocher_commins_inadequate],
    c_chsh_proposed_experiment,
    reason="Previous experiments (Wu-Shaknov, Kocher-Commins) were inadequate for testing "
    "local hidden variables. The proposed CHSH experiment extends the Kocher-Commins "
    "setup to include the necessary measurements at 22.5° and 67.5°.",
)

# Strategy 12: Tsirelson bound as QM maximum
_strat_tsirelson_bound = deduction(
    [c_qm_predicts_violation_chsh, c_chsh_optimal_angles],
    c_chsh_tsirelson_bound,
    reason="QM predicts CHSH violation with S = 2√2 at optimal angles. This value "
    "represents the maximum possible violation in QM, known as Tsirelson's bound. "
    "No quantum state can exceed this value.",
)

# Strategy 13: Experimental test of locality
_strat_experimental_locality_test = deduction(
    [c_chsh_standard_form, c_qm_predicts_violation_chsh],
    c_chsh_experimental_consequence,
    reason="The CHSH inequality and its QM violation transform the locality debate "
    "into an experimental test. If experiments show S > 2, local hidden variables are "
    "ruled out; if S ≤ 2, they remain viable.",
)

# Strategy 14: Generality beyond photons
_strat_generality_beyond_photons = deduction(
    [c_chsh_particle_pair_setup, c_chsh_standard_form],
    c_chsh_general_beyond_photons,
    reason="The CHSH setup and inequality require only two settings and two outcomes "
    "per side, not photon-specific properties. Therefore the inequality applies to "
    "various two-level quantum systems.",
    background=[s_chsh_particle_setup],
)

# Strategy 15: Detection loophole identification
_strat_detection_loophole = abduction(
    observation=c_chsh_detection_loophole,
    hypothesis=alt_chsh_detector_conspiracy,
    alternative=c_chsh_experimental_consequence,
    reason="The CHSH derivation requires that joint detection probability is independent "
    "of settings. If this fails—e.g., if hidden variables affect which photons emerge "
    "in a setting-dependent way—then a local hidden variable theory could potentially "
    "reproduce QM violations. This is the detection loophole.",
    background=[c_chsh_detection_assumption],
)

# Strategy 16: Superdeterminism alternative
_strat_superdeterminism_chsh = abduction(
    observation=c_chsh_experimental_consequence,
    hypothesis=alt_chsh_superdeterminism_settings,
    alternative=c_local_hv_incompatible_with_qm,
    reason="The CHSH conclusion assumes measurement settings can be chosen independently "
    "of hidden variables λ. If settings and λ are correlated (superdeterminism), "
    "the derivation doesn't apply. This offers a potential loophole around the "
    "experimental consequences.",
)

# Strategy 17: Main CHSH theorem
_strat_chsh_main_theorem = deduction(
    [c_chsh_standard_form, c_qm_predicts_violation_chsh, c_chsh_tsirelson_bound],
    c_chsh_experimental_consequence,
    reason="Local hidden variables must satisfy |S| ≤ 2. QM predicts S = 2√2 at "
    "optimal settings. This contradiction transforms the philosophical debate "
    "into a decisive experimental test.",
)
