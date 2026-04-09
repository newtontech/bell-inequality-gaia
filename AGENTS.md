# AGENTS.md — Bell Inequality Gaia Knowledge Package

## Project Overview

This project formalizes the historical chain from the EPR Paradox (1935) through Bell's Theorem (1964) to modern loophole-free Bell tests (2015-2022) using Gaia Lang DSL.

## Current Task: Formalize EPR (1935) Paper

Formalize Einstein, Podolsky, and Rosen's 1935 paper "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" (Phys. Rev. 47, 777-780).

**Source:** `artifacts/1935_einstein_epr/einstein_podolsky_rosen_1935.pdf`
**Full text:** `artifacts/1935_einstein_epr/epr_1935_full_text.txt`

## Package Structure

```
bell-inequality-gaia/
├── src/
│   └── bell_inequality/
│       ├── __init__.py
│       ├── motivation.py          # §1: EPR setup, criterion of reality, initial dilemma
│       ├── s2_epr_argument.py     # §2: Two-particle argument, conclusion
│       └── reviews/
│           ├── __init__.py
│           └── self_review.py
├── artifacts/
│   └── 1935_einstein_epr/
│       ├── einstein_podolsky_rosen_1935.pdf
│       └── epr_1935_full_text.txt
├── pyproject.toml
└── .venv/  (Python 3.13, gaia-lang)
```

## Paper Structure (EPR 1935)

### §1 — Introduction (→ `motivation.py`)
- Distinction between objective reality and physical concepts
- Two criteria: correctness (experiment) and completeness (every element of reality has counterpart)
- **Criterion of Reality**: If without disturbing a system we can predict with certainty the value of a physical quantity, then there exists an element of physical reality corresponding to it
- Single-particle illustration: momentum eigenstate → definite momentum, indefinite position
- **Initial dilemma**: Either (1) QM description by wave function is not complete, or (2) non-commuting quantities cannot have simultaneous reality

### §2 — Two-Particle Argument (→ `s2_epr_argument.py`)
- Two systems I and II interact then separate (t > T)
- Measuring A on system I → system II in state φ_k (wave packet reduction)
- Measuring B on system I → system II in state ψ_s
- Specific example: two particles, momentum and position
  - Measuring momentum p of particle 1 → particle 2 has momentum −p
  - Measuring position x of particle 1 → particle 2 has position x + x₀
- Since PQ − QP ≠ 0, both P and Q are elements of reality for system II
- **Conclusion**: Negation of (1) implies negation of (2), therefore QM is incomplete
- Anticipated objection: reality depends on measurement? "No reasonable definition of reality could permit this"
- Final note: complete theory may be possible (belief of EPR)

## Gaia CLI Commands

```bash
source .venv/bin/activate   # Activate Python 3.13 env
gaia compile .
gaia check .
gaia infer .
gaia render . --target github
gaia render . --target docs
```
