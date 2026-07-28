# Corrigendum request — Appendix B scoring model

> **Draft for the author to send.** Fill the bracketed fields, attach `Appendix-B-Scoring-v2.0.md`
> (or a PDF rendering of it), and send to the volume editors / publisher's production contact.
> Nothing here is submitted automatically.

---

**To:** [Volume editor(s) / Publisher production contact]
**From:** L. Tate
**Date:** [date]
**Re:** Corrigendum — Appendix B of "Aligned Minds, Efficient Machines: Integrating Neuromorphic
Computing for Personalized AI" [volume / chapter number / DOI]

Dear [Editor],

I am writing to request a corrigendum for the chapter cited above. After publication I identified
errors in **Appendix B (the SCANAQ scoring breakdown)**. They affect how questionnaire responses are
turned into profiles; they do **not** affect the body of the chapter, its claims, its figures, or
**Appendix A** (the questionnaire instrument itself — item text, item counts, and response scales are
unchanged and correct).

I have prepared a corrected Appendix B, attached. I would be grateful if it could be issued as a
corrigendum and, where the publication format allows, substituted for the original appendix in the
online version.

## What is wrong, and why it matters

Appendix B specifies how each section is scored and labelled. In four of the eight sections the
specification is incorrect, such that a reader following it would assign profiles that are backwards
or undefined:

1. **Section A (Executive Functioning) — inverted interpretation.** All eight items are worded as
   difficulties on a 1 = Never / 3 = Often scale, so the lowest total (8) reflects the *fewest*
   difficulties. The published table labels the low range (8–13) as "Difficulty initiating and
   planning tasks" and the high range (14–24) as "Strong working memory" — the reverse of the items'
   direction.

2. **Section C (Impulsivity) — inverted interpretation.** The same error: the minimum score range
   (6–12) is labelled "High Motor Impulsivity… Acts impulsively," although 6 is the least impulsive
   score attainable.

3. **Section B (Emotion Regulation) — two constructs summed into one.** Cognitive reappraisal
   (Q9–Q10) and expressive suppression (Q11–Q12) are distinct strategies, but the published table
   sums them into a single total and reads a two-dimensional label from it. As a result two of the
   four profiles are unreachable, and opposite response patterns receive the same label — for
   example, maximum reappraisal with minimum suppression (14 + 2 = 16) and its exact opposite
   (2 + 14 = 16) both total 16 and both map to "Low Reappraisal, High Suppression." The corrected
   version scores the two strategies separately.

4. **Section E (Decision-Making Style) — undefined for tied responses.** The rule selects "the single
   highest-scoring item" among Q22–Q26, but specifies nothing for ties. Of the 3,125 possible
   response patterns, 43.4% contain a tie for the maximum and are therefore undefined. The corrected
   version adds a co-dominant-style rule and an all-equal case.

Two further sections produce **incorrect totals** (though the band labels were unaffected in the
published version):

5. **Sections G (Perceived Stress) and H (Empathy) — reverse-keyed items summed raw.** Q32 ("…things
   were going your way") and Q35 ("difficult to see things from the other person's point of view")
   are worded opposite to their sections' direction and must be transformed (`6 − raw`) before
   summing. The published Global Note ("scores are summed within each section") shows they were
   summed raw, shifting those section totals by up to 4 points.

The corrected Appendix B also removes an unsupported description in Section H (the published text
refers to "personal distress," which no item measures), separates the Fantasy item (Q36) from the
empathy total, and adds an explicit missing-data rule. A complete list is in the *Summary of
corrections* at the end of the attached file.

## Effect on results already produced

Any profile generated with the published Appendix B should be **recomputed from the raw item
responses** using the corrected scoring. The old profile codes cannot be mechanically converted,
because in the affected sections the underlying subscale values were never computed. Where only a
profile code was retained (without the raw responses), it cannot be migrated.

## Authoritative version and a minor citation fix

The corrected scoring model is maintained openly in the SCAN-Resources repository, archived on Zenodo
under concept DOI [10.5281/zenodo.14053202](https://doi.org/10.5281/zenodo.14053202), with a full
changelog of the corrections. The attached appendix is a publication-ready extract of it.

While preparing this request I also noticed that the reference-list entry for the SCAN-Resources
deposit (Tate, 2024c) gives a **truncated DOI** — `10.5281/zenodo.140532` — which does not resolve.
The correct DOI is **10.5281/zenodo.14053202**. If the corrigendum can also correct that link, I
would appreciate it.

Please let me know what you need from me to proceed, and whether there is a preferred format for the
replacement appendix.

Thank you for your help.

Kind regards,
L. Tate

---

**Attachment:** `Appendix-B-Scoring-v2.0.md` — corrected Appendix B (render to PDF if the publisher
requires it; the file carries no author metadata).
