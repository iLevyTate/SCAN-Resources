# Appendix B (corrected) — SCANAQ Scoring Breakdown, Descriptions, and PFC-Inspired Suggestions

| | |
|---|---|
| **Scoring model version** | 2.0.0 (corrected) |
| **Applies to instrument version** | 1.0.0 (SCANAQ — 36 items, 8 sections; unchanged) |
| **Replaces** | Appendix B as published (scoring model 1.0.0) |

> **This appendix replaces the published Appendix B**, which used scoring model 1.0.0 and produced
> incorrect profiles in four of eight sections (A, B, C, E), with two further sections (G, H)
> yielding incorrect section totals. The
> **item text, item counts, and response scales in Appendix A are unchanged**; only the scoring and
> interpretation of those responses is corrected. Profiles produced with the published Appendix B
> must be **rescored from the raw item responses** — the old profile codes cannot be mechanically
> converted. The full list of corrections is in the *Summary of corrections* at the end of this
> appendix.

The authoritative, continuously maintained version of this scoring model is
`SCANAQ Numerical Scoring Breakdown.md` in the SCAN-Resources repository (Zenodo concept DOI
[10.5281/zenodo.14053202](https://doi.org/10.5281/zenodo.14053202)). This appendix is a
publication-ready extract of it.

---

## Scoring principles

Five rules govern every section, so that each threshold is derived rather than asserted.

1. **Score subscales, not section totals, where a label names more than one dimension.** A
   "high X, low Y" label cannot be recovered from a single sum at any cut point.
2. **Band boundaries are derived from named scale anchors** — at the tertiles of the anchor range for
   sections of ≥ 6 items, and at the neutral anchor for shorter sections — never at arbitrary
   integers.
3. **Direction is stated explicitly.** Deficit-worded sections (A, C, G) score upward toward
   difficulty; capability-worded sections (D, F, H) score upward toward capability.
4. **Reverse-keyed items are transformed (`6 − raw`) before summing.** This applies to Q32
   (Section G) and Q35 (Section H), which are worded opposite to their sections' direction.
5. **Missing responses are not imputed.** A subscale is scored only if all its items are answered;
   otherwise it is reported as `not_scored`.

---

## Section A: Executive Functioning (EF) — Items 1–8

**Scale** 1 (Never) – 3 (Often), all items deficit-worded · **Range** 8–24 ·
**Higher = more executive-functioning difficulty.** Single total; the eight items span too many
facets to support reliable subscales.

| PROFILE CODE | PROFILE LABEL | SCORE RANGE | ITEMS | DESCRIPTION | PFC-INSPIRED SUGGESTION |
|---|---|---|---|---|---|
| `EF-LOW` | Low difficulty | 8–13 | 1–8 | Few reported executive-functioning difficulties. | Maintain existing structures; no targeted scaffolding indicated. |
| `EF-MOD` | Moderate difficulty | 14–18 | 1–8 | Intermittent difficulty with initiation, organization, or follow-through. | Provide planning tools, reminders, and organizational aids; break tasks into smaller steps. |
| `EF-HIGH` | High difficulty | 19–24 | 1–8 | Frequent difficulty across multiple executive functions. | Provide planning tools, reminders, and organizational aids; break tasks into smaller steps. Prioritize external structure over recall. |

> **Correction.** The published table assigned the *lowest* score range (8–13) the label
> "Difficulty initiating and planning tasks" and the *highest* (14–24) "Strong working memory." All
> eight items are deficit-worded, so 8 is the least-impaired score: the interpretation was inverted.

**Content pointers (not scored).** For each item answered `3` (Often), emit a plain restatement of
what the respondent reported. These are restatements, not measurements — a single item cannot support
a facet-level claim such as "working memory is impaired," so do not aggregate, score, or threshold
them.

| Item | Pointer |
|---|---|
| Q1 | Reports frequent difficulty getting started on tasks |
| Q2 | Reports frequently forgetting instructions |
| Q3 | Reports frequent difficulty controlling emotions |
| Q4 | Reports frequent careless mistakes |
| Q5 | Reports frequently getting stuck on one approach |
| Q6 | Reports frequent difficulty planning ahead |
| Q7 | Reports frequent difficulty organizing tasks |
| Q8 | Reports frequent difficulty tracking belongings |

---

## Section B: Emotion Regulation (ER) — Items 9–12

**Scale** 1 (Strongly Disagree) – 7 (Strongly Agree) · **Higher = more use of that strategy.**
Two independent subscales — cognitive reappraisal (Q9 + Q10) and expressive suppression
(Q11 + Q12), each range 2–14, with High ≥ 9 (mean > neutral anchor 4).

| PROFILE CODE | PROFILE LABEL | REAPPRAISAL | SUPPRESSION | DESCRIPTION | PFC-INSPIRED SUGGESTION |
|---|---|---|---|---|---|
| `ER-RH-SL` | High Reappraisal, Low Suppression | High (9–14) | Low (2–8) | Strong reframing with open emotional expression. | Provide expressive-regulation tools to fine-tune social display and contextual appropriateness. |
| `ER-RL-SH` | Low Reappraisal, High Suppression | Low (2–8) | High (9–14) | Difficulty reframing; relies on suppressing expression. | Train cognitive reappraisal via CBT-style reframing tools and guided cognitive restructuring. |
| `ER-RH-SH` | High Reappraisal, High Suppression | High (9–14) | High (9–14) | Reframes effectively but also masks expression; strategy use may be effortful or context-driven. | Explore *when* suppression is deployed; reduce reliance where expression is safe, retain it where contextually warranted. |
| `ER-RL-SL` | Low Reappraisal, Low Suppression | Low (2–8) | Low (2–8) | Limited use of either strategy; emotions largely experienced and expressed unregulated. | Introduce foundational regulation skills — affect labeling and reappraisal — before strategy-selection work. |

> **Correction.** The published table summed reappraisal and suppression into one 4–28 total, then
> read a two-dimensional label off it. This made two of the four profiles unreachable and mapped
> opposite response patterns to the same label — e.g. maximum reappraisal / minimum suppression
> (14 + 2 = 16) and its exact opposite (2 + 14 = 16) both scored 16. The two strategies are now
> scored separately.

---

## Section C: Impulsivity (IMP) — Items 13–18

**Scale** 1 (Rarely/Never) – 4 (Almost Always/Always), deficit-worded · **Range** 6–24 ·
**Higher = more impulsivity.** Reported as an overall severity band **plus** a subtype.

**Overall severity** — tertiles of the 1–4 anchor range:

| PROFILE CODE | PROFILE LABEL | SCORE RANGE | ITEMS |
|---|---|---|---|
| `IMP-SEV-LOW` | Low impulsivity | 6–11 | 13–18 |
| `IMP-SEV-MOD` | Moderate impulsivity | 12–17 | 13–18 |
| `IMP-SEV-HIGH` | High impulsivity | 18–24 | 13–18 |

**Subtype** — three subscales reported as per-item means so they are commensurable: Attentional
(Q13, single item, indicative only), Motor (Q14 + Q15 + Q16), Non-planning (Q17 + Q18). Declare a
dominant subtype only if the leading mean exceeds the next by ≥ 0.50; otherwise `IMP-MIXED`.

| PROFILE CODE | CONDITION | PFC-INSPIRED SUGGESTION |
|---|---|---|
| `IMP-ATT` | Attentional leads by ≥ 0.50 | Provide attentional-control aids — mindfulness, focus timers, distraction blockers. |
| `IMP-MOT` | Motor leads by ≥ 0.50 | Embed pause-and-plan prompts before action; add commitment devices at points of purchase or decision. |
| `IMP-NP` | Non-planning leads by ≥ 0.50 | Use external structure, checklists, and "if-then" implementation intentions; extend planning horizon. |
| `IMP-MIXED` | No subscale leads by ≥ 0.50 | Address overall severity rather than a subtype; re-assess with a fuller impulsivity measure if subtype matters. |

> **Correction.** The published table labelled the *lowest* range (6–12) "High Motor Impulsivity…
> Acts impulsively" — 6 is the least impulsive score attainable, so the polarity was inverted — and
> derived the two-dimensional "High Attentional, Low Motor" label from a single sum.

---

## Section D: Risk Propensity (RP) — Items 19–21

**Scale** 1 (Strongly Disagree) – 5 (Strongly Agree) · **Range** 3–15 · **Higher = more risk-taking.**
Neutral anchor 3. *(Unchanged from the published appendix.)*

| PROFILE CODE | PROFILE LABEL | SCORE RANGE | ITEMS | DESCRIPTION | PFC-INSPIRED SUGGESTION |
|---|---|---|---|---|---|
| `RP-LOW` | Low risk-taking | 3–9 | 19–21 | Avoids risk; prefers safer choices. | Scaffold calculated exploration; present graded exposure to uncertainty with feedback. |
| `RP-HIGH` | High risk-taking | 10–15 | 19–21 | Seeks and enjoys taking risks. | Provide risk-assessment tools, consequence simulators, and decision-hygiene checklists. |

---

## Section E: Decision-Making Style (DM) — Items 22–26

**Scale** 1 (Strongly Disagree) – 5 (Strongly Agree). **No total is computed** — the five items are
one item each from five *different* decision-style subscales, so summing them would add unrelated
constructs. Score each item independently; the profile is the **argmax** across the five.

| STYLE CODE | ITEM | STYLE LABEL | DESCRIPTION | PFC-INSPIRED SUGGESTION |
|---|---|---|---|---|
| `DM-RAT` | Q22 | Rational | Logical, systematic decision-making. | Provide data-driven tools, structured analysis frameworks, and MCDA/utility modeling. |
| `DM-INT` | Q23 | Intuitive | Relies on instincts. | Pair intuition with post-hoc analytical checks; use scenarios and simulations for calibration. |
| `DM-DEP` | Q24 | Dependent | Seeks guidance and collaboration. | Offer collaborative tools and decision aids; scaffold autonomy via staged independence. |
| `DM-AVO` | Q25 | Avoidant | Procrastinates or avoids decisions. | Use proactive prompts, deadlines, and commitment devices; provide bounded-choice frameworks. |
| `DM-SPO` | Q26 | Spontaneous | Quick, reflexive decisions with limited forethought. | Introduce pause rules ("10-second rule"), consequence visualizations, and pre-commitment plans. |

**Tie rule (added).** Of the 3,125 possible response patterns, only 56.6% have a unique highest item;
the remaining 43.4% are ties, for which the published appendix specified no rule.

- **Two- to four-way tie** → report **co-dominant styles** as an ordered set, e.g. `DM-RAT+DM-AVO`.
- **All five equal** → `DM-UNDIFF` (undifferentiated).

> **Correction.** The published rule ("determine the single highest-scoring item") is undefined for
> the 43.4% of response patterns that contain a tie for the maximum. Each style also rests on a
> single item and should be treated as indicative.

---

## Section F: Self-Efficacy (SE) — Items 27–29

**Scale** 1 (Not at All True) – 4 (Exactly True) · **Range** 3–12 · **Higher = more self-efficacy.**
Anchor 3 ("Moderately True"). *(Unchanged from the published appendix.)*

| PROFILE CODE | PROFILE LABEL | SCORE RANGE | ITEMS | DESCRIPTION | PFC-INSPIRED SUGGESTION |
|---|---|---|---|---|---|
| `SE-LOW` | Low self-efficacy | 3–8 | 27–29 | Low confidence handling problems and challenges. | Build mastery via graded goals, mentorship, success tracking, and strengths-based reflection. |
| `SE-HIGH` | High self-efficacy | 9–12 | 27–29 | Confident and effective under challenge. | Leverage leadership potential; assign complex tasks; promote peer coaching and knowledge transfer. |

---

## Section G: Perceived Stress (PS) — Items 30–32

**Scale** 1 (Never) – 5 (Very Often) · **Range** 3–15 · **Higher = more perceived stress.**

> **Reverse-key Q32** (`6 − raw`) before summing. Q32 is the one positively-worded item in this
> section — reporting that things often went one's way indicates *less* stress — so it runs opposite
> to the section's direction.

Bands unchanged from the published appendix; the inputs are now correct.

| PROFILE CODE | PROFILE LABEL | SCORE RANGE | ITEMS | DESCRIPTION | PFC-INSPIRED SUGGESTION |
|---|---|---|---|---|---|
| `PS-LOW` | Low perceived stress | 3–9 | 30–32 | Reports lower stress frequency. | Maintain resilience practices; add anticipatory coping plans for high-demand periods. |
| `PS-HIGH` | High perceived stress | 10–15 | 30–32 | Frequently stressed or overwhelmed. | Provide stress management — CBT techniques, relaxation, time-buffering, prioritization aids. |

> **Correction.** The published Global Note ("scores are summed within each section") summed Q32
> raw, inverting its contribution and shifting the section total by up to 4 points.
>
> **Norming caveat.** These items are adapted from the Perceived Stress Scale, which is natively
> anchored 0–4; the SCANAQ uses 1–5. Published PSS norms, cutoffs, and percentiles do not apply to
> these totals.

---

## Section H: Empathy & Social Cognition (ESC) — Items 33–36

**Scale** 1 (Does Not Describe Me Well) – 5 (Describes Me Very Well) · **Higher = more of the named
construct.**

> **Reverse-key Q35** (`6 − raw`) before use. Q35 is a reverse-worded perspective-taking item —
> phrased opposite to the section's direction.

**Three separate outputs** — empathic concern, perspective taking, and fantasy are distinct
constructs and are not summed into one another.

| PROFILE CODE | SUBSCALE | ITEMS | RANGE | LOW / HIGH | PFC-INSPIRED SUGGESTION |
|---|---|---|---|---|---|
| `ESC-EC-{LOW,HIGH}` | Empathic Concern | Q33 + Q34 | 2–10 | Low 2–6 / High 7–10 | High: encourage mentoring and leadership roles; integrate into cooperative team workflows. Low: social-skills training and feedback on empathic accuracy. |
| `ESC-PT-{LOW,HIGH}` | Perspective Taking | `6 − Q35` | 1–5 | Low 1–3 / High 4–5 | Low: perspective-taking exercises and structured viewpoint-switching prompts. |
| `ESC-FS-{LOW,HIGH}` | Fantasy | Q36 | 1–5 | Low 1–3 / High 4–5 | Descriptive only — not an empathy indicator. |

**Optional convenience index.** `ESC-EMPATHY = EC + PT` (range 3–15; low 3–9, high 10–15) may be
reported for continuity with the published single High/Low Empathy output. It is a convenience index,
not a construct; prefer the separate outputs.

> **Corrections.** (1) Q35 was summed raw. (2) Fantasy (Q36) was folded into the empathy total; it
> measures imaginative transportation into fiction rather than empathy, and is now reported
> separately.

---

## Global notes

- Profiles align and personalize SCAN's agent behaviors; they are **not diagnostic categories**.
- Every scored record must retain `instrument_version`, `scoring_model_version`, and — mandatorily —
  the **raw item responses**. Profile codes are derived and cannot be migrated to a future scoring
  model without the raw responses.
- Ensure all processing complies with applicable privacy, ethical, and regulatory standards.

---

## Summary of corrections relative to the published Appendix B

| # | Section | Correction |
|---|---|---|
| 1 | A — Executive Functioning | Polarity un-inverted: low score now = low difficulty. |
| 2 | C — Impulsivity | Polarity un-inverted: low score now = low impulsivity. |
| 3 | B — Emotion Regulation | Split into reappraisal and suppression subscales; two previously unreachable profiles restored. |
| 4 | B, C | Two-dimensional labels no longer derived from a single sum. |
| 5 | G, H | Q32 and Q35 reverse-keyed (`6 − raw`) before summing. |
| 6 | H — Empathy | Fantasy (Q36) separated from the empathy total; no longer counted toward empathy. |
| 7 | E — Decision-Making | Tie rule added for the 43.4% of patterns previously undefined. |
| 8 | all | Missing-data rule added; band boundaries derived from named anchors; section renamed "Executive Functioning" for consistency with Appendix A. |

*Appendix A (the instrument itself — item text, counts, and response scales) is unchanged.*
