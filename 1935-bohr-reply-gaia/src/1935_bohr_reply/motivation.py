"""Introduction — Bohr's response to EPR: the criterion of reality contains an essential ambiguity."""

from gaia.lang import claim, setting, question

# ── Background: Bohr's aim ──

s_bohr_aim = setting(
    "Bohr responds to EPR's argument that QM is incomplete by showing that their "
    "'criterion of physical reality' contains an essential ambiguity when applied to "
    "quantum phenomena. He aims to show that QM, within its scope, fulfills all "
    "rational demands of completeness through the viewpoint of 'complementarity.'",
    title="Bohr's response: criterion of reality is ambiguous",
)

# ── Bohr's summary of EPR's argument ──

c_bohr_summarizes_epr = claim(
    "EPR show that in QM, just as in classical mechanics, it is possible under "
    "suitable conditions to predict the value of any given variable pertaining to "
    "the description of a mechanical system from measurements performed entirely on "
    "other systems which previously have been in interaction with it. According to "
    "their criterion, they therefore ascribe an element of reality to each of the "
    "quantities represented by such variables.",
    title="Bohr's summary of EPR's prediction argument",
)

# ── Bohr's assessment of EPR's conclusion ──

c_bohr_rejects_epr_conclusion = claim(
    "Such argumentation would hardly seem suited to affect the soundness of "
    "quantum-mechanical description, which is based on a coherent mathematical "
    "formalism covering automatically any procedure of measurement like that "
    "indicated by EPR.",
    title="Bohr: EPR argumentation does not undermine QM soundness",
)

# ── The key insight: ambiguity in "without disturbing" ──

c_criterion_ambiguity = claim(
    "The EPR criterion of physical reality contains an ambiguity as regards the "
    "meaning of the expression 'without in any way disturbing a system.' There is "
    "no question of a mechanical disturbance of the system under investigation "
    "during the last critical stage of the measuring procedure, but there is "
    "essentially the question of an influence on the very conditions which define "
    "the possible types of predictions regarding the future behavior of the system.",
    title="Key: 'without disturbing' has an essential ambiguity",
)

# ── Bohr's counter-conclusion ──

c_bohr_conclusion = claim(
    "Since the conditions which define possible types of predictions constitute "
    "an inherent element of the description of any phenomenon to which the term "
    "'physical reality' can be properly attached, the argumentation of EPR does "
    "not justify their conclusion that quantum-mechanical description is essentially "
    "incomplete.",
    title="Bohr's conclusion: EPR argument does not justify incompleteness",
)
