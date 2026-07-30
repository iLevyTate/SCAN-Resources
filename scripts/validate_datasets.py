#!/usr/bin/env python3
"""Validate the PFC agent training datasets.

Checks every invariant established during the repository audit, so regressions
are caught rather than rediscovered:

  structure   valid UTF-8, one JSON object per line, no BOM/CRLF, EOF newline
  schema      exactly [system, user, assistant], non-empty trimmed content
  prompts     one system prompt per region, matching the generation-prompt spec
  duplicates  no exact-duplicate records, user prompts, or assistant responses
  leakage     no user prompt shared between a region's train and validation split
  overlap     no user prompt shared across two different regions

Usage:
    python3 scripts/validate_datasets.py [--strict]

`--strict` additionally fails on near-duplicates and low lexical diversity,
which are quality signals rather than correctness bugs.

Standard library only. Exit code 0 if all checks pass, 1 otherwise.
"""

from __future__ import annotations

import collections
import difflib
import itertools
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "TrainingDatasets"
SPEC = ROOT / "Forms" / "PFC Agent Training Data Generation Prompt.md"

REGIONS = ["acc", "dlpfc", "mPFC", "ofc", "vmpfc"]
SPLITS = ["training", "validation"]

# Canonical system prompts, verbatim from the generation-prompt spec. Kept here
# so a drift between spec and data is a test failure, not a silent divergence.
EXPECTED_SYSTEM = {
    "dlpfc": "The assistant is an expert in executive control, working memory, and higher-order planning.",
    "vmpfc": "The assistant specializes in emotional regulation, social cognition, and risk evaluation.",
    "ofc": "The assistant evaluates trade-offs, rewards, and long-term outcomes.",
    "acc": "The assistant detects conflicts, monitors task errors, and regulates competing priorities.",
    "mPFC": "The assistant integrates multi-source inputs to offer value-based, empathetic recommendations.",
}

# Expected record counts, kept in sync with the dataset cards (README.md and
# TrainingDatasets/README.md). Hardcoded so an accidental drop or duplication
# during regeneration fails CI rather than passing structurally while silently
# contradicting the docs — the same rationale as EXPECTED_SYSTEM above. When
# counts change intentionally, update the data, these values, and both READMEs
# together.
EXPECTED_COUNTS = {
    "acc_training_data.jsonl": 120, "acc_validation_data.jsonl": 29,
    "dlpfc_training_data.jsonl": 90, "dlpfc_validation_data.jsonl": 22,
    "mPFC_training_data.jsonl": 107, "mPFC_validation_data.jsonl": 26,
    "ofc_training_data.jsonl": 103, "ofc_validation_data.jsonl": 25,
    "vmpfc_training_data.jsonl": 88, "vmpfc_validation_data.jsonl": 22,
}

NEAR_DUP_RATIO = 0.90
MIN_TTR = 0.20

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def normalize(s: str) -> str:
    s = s.lower().replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').replace("—", "-")
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", s).split())


def load() -> dict[str, list[tuple[int, dict]]]:
    """Parse every dataset file, reporting structural problems as failures."""
    data: dict[str, list[tuple[int, dict]]] = {}
    for region in REGIONS:
        for split in SPLITS:
            name = f"{region}_{split}_data.jsonl"
            path = DATA / name
            if not path.exists():
                fail(f"{name}: missing")
                continue

            raw = path.read_bytes()
            if raw.startswith(b"\xef\xbb\xbf"):
                fail(f"{name}: has a UTF-8 BOM")
            if b"\r\n" in raw:
                fail(f"{name}: has CRLF line endings")
            if raw and not raw.endswith(b"\n"):
                fail(f"{name}: no newline at end of file")
            if raw.endswith(b"\n\n"):
                fail(f"{name}: trailing blank line")

            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError as exc:
                fail(f"{name}: not valid UTF-8 ({exc})")
                continue

            records = []
            for lineno, line in enumerate(text.splitlines(), 1):
                if not line.strip():
                    fail(f"{name}:{lineno}: blank line")
                    continue
                if line != line.strip():
                    fail(f"{name}:{lineno}: leading or trailing whitespace")
                try:
                    records.append((lineno, json.loads(line)))
                except json.JSONDecodeError as exc:
                    fail(f"{name}:{lineno}: invalid JSON ({exc})")
            data[name] = records
    return data


def check_schema(data) -> None:
    for name, records in data.items():
        for lineno, obj in records:
            where = f"{name}:{lineno}"
            if set(obj) != {"messages"}:
                fail(f"{where}: top-level keys {sorted(obj)}, expected ['messages']")
                continue
            msgs = obj["messages"]
            if not isinstance(msgs, list):
                fail(f"{where}: 'messages' is not a list")
                continue
            if [m.get("role") for m in msgs] != ["system", "user", "assistant"]:
                fail(f"{where}: role sequence {[m.get('role') for m in msgs]}")
            for i, m in enumerate(msgs):
                if set(m) != {"role", "content"}:
                    fail(f"{where}: message {i} keys {sorted(m)}")
                content = m.get("content")
                if not isinstance(content, str):
                    fail(f"{where}: message {i} content is not a string")
                elif not content.strip():
                    fail(f"{where}: message {i} content is empty")
                elif content != content.strip():
                    fail(f"{where}: message {i} content has surrounding whitespace")


def check_system_prompts(data) -> None:
    """Each region uses exactly one system prompt, and it matches the spec."""
    spec_text = SPEC.read_text(encoding="utf-8") if SPEC.exists() else ""
    for region in REGIONS:
        expected = EXPECTED_SYSTEM[region]
        if spec_text and expected not in spec_text:
            fail(f"{region}: expected system prompt is absent from {SPEC.name} "
                 f"— spec and validator have drifted")
        for split in SPLITS:
            name = f"{region}_{split}_data.jsonl"
            found = {o["messages"][0]["content"] for _, o in data.get(name, [])
                     if o.get("messages")}
            if not found:
                continue
            if len(found) > 1:
                fail(f"{name}: {len(found)} distinct system prompts, expected 1")
            for prompt in found:
                if prompt != expected:
                    fail(f"{name}: system prompt does not match spec\n"
                         f"       expected: {expected}\n"
                         f"       found:    {prompt}")


def check_duplicates(data) -> None:
    for name, records in data.items():
        for label, extract in (("record", lambda o: json.dumps(o, sort_keys=True)),
                               ("user prompt", lambda o: o["messages"][1]["content"].strip()),
                               ("assistant response", lambda o: o["messages"][2]["content"].strip())):
            seen: dict[str, int] = {}
            for lineno, obj in records:
                try:
                    key = extract(obj)
                except (KeyError, IndexError, TypeError):
                    continue
                if key in seen:
                    fail(f"{name}: duplicate {label} on lines {seen[key]} and {lineno}")
                else:
                    seen[key] = lineno


def _user_prompt(obj) -> str | None:
    """User-prompt text, or None for a malformed record (already flagged by
    check_schema). Lets the downstream checks skip it instead of crashing."""
    try:
        return obj["messages"][1]["content"]
    except (KeyError, IndexError, TypeError):
        return None


def check_counts(data) -> None:
    """Record counts match the dataset cards, so a silent drop or duplication
    during regeneration fails CI rather than diverging from the READMEs."""
    for name, expected in EXPECTED_COUNTS.items():
        actual = len(data.get(name, []))
        if actual != expected:
            fail(f"{name}: {actual} records, expected {expected} "
                 f"(reconcile the data, EXPECTED_COUNTS, and both READMEs)")


def check_leakage(data) -> None:
    """No user prompt may appear in both a region's train and validation split."""
    for region in REGIONS:
        train = data.get(f"{region}_training_data.jsonl", [])
        val = data.get(f"{region}_validation_data.jsonl", [])
        seen = {normalize(p): ln for ln, o in train if (p := _user_prompt(o)) is not None}
        for lineno, obj in val:
            p = _user_prompt(obj)
            if p is None:
                continue
            key = normalize(p)
            if key in seen:
                fail(f"{region}: validation line {lineno} duplicates training "
                     f"line {seen[key]} (train/validation leakage)")


def check_cross_region(data) -> None:
    """A prompt shared by two regions undermines the specialization premise."""
    index: dict[str, list[str]] = collections.defaultdict(list)
    for name, records in data.items():
        region = name.split("_")[0]
        for lineno, obj in records:
            p = _user_prompt(obj)
            if p is None:
                continue
            index[normalize(p)].append(f"{region} ({name}:{lineno})")
    for prompt, locations in index.items():
        regions = {loc.split(" ")[0] for loc in locations}
        if len(regions) > 1:
            fail(f"prompt shared across regions {sorted(regions)}: {prompt[:70]}...\n"
                 f"       {'; '.join(locations)}")


def check_quality(data) -> None:
    """Near-duplicates and lexical diversity. Warnings unless --strict."""
    report = fail if "--strict" in sys.argv else warn
    for name, records in data.items():
        prompts = [(ln, normalize(o["messages"][1]["content"])) for ln, o in records]
        for (l1, a), (l2, b) in itertools.combinations(prompts, 2):
            if not a or not b:
                continue
            if abs(len(a) - len(b)) / max(len(a), len(b)) > 0.3:
                continue
            if difflib.SequenceMatcher(None, a, b).ratio() >= NEAR_DUP_RATIO:
                report(f"{name}: lines {l1} and {l2} are near-duplicate prompts")

        tokens = [w for _, o in records for w in normalize(o["messages"][2]["content"]).split()]
        if tokens:
            ttr = len(set(tokens)) / len(tokens)
            if ttr < MIN_TTR:
                report(f"{name}: type-token ratio {ttr:.3f} below {MIN_TTR} "
                       f"— responses are lexically narrow")


def main() -> int:
    if not DATA.is_dir():
        print(f"error: {DATA} not found", file=sys.stderr)
        return 1

    data = load()
    check_schema(data)
    check_system_prompts(data)
    check_counts(data)
    check_duplicates(data)
    check_leakage(data)
    check_cross_region(data)
    check_quality(data)

    total = sum(len(r) for r in data.values())
    print(f"{len(data)} files, {total} records\n")
    for name in sorted(data):
        print(f"  {name:34} {len(data[name]):>4} records")

    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  ! {w}")

    if failures:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures:
            print(f"  x {f}")
        return 1

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
