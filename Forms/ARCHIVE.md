# Archived Appendices

The two PDFs in this directory are **Appendix A** and **Appendix B** of the published paper. They
are the record of what reviewers saw and what the Zenodo DOI archived.

| File | Appendix | Corresponds to |
|---|---|---|
| `Synthetic Cognitive Augmentation Network Alignment Questionnaire (SCANAQ).pdf` | A | Instrument 1.0.0 |
| `SCANAQ Scoring Breakdown, Descriptions, and PFC-Inspired Suggestions.pdf` | B | Scoring model **1.0.0** |

Both were added in commit `536b5f9` (2025-07-31).

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

> Note that the copies archived on Zenodo, and the blobs in commit `536b5f9`, still carry the
> original metadata. Removing it there requires publishing a new Zenodo version and rewriting git
> history respectively.

## If replacement appendices are needed

Do **not** regenerate these files in place. Publish new ones under new filenames
(`Appendix-A-SCANAQ-v2.0.pdf`, `Appendix-B-Scoring-v2.0.pdf`) from appendix-scoped sources, and
leave the originals as the archived record. Silently replacing a published appendix makes this
repository disagree with the literature that cites it.

## Corrected Appendix B (2.0.0)

`Appendix-B-Scoring-v2.0.md` is a corrected, publication-ready Appendix B built from
`SCANAQ Numerical Scoring Breakdown.md`. It exists as a new file, per the rule above — the original
1.0.0 PDF is left untouched as the archived record. A corrigendum request the author can send to the
publisher accompanies it at `../Corrections/corrigendum-appendix-B.md`. Appendix A is **not** yet
replaced: it reproduces third-party instrument items whose reuse terms have to be settled first (see
`../PROVENANCE.md` and `../NOTICE.md`).
