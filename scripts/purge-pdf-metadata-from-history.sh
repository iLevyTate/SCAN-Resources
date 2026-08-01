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
# REQUIREMENTS (only for --run; the dry run needs neither)
#   git-filter-repo   https://github.com/newren/git-filter-repo
#                     pip install git-filter-repo
#
set -euo pipefail

OLD_SCORING="c15ffc8753227d28803c6ca449c89f1defe2bfd1"
OLD_QUESTIONNAIRE="48db2ecf5d3152f92ee864d6a279a71c0406befb"

# The search term is reconstructed from fragments rather than written out, so
# this file is not itself a plaintext copy of the name it exists to erase —
# and so the verification below cannot match its own source (an earlier version
# grepped `git log -p` for a literal name and matched this very line).
NEEDLE="$(printf '%s%s %s%s' 'Benj' 'amin' 'Ken' 'nedy')"

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

say()  { printf '\n\033[1m%s\033[0m\n' "$*"; }
fail() { printf '\033[31merror:\033[0m %s\n' "$*" >&2; exit 1; }

# Print the SHA of every *reachable* blob whose raw bytes contain the needle.
# Unlike `git log -p | grep`, this reads blob content directly, so it sees
# binary files (PDFs) — `git log` only prints "Binary files … differ" for them.
blobs_with_name() {
  git rev-list --objects --all 2>/dev/null \
    | awk '{print $1}' \
    | git cat-file --batch-check='%(objecttype) %(objectname)' 2>/dev/null \
    | awk '$1 == "blob" { print $2 }' \
    | sort -u \
    | while read -r sha; do
        # grep -c (not -q): -q exits on first match and SIGPIPEs the upstream
        # cat-file, which `set -o pipefail` turns into a non-zero pipeline, so
        # a match would be silently dropped for larger (binary) blobs. Counting
        # forces grep to consume all input, so no early exit and no SIGPIPE.
        if [ "$(git cat-file blob "$sha" 2>/dev/null | strings | grep -ci "$NEEDLE" || true)" -gt 0 ]; then
          printf '%s\n' "$sha"
        fi
      done
}

# Is a given blob SHA reachable from any ref?
blob_reachable() {
  git rev-list --objects --all 2>/dev/null | awk '{print $1}' | grep -qx "$1"
}

# ---------------------------------------------------------------------------
say "1. Survey (read-only)"

# Resolve the cleaned replacement blobs. This works without git-filter-repo and
# without a clean tree, so the dry run below needs neither.
NEW_SCORING="$(git rev-parse "HEAD:Forms/SCANAQ Scoring Breakdown, Descriptions, and PFC-Inspired Suggestions.pdf")"
NEW_QUESTIONNAIRE="$(git rev-parse "HEAD:Forms/Synthetic Cognitive Augmentation Network Alignment Questionnaire (SCANAQ).pdf")"

for blob in "$NEW_SCORING" "$NEW_QUESTIONNAIRE"; do
  if [ "$(git cat-file -p "$blob" | strings | grep -ci "$NEEDLE" || true)" -gt 0 ]; then
    fail "replacement blob ${blob:0:8} still contains the name. Re-run the metadata strip first."
  fi
done

echo "  old blobs : ${OLD_SCORING:0:8}  ${OLD_QUESTIONNAIRE:0:8}"
echo "  new blobs : ${NEW_SCORING:0:8}  ${NEW_QUESTIONNAIRE:0:8}  (verified clean)"

mapfile -t BEFORE_BLOBS < <(blobs_with_name)
echo "  reachable blobs still carrying the name: ${#BEFORE_BLOBS[@]}"
for sha in "${BEFORE_BLOBS[@]:-}"; do
  [[ -n "$sha" ]] && echo "    - ${sha:0:12}"
done

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
say "2. Preflight (--run only)"

command -v git-filter-repo >/dev/null 2>&1 \
  || fail "git-filter-repo not found. Install with: pip install git-filter-repo"

[[ -z "$(git status --porcelain)" ]] \
  || fail "working tree is dirty. Commit or stash first."

# ---------------------------------------------------------------------------
say "3. Backup"

BACKUP="../SCAN-Resources-backup-$(git rev-parse --short HEAD)"
[[ -e "$BACKUP" ]] && fail "backup path $BACKUP already exists"
git clone --mirror . "$BACKUP"
echo "  mirror clone written to $BACKUP"
echo "  if anything goes wrong, restore from there."

# ---------------------------------------------------------------------------
say "4. Rewrite"

# Map old blob -> new blob. filter-repo applies this at every commit that
# references them, so the replacement is complete rather than tip-only.
MAPFILE="$(mktemp)"
trap 'rm -f "$MAPFILE"' EXIT
printf '%s==>%s\n' "$OLD_SCORING" "$NEW_SCORING" >> "$MAPFILE"
printf '%s==>%s\n' "$OLD_QUESTIONNAIRE" "$NEW_QUESTIONNAIRE" >> "$MAPFILE"

# The needle is passed through the environment, never written into the callback
# source, so this rewrite step is not itself a plaintext copy of the name.
PURGE_NEEDLE="$NEEDLE" git filter-repo --force --replace-refs delete-no-add --blob-callback "
import os, subprocess
mapping = {}
for line in open('$MAPFILE'):
    old, new = line.strip().split('==>')
    mapping[old] = new
oid = blob.original_id
oid = oid.decode() if isinstance(oid, bytes) else oid
if oid in mapping:
    # The two appendix PDFs: swap in the fully cleaned blobs (XMP stream and
    # ContentTypeId removed, not just the name string).
    blob.data = subprocess.run(
        ['git', 'cat-file', 'blob', mapping[oid]],
        capture_output=True, check=True).stdout
else:
    # Any other blob that happens to carry the name in text — e.g. an earlier
    # committed version of this very script — has it redacted in place. Without
    # this the two-PDF map would leave those blobs behind and the verify step
    # below would (correctly) refuse to declare success.
    needle = os.environ['PURGE_NEEDLE'].encode()
    if needle in blob.data:
        blob.data = blob.data.replace(needle, b'Levy Tate')
"

# ---------------------------------------------------------------------------
say "5. Verify"

# Two independent checks, neither relying on `git log -p` (which cannot see
# binary blobs) or on a literal name (which would match this script's source).

# (a) The two known old blobs must no longer be reachable from any ref.
for sha in "$OLD_SCORING" "$OLD_QUESTIONNAIRE"; do
  if blob_reachable "$sha"; then
    fail "old blob ${sha:0:12} is still reachable — do NOT force-push. Restore from $BACKUP."
  fi
done
echo "  both original blobs unreachable"

# (b) No reachable blob anywhere in history still contains the name.
mapfile -t AFTER_BLOBS < <(blobs_with_name)
echo "  reachable blobs carrying the name — before: ${#BEFORE_BLOBS[@]}  after: ${#AFTER_BLOBS[@]}"
if [[ "${#AFTER_BLOBS[@]}" -ne 0 ]]; then
  for sha in "${AFTER_BLOBS[@]}"; do echo "    still present: ${sha:0:12}"; done
  fail "name still present in history — do NOT force-push. Restore from $BACKUP."
fi

# (c) Working-tree PDFs clean (nullglob so a rename can't make the loop vacuous).
shopt -s nullglob
pdfs=(Forms/*.pdf)
[[ "${#pdfs[@]}" -ge 2 ]] || fail "expected the two appendix PDFs in Forms/, found ${#pdfs[@]}"
for f in "${pdfs[@]}"; do
  if [ "$(strings "$f" | grep -ci "$NEEDLE" || true)" -gt 0 ]; then
    fail "$f still contains the name"
  fi
done
echo "  working tree PDFs clean (${#pdfs[@]} checked)"

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
