#!/usr/bin/env bash
#
# Purge the author's legal name from git history.
#
# WHAT THIS FIXES
#   Commit 291a991 stripped identifying metadata from the two appendix PDFs in
#   the working tree. It did not touch history. The original blobs are still
#   reachable:
#
#       git show c15ffc8753227d28803c6ca449c89f1defe2bfd1   # scoring appendix
#       git show 48db2ecf5d3152f92ee864d6a279a71c0406befb   # questionnaire appendix
#
#   Both were introduced by commit 536b5f9, which is on origin/main. Anyone can
#   read the name out of them today.
#
#   This script replaces those two blobs, everywhere they appear in history,
#   with the cleaned versions already committed. Every other commit, file, and
#   message is preserved. Commit SHAs from 536b5f9 onward will change.
#
# THIS REWRITES PUBLISHED HISTORY.
#   Everyone with a clone must re-clone afterward. Read the whole script before
#   running it. It does nothing until you pass --run.
#
# REQUIREMENTS
#   git-filter-repo   https://github.com/newren/git-filter-repo
#                     pip install git-filter-repo
#
set -euo pipefail

OLD_SCORING="c15ffc8753227d28803c6ca449c89f1defe2bfd1"
OLD_QUESTIONNAIRE="48db2ecf5d3152f92ee864d6a279a71c0406befb"
NEEDLE="Benjamin Kennedy"

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

say()  { printf '\n\033[1m%s\033[0m\n' "$*"; }
fail() { printf '\033[31merror:\033[0m %s\n' "$*" >&2; exit 1; }

# ---------------------------------------------------------------------------
say "1. Preflight"

command -v git-filter-repo >/dev/null 2>&1 \
  || fail "git-filter-repo not found. Install with: pip install git-filter-repo"

[[ -z "$(git status --porcelain)" ]] \
  || fail "working tree is dirty. Commit or stash first."

# The cleaned blobs must already be committed — this script reuses them rather
# than regenerating, so the replacement is byte-for-byte what you reviewed.
NEW_SCORING="$(git rev-parse "HEAD:Forms/SCANAQ Scoring Breakdown, Descriptions, and PFC-Inspired Suggestions.pdf")"
NEW_QUESTIONNAIRE="$(git rev-parse "HEAD:Forms/Synthetic Cognitive Augmentation Network Alignment Questionnaire (SCANAQ).pdf")"

for blob in "$NEW_SCORING" "$NEW_QUESTIONNAIRE"; do
  if git cat-file -p "$blob" | strings | grep -qi "$NEEDLE"; then
    fail "replacement blob $blob still contains the name. Re-run the metadata strip first."
  fi
done

echo "  old blobs : ${OLD_SCORING:0:8}  ${OLD_QUESTIONNAIRE:0:8}"
echo "  new blobs : ${NEW_SCORING:0:8}  ${NEW_QUESTIONNAIRE:0:8}  (verified clean)"

BEFORE="$(git log --all -p 2>/dev/null | grep -ci "$NEEDLE" || true)"
echo "  occurrences in history right now: $BEFORE"

if [[ "${1:-}" != "--run" ]]; then
  cat <<EOF

  DRY RUN — nothing has been changed.

  To execute:
      bash scripts/purge-pdf-metadata-from-history.sh --run

  After it completes you must force-push (the script will not do this):
      git push --force-with-lease origin main
      git push --force-with-lease origin claude/codebase-audit-7uqnts

  Then, and this part matters: ask GitHub Support to garbage-collect
  unreachable objects. A force-push alone leaves the old blobs retrievable
  by direct SHA URL, e.g.
      https://github.com/iLevyTate/SCAN-Resources/blob/$OLD_SCORING

  Still outside this repository entirely:
    - Zenodo (10.5281/zenodo.14053202) holds the un-stripped PDFs.
      Records are immutable; publish a new version with the cleaned files.
    - Any paper submission carrying these appendices has the same metadata.
EOF
  exit 0
fi

# ---------------------------------------------------------------------------
say "2. Backup"

BACKUP="../SCAN-Resources-backup-$(git rev-parse --short HEAD)"
[[ -e "$BACKUP" ]] && fail "backup path $BACKUP already exists"
git clone --mirror . "$BACKUP"
echo "  mirror clone written to $BACKUP"
echo "  if anything goes wrong, restore from there."

# ---------------------------------------------------------------------------
say "3. Rewrite"

# Map old blob -> new blob. filter-repo applies this at every commit that
# references them, so the replacement is complete rather than tip-only.
MAPFILE="$(mktemp)"
trap 'rm -f "$MAPFILE"' EXIT
printf '%s==>%s\n' "$OLD_SCORING" "$NEW_SCORING" >> "$MAPFILE"
printf '%s==>%s\n' "$OLD_QUESTIONNAIRE" "$NEW_QUESTIONNAIRE" >> "$MAPFILE"

git filter-repo --force --replace-refs delete-no-add --blob-callback "
import subprocess
mapping = {}
for line in open('$MAPFILE'):
    old, new = line.strip().split('==>')
    mapping[old] = new
if blob.original_id and blob.original_id.decode() in mapping:
    replacement = mapping[blob.original_id.decode()]
    blob.data = subprocess.run(
        ['git', 'cat-file', 'blob', replacement],
        capture_output=True, check=True).stdout
"

# ---------------------------------------------------------------------------
say "4. Verify"

AFTER="$(git log --all -p 2>/dev/null | grep -ci "$NEEDLE" || true)"
echo "  occurrences in history before : $BEFORE"
echo "  occurrences in history after  : $AFTER"

[[ "$AFTER" == "0" ]] || fail "name still present in history — do NOT force-push. Restore from $BACKUP."

for f in Forms/*.pdf; do
  n="$(strings "$f" | grep -ci "$NEEDLE" || true)"
  [[ "$n" == "0" ]] || fail "$f still contains the name"
done
echo "  working tree PDFs clean"

# filter-repo drops the remote as a safety measure; the operator re-adds it
# deliberately as part of deciding to publish the rewrite.
cat <<EOF

  History rewritten and verified.

  git-filter-repo has removed the 'origin' remote by design. Re-add it and
  force-push only when you are ready:

      git remote add origin <your-remote-url>
      git push --force-with-lease origin main
      git push --force-with-lease origin claude/codebase-audit-7uqnts

  Then ask GitHub Support to garbage-collect unreachable objects, and publish
  a new Zenodo version with the cleaned PDFs.
EOF
