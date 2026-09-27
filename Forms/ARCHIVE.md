# Archived Appendices

One PDF remains in this directory: **Appendix B** of the published paper, the record of what
reviewers saw and what the Zenodo DOI archived.

| File | Appendix | Corresponds to | Status |
|---|---|---|---|
| `Synthetic Cognitive Augmentation Network Alignment Questionnaire (SCANAQ).pdf` | A | Instrument 1.0.0 | Removed from the tree 2026-09-27 (see below) |
| `SCANAQ Scoring Breakdown, Descriptions, and PFC-Inspired Suggestions.pdf` | B | Scoring model **1.0.0** | Retained |

Both were added in commit `536b5f9` (2025-07-31).

## Appendix A removed from the tree, 2026-09-27

The Appendix A PDF was deleted from the working tree in the commit that added this section. Its
Section A tracks the BRIEF-A closely, and PAR Inc., the BRIEF-A's publisher, does not grant
permission to reproduce its items in any publication (`../PROVENANCE.md`, *Reuse terms, verified
2026-09-16*). Every release cut from this repository was redistributing that text. The 2.1.0
questionnaire markdown carries the replacement Section A wording and contains no BRIEF-A item.

The archived record is not lost. The file is unchanged in git history through commit `291a991`,
and the 1.1.0 Zenodo version ([10.5281/zenodo.16711302](https://doi.org/10.5281/zenodo.16711302))
holds the copy that the published chapter's citation resolves to. Zenodo versions cannot be edited,
so that copy stays as published. Anyone who needs the printed Appendix A should use the chapter
itself (DOI 10.4018/979-8-3373-5702-7.ch005) or the Zenodo 1.1.0 files.

## The markdown is authoritative

**Appendix B documents scoring model 1.0.0, which produced incorrect profiles in four of eight
sections.** It is retained as the published record, not as guidance. Do not score responses with it.

`SCANAQ Numerical Scoring Breakdown.md` (scoring model 2.0.0) supersedes it. See that file's
Appendix 2 for the full list of corrections, and `CHANGELOG.md` for the effect on previously scored
data.

## Known divergences from the current markdown

These are preserved deliberately — the appendices reflect what was published:

- **Scoring model.** Appendix B carries the model 1.0.0 bands and profile codes (`1A`–`8B`),
  including the inverted Executive Functioning and Impulsivity polarity, the conflated Emotion
  Regulation total, and the un-reverse-keyed Q32 and Q35.
- **Naming.** Appendix B prints "Executive Function"; Appendix A, the README, and the current
  markdown all use "Executive Functioning". Normalization stops at the archive boundary.
- **Appendix A is not a render of the questionnaire markdown.** It is a response-entry form with
  per-section rating-scale tables and condensed completion notes, and omits roughly 90 lines of the
  markdown (About, Privacy, Implementer notes, Next Steps, Note to Users). The 36 items and all
  response-scale anchors are identical in both — verified item by item.
- **Appendix B's suggestion text is richer than model 1.0.0's markdown was.** That wording has been
  carried forward into scoring model 2.0.0 rather than discarded.

## Metadata

Both files were rewritten in commit `291a991` to remove identifying metadata: the `/Author` field
and XMP `dc:creator` (which carried the author's legal name rather than the publication pseudonym),
a SharePoint `/ContentTypeId` GUID, and authoring-toolchain strings.

Page content is untouched — extracted text is byte-identical to the originals (4,386 and 5,460
characters). Only the metadata streams changed.

> The copies archived on Zenodo, and the blobs in commit `536b5f9`, still carry the original
> metadata. A history-rewrite script was prepared for the 2.0.0 release and dry-run only. On
> 2026-09-27 the decision was taken not to run it, and the script was removed: the Zenodo 1.1.0
> copies cannot be edited, so a rewrite would leave the metadata reachable anyway, and the author's
> correction correspondence with both publishers is already conducted under the legal name. Rewriting
> published history would force every clone holder to re-clone for no gain in privacy.

## If replacement appendices are needed

Do **not** regenerate these files in place. Publish new ones under new filenames
(`Appendix-A-SCANAQ-v2.0.pdf`, `Appendix-B-Scoring-v2.0.pdf`) from appendix-scoped sources, and
leave the originals as the archived record. Silently replacing a published appendix makes this
repository disagree with the literature that cites it.

## Corrected Appendix B (2.0.0)

`Appendix-B-Scoring-v2.0.md` is a corrected, publication-ready Appendix B built from
`SCANAQ Numerical Scoring Breakdown.md`. It exists as a new file, per the rule above — the original
1.0.0 PDF is left untouched as the archived record. A corrigendum request the author can send to the
publisher accompanies it at `../Corrections/corrigendum-appendix-B.md`. Appendix A's replacement is
the Section A wording in instrument 2.1.0, which the author has asked IGI Global to substitute into
the published chapter (see `../PROVENANCE.md` and `../NOTICE.md`).
