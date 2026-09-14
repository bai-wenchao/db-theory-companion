# Round-6 revision plan — 2026-09-14

Master review of the current book (`main.pdf`, 53pp, 11 chapters written
pre-pilot): all 9 existing tool chapters predate the round-3/4/5 conventions
uniformly — audit found 0/9 with `\setcounter{section}{-1}`, objectives,
recap, appendix, or the exemplar anatomy; 0/9 use `\citep`; 1 reachbox each
(prose good, structure missing); no per-chapter `\bibliography` tails. The
pilot (ch0 + ch1 concentration, 26pp) is the approved target
(`CHAPTER-RULES.md` = binding spec).

Goal: all 13 tool chapters at pilot spec, then ch0 refresh + index + v1.0.

## Waves (≤4 agents, quota-gated: `scripts/quota_check.py` before each)

Chapter order = corpus frequency (user round-6 feedback): reductions (50) is
Chapter 1, concentration (38) Chapter 2, … (see ch0 map table).

| Wave | Chapters (book #) | Kind |
|---|---|---|
| 1 | reduction (1), induction (3), estimation-theory (4), adversarial-construction (5) | revise |
| 2 | dp-composition (6), exchange-greedy (7), spectral-matrix (8), amortized-potential (9) | revise |
| 3 | coresets-rnla (10, NEW), information-theory (11, NEW), communication-complexity (12, NEW), online-decisions (13, hand-picked exemplars) | 3 new + 1 revise |

## Per-chapter exemplars (plan.json slices; PODS capped ≤1 per chapter, 2 for communication-complexity)

- **reduction** (50 papers, Ch. 1): 136(PODS), 289, 350, 357, 264, 375
- **induction** (36, Ch. 3): 114(PODS), 371, 307, 153, 233, 290
- **estimation-theory** (27, Ch. 4): 115(PODS), 231, 102, 373, 293, 377
- **adversarial-construction** (21, Ch. 5): 166(PODS), 306, 349, 123, 150, 179
- **dp-composition** (18, Ch. 6): 298, 178(PODS), 337, 263, 073, 214
- **exchange-greedy** (16, Ch. 7): 053(PODS), 200, 031, 009, 224, 229
- **spectral-matrix** (13, Ch. 8): 038(PODS), 303, 235, 190, 101, 265
- **amortized-potential** (11, Ch. 9): 177(PODS), 015, 180, 363, 274, 203
- **coresets-rnla** (8, Ch. 10, NEW; merged coresets-geometry + randomized-nla): 289, 053(PODS), 303, 349, 052, 127
- **information-theory** (5, Ch. 11, NEW): 185(PODS), 079, 231, 279, 237
- **communication-complexity** (4, Ch. 12, NEW): 115(PODS), 243(PODS), 357, 070 — PODS cap = 2 here
- **online-decisions** (4, Ch. 13; plan.json empty → hand-picked): 242 "To Adapt or
  Not to Adapt, That is the Ski Question", 094 "Enumerating Graph Pattern
  Matches with ML Oracles", 221 "SHoCLean: Bridging Soft and Hard
  Constraints for Multivariate Time Series Cleaning", 140 "Interpretable
  Attribute Discretization"

Recurring papers (079, 231, 357, 289, 303, 349, 053 …) are intentional —
each chapter treats them under its own lens (R5).

## Agent protocol (each chapter agent)

Read: `CHAPTER-RULES.md` → `chapters/concentration-ineq.tex` (reference) →
own `chapters/<tool>.tex` (existing) → `digest/<tool>.md` → per-exemplar
notes (`grep -l sigmod26-NNN ../notes/sigmod26/batch_*.md`) →
`../data/sigmod26/theory/<id>.md` only when a statement must be transcribed
precisely. Write the revised chapter + ensure every `\citep` key resolves in
`chapters/<tool>-all.bib` (corpus keys verbatim from `refs.bib`; classic
bg keys from `chapters/<tool>.bib`). New chapters: create the file (replace
the stub) + create `<tool>-all.bib` + `<tool>.bib` (bg refs). Reply ≤5 lines.
New-chapter agents additionally read `plan.json`'s slice for usage/quotes.

## Master, after each wave

1. Acceptance greps (CHAPTER-RULES.md checklist) on each revised chapter.
2. `./build.sh main` (full book) — byte-stable, 0 errors; spot-vision any
   suspicious page (`pdftotext -bbox` first).
3. Commit per chapter: `feat(chapters): revise <tool> chapter to pilot spec`.

## Post-rollout (master, last)

1. ch0 refresh: map-table Papers/Ex. counts against final chapters; §0.7
   prose; verify 13-row table matches the built book (ch0 is finalized LAST,
   per standing spec).
2. Script-generated Index part (backmatter).
3. Version bump → `\bookversion{1.0}` / status "First complete edition";
   final `./build.sh main`; commit `feat(book): complete 13-chapter first edition`.
4. Update CLAUDE.md runbook + memory; CHECKPOINT.md updated each wave.
