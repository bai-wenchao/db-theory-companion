# CAVEATS — internal survey-quality log (NOT part of the book)

Removed from `chapters/ch0.tex` §"Caveats" on 2026-09-14 per user decision
("log it locally for re-check; do not expose it to readers").
Re-check these bias notes before any public release / venue claim.

1. **Source asymmetry.** The corpus mixes 137 arXiv-TeX extractions with 248
   camera-ready PDF extractions; the PDF path is noisier (pdftotext unicode
   mangling, table fragments). Aggregate counts treat both equally.
2. **arXiv theory-density bias.** The arXiv cohort is measurably theory-denser
   (1.7x extraction score), so depth-oriented shares (tightness, lower bounds,
   proofs-per-paper) carry an upward bias from the arXiv fraction.
3. **PODS contamination of the arXiv bias.** Roughly a third of the apparent
   arXiv theory-friendliness was PODS-issue contamination (DOI band
   10.1145/3801890–3801919 = PACMMOD Vol 4 No 2) — hence the \pods markers in
   the book and the PODS carve-out in the addendum report.
4. **Fixed vocabulary.** Tags come from the controlled taxonomy in
   ../CLAUDE.md; long-tail techniques (branching recurrences, min–plus algebras,
   GPU work–span analysis) appear only as free-text tags and enter chapters
   solely when a featured exemplar uses them.

Cross-references: report/sigmod26_survey_addendum.md (PODS carve-out analysis),
index/sigmod26_tags.md (all aggregates). Bias-aware statements to keep in the
book: the PODS markers + the one-line note in §1.1 (extraction provenance).
