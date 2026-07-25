# Changelog

All notable changes to this repository are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

This repository carries **two independent version streams**:

- **`instrument_version`** — SCANAQ item text, item count, response scales, section order
- **`scoring_model_version`** — the scoring and profile specification

A change to either can invalidate previously collected data, so they are tracked separately.
Every scored output should record both.

### Version bump rules

| Level | Meaning |
|---|---|
| **MAJOR** | Could change the profile assigned to an *unchanged* response set — thresholds, keying, subscale composition, code identity |
| **MINOR** | Adds outputs without changing existing ones |
| **PATCH** | Wording, typos, formatting; no computational effect |

---

## [2.0.0] — 2026-07-25

Instrument version: **1.0.0** (unchanged) · Scoring model: **1.0.0 → 2.0.0** (MAJOR)

### Effect on previously scored data

**Any response set scored under model 1.0.0 must be rescored from raw item responses.** Profile
codes cannot be mechanically converted, and no conversion function is provided — offering one would
imply a valid conversion exists.

| Section | Convertible? |
|---|---|
| Executive Functioning, Impulsivity | **No** — v1 bands ran opposite to the items' direction |
| Emotion Regulation, Empathy | **No** — v1 derived two-dimensional labels from single sums, and summed reverse-keyed items raw |
| Perceived Stress | **No** — bands unchanged, but Q32 was summed raw, so totals were wrong by up to 4 points |
| Decision-Making | **Partial** — relabels cleanly only where v1 had a unique winner; v1 had no tie rule |
| Risk Propensity, Self-Efficacy | **Yes** — direct relabel, bands unchanged |

If you hold profile codes without the underlying raw responses, they cannot be migrated. Going
forward, `raw_responses` is a mandatory field on every scored record.

### Fixed

- **Executive Functioning polarity was inverted.** All eight items are deficit-worded on a
  1 = Never / 3 = Often scale, so 8 is the *least*-impaired score. Model 1.0.0 labelled 8–13
  "Difficulty initiating and planning tasks" and 14–24 "Strong working memory".
- **Impulsivity polarity was inverted.** 6 — the least impulsive score attainable — was labelled
  "High Motor Impulsivity… Acts impulsively".
- **Emotion Regulation conflated two opposed constructs.** Reappraisal (Q9–10) and suppression
  (Q11–12) were summed into one total, making the section's own labels unreachable: maximum
  reappraisal with minimum suppression (14 + 2 = 16) and its exact opposite (2 + 14 = 16) both
  scored 16 and both received "Low Reappraisal, High Suppression". Now scored as two subscales,
  yielding a genuine 2 × 2 in which two previously unrepresentable profiles are reachable.
- **Q32 and Q35 were summed raw despite being reverse-keyed** in their source instruments. Model
  1.0.0's global note ("scores are summed within each section") confirms this was systematic.
  Both are now transformed as `6 − raw` before summing.
- **Two-dimensional labels derived from one-dimensional sums.** "High Inhibition, Low Planning" and
  "High Attentional, Low Motor" cannot be recovered from a total at any threshold. Now computed from
  subscales, or removed.
- **Empathy section claimed a construct it does not measure.** No item measures personal distress;
  the claim has been removed from the questionnaire.
- **Decision-Making Style had no tie-break rule.** Of the 3,125 possible response patterns for
  Q22–26, only 56.6% have a unique highest item — the remaining 43.4% were undefined. Ties now
  produce co-dominant style sets, and an all-equal response produces `DM-UNDIFF`.
- **No missing-data rule existed** although the questionnaire explicitly permits skipping items.
  Subscales with an unanswered item are now reported as `not_scored`; there is no proration or
  imputation.
- **Band boundaries were asserted rather than derived.** Executive Functioning, Emotion Regulation,
  and Impulsivity thresholds were all asymmetric and unexplained. Boundaries are now placed at named
  scale anchors under a stated rule, so a future threshold either satisfies the rule or is a bug.
- **`4A`/`4B` inverted the A/B convention** used by every other code family.
- **"Executive Function" / "Executive Functioning"** naming inconsistency between the scoring file
  and the questionnaire.

### Changed

- Profile codes replaced with a self-describing namespace (`EF-MOD`, `ER-RH-SL`, `IMP-MOT`,
  `DM-RAT+DM-AVO`, …). Reusing `1A`–`8B` with corrected meanings would have failed *silently* —
  a stored code would give no way to tell which model assigned it.
- The scoring file's three redundant representations collapsed into one canonical per-section view.
  A single threshold change previously required four to six edits, and the representations had
  already diverged.
- Suggestion text from the archived Appendix B — richer than the markdown's — carried forward
  rather than discarded.
- **DLPFC and ACC datasets regenerated.** DLPFC type-token ratio 0.106 → 0.320 (training) and
  0.094 → 0.390 (validation); its most common opening trigram fell from 27% of responses to 2%.
  ACC content exercising its actual role — conflict monitoring, error detection, performance
  regulation — rose from 17% to 82% (training) and 11% to 76% (validation), with
  prioritization-only content falling from 53% to 2%.
  ACC validation shrank from 80 to 50 records; total corpus 790 → 760.
- Three defective records rewritten rather than deleted: two duplicate mPFC validation records, and
  an OFC record that shared a prompt verbatim with an mPFC record.

### Added

- `PROVENANCE.md` — SCANAQ items appear to derive from seven established instruments (BRIEF-family,
  ERQ, BIS-11, GDMS, GSE, PSS, IRI), none previously cited. **These attributions are unverified**
  and must be confirmed against the source publications.
- `NOTICE.md` — scopes the MIT grant to original content, disclaiming third-party item text.
- `CITATION.cff`, `Forms/ARCHIVE.md`, this changelog.
- `scripts/score_scanaq.py` — executable reference implementation of scoring model 2.0.0, with the
  specification's worked example as a self-test.
- `scripts/validate_datasets.py` — re-runnable checks for every dataset invariant.

### Security

- Identifying metadata removed from both appendix PDFs. They carried the author's legal name in the
  `/Info` dictionary and the XMP `dc:creator` field, defeating the publication pseudonym used for
  blind peer review, along with a SharePoint content-type GUID. Page content is unchanged.
  **Not yet addressed:** the original blobs remain readable in commit `536b5f9`, and the Zenodo
  archive still holds the un-stripped files.

---

## [1.0.0] — 2025-07-31

Instrument version **1.0.0** · Scoring model **1.0.0** (assigned retroactively)

The state published as Appendix A and Appendix B and archived under the Zenodo DOI. Contains the
scoring defects listed above. Preserved as the published record — see `Forms/ARCHIVE.md`.
