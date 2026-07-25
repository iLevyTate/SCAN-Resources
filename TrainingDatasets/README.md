# PFC Agent Training Datasets

Synthetic instruction-tuning dialogues for five prefrontal-cortex-simulating agents in the SCAN
architecture. Each record is a single-turn exchange: a system prompt defining the agent's cognitive
role, a user scenario, and a role-grounded response.

## Format

One JSON object per line, UTF-8, newline-terminated:

```json
{"messages": [
  {"role": "system",    "content": "<role definition>"},
  {"role": "user",      "content": "<scenario>"},
  {"role": "assistant", "content": "<response>"}
]}
```

Exactly three messages in that order. No other keys at any level.

## Contents

| Region | Training | Validation | Total | System prompt |
|---|---:|---:|---:|---|
| ACC — Anterior Cingulate | 99 | 50 | 149 | detects conflicts, monitors task errors, and regulates competing priorities |
| DLPFC — Dorsolateral | 66 | 46 | 112 | expert in executive control, working memory, and higher-order planning |
| mPFC — Medial | 95 | 96 | 191 | integrates multi-source inputs to offer value-based, empathetic recommendations |
| OFC — Orbitofrontal | 100 | 99 | 199 | evaluates trade-offs, rewards, and long-term outcomes |
| vmPFC — Ventromedial | 60 | 45 | 105 | specializes in emotional regulation, social cognition, and risk evaluation |
| **Total** | **420** | **336** | **756** | |

System prompts are verbatim from the role specification in
`../Forms/PFC Agent Training Data Generation Prompt.md`. Each region uses exactly one, identical
across its training and validation splits — `../scripts/validate_datasets.py` enforces this.

## Provenance

Synthetically generated. The ACC, DLPFC, and vmPFC sets were regenerated in release 2.0.0; mPFC and OFC
date from the original corpus. See `../Forms/PFC Agent Training Data Generation Prompt.md` for
the generation methodology and the source datasets recommended for grounding scenarios.

## Validation

```sh
python3 scripts/validate_datasets.py          # correctness
python3 scripts/validate_datasets.py --strict # also fails on quality warnings
```

Enforced invariants: valid UTF-8 and JSON per line; no BOM, CRLF, or trailing blank lines; exact
`system`/`user`/`assistant` schema with non-empty trimmed content; one spec-matching system prompt
per region; no duplicate records, prompts, or responses within a file; no train/validation leakage;
no prompt shared across regions.

## Known limitations

**Validation splits are oversized.** They run 30–50% of each region's data against a conventional
10–20%. Rebalancing is deferred until content stabilizes, since it changes record counts.

**mPFC and OFC overlap substantially.** Their thematic profiles are close — OFC carries a large
share of social content and mPFC a large share of trade-off content — and several near-duplicate
prompt pairs remain within each. Both are candidates for the regeneration already applied to ACC
and DLPFC.

**Lexical diversity varies by region.** Type-token ratios: ACC 0.30/0.39, DLPFC 0.32/0.39,
vmPFC 0.33/0.37, but mPFC 0.19/0.16 and OFC 0.17/0.17. The lower figures indicate formulaic
phrasing that will be reproduced by a model trained on them.

**No human review.** Responses are plausible advice, not validated guidance, and have not been
checked by domain experts.

**Scale.** 756 records is small for instruction tuning. Suited to adapter-based fine-tuning or as a
seed set, not to training from scratch.

## Intended use

Research on multi-agent cognitive architectures. The advice content is illustrative and is not
professional guidance of any kind. Nothing here is a clinical or psychological instrument — for the
SCANAQ questionnaire and its scoring model, see `../Forms/`.
