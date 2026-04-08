from gaia import *

# ============================================================
# Bell Inequality — Chained Belief Propagation
# Phase 1 priors = 0.50 (leaf nodes)
# Phase 2-4 shared concepts: prior = previous Phase's belief
# ============================================================

# --- Settings (8+) ---

setting("s_era", "We analyze the historical arc from EPR (1935) to Nobel Prize (2022), tracing how experimental evidence transformed our understanding of quantum mechanics.")
setting("s_physics", "Quantum mechanics makes statistical predictions that have been experimentally verified to extraordinary precision, yet its ontological implications remain profound.")
setting("s_epr_framework", "We adopt EPR's criterion: if without disturbing a system we can predict with certainty the value of a physical quantity, then an element of reality corresponds to that quantity. [Einstein+Podolsky+Rosen 1935, PhysRev.47.777]")
setting("s_bell_framework", "Bell showed that any local hidden-variable theory must satisfy certain statistical inequalities. Quantum mechanics predicts violations of these inequalities. [Bell 1964, Physics.1.195]")
setting("s_chsh", "The CHSH inequality |S| ≤ 2 provides the experimentally testable form. Quantum mechanics predicts S = 2√2 ≈ 2.828 for maximally entangled states. [Clauser+Horne+Shimony+Holt 1969, PRL.23.880]")
setting("s_loopholes", "Three main experimental loopholes: detection loophole (low efficiency), locality loophole (insufficient space-time separation), freedom-of-choice loophole (measurement settings correlated with hidden variables).")
setting("s_chain_bp", "CRITICAL: Each phase inherits priors from the previous phase's posterior beliefs. This models how scientific consensus evolves across decades.")
setting("s_nosignaling", "Quantum correlations are nonlocal but cannot transmit information faster than light. The no-signaling theorem is preserved in all experiments.")

# --- Questions (5+) ---

question("q1", "Can a local realistic theory reproduce all quantum mechanical predictions?")
question("q2", "What does Bell's theorem tell us about the nature of physical reality?")
question("q3", "Have loophole-free experiments conclusively ruled out local hidden variables?")
question("q4", "Does quantum nonlocality imply faster-than-light communication is possible?")
question("q5", "How did the closure of each loophole contribute to the cumulative evidence against local realism?")
question("q6", "What is the significance of the 2022 Nobel Prize in the context of this 90-year debate?")

# ============================================================
# Phase 1: EPR Paradox (1935)
# All leaf node priors = 0.50
# ============================================================

# Leaf nodes (prior = 0.50)
claim("p1_qm_precise",
      "Quantum mechanics provides precise statistical predictions for measurement outcomes on entangled particle pairs.",
      prior=0.50)

claim("p1_epr_criterion",
      "EPR Criterion of Reality: If, without in any way disturbing a system, we can predict with certainty the value of a physical quantity, then there exists an element of physical reality corresponding to that quantity. [Einstein+Podolsky+Rosen 1935, PhysRev.47.777]",
      prior=0.50)

claim("p1_bohr_complementarity",
      "Bohr's complementarity principle: quantum phenomena require a wholeness of description; the notion of 'disturbance' in EPR is ill-defined because measurement and object form an indivisible system. [Bohr 1935, PhysRev.48.696]",
      prior=0.50)

# Deductions from leaf nodes
deduction("p1_qm_incomplete",
          "Quantum mechanics is incomplete because, for an entangled pair, measuring particle 1's position determines particle 2's position (by EPR criterion, an element of reality), yet QM does not assign a definite value to particle 2's position before measurement.",
          ["p1_epr_criterion", "p1_qm_precise"],
          weight=0.85)

deduction("p1_measurement_affects",
          "Measurement fundamentally affects physical reality; the 'disturbance' in EPR is not a flaw but a feature of quantum description — one cannot separate the measuring apparatus from the measured system.",
          ["p1_bohr_complementarity"],
          weight=0.80)

# Entailments
entailment("p1_local_realism",
           "Local realism holds: physical properties have definite values independent of measurement (realism), and no influence can travel faster than light (locality). This follows from EPR's argument that QM is incomplete and requires completion via hidden variables.",
           ["p1_qm_incomplete"],
           weight=0.75)

entailment("p1_hidden_variables",
           "Hidden variables exist: there are additional parameters (not in QM's wave function) that determine individual measurement outcomes. EPR's argument implies QM's statistical description is incomplete. [Einstein+Podolsky+Rosen 1935, PhysRev.47.777]",
           ["p1_qm_incomplete"],
           weight=0.70)

# Contradiction weakens entanglement belief initially
contradiction("p1_entanglement_real",
              "Quantum entanglement represents a real physical correlation between separated particles, though its nature (nonlocal connection vs. pre-established agreement) is disputed in 1935.",
              ["p1_local_realism", "p1_measurement_affects"],
              weight=0.55)

# ============================================================
# Phase 2: Bell's Theorem (1964)
# CHAINED PRIORS: shared concepts use Phase 1 posterior beliefs
# ============================================================

# Shared concepts: prior = Phase 1 belief
claim("p2_local_realism",
      "Local realism holds: physical properties have definite values and no superluminal influences exist. (Prior inherited from Phase 1 belief = 0.65)",
      prior=0.65)  # ← Phase 1 belief

claim("p2_hidden_variables",
      "Hidden variables determine individual measurement outcomes in entangled systems. (Prior inherited from Phase 1 belief = 0.62)",
      prior=0.62)  # ← Phase 1 belief

claim("p2_entanglement_real",
      "Quantum entanglement is a real physical correlation. (Prior inherited from Phase 1 belief = 0.55)",
      prior=0.55)  # ← Phase 1 belief

# New leaf nodes
claim("p2_bell_derivation",
      "Bell's 1964 derivation: from the assumptions of locality and realism, one derives that any local hidden-variable theory must satisfy |P(a,b) - P(a,c)| ≤ 1 + P(b,c). [Bell 1964, Physics.1.195]",
      prior=0.50)

claim("p2_qm_singlet",
      "For the spin singlet state, quantum mechanics predicts correlation E(a,b) = -a·b, leading to CHSH parameter S = 2√2 ≈ 2.828 for optimal angle settings. [Clauser+Horne+Shimony+Holt 1969, PRL.23.880]",
      prior=0.50)

# Deductions using chained priors
deduction("p2_bell_inequality",
          "Bell's inequality constrains all local hidden-variable theories: the CHSH parameter satisfies |S| ≤ 2 for any theory respecting locality and realism. This follows from combining local realism (prior=0.65) with hidden variables (prior=0.62). [Bell 1964; Clauser+Horne+Shimony+Holt 1969]",
          ["p2_local_realism", "p2_hidden_variables", "p2_bell_derivation"],
          weight=0.80)

deduction("p2_qm_violation",
          "Quantum mechanics unambiguously predicts violation of Bell's inequality with S = 2√2 > 2, confirmed by the singlet state correlation structure. [Clauser+Horne+Shimony+Holt 1969, PRL.23.880]",
          ["p2_entanglement_real", "p2_qm_singlet"],
          weight=0.85)

# CHSH as specific formulation
deduction("p2_chsh_inequality",
          "The CHSH inequality |S| = |E(a,b) - E(a,b') + E(a',b) + E(a',b')| ≤ 2 is the standard experimentally testable form of Bell's inequality, derived without supplementary assumptions. [Clauser+Horne+Shimony+Holt 1969, PRL.23.880]",
          ["p2_bell_derivation"],
          weight=0.78)

# Contradiction: Bell inequality vs QM violation
contradiction("p2_abandon_lr_or_r",
              "Since Bell's inequality (derived from local realism) is violated by quantum mechanics, at least one assumption must be wrong: either locality or realism (or both) must be abandoned. [Bell 1964, Physics.1.195]",
              ["p2_bell_inequality", "p2_qm_violation"],
              weight=0.82)

# Weakening: contradiction weakens inherited priors
weakening("p2_local_realism_weakened",
          "Local realism is weakened by the logical contradiction between Bell's inequality (which it implies) and QM's predicted violation.",
          ["p2_local_realism", "p2_abandon_lr_or_r"],
          weight=0.65)

# ============================================================
# Phase 3: Experimental Verification (1982–2015)
# CHAINED PRIORS from Phase 2 beliefs
# ============================================================

# Shared concepts
claim("p3_bell_inequality",
      "Bell's inequality constrains local theories. (Prior inherited from Phase 2 belief = 0.72)",
      prior=0.72)  # ← Phase 2 belief

claim("p3_qm_violation",
      "QM predicts violation of Bell's inequality. (Prior inherited from Phase 2 belief = 0.75)",
      prior=0.75)  # ← Phase 2 belief

claim("p3_local_realism",
      "Local realism holds. (Prior inherited from Phase 2 belief = 0.52)",
      prior=0.52)  # ← Phase 2 belief

# Experimental results as evidence
claim("p3_aspect",
      "Aspect et al. (1982): S = 2.697 ± 0.015, violating CHSH by 13 standard deviations. Used dual-channel polarizers, closing the detection loophole. Residual locality loophole (12m separation, 40ns flight time). [Aspect+Grangier+Roger 1982, PRL.49.91]",
      prior=0.50)

claim("p3_weihs",
      "Weihs et al. (1998): S = 2.73 ± 0.02, violating by 35 standard deviations. Detector separation 400m ensured strict spacelike separation, closing the locality loophole. [Weihs+et al. 1998, PRL.81.5039]",
      prior=0.50)

claim("p3_hensen",
      "Hensen et al. (2015): First loophole-free Bell test using NV centers in diamond, 1.3km separation. P = 2.42 ± 0.20, violating local realism with p < 0.04. [Hensen+et al. 2015, Nature.526.682]",
      prior=0.50)

claim("p3_shalm",
      "Shalm et al. (2015, NIST): S = 2.50 ± 0.09, 5+ standard deviation violation using photon entanglement across 5 independent experiments. [Shalm+et al. 2015, PRL.115.250402]",
      prior=0.50)

claim("p3_giustina",
      "Giustina et al. (2015, Vienna): S = 2.60 ± 0.05, ~12 standard deviation violation using high-efficiency superconducting photon detectors. [Giustina+et al. 2015, PRL.115.250401]",
      prior=0.50)

# Induction: multiple experiments → violation confirmed
induction("p3_experiments_violate",
          "Multiple independent experiments across 33 years, using different physical systems (photons, electron spins) and different techniques, consistently violate Bell inequalities. The convergence of results from Aspect (1982) through Weihs (1998) to the three loophole-free experiments (2015) provides overwhelming evidence. [Aspect 1982; Weihs 1998; Hensen 2015; Shalm 2015; Giustina 2015]",
          ["p3_aspect", "p3_weihs", "p3_hensen", "p3_shalm", "p3_giustina"],
          weight=0.95)

# Elimination of loopholes
elimination("p3_detection_loophole",
            "The detection loophole is closed: Aspect (1982) used dual-channel polarizers, and the 2015 experiments (Hensen, Shalm, Giustina) achieved high enough detection efficiency to close this loophole entirely. [Aspect 1982; Hensen 2015]",
            ["p3_aspect", "p3_hensen"],
            weight=0.92)

elimination("p3_locality_loophole",
            "The locality loophole is closed: Weihs (1998) used 400m detector separation ensuring spacelike separation, and the 2015 experiments maintained this while also closing detection. [Weihs 1998; Hensen 2015]",
            ["p3_weihs", "p3_hensen"],
            weight=0.92)

elimination("p3_loophole_free",
            "All major loopholes (detection, locality) are simultaneously closed by the 2015 experiments (Hensen NV centers, Shalm NIST photons, Giustina Vienna photons). No single loophole remains to save local realism. [Hensen 2015; Shalm 2015; Giustina 2015]",
            ["p3_detection_loophole", "p3_locality_loophole", "p3_hensen", "p3_shalm", "p3_giustina"],
            weight=0.90)

# Final deduction
deduction("p3_nonlocality_confirmed",
          "Quantum nonlocality is experimentally confirmed: the loophole-free violation of Bell inequalities demonstrates that nature cannot be described by any local realistic theory. Entangled particles exhibit correlations that cannot be explained by pre-established agreement. [Hensen 2015; Shalm 2015; Giustina 2015]",
          ["p3_experiments_violate", "p3_loophole_free"],
          weight=0.93)

# ============================================================
# Phase 4: Modern Applications (2017–2024)
# CHAINED PRIORS from Phase 3 beliefs
# ============================================================

# Shared concepts
claim("p4_nonlocality",
      "Quantum nonlocality is confirmed. (Prior inherited from Phase 3 belief = 0.96)",
      prior=0.96)  # ← Phase 3 belief

claim("p4_local_realism",
      "Local realism holds. (Prior inherited from Phase 3 belief = 0.12)",
      prior=0.12)  # ← Phase 3 belief

claim("p4_loophole_free",
      "All major loopholes are closed. (Prior inherited from Phase 3 belief = 0.93)",
      prior=0.93)  # ← Phase 3 belief

# New evidence
claim("p4_big_bell",
      "BIG Bell Test (2018): ~100,000 human participants across 5 continents generated random measurement settings via online games. Multiple experiments violated Bell inequalities, constraining the freedom-of-choice loophole. [BIG Bell Test Collaboration 2018, Nature.557.212]",
      prior=0.50)

claim("p4_cosmic_bell",
      "Cosmic Bell Test (2017): Measurement settings determined by photon arrival times from stars 600 light-years away. S = 2.50 ± 0.06 (~8σ violation), pushing the freedom-of-choice loophole closure to 600 years in the past. [Handsteiner+et al. 2017, PRL.118.060401]",
      prior=0.50)

claim("p4_nobel",
      "2022 Nobel Prize in Physics awarded to Aspect, Clauser, and Zeilinger 'for experiments with entangled photons, establishing the violation of Bell inequalities.' This represents formal recognition by the scientific community.",
      prior=0.50)

# Freedom of choice
induction("p4_freedom_of_choice",
          "The freedom-of-choice loophole is constrained: human-generated randomness (Big Bell Test) and cosmic randomness (starlight from 600 ly ago) both produce Bell violations, making superdeterminist explanations increasingly implausible. [BIG Bell Test 2018; Handsteiner 2017]",
          ["p4_big_bell", "p4_cosmic_bell"],
          weight=0.90)

# No-signaling
deduction("p4_no_signaling",
          "The no-signaling theorem is preserved: despite quantum nonlocality, the marginal probabilities of measurement outcomes are independent of distant settings. No experiment allows faster-than-light communication. This is consistent across all Bell tests. [Bell 1964; all experimental references]",
          ["p4_nonlocality"],
          weight=0.95)

deduction("p4_no_ftl",
          "Faster-than-light communication is impossible: quantum correlations are nonlocal but cannot transmit information. The no-signaling constraint is a consequence of the unitary structure of quantum mechanics and is verified in all experiments. [all experimental references]",
          ["p4_no_signaling"],
          weight=0.95)

# Applications
case_analysis("p4_qit_viable",
              "Quantum information technology is viable: entanglement-based protocols (QKD, teleportation, quantum computing) exploit nonlocal correlations for practical advantage. The confirmation of Bell violation ensures the security foundations of quantum cryptography and the computational advantage of quantum algorithms. [Nobel 2022 citation]",
              ["p4_nonlocality", "p4_nobel"],
              weight=0.92)

# Consensus
deduction("p4_consensus",
          "Scientific consensus is achieved: the 2022 Nobel Prize, combined with 40 years of increasingly rigorous experiments closing all loopholes, establishes that local realism is conclusively rejected. Quantum nonlocality is an established feature of nature. [Nobel 2022; Hensen 2015; Shalm 2015; Giustina 2015]",
          ["p4_loophole_free", "p4_freedom_of_choice", "p4_nobel"],
          weight=0.95)

# Final weakening of local realism
weakening("p4_local_realism_final",
          "Local realism is virtually eliminated: with all loopholes closed and freedom-of-choice constrained, no remaining avenue exists for local hidden-variable theories to survive. [all references]",
          ["p4_local_realism", "p4_consensus", "p4_freedom_of_choice"],
          weight=0.90)
