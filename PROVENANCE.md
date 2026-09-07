# Provenance of SCANAQ Items

> **Status: UNVERIFIED — requires confirmation before further distribution.**
>
> The attributions below were identified by wording correspondence and exact response-scale anchor
> matches during a repository audit. They have **not** been checked against the source publications.
> Each row is marked with its verification status. Confirm every entry before publishing, citing, or
> redistributing this instrument.

The SCANAQ is an **ad-hoc composite**. In **instrument 2.0.0**, Sections A (Executive Functioning)
and D (Risk Propensity) were independently reworded to measure their constructs — the BRIEF family
and the GRiPS respectively — **without reproducing source text**. The remaining 25 items (Sections B,
C, E, F, G, H) still appear drawn or adapted from six established instruments, three to eight items
per source, and their reuse terms are **unverified**. This document records what those sources appear
to be, what was changed, and what reuse terms apply.

## Why this matters

1. **Licensing.** This repository is MIT-licensed, which grants recipients broad reuse rights. That
   grant cannot extend to third-party item text the author does not own. See `NOTICE.md`.
2. **Validity.** Section scores here are **not** the source instruments' scores. Item subsets were
   taken, and at least one response scale was re-anchored. Published norms, cutoffs, and percentile
   tables from the source instruments **do not apply** to SCANAQ scores.
3. **Scoring correctness.** The subscale structure in scoring model 2.0.0 derives directly from these
   sources — reverse-keying Q32 is justified only by its being a PSS reverse item; splitting Q9–10
   from Q11–12 only by their being ERQ reappraisal vs. suppression items. Provenance and correct
   scoring are the same piece of work.

---

## Section-by-section

| Section | Items | Apparent source | Verification | Reuse terms |
|---|---|---|---|---|
| **A** Executive Functioning | 1–8 | Construct basis: BRIEF family (PAR Inc.). **Reworded in 2.0.0 — no source text reproduced.** | Reworded (construct only) | Original wording, MIT. Constructs are not copyrightable; BRIEF's item *text* is PAR's and is not reproduced. |
| **B** Emotion Regulation | 9–12 | ERQ — Emotion Regulation Questionnaire (Gross & John, 2003) | UNVERIFIED | Journal-published; customarily free for research use with citation. |
| **C** Impulsivity | 13–18 | BIS-11 — Barratt Impulsiveness Scale (Patton, Stanford & Barratt, 1995) | UNVERIFIED | Journal-published; customarily free for research use with citation. |
| **D** Risk Propensity | 19–21 | Construct basis: GRiPS (Zhang, Highhouse & Nye, 2019). **Reworded in 2.0.0 — no source text reproduced.** | Reworded (construct only) | Original wording, MIT. |
| **E** Decision-Making Style | 22–26 | GDMS — General Decision-Making Style (Scott & Bruce, 1995) | UNVERIFIED | Journal-published; customarily free for research use with citation. |
| **F** Self-Efficacy | 27–29 | GSE — General Self-Efficacy Scale (Schwarzer & Jerusalem, 1995) | UNVERIFIED | Generally free for research use with citation. |
| **G** Perceived Stress | 30–32 | PSS — Perceived Stress Scale (Cohen, Kamarck & Mermelstein, 1983) | UNVERIFIED | Not public domain; permission terms apply. |
| **H** Empathy and Social Cognition | 33–36 | IRI — Interpersonal Reactivity Index (Davis, 1980, 1983) | UNVERIFIED | Journal-published; customarily free for research use with citation. |

---

## Adaptations made

These differences from the apparent sources are material and must be disclosed wherever SCANAQ
results are reported.

### Item subsets

Only a fraction of each source instrument is used. Subscale reliability is therefore **not** that of
the published instrument, and in several cases is unestimable:

| Section | Items used | Source instrument length |
|---|---|---|
| A | 8 | BRIEF-A has 75 items |
| B | 4 | ERQ has 10 (6 reappraisal, 4 suppression) |
| C | 6 | BIS-11 has 30 |
| E | 5 | GDMS has 25 — one item per style subscale |
| F | 3 | GSE has 10 |
| G | 3 | PSS has 10 (PSS-10) or 4 (PSS-4) |
| H | 4 | IRI has 28 across four subscales |

### Response-scale re-anchoring

**Section G (Perceived Stress) is anchored 1–5; the PSS is natively anchored 0–4.** Every SCANAQ
Perceived Stress total is therefore shifted **+3** relative to a PSS score computed from the same
responses. These three items also do not constitute any standard PSS short form. PSS norms and
cutoffs must not be cited against SCANAQ Perceived Stress scores.

### Single-item subscales

Seven scored outputs rest on a single item, where reliability is undefined (Cronbach's α is
unestimable at n = 1) and measurement error is fully confounded with the score:

- Q13 — Attentional impulsivity
- Q35 — Perspective taking (**and it is reverse-keyed**, the weakest output in the model)
- Q22–Q26 — all five decision-making styles

Scoring model 2.0.0 labels these as indicative and requires a margin before drawing comparative
conclusions from them. It does not make them reliable.

### Construct overlap

Q3 ("I have trouble keeping my emotions under control") is emotion-regulation content inside the
Executive Functioning total, while Section B measures emotion regulation separately. Sections A and
B share variance by construction.

---

## Required actions

1. **Sections A and D are resolved by rewording (instrument 2.0.0).** Their items were independently
   rewritten to measure the BRIEF-family and GRiPS constructs without reproducing source text — the
   commercial exposure (BRIEF / PAR Inc.) is the reason A was done first. Two caveats stand:
   rewording is the standard non-infringing remedy but **is not a substitute for legal review** — a
   very close paraphrase of a short item can still be a derivative work, and the BRIEF items warrant
   a careful eye — and the reworded items do **not** carry the source instruments' validation.
2. **Verify the remaining sections (B, C, E, F, G, H) against the source publications.** Determine
   for each whether the SCANAQ items are *verbatim*, *adapted*, or *independently written* — the
   distinction is dispositive for licensing. These remain reproduced-or-adapted and unverified. The
   same rework remedy is available for any that turn out to be reproductions.
3. **Confirm PSS permission terms** (Section G), which are more restrictive than the other
   journal-published instruments.
4. **Add full citations** for every confirmed source, in this file and in the questionnaire.

---

## Not a validated instrument

The SCANAQ as assembled has not undergone reliability or validity testing. Per-section reliability
is unknown, and undefined for the single-item subscales listed above. It is a self-assessment and
personalization tool for aligning the SCAN system to a user's stated preferences. It is **not** a
diagnostic instrument and results are not comparable to scores from the source instruments.
