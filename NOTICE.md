# Notice — Scope of the MIT License

`SCAN-Resources` is released under the MIT License (see `LICENSE`). This notice clarifies what that
grant does and does not cover.

## Covered by the MIT License

The original content of this repository:

- The SCAN project documentation (`README.md`, this notice, `PROVENANCE.md`, `CHANGELOG.md`)
- The **SCANAQ scoring model** — subscale structure, banding rules, profile-code taxonomy, and
  scoring logic (`Forms/SCANAQ Numerical Scoring Breakdown.md`, `scripts/score_scanaq.py`)
- The **Cognitive Augmentation User Survey Evaluation (CAUSE)** instrument
- The **PFC agent training datasets** (`TrainingDatasets/*.jsonl`) and the generation prompt
  (`Forms/PFC Agent Training Data Generation Prompt.md`)
- All scripts under `scripts/`

## NOT covered by the MIT License

**Third-party questionnaire item text reproduced or adapted in the SCANAQ.**

The 36 SCANAQ items appear to derive from established psychometric instruments — including the
BRIEF-family, ERQ, BIS-11, GDMS, GSE, PSS, and IRI — which remain the property of their respective
copyright holders. See `PROVENANCE.md` for the section-by-section breakdown.

**These attributions are unverified.** They were identified during a repository audit by wording
correspondence and response-scale matching, and have not been confirmed against the source
publications.

No license to that third-party item text is granted here, and none can be. **Anyone reproducing,
redistributing, or administering the SCANAQ must obtain their own permissions from the relevant
rights holders.** At least one apparent source (BRIEF, published by PAR Inc.) is a commercial
instrument requiring a paid license.

## Effect

The MIT grant applies to the structure, scoring, code, datasets, and documentation authored for this
project. It does not, and cannot, extend to material this project does not own. If you intend to use
the SCANAQ itself rather than the scoring model or datasets, resolve the item provenance questions
in `PROVENANCE.md` first.
