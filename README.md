# SCAN-Resources

[![DOI](https://zenodo.org/badge/885073150.svg)](https://doi.org/10.5281/zenodo.14053202)

Resources for the **Synthetic Cognitive Augmentation Network (SCAN)**: the SCANAQ alignment
questionnaire and its scoring model, a user survey, a generation prompt for synthetic training
dialogues, and JSONL datasets for five prefrontal-cortex-simulating agents.

| | |
|---|---|
| **Instrument version** | 1.0.0 |
| **Scoring model version** | 2.0.0 |
| **Release** | 2.0.0 — see [`CHANGELOG.md`](CHANGELOG.md) |

> **Read before using the SCANAQ.** Two things materially affect whether this instrument is
> appropriate for your purpose:
>
> - **Item provenance is unverified.** The 36 items appear to derive from established psychometric
>   instruments whose reuse terms have not been confirmed — one of which is commercially licensed.
>   See [`PROVENANCE.md`](PROVENANCE.md) and [`NOTICE.md`](NOTICE.md).
> - **Scoring model 1.0.0 was incorrect** in four of eight sections. If you scored responses with
>   it, they must be rescored from raw item responses; profile codes cannot be converted. See
>   [`CHANGELOG.md`](CHANGELOG.md).

---

## Forms

### `Synthetic Cognitive Augmentation Network Alignment Questionnaire.md`
The **SCANAQ** — 36 items across eight sections, each with its own response scale, assessing
cognitive functioning and preferences in order to align SCAN with a user's profile.

- Executive Functioning · Emotion Regulation · Impulsivity · Risk Propensity
- Decision-Making Style · Self-Efficacy · Perceived Stress · Empathy and Social Cognition

Item text, item count, and response scales are **frozen at instrument version 1.0.0**. Changing any
of them invalidates previously collected responses and requires an instrument version bump.

### `SCANAQ Numerical Scoring Breakdown.md`
**Scoring model 2.0.0** — authoritative. Defines how responses become a cognitive alignment profile:

- **Subscale scoring** where a profile label names more than one dimension. Emotion Regulation,
  Impulsivity, and Empathy are scored as separate subscales rather than section totals.
- **Band boundaries derived from named scale anchors** under a stated rule, rather than asserted.
- **Reverse-keying** for Q32 and Q35, which are worded opposite to their sections' direction.
- **Missing-data handling** — subscales with unanswered items report `not_scored`; nothing is
  imputed or prorated.
- **Tie rules** for Decision-Making Style, which is undefined for 43.4% of possible response
  patterns without them.
- A **worked example** that doubles as a regression test for the specification.

### `PFC Agent Training Data Generation Prompt.md`
Prompts, role definitions, and format specification for generating synthetic training dialogues for
the five PFC agents. The canonical source for each agent's system prompt.

### `Cognitive Augmentation User Survey Evaluation.md`
The **CAUSE** survey — 50 questions across 11 sections gathering user requirements, perceived value,
interface preferences, pain points, privacy concerns, demographics, and pricing perception.

### Archived appendices (PDF)
`Synthetic Cognitive Augmentation Network Alignment Questionnaire (SCANAQ).pdf` and
`SCANAQ Scoring Breakdown, Descriptions, and PFC-Inspired Suggestions.pdf` are **Appendix A and
Appendix B of the published paper**, frozen as the archived record.

> **Appendix B documents scoring model 1.0.0 and contains known errors.** The markdown is
> authoritative. See [`Forms/ARCHIVE.md`](Forms/ARCHIVE.md).

---

## Training Datasets

JSONL training and validation data for five PFC agents — **528 records**, 425 training and 103
validation, split 80/20 in every region.

| Region | Cognitive role | Train | Val |
|---|---|---:|---:|
| **ACC** — Anterior Cingulate | Conflict monitoring, error detection, performance regulation | 120 | 29 |
| **DLPFC** — Dorsolateral | Executive control, working memory, higher-order planning | 90 | 22 |
| **mPFC** — Medial | Perspective-taking, social inference, value-based recommendation | 71 | 17 |
| **OFC** — Orbitofrontal | Reward evaluation, decision optimization, outcome prediction | 60 | 14 |
| **vmPFC** — Ventromedial | Emotional regulation, risk evaluation, affective reasoning | 84 | 21 |

Each region uses exactly one system prompt, taken verbatim from the generation-prompt specification
and identical across its splits. See [`TrainingDatasets/README.md`](TrainingDatasets/README.md) for
the dataset card, provenance, and known limitations.

---

## Scripts

```sh
python3 scripts/score_scanaq.py               # reference scorer + specification self-test
python3 scripts/validate_datasets.py          # dataset invariants
python3 scripts/validate_datasets.py --strict # also fails on quality warnings
```

Standard library only, no dependencies.

---

## Versions and DOIs

| Release | Instrument | Scoring model | DOI |
|---|---|---|---|
| 2.0.0 | 1.0.0 | 2.0.0 | *(pending — publish a new Zenodo version)* |
| 1.0.0 | 1.0.0 | 1.0.0 | archived under the concept DOI |

The badge above points at the **concept DOI**, which always resolves to the newest version. **Papers
and scored outputs should cite the version DOI**, not the concept DOI, so that the scoring model in
use is unambiguous. With that convention the archive does not contradict this repository — it *is*
scoring model 1.0.0, and the mapping is published here.

Every scored output should record `instrument_version`, `scoring_model_version`, and — mandatorily —
`raw_responses`. Profile codes are derived and disposable; raw responses are the only field that
survives a scoring-model change.

---

## License scope

Released under the [MIT License](LICENSE), which covers the **original content** of this repository:
the SCAN documentation, the SCANAQ scoring model and profile taxonomy, the CAUSE survey, the
training datasets, the generation prompts, and the scripts.

It does **not** cover third-party questionnaire item text reproduced or adapted in the SCANAQ, which
remains the property of its respective copyright holders. Anyone administering or redistributing the
SCANAQ must obtain their own permissions. See [`NOTICE.md`](NOTICE.md) and
[`PROVENANCE.md`](PROVENANCE.md).

## Not a validated instrument

The SCANAQ is an ad-hoc composite assembled from item subsets of other instruments. It has **not**
undergone reliability or validity testing in this form. Per-section reliability is unknown, and
undefined for the sections scored from a single item. Section scores are not the source instruments'
scores, and published norms and cutoffs from those instruments do not apply.

It is a self-assessment and personalization tool for aligning SCAN to a user's stated preferences.
It is not a diagnostic instrument and does not replace professional evaluation.

---

## Citation

See [`CITATION.cff`](CITATION.cff). Cite the version DOI for the release you used.
