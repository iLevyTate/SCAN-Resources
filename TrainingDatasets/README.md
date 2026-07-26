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
| ACC — Anterior Cingulate | 120 | 29 | 149 | detects conflicts, monitors task errors, and regulates competing priorities |
| DLPFC — Dorsolateral | 90 | 22 | 112 | expert in executive control, working memory, and higher-order planning |
| mPFC — Medial | 107 | 26 | 133 | integrates multi-source inputs to offer value-based, empathetic recommendations |
| OFC — Orbitofrontal | 103 | 25 | 128 | evaluates trade-offs, rewards, and long-term outcomes |
| vmPFC — Ventromedial | 84 | 21 | 105 | specializes in emotional regulation, social cognition, and risk evaluation |
| **Total** | **504** | **123** | **627** | |

System prompts are verbatim from the role specification in
`../Forms/PFC Agent Training Data Generation Prompt.md`. Each region uses exactly one, identical
across its training and validation splits — `../scripts/validate_datasets.py` enforces this.

## Provenance

Synthetically generated. All five regions were regenerated in release 2.0.0 against their
role specifications. See `../Forms/PFC Agent Training Data Generation Prompt.md` for
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

**Small corpus.** Regeneration prioritized role fidelity and diversity over volume, so the corpus
shrank from 790 records to 627. The reduction is concentrated in mPFC (191 → 133) and OFC
(199 → 128), where much of the original content was near-duplicate phrasing or belonged to the
other region. Validation sets run 21–29 records each — correct as a ratio, but thin in absolute
terms for evaluating a checkpoint.

**Single-turn only.** Every record is one exchange. Nothing here trains multi-turn behaviour,
clarifying questions, or context carried across turns.

**Synthetic throughout.** No record derives from a real user interaction, so the scenario
distribution reflects what was imagined rather than what users actually ask.

**No human review.** Responses are plausible advice, not validated guidance, and have not been
checked by domain experts.

**Scale.** 627 records is small for instruction tuning. Suited to adapter-based fine-tuning or as a
seed set, not to training from scratch.

## Intended use

Research on multi-agent cognitive architectures. The advice content is illustrative and is not
professional guidance of any kind. Nothing here is a clinical or psychological instrument — for the
SCANAQ questionnaire and its scoring model, see `../Forms/`.
