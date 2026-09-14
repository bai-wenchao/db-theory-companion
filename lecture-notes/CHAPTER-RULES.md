# Chapter-writing rules — lecture notes (binding for every chapter)

Distilled from the pilot rounds 1–5 (user feedback, 2026-09-13/14). The
reference implementation is `chapters/concentration-ineq.tex`; `main.tex` is
the canonical preamble. When this file and an old chapter disagree, this file
wins. Numbered rules (R1…) are referenced by the revision plan and by
chapter-agent prompts.

## R1. Numbering: chapters AND sections start at 0

- Chapters number from 0 (Introduction = Chapter 0) via
  `\setcounter{chapter}{-1}` after `\tableofcontents` in `main.tex`.
- Sections number from x.0 inside EVERY chapter: **x.0 introduces the tool;
  exemplars start at x.1.** Every chapter file therefore opens with the
  two-line convention
  ```latex
  \chapter{Title Case Title}
  \setcounter{section}{-1}   % sections start at <x>.0 (see main.tex comment)
  ```
  There is NO safe global hook for this (hyperref's `\@chapter` is
  parameterless and forwards to `\Hy@org@chapter`, defined only at
  `\begin{document}`) — the explicit `\setcounter` is mandatory.
- The appendix is the LAST NUMBERED section of the chapter
  (`\section{Appendix}`, i.e. x.5 in a five-section chapter).

## R2. Chapter skeleton (exact order)

1. Two-line opener (R1) + `\label{ch:<short>}`.
2. `\begin{objectives}…\end{objectives}` — 3–4 SHORT bullets (margin column
   is narrow): what to recognize, what to prove/match, what to tune.
3. Two-paragraph chapter overview: what the tool is for in plain words, and
   the corpus count (papers tagged, flagship pairings). End with one
   sentence pointing at the advanced section.
4. §x.0 "The tool: <name>" — the formal core:
   - the uniform problem class in prose, then the ladder/taxonomy of the
     tool's variants as numbered theorem-environment statements
     (Markov→Chebyshev→… style), each with a proof or proof-sketch;
   - at most ONE TikZ/pgfplots figure, only if it genuinely helps;
   - a `remarkbox` for notation conventions when needed;
   - a "how to choose <variant>" subsection (mechanical selection procedure);
   - a `reachbox` "When to Reach for <tool>" with the numbered recipe
     (name the object, check structure, tune δ, union-bound).
5. Exemplar sections x.1, x.2, … — one real corpus paper each, anatomy per
   R4. 3–4 basic exemplars before the advanced section.
6. § "Advanced usage and further reading" — harder variants as subsections,
   1–2 advanced exemplars sketched in one `\paragraph` each, then a short
   further-reading itemize (textbooks + originals + a refresher).
7. `\begin{recap}…\end{recap}` — the "Chapter Recap" bullets (what the tool
   is / which variant when / why it works / what the corpus showed /
   advanced pointers). Recap comes BEFORE the appendix.
8. `\section{Appendix}` + ONE sentence: "Proofs omitted from the main text
   are collected here." (No convention meta.) Then one
   `\subsubsection*{Proof of Theorem~\ref{…} (short name)}` per deferred
   proof: italic "Statement (recalled)." + `\eop`, then the full proof.
   Appendix titles MUST fit ONE line (≤ ~52 chars) — no stretched two-line
   headings (kernel headings justify; `\raggedright` helps but titles that
   wrap still look bad).
9. Tail:
   ```latex
   \bibliographystyle{plainnat}
   \bibliography{chapters/<tool>-all}
   ```

## R3. Boxes: exactly three semantics

- `remarkbox` (slate) — low-salience asides, notation.
- `reachbox` (teal) — practitioner guidance, "when to reach" + recipe.
- `recap` (ocre) — chapter-end summary, bare `\item` bullets.
- Theorems/lemmas/corollaries/propositions/definitions use the `ocrenumbox`
  numbered style (shared per-chapter counter, "Theorem 2.1" numbering).
- NO `algorithmblock` / algorithm-box theme. Pseudocode, when needed, is a
  numbered list inside a `reachbox`. Learning objectives live in the margin
  (`objectives` env), never in the text flow.

## R4. Exemplar section anatomy (every exemplar, in this order)

1. **Lead paragraph** (no heading): plain-language background written from
   the paper's abstract — venue + marker, what problem the paper attacks in
   ordinary words, why it matters, headline results. 5–8 sentences,
   reader-friendly; formalism only where unavoidable. NO curation meta
   ("kept because it is the cleanest exhibit" is forbidden — round-4 rule).
2. `\paragraph{Problem.}` — the formal model/setup.
3. `\paragraph{Guarantee.}` — the paper's key statement in a theorem env,
   transcribed with cleaned notation and sourced ("Theorem 4 of the
   paper"). Ends with `\eop` (text) or `\eopm` inside a display.
4. `\paragraph{How <tool> is applied.}` — name the random object/induction
   variable/reduction, the structure, the rung/variant used, the δ-tuning;
   include the workhorse lemma + proof sketch, full proof → appendix.
5. `\paragraph{What it buys.}` — the systems payoff in 2–4 sentences.

## R5. Citations and markers

- `\citep` EVERYWHERE (never `\cite` — even though main.tex aliases it).
- PODS-issue exemplars: append `\pods` after the citation (e.g.
  `\citep{sigmod26-175}\pods`). At most ONE PODS exemplar per chapter
  (TWO for communication complexity, whose corpus presence is small).
- A paper may recur in a second chapter when it is a clean exhibit of two
  tools; each chapter treats it under its own lens.
- Chapter-map/ch0 prose never cites internal `sigmod26-NNN` IDs (round-5
  rule); exemplar papers are findable via each chapter's reference list.

## R6. Floats, math, markers

- Wide floats use `widefigure`/`widetable` (kernel float + tufte fullwidth;
  parity-correct). Regular floats stay in the text column. Captions small,
  `labelsep=colon`.
- End-of-statement marker: `\eopm` = `\tag*{\rule{1.1ex}{1.1ex}}` INSIDE
  displays (flush right — never `\qquad\mbox{}`); `\eop` after text
  statements. Proof env keeps the redefined solid-square `\qedsymbol`.
- Sidenotes for asides; footnotes sparingly. `\sidenote` rebinds `\cite`
  safely (main.tex aliases both tufte variants to `\citep`).

## R7. Writing quality (round-5 emphasis)

- Basic first, then advanced: 3–4 basic exemplars before the advanced
  section; the ladder before the exotica.
- Plain language before formalism; explain what the problem is and why it
  matters as the paper's abstract would to a practitioner.
- Self-contained sections: a reader entering at x.2 needs no x.1.
- Transcribe statements from the papers (machine-extracted), paraphrasing
  conservatively where extraction was noisy; source every transcribed
  statement ("Lemma 4.4 of the paper, notation cleaned").

## R8. Bibliography

- Per-chapter lists: `\bibliographystyle{plainnat}` +
  `\bibliography{chapters/<tool>-all}` (renders as a `References` section
  inside the chapter — main.tex's `\bibsection`).
- `<tool>-all.bib` = corpus `sigmod26-NNN` entries the chapter cites
  (copy verbatim from `refs.bib`) + classic background refs
  (`<tool>-bgN` keys, reuse `chapters/<tool>.bib` entries where good).
- Before finishing: every `\citep` key must resolve in `<tool>-all.bib`.

## R9. Build and verification (master-run; agents build nothing)

- `./build.sh pilot` regenerates `main-pilot.tex` (ch0 + concentration
  only) and builds it; `./build.sh main` builds the full book.
- **Byte-stable rule**: after wiping aux, run pdflatex until the PDF is
  byte-identical twice in a row (≥4 runs). tufte's `\titlecontents` wraps
  every ToC entry in `fullwidth` = `adjustwidth*` (changepage), which
  resolves page parity from aux data written by the PREVIOUS run — three
  runs leave ToC entries shifted exactly one overhang (167.4pt) off the
  left paper edge.
- Visual check loop: `pdftoppm -r 110 -png -f N -l N <pdf> /tmp/p` → Read
  PNG → `analyze_image`. `pdftotext -f N -l N -bbox` is geometric ground
  truth and beats vision judgment. Known vision false alarms: floats that
  moved to the next page (normal `[htbp]`), the `\pods` superscript
  reading as a malformed citation.

## R10. Versioning and git

- Version page (verso of title): `\bookversion`, `\bookstatus`,
  `\buildstamp` (written by `build.sh`; `\today` fallback). Bump
  `\bookversion` at milestones (0.x during rollout; 1.0 when all 13
  chapters + index are done).
- Conventional commits (https://www.conventionalcommits.org/v1.0.0):
  `feat(chapters): …`, `docs(lecture-notes): …`, `fix(build): …`, …
  Commit messages end with `Co-Authored-By: Claude Code <noreply@anthropic.com>`.

## Acceptance checklist (master, per chapter)

```
grep -c '\\setcounter{section}{-1}'  == 1        # R1
grep -c 'begin{objectives}'          == 1        # R2
grep -c 'begin{recap}'               == 1        # R2 (before Appendix)
grep -c 'begin{reachbox}'            >= 1        # R2
grep -c 'begin{algorithmblock}'      == 0        # R3
grep -c '\\cite{'                    == 0        # R5 (must be \citep)
grep -c 'paragraph{Problem'          >= 3        # R4 anatomy
grep -c 'section{Appendix}'          == 1        # R2
tail: \bibliographystyle{plainnat} + \bibliography{chapters/<tool>-all}
appendix \subsubsection* titles ≤ 1 line         # R2.8
```
