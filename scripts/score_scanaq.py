#!/usr/bin/env python3
"""Reference implementation of SCANAQ scoring model 2.0.0.

Mirrors `Forms/SCANAQ Numerical Scoring Breakdown.md`. Run with no arguments to
verify the worked example in section 11 of that document:

    python3 scripts/score_scanaq.py

Standard library only. Instrument version 1.0.0 (36 items, 8 sections).
"""

from __future__ import annotations

import sys

INSTRUMENT_VERSION = "2.0.0"  # current instrument; scoring applies to 1.0.0 and 2.0.0 alike
SCORING_MODEL_VERSION = "2.0.0"

# Section -> (items, scale_min, scale_max). Frozen at instrument 1.0.0.
SCALES = {
    "A": (range(1, 9), 1, 3),
    "B": (range(9, 13), 1, 7),
    "C": (range(13, 19), 1, 4),
    "D": (range(19, 22), 1, 5),
    "E": (range(22, 27), 1, 5),
    "F": (range(27, 30), 1, 4),
    "G": (range(30, 33), 1, 5),
    "H": (range(33, 37), 1, 5),
}

# Items worded opposite to their section's direction (spec section 1.4).
REVERSED = {32: 6, 35: 6}  # item -> (scale_max + scale_min)

# Single-total band tables (sections scored as one summed total). Defined once
# here and used by both score() and the self-test, so the test checks the
# *declared* bands against the attainable score range rather than comparing an
# expression to itself. Sections B (subscales), E (argmax, no total), and H's
# subscales are not single-total and are handled inline in score().
TOTAL_BANDS = {
    "A": [(8, 13, "EF-LOW"), (14, 18, "EF-MOD"), (19, 24, "EF-HIGH")],
    "C": [(6, 11, "IMP-SEV-LOW"), (12, 17, "IMP-SEV-MOD"), (18, 24, "IMP-SEV-HIGH")],
    "D": [(3, 9, "RP-LOW"), (10, 15, "RP-HIGH")],
    "F": [(3, 8, "SE-LOW"), (9, 12, "SE-HIGH")],
    "G": [(3, 9, "PS-LOW"), (10, 15, "PS-HIGH")],
}

EF_POINTERS = {
    1: "Reports frequent difficulty getting started on tasks",
    2: "Reports frequently forgetting instructions",
    3: "Reports frequent difficulty controlling emotions",
    4: "Reports frequent careless mistakes",
    5: "Reports frequently getting stuck on one approach",
    6: "Reports frequent difficulty planning ahead",
    7: "Reports frequent difficulty organizing tasks",
    8: "Reports frequent difficulty tracking belongings",
}

DM_STYLES = {22: "DM-RAT", 23: "DM-INT", 24: "DM-DEP", 25: "DM-AVO", 26: "DM-SPO"}

NOT_SCORED = "not_scored"


def keyed(responses: dict[int, int], item: int) -> int | None:
    """Return the item's response, reverse-keyed if required (spec 1.4)."""
    raw = responses.get(item)
    if raw is None:
        return None
    return REVERSED[item] - raw if item in REVERSED else raw


def subscale(responses: dict[int, int], items) -> int | None:
    """Sum a subscale, or None if any constituent item is unanswered (spec 1.5).

    No proration and no imputation — a partially answered subscale is not scored.
    """
    vals = [keyed(responses, i) for i in items]
    return None if any(v is None for v in vals) else sum(vals)


def band(total: int | None, bands: list[tuple[int, int, str]]) -> str:
    if total is None:
        return NOT_SCORED
    for lo, hi, code in bands:
        if lo <= total <= hi:
            return code
    raise AssertionError(f"total {total} outside all bands {bands}")


def score(responses: dict[int, int]) -> dict:
    out: dict = {"codes": [], "pointers": [], "subscales": {}}

    def emit(code: str) -> None:
        out["codes"].append(code)

    # --- A: Executive Functioning. Higher = more difficulty. Tertiles of 1-3.
    ef = subscale(responses, SCALES["A"][0])
    out["subscales"]["EF_total"] = ef
    emit(band(ef, TOTAL_BANDS["A"]))
    for item, text in EF_POINTERS.items():
        if responses.get(item) == 3:
            out["pointers"].append(text)

    # --- B: Emotion Regulation. Two subscales, neutral anchor 4 -> mean<=4 low.
    reap = subscale(responses, [9, 10])
    supp = subscale(responses, [11, 12])
    out["subscales"].update(ER_reappraisal=reap, ER_suppression=supp)
    if reap is None or supp is None:
        emit(NOT_SCORED)
    else:
        emit(f"ER-R{'H' if reap >= 9 else 'L'}-S{'H' if supp >= 9 else 'L'}")

    # --- C: Impulsivity. Severity via tertiles of 1-4; subtype via per-item means.
    imp = subscale(responses, SCALES["C"][0])
    out["subscales"]["IMP_total"] = imp
    emit(band(imp, TOTAL_BANDS["C"]))

    means = {}
    for name, items in (("IMP-ATT", [13]), ("IMP-MOT", [14, 15, 16]), ("IMP-NP", [17, 18])):
        s = subscale(responses, items)
        means[name] = None if s is None else s / len(items)
    out["subscales"]["IMP_means"] = means
    if any(v is None for v in means.values()):
        emit(NOT_SCORED)
    else:
        ranked = sorted(means.items(), key=lambda kv: kv[1], reverse=True)
        # Dominance requires a >=0.50 margin, else the single-item Attentional
        # subscale can win on noise alone.
        emit(ranked[0][0] if ranked[0][1] - ranked[1][1] >= 0.50 else "IMP-MIXED")

    # --- D: Risk Propensity. Neutral anchor 3 -> mean<=3 low.
    rp = subscale(responses, SCALES["D"][0])
    out["subscales"]["RP_total"] = rp
    emit(band(rp, TOTAL_BANDS["D"]))

    # --- E: Decision-Making. No total; argmax with co-dominant ties.
    dm = {i: responses.get(i) for i in DM_STYLES}
    if any(v is None for v in dm.values()):
        emit(NOT_SCORED)
    else:
        top = max(dm.values())
        winners = [DM_STYLES[i] for i in sorted(dm) if dm[i] == top]
        emit("DM-UNDIFF" if len(winners) == 5 else "+".join(winners))

    # --- F: Self-Efficacy. Anchor 3 ("Moderately True") -> mean<3 low.
    se = subscale(responses, SCALES["F"][0])
    out["subscales"]["SE_total"] = se
    emit(band(se, TOTAL_BANDS["F"]))

    # --- G: Perceived Stress. Q32 reverse-keyed by keyed().
    ps = subscale(responses, SCALES["G"][0])
    out["subscales"]["PS_total"] = ps
    emit(band(ps, TOTAL_BANDS["G"]))

    # --- H: Empathy. Three separate outputs; Q35 reverse-keyed. Fantasy never summed.
    ec = subscale(responses, [33, 34])
    pt = subscale(responses, [35])
    fs = subscale(responses, [36])
    out["subscales"].update(ESC_EC=ec, ESC_PT=pt, ESC_FS=fs)
    emit(band(ec, [(2, 6, "ESC-EC-LOW"), (7, 10, "ESC-EC-HIGH")]))
    emit(band(pt, [(1, 3, "ESC-PT-LOW"), (4, 5, "ESC-PT-HIGH")]))
    emit(band(fs, [(1, 3, "ESC-FS-LOW"), (4, 5, "ESC-FS-HIGH")]))
    if ec is not None and pt is not None:
        emit(band(ec + pt, [(3, 9, "ESC-EMPATHY-LOW"), (10, 15, "ESC-EMPATHY-HIGH")]))
    else:
        emit(NOT_SCORED)  # placeholder so codes keep fixed length/positions (spec 1.5)

    out["instrument_version"] = INSTRUMENT_VERSION
    out["scoring_model_version"] = SCORING_MODEL_VERSION
    return out


# --------------------------------------------------------------------------
# Self-tests
# --------------------------------------------------------------------------

WORKED_EXAMPLE = dict(
    zip(
        range(1, 37),
        [3, 2, 1, 2, 3, 3, 2, 1]      # Q1-8    A
        + [6, 5, 2, 3]                 # Q9-12   B
        + [2, 4, 4, 3, 2, 1]           # Q13-18  C
        + [4, 3, 2]                    # Q19-21  D
        + [5, 3, 2, 5, 1]              # Q22-26  E
        + [3, 2, 4]                    # Q27-29  F
        + [4, 4, 2]                    # Q30-32  G
        + [4, 5, 4, 2],                # Q33-36  H
    )
)

WORKED_EXAMPLE_CODES = [
    "EF-MOD", "ER-RH-SL", "IMP-SEV-MOD", "IMP-MOT", "RP-LOW",
    "DM-RAT+DM-AVO", "SE-HIGH", "PS-HIGH",
    "ESC-EC-HIGH", "ESC-PT-LOW", "ESC-FS-LOW", "ESC-EMPATHY-HIGH",
]


def _check(label: str, got, want) -> bool:
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"         expected {want!r}\n         got      {got!r}")
    return ok


def main() -> int:
    ok = True
    print("Worked example (spec section 11)")
    r = score(WORKED_EXAMPLE)
    ok &= _check("profile codes", r["codes"], WORKED_EXAMPLE_CODES)
    ok &= _check("EF total 17", r["subscales"]["EF_total"], 17)
    ok &= _check("ER reappraisal 11 / suppression 5",
                 (r["subscales"]["ER_reappraisal"], r["subscales"]["ER_suppression"]), (11, 5))
    ok &= _check("IMP means ATT 2.00 / MOT 3.67 / NP 1.50",
                 tuple(round(v, 2) for v in r["subscales"]["IMP_means"].values()),
                 (2.00, 3.67, 1.50))
    ok &= _check("PS total 12 (Q32 reverse-keyed 2 -> 4)", r["subscales"]["PS_total"], 12)
    ok &= _check("ESC EC 9 / PT 2 (Q35 reverse-keyed 4 -> 2)",
                 (r["subscales"]["ESC_EC"], r["subscales"]["ESC_PT"]), (9, 2))
    ok &= _check("3 EF pointers (Q1, Q5, Q6)", len(r["pointers"]), 3)

    print("\nBand tables tile each section's full attainable score range")
    for sec, bands in TOTAL_BANDS.items():
        items, lo, hi = SCALES[sec]
        n = len(list(items))
        span = (min(b[0] for b in bands), max(b[1] for b in bands))
        ok &= _check(f"section {sec}: bands span {n*lo}-{n*hi} (n items x scale)",
                     span, (n * lo, n * hi))
        contiguous = all(bands[i + 1][0] == bands[i][1] + 1 for i in range(len(bands) - 1))
        ok &= _check(f"section {sec}: bands contiguous, no gaps or overlaps", contiguous, True)

    print("\nPolarity regression (the model 1.0.0 bugs)")
    best = {**{i: 1 for i in range(1, 9)}, **{i: 1 for i in range(13, 19)}}
    ok &= _check("all-Never on deficit-worded EF items -> EF-LOW",
                 score({**WORKED_EXAMPLE, **best})["codes"][0], "EF-LOW")
    worst = {i: 3 for i in range(1, 9)}
    ok &= _check("all-Often on deficit-worded EF items -> EF-HIGH",
                 score({**WORKED_EXAMPLE, **worst})["codes"][0], "EF-HIGH")
    ok &= _check("least-impulsive responses -> IMP-SEV-LOW",
                 score({**WORKED_EXAMPLE, **{i: 1 for i in range(13, 19)}})["codes"][2],
                 "IMP-SEV-LOW")

    print("\nER 2x2 separates the profiles that collided at 16 under model 1.0.0")
    hi_reap = {**WORKED_EXAMPLE, 9: 7, 10: 7, 11: 1, 12: 1}   # v1 total 16
    hi_supp = {**WORKED_EXAMPLE, 9: 1, 10: 1, 11: 7, 12: 7}   # v1 total 16
    ok &= _check("max reappraisal / min suppression -> ER-RH-SL",
                 score(hi_reap)["codes"][1], "ER-RH-SL")
    ok &= _check("min reappraisal / max suppression -> ER-RL-SH",
                 score(hi_supp)["codes"][1], "ER-RL-SH")

    print("\nDecision-Making tie handling")
    ok &= _check("all five equal -> DM-UNDIFF",
                 score({**WORKED_EXAMPLE, **{i: 4 for i in range(22, 27)}})["codes"][5],
                 "DM-UNDIFF")
    ok &= _check("unique winner -> single style",
                 score({**WORKED_EXAMPLE, 22: 5, 23: 1, 24: 1, 25: 1, 26: 1})["codes"][5],
                 "DM-RAT")

    print("\nMissing data is not imputed")
    partial = {k: v for k, v in WORKED_EXAMPLE.items() if k != 10}
    ok &= _check("one ER item unanswered -> not_scored for that section",
                 score(partial)["codes"][1], NOT_SCORED)
    ok &= _check("other sections still scored", score(partial)["codes"][0], "EF-MOD")

    print("\n" + ("ALL CHECKS PASSED" if ok else "FAILURES PRESENT"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
