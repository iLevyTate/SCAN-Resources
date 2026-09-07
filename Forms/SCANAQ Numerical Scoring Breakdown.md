# SCANAQ Scoring Model

| | |
|---|---|
| **Scoring model version** | 2.0.0 |
| **Applies to instrument version** | 1.0.0 and 2.0.0 (SCANAQ, 36 items, 8 sections) |
| **Status** | Current — authoritative |
| **Supersedes** | Scoring model 1.0.0 (see [Appendix 1](#appendix-1--migration-from-scoring-model-100)) |

> **Scoring model 1.0.0 produced incorrect profiles in four of eight sections.** It is preserved
> in the archived paper appendix (`SCANAQ Scoring Breakdown, Descriptions, and PFC-Inspired
> Suggestions.pdf`) as the published record. Do not score new responses with it. See
> [Appendix 1](#appendix-1--migration-from-scoring-model-100) before reusing any previously
> scored data.

---

## 1. Scoring principles

These five rules govern every section. They exist so that a future change to any threshold is
checkable rather than asserted.

### 1.1 Score subscales, not section totals

A profile label that names two dimensions ("high X, low Y") cannot be derived from a single sum —
that is an arity error, not a threshold error, and no choice of cut point fixes it. Where a label is
multi-dimensional, the section is scored as separate subscales. Where a label is genuinely scalar,
a single total is used.

### 1.2 Band boundaries are derived from scale anchors

Bands are defined on the **mean item response**, with boundaries at *named anchor values* of that
section's response scale — never at arbitrary integers.

- Sections with **≥ 6 items** get three bands, at the tertiles of the anchor range.
- Sections with **< 6 items** get two bands, at the neutral anchor (or, for scales with no neutral
  point, at the anchor marking the qualitative shift).

Each section below records the anchor used. A threshold that does not satisfy this rule is a bug.

### 1.3 Direction of scoring is stated explicitly

Every scored output declares whether a higher score means *more* or *less* of the named construct.
Deficit-worded sections (A, C, G) score upward toward difficulty; capability-worded sections
(D, F, H) score upward toward capability.

### 1.4 Reverse-keyed items are reverse-keyed before summing

Two items are worded opposite to their section's direction and are transformed as
`reversed = (scale_max + scale_min) − raw` before entering any total:

| Item | Description | Section | Transform |
|---|---|---|---|
| **Q32** | Positively-worded stress item — higher raw indicates *less* stress | G Perceived Stress | `6 − raw` |
| **Q35** | Reverse-worded perspective-taking item | H Empathy | `6 − raw` |

Summing these raw — as scoring model 1.0.0 did — inverts their contribution.

### 1.5 Missing responses are not imputed

Respondents are explicitly permitted to skip items. A subscale is computed **only if every one of
its items is answered**; otherwise it is emitted as `not_scored` and the remaining subscales are
scored normally. There is no proration and no imputation — prorating a two-item subscale from one
answer is not measurement.

---

## 2. Section A — Executive Functioning (EF)

**Items** 1–8 · **Scale** 1 (Never) – 3 (Often) · **Range** 8–24
**Direction** Higher = **more** executive-functioning difficulty. All eight items are deficit-worded.

**Single total, no subscales.** Eight items spanning seven distinct facets cannot support reliable
subscales; only Plan/Organize (Q6+Q7) has more than one item.

**Banding** — tertiles of the 1–3 anchor range (mean 1.67 / 2.33):

| Code | Band | Total | Description | Suggestion |
|---|---|---|---|---|
| `EF-LOW` | Low difficulty | 8–13 | Few reported executive-functioning difficulties. | Maintain existing structures; no targeted scaffolding indicated. |
| `EF-MOD` | Moderate difficulty | 14–18 | Intermittent difficulty with initiation, organization, or follow-through. | Provide planning tools, reminders, and organizational aids; break tasks into smaller steps. |
| `EF-HIGH` | High difficulty | 19–24 | Frequent difficulty across multiple executive functions. | Provide planning tools, reminders, organizational aids; break tasks into smaller steps. Prioritize external structure over recall. |

**Content pointers (not scored).** For each item answered `3` (Often), emit a plain restatement of
what the respondent reported:

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

> These are **restatements, not measurements.** A single item cannot support a facet-level claim
> such as "working memory is impaired." Do not aggregate, score, or threshold them.

> **Construct overlap.** Q3 ("trouble keeping my emotions under control") is emotion-regulation
> content inside the EF total, while Section B measures emotion regulation separately. Sections A
> and B therefore share variance by construction. Documented, not corrected — changing items would
> require an instrument version bump.

---

## 3. Section B — Emotion Regulation (ER)

**Items** 9–12 · **Scale** 1 (Strongly Disagree) – 7 (Strongly Agree)
**Direction** Higher = **more** use of that strategy.

**Two subscales.** Reappraisal and suppression are distinct, weakly related strategies. Scoring
model 1.0.0 summed them into one 4–28 total, which made its own labels unreachable: maximum
reappraisal with minimum suppression (14 + 2 = 16) and its exact opposite (2 + 14 = 16) both scored
16 and both received "Low Reappraisal, High Suppression."

| Subscale | Items | Range | Low | High |
|---|---|---|---|---|
| Cognitive Reappraisal | Q9 + Q10 | 2–14 | 2–8 | 9–14 |
| Expressive Suppression | Q11 + Q12 | 2–14 | 2–8 | 9–14 |

**Banding** — neutral anchor 4 ("Neither Agree nor Disagree"); mean ≤ 4 is low. A subscale sum of 8
(mean exactly 4.0, full neutrality) falls in the low band by convention.

**Profile — a genuine 2 × 2.** Two of these cells could not be represented at all under the previous
model:

| Code | Reappraisal | Suppression | Description | Suggestion |
|---|---|---|---|---|
| `ER-RH-SL` | High | Low | Strong reframing with open emotional expression. | Provide expressive-regulation tools to fine-tune social display and contextual appropriateness. |
| `ER-RL-SH` | Low | High | Difficulty reframing; relies on suppressing expression. | Train cognitive reappraisal via CBT-style reframing tools and guided cognitive restructuring. |
| `ER-RH-SH` | High | High | Reframes effectively but also masks expression; strategy use may be effortful or context-driven. | Explore *when* suppression is deployed; reduce reliance on it where expression is safe, retain it where contextually warranted. |
| `ER-RL-SL` | Low | Low | Limited use of either regulation strategy; emotions may be experienced and expressed largely unregulated. | Introduce foundational regulation skills — affect labeling and reappraisal — before strategy-selection work. |

---

## 4. Section C — Impulsivity (IMP)

**Items** 13–18 · **Scale** 1 (Rarely/Never) – 4 (Almost Always/Always) · **Range** 6–24
**Direction** Higher = **more** impulsivity.

### 4.1 Overall severity

**Banding** — tertiles of the 1–4 anchor range (mean 2.0 "Occasionally" / 3.0 "Often"):

| Code | Band | Total |
|---|---|---|
| `IMP-SEV-LOW` | Low | 6–11 |
| `IMP-SEV-MOD` | Moderate | 12–17 |
| `IMP-SEV-HIGH` | High | 18–24 |

### 4.2 Subtype

Three subscales, **always reported side by side** as per-item means so they are commensurable
despite different item counts:

| Subscale | Items | Raw range | Per-item mean |
|---|---|---|---|
| Attentional | Q13 | 1–4 | 1.00–4.00 — **single item, indicative only** |
| Motor | Q14 + Q15 + Q16 | 3–12 | 1.00–4.00 |
| Non-planning | Q17 + Q18 | 2–8 | 1.00–4.00 |

**Dominance rule.** Declare a dominant subtype **only if the leading mean exceeds the next by
≥ 0.50** (half an anchor step). Otherwise emit `IMP-MIXED`.

| Code | Condition | Suggestion |
|---|---|---|
| `IMP-ATT` | Attentional leads by ≥ 0.50 | Provide attentional control aids — mindfulness, focus timers, distraction blockers. |
| `IMP-MOT` | Motor leads by ≥ 0.50 | Embed pause-and-plan prompts before action; add commitment devices at points of purchase or decision. |
| `IMP-NP` | Non-planning leads by ≥ 0.50 | Use external structure, checklists, and "if-then" implementation intentions; extend planning horizon. |
| `IMP-MIXED` | No subscale leads by ≥ 0.50 | Address overall severity rather than a subtype; re-assess with a fuller impulsivity measure if subtype matters. |

> The three subscales carry very different measurement error — Attentional rests on one item with
> four possible values. Taking an unguarded argmax across them would let noise decide the subtype;
> the 0.50 margin is what prevents that.

---

## 5. Section D — Risk Propensity (RP)

**Items** 19–21 · **Scale** 1 (Strongly Disagree) – 5 (Strongly Agree) · **Range** 3–15
**Direction** Higher = **more** risk-taking.
**Banding** — neutral anchor 3; mean ≤ 3 is low. *(Unchanged from model 1.0.0.)*

| Code | Band | Total | Description | Suggestion |
|---|---|---|---|---|
| `RP-LOW` | Low risk-taking | 3–9 | Avoids risk; prefers safer choices. | Scaffold calculated exploration; present graded exposure to uncertainty with feedback. |
| `RP-HIGH` | High risk-taking | 10–15 | Seeks and enjoys taking risks. | Provide risk-assessment tools, consequence simulators, and decision-hygiene checklists. |

---

## 6. Section E — Decision-Making Style (DM)

**Items** 22–26 · **Scale** 1 (Strongly Disagree) – 5 (Strongly Agree)

> **No total is computed for this section.** Q22–Q26 are one item each from five *different*
> decision-style subscales. Summing them would add unrelated constructs, so no cumulative range is
> defined or published.

**Rule.** Score each item independently; the profile is the **argmax** across the five.

| Code | Item | Style | Suggestion |
|---|---|---|---|
| `DM-RAT` | Q22 | Rational | Provide data-driven tools, structured analysis frameworks, and MCDA/utility modeling. |
| `DM-INT` | Q23 | Intuitive | Pair intuition with post-hoc analytical checks; use scenarios and simulations for calibration. |
| `DM-DEP` | Q24 | Dependent | Offer collaborative tools and decision aids; scaffold autonomy via staged independence. |
| `DM-AVO` | Q25 | Avoidant | Use proactive prompts, deadlines, and commitment devices; provide bounded-choice frameworks. |
| `DM-SPO` | Q26 | Spontaneous | Introduce pause rules ("10-second rule"), consequence visualizations, and pre-commitment plans. |

**Ties.** Of the 3,125 possible response patterns for Q22–26, only **56.6% have a unique highest
item** — 43.4% are ties (32.0% two-way, 9.6% three-way, 1.6% four-way, 0.2% five-way). Model 1.0.0
specified no rule for any of them.

- **2–4 way tie** → report **co-dominant styles** as an ordered set, e.g. `DM-RAT+DM-SPO`. Do not
  resolve arbitrarily; a person equally rational and spontaneous is a real profile.
- **All five equal** → `DM-UNDIFF` (undifferentiated). Distinct from a co-dominant set, and a
  realistic pattern for uniformly low or uniformly high responders.

> Every style rests on a **single item**. Treat all five scores as indicative, and prefer the
> co-dominant set over forcing a single winner.

---

## 7. Section F — Self-Efficacy (SE)

**Items** 27–29 · **Scale** 1 (Not at All True) – 4 (Exactly True) · **Range** 3–12
**Direction** Higher = **more** self-efficacy.
**Banding** — anchor 3 ("Moderately True"); mean < 3 is low. *(Unchanged from model 1.0.0.)*

| Code | Band | Total | Description | Suggestion |
|---|---|---|---|---|
| `SE-LOW` | Low self-efficacy | 3–8 | Low confidence handling problems and challenges. | Build mastery via graded goals, mentorship, success tracking, and strengths-based reflection. |
| `SE-HIGH` | High self-efficacy | 9–12 | Confident and effective under challenge. | Leverage leadership potential; assign complex tasks; promote peer coaching and knowledge transfer. |

---

## 8. Section G — Perceived Stress (PS)

**Items** 30–32 · **Scale** 1 (Never) – 5 (Very Often) · **Range** 3–15
**Direction** Higher = **more** perceived stress.

> **Q32 must be reverse-keyed** (`6 − raw`) before summing — see [§1.4](#14-reverse-keyed-items-are-reverse-keyed-before-summing). It is
> positively worded; a respondent reporting things often went their way is reporting *less* stress.

**Banding** — neutral anchor 3; mean ≤ 3 is low. *(Bands unchanged from model 1.0.0; the inputs are
now correct.)*

| Code | Band | Total | Description | Suggestion |
|---|---|---|---|---|
| `PS-LOW` | Low perceived stress | 3–9 | Reports lower stress frequency. | Maintain resilience practices; add anticipatory coping plans for high-demand periods. |
| `PS-HIGH` | High perceived stress | 10–15 | Frequently stressed or overwhelmed. | Provide stress management — CBT techniques, relaxation, time-buffering, prioritization aids. |

> **Not comparable to published stress norms.** These three items are adapted from the Perceived
> Stress Scale, which is natively anchored **0–4**; the SCANAQ uses **1–5**, shifting every total by
> +3. This is also not any standard PSS short form. PSS norms, cutoffs, and percentiles **do not
> apply** and must not be cited against these scores.

---

## 9. Section H — Empathy and Social Cognition (ESC)

**Items** 33–36 · **Scale** 1 (Does Not Describe Me Well) – 5 (Describes Me Very Well)
**Direction** Higher = **more** of the named construct.

> **Q35 must be reverse-keyed** (`6 − raw`) — see [§1.4](#14-reverse-keyed-items-are-reverse-keyed-before-summing). It is worded opposite to the
> section's direction.

**Three separate outputs.** Empathic concern, perspective taking, and fantasy are distinct
constructs and are not summed into one another.

| Code | Subscale | Items | Range | Low | High | Suggestion (high / low) |
|---|---|---|---|---|---|---|
| `ESC-EC-{LOW,HIGH}` | Empathic Concern | Q33 + Q34 | 2–10 | 2–6 | 7–10 | High: encourage mentoring and leadership roles; integrate into cooperative team workflows. Low: social skills training and feedback on empathic accuracy. |
| `ESC-PT-{LOW,HIGH}` | Perspective Taking | `6 − Q35` | 1–5 | 1–3 | 4–5 | Low: perspective-taking exercises and structured viewpoint-switching prompts. |
| `ESC-FS-{LOW,HIGH}` | Fantasy | Q36 | 1–5 | 1–3 | 4–5 | Descriptive only — see caution below. |

**Banding** — neutral anchor 3; mean ≤ 3 is low.

**Optional convenience index.** `ESC-EMPATHY = EC + PT` (range 3–15; low 3–9, high 10–15) may be
reported for continuity with model 1.0.0's single High/Low Empathy output. It is a **convenience
index, not a construct** — the two subscales correlate only modestly. Prefer the separate outputs.

> **Fantasy is not an empathy indicator.** Q36 measures imaginative transportation into fictional
> situations. It is reported for descriptive completeness and is **never** summed into empathy.
>
> **Perspective Taking rests on one reverse-keyed item** — the weakest output in this model.
> Reverse-keyed items are precisely what inattentive responders answer incorrectly, and there is no
> second perspective-taking item available to detect it. Treat `ESC-PT` as indicative only.
>
> **"Personal distress" is not measured.** Model 1.0.0's documentation claimed this section covered
> empathic concern, personal distress, perspective-taking, and fantasy. No item measures personal
> distress; the claim has been removed.

---

## 10. Output record

Every scored result must carry:

```json
{
  "instrument_version": "2.0.0",
  "scoring_model_version": "2.0.0",
  "scored_at": "<ISO-8601>",
  "raw_responses": { "Q1": 2, "Q2": 1, "…": "…", "Q36": 4 },
  "codes": ["EF-MOD", "ER-RL-SH", "IMP-SEV-MOD", "IMP-MIXED", "…"]
}
```

> **`raw_responses` is mandatory.** Profile codes are derived and disposable; raw item responses are
> the only field that survives a scoring-model change. A stored code without its raw responses
> cannot be migrated — it can only be discarded.

---

## 11. Worked example

A complete response set with every intermediate value. This doubles as the regression test for this
document: anyone can verify the spec against itself.

**Responses** — Q1–8: `3,2,1,2,3,3,2,1` · Q9–12: `6,5,2,3` · Q13–18: `2,4,4,3,2,1` ·
Q19–21: `4,3,2` · Q22–26: `5,3,2,5,1` · Q27–29: `3,2,4` · Q30–32: `4,4,2` · Q33–36: `4,5,4,2`

| Section | Computation | Result |
|---|---|---|
| **A EF** | 3+2+1+2+3+3+2+1 = **17** → band 14–18 | `EF-MOD` |
| | Items answered 3: Q1, Q5, Q6 | Pointers: difficulty starting tasks; getting stuck on one approach; planning ahead |
| **B ER** | Reappraisal 6+5 = **11** (≥9 → High); Suppression 2+3 = **5** (≤8 → Low) | `ER-RH-SL` |
| **C IMP** | Severity 2+4+4+3+2+1 = **16** → band 12–17 | `IMP-SEV-MOD` |
| | Attentional 2/1 = **2.00**; Motor (4+4+3)/3 = **3.67**; Non-planning (2+1)/2 = **1.50** | |
| | Motor leads by 3.67 − 2.00 = **1.67** ≥ 0.50 | `IMP-MOT` |
| **D RP** | 4+3+2 = **9** → band 3–9 | `RP-LOW` |
| **E DM** | Q22=5, Q23=3, Q24=2, Q25=5, Q26=1 → max 5, tied on Q22 and Q25 | `DM-RAT+DM-AVO` |
| **F SE** | 3+2+4 = **9** → band 9–12 | `SE-HIGH` |
| **G PS** | Q32 reversed = 6−2 = 4; total 4+4+**4** = **12** → band 10–15 | `PS-HIGH` |
| | *(scored raw it would be 4+4+2 = 10 — same band here, but 2 points lower)* | |
| **H ESC** | EC 4+5 = **9** (≥7 → High) | `ESC-EC-HIGH` |
| | PT = 6−4 = **2** (≤3 → Low) | `ESC-PT-LOW` |
| | Fantasy Q36 = **2** (≤3 → Low) | `ESC-FS-LOW` |
| | *(convenience index: 9 + 2 = 11 → High)* | `ESC-EMPATHY-HIGH` |

Note the two profiles this example surfaces that model 1.0.0 could not express: high empathic
concern alongside low perspective taking, and a co-dominant rational/avoidant decision style.

---

## Appendix 1 — Migration from scoring model 1.0.0

**Previously scored data cannot be mechanically converted. It must be rescored from raw item
responses.** No conversion function is provided, because providing one would imply a valid
conversion exists.

| v1.0.0 | v2.0.0 | Convertible? |
|---|---|---|
| `4A` / `4B` (EF) | `EF-LOW` / `EF-MOD` / `EF-HIGH` | **No.** v1 assigned these under inverted polarity — 4A labelled the *fewest*-difficulty band as difficulty. The bands do not correspond. |
| `2A` / `2B` (ER) | `ER-R{H,L}-S{H,L}` | **No.** v1 derived a two-dimensional label from one sum; the underlying subscale values were never computed. |
| `5A` / `5B` (IMP) | `IMP-SEV-*` + `IMP-{ATT,MOT,NP,MIXED}` | **No.** Same arity error, plus v1's bands ran opposite to impulsivity direction. |
| `3A` / `3B` (ESC) | `ESC-EC-*`, `ESC-PT-*`, `ESC-FS-*` | **No.** v1 summed a reverse-keyed item raw and folded fantasy into empathy. |
| `6A` / `6B` (RP) | `RP-HIGH` / `RP-LOW` | **Yes** — direct relabel; bands unchanged. |
| `7A` / `7B` (SE) | `SE-HIGH` / `SE-LOW` | **Yes** — direct relabel; bands unchanged. |
| `8A` / `8B` (PS) | `PS-HIGH` / `PS-LOW` | **No.** Bands are unchanged but Q32 was summed raw, so totals were wrong by up to 4 points. |
| `1A`–`1E` (DM) | `DM-{RAT,INT,DEP,AVO,SPO}` | **Partial** — relabels cleanly where v1 had a unique winner, but v1 had no tie rule, so any tied response set was resolved arbitrarily or not at all. |

**Why the codes were renamed rather than reused.** Keeping `4A` while changing its meaning fails
*silently*: a stored `4A` gives no way to tell which model assigned it. A visible break is safer
than a stable identifier with drifted semantics. The v1 numeric prefixes were also ordered neither
by section (A–H) nor consistently by name.

---

## Appendix 2 — Changes from scoring model 1.0.0

1. **Executive Functioning polarity corrected.** v1 labelled 8–13 "difficulty initiating and
   planning" and 14–24 "strong working memory". All eight items are deficit-worded, so 8 is the
   *least*-impaired score. Inverted.
2. **Impulsivity polarity corrected.** v1 labelled 6–12 — the least impulsive range attainable —
   "high motor impulsivity; acts impulsively".
3. **Two-dimensional labels replaced.** "High Inhibition, Low Planning" and "High Attentional, Low
   Motor" were read off single sums. Now computed from subscales, or removed.
4. **Emotion Regulation split** into reappraisal and suppression, making two previously
   unrepresentable profiles reachable.
5. **Q32 and Q35 reverse-keyed.** v1's global note ("scores are summed within each section")
   confirms they were summed raw.
6. **"Personal distress" claim removed** — no item measures it.
7. **Decision-Making tie rules added**, covering the 43.4% of response patterns v1 left undefined;
   the misleading cumulative range is explicitly not published.
8. **Missing-data rule added.** Skipping is permitted by the questionnaire; v1 defined no behaviour.
9. **Band boundaries now derived** from named scale anchors (§1.2) rather than asserted. v1's
   Executive Functioning, Emotion Regulation, and Impulsivity thresholds were all asymmetric and
   unexplained.
10. **Three redundant tables collapsed** into one canonical per-section view, ending the drift
    between them.
11. **"Executive Function" renamed "Executive Functioning"**, matching the questionnaire and README.

See `PROVENANCE.md` for the source instruments these items derive from, and the reuse terms that
apply to them.
