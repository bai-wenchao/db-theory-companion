# CHECKPOINT — 2026-09-14 14:2x (round-5 pilot DONE + verified; awaiting user confirmation)

Weekly 26% > soft 25.6% (frozen cap until 15:00 9/14). Master idles; no
subagent launches until headroom returns AND user confirms pilot.

## State
- **Pilot round-5 feedback: ALL 3 items done, rebuilt, verified (vision + bbox)**
  — `lecture-notes/pilot-chapter2.pdf` (26pp, 362,479 bytes, 0 errors,
  same 2 pre-existing overfulls):
  1. **Sections from 0**: every `\chapter{...}` is followed by
     `\setcounter{section}{-1}` (convention documented in main.tex lines
     92–100). x.0 = tool intro, exemplars from x.1. ToC verified: ch0 =
     0.0–0.8; ch1 = 1.0 "The tool: …" (1.0.1, 1.0.2), 1.1 Trimmed,
     1.2 MaxRS, 1.3 S4S, 1.4 Advanced (1.4.1–1.4.3), 1.5 Appendix.
     There is NO safe global hook (hyperref `\@chapter` is parameterless,
     forwards to `\Hy@org@chapter` defined only at `\begin{document}`) —
     per-chapter `\setcounter` is REQUIRED at rollout.
  2. **Richer exemplar leads**: all 5 exemplar intros (§1.1–1.3 + the two
     in 1.4.2) rewritten as fuller plain-language background paragraphs
     sourced from the papers' abstracts — venue, what problem the paper
     attacks, headline results, in reader-friendly wording — before
     `\paragraph{Problem.}`.
  3. **Map table de-ID'd**: Table 1 now 4 columns (Ch. / Tool / Papers /
     Ex.), star-exemplar ID column REMOVED; §0.7 prose no longer cites
     sigmod26-IDs. Verified: no "sigmod26-" strings on the table page.
- **BUILD RULE (new, from the ToC regression)**: tufte's `\titlecontents`
  wraps EVERY ToC entry in `fullwidth` = `adjustwidth*` (changepage),
  which resolves page parity from aux data written by the PREVIOUS run.
  After `rm -f main-pilot.{aux,toc,out}`, **3 pdflatex runs are NOT
  enough**: most ToC entries land 167.4pt left of the text edge (off
  paper). FIX = run pdflatex until the PDF is **byte-stable (≥4 runs)**.
  The stable build is clean (only chapter numbers "0"/"1" left of the
  text edge, as tufte intends).
- Build: `cd lecture-notes && rm -f main-pilot.{aux,toc,out} &&
  pdflatex -interaction=nonstopmode main-pilot.tex &&
  bibtex chapters/concentration-ineq && pdflatex ×3+ (until byte-stable)`.
- Visual check loop: `pdftoppm -r 110 -png -f N -l N main-pilot.pdf /tmp/rX`
  → Read PNG → CDN URL → `mcp__4_5v_mcp__analyze_image` (signatures
  per-URL; 400 = stale, re-Read for a fresh one). Prefer
  `pdftotext -f N -l N -bbox` for spacing/alignment questions — geometric
  ground truth beats vision judgment (vision false alarms this round:
  "table missing" = it floated to the next page; "[8]PODS" = the intended
  `\pods` superscript).

## Resume (in order)
1. User confirms pilot-chapter2.pdf → then rollout (quota permitting, after
   15:00 9/14).
2. Rollout = rewrite 12 remaining chapters to pilot spec (structure per
   concentration-ineq.tex: two-line opener `\chapter{...}` +
   `\setcounter{section}{-1}` → margin objectives → tool-intro (x.0) w/
   ladder + proofs + bg refs → self-contained exemplar sections from x.1
   with abstract-sourced plain-language lead paragraphs → "Advanced usage
   and further reading" → recap → Appendix w/ short single-line
   "Proof of Theorem N" subsubsections + \eop/\eopm → per-chapter
   `\bibliography{chapters/<tool>-all}`). Waves ≤4, `quota_check.py`
   before EVERY launch (exit 3 = stop + this checkpoint).
3. Round-3/4/5 rules to PROPAGATE at rollout: exactly 3 box semantics (NO
   algorithmblock); recap BEFORE appendix; `\citep` everywhere;
   widefigure/widetable for wide floats; `\eopm` via `\tag*` (never
   `\qquad\mbox`); appendix titles single-line ≤~52 chars; exemplar leads
   = venue + what-it-does + abstract-sourced plain-language background,
   no curation meta; appendix intro one sentence; **sections number from
   x.0 via per-chapter `\setcounter{section}{-1}`**; **build until
   byte-stable (≥4 pdflatex runs after rm aux)**.
4. Known gaps at rollout: plan.json `online-decisions` exemplars EMPTY
   (hand-pick 242/094/221/140 per ch0 table or relax dedup); 3 new chapters
   (information-theory, communication-complexity, coresets-rnla) need
   `-all.bib` + includes; main.tex → 13-chapter include order.
5. After chapters: script-generated Index part, final ch0 refresh, update
   CLAUDE.md runbook + memory.
