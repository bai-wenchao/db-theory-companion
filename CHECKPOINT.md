# CHECKPOINT — 2026-09-15 (typography fixes done; wave 2a in flight)

## TEMPORARY quota rule (user-granted, 9/15 ONLY)
User authorized raising today's stop bar to **80% of the weekly quota**.
`scripts/quota_check.py` is UNMODIFIED (still reports the normal day-bound;
its STOP verdict is overridden in-session today only). Original governor
applies on every other day without exception. Snapshot at wave launch:
weekly 49%, 5h-window 1% → ~31pt headroom under the temporary bar.
Cron 14:53 gate-check deleted (gate open).

## Typography fixes (user round-7 report) — DONE, vision-verified, committed
- `849e3b3` \eop parfillskip leak: the ungrouped `\parfillskip=0pt` in \eop
  leaked globally from Ch.1's first text-mode \eop → every later paragraph's
  last line justified full-width, chapter titles stretched. Fixed by grouping
  `{\parfillskip=0pt\finalhyphendemerits=0\par}`. Verified pp.33/35/69.
- `3759316` wrapped headings justified: titlesec [hang]/[display] titles are
  justified paragraphs → re-asserted tufte's \titleformat for
  chapter/section/subsection with \raggedright in the before-body arg
  (same rationale as the subsubsection re-arm). Verified p.69 §4.3.2.
- Book builds clean: 123pp, 0 errors, 18 overfulls.

## Wave 2a IN FLIGHT (4 agents, launched 9/15 after the two fix commits)
estimation-theory Ch.4 (RELAUNCHED fresh — the killed wave-1 agent did not
survive session compaction, SendMessage resume impossible): 115(PODS),231,
102,373 full; 293,377 sketches. dp-composition Ch.6: 298,178(PODS),337,263
full; 073,214 sketches. exchange-greedy Ch.7: 053(PODS),200,031,009 full;
224,229 sketches. spectral-matrix Ch.8: 038(PODS),303,235,190 full; 101,265
sketches. Agent protocol: read CHAPTER-RULES.md + concentration-ineq.tex
reference + digest/<tool>.md (theory/<id>.md only if digests insufficient),
full rewrite 750–850 lines, no build, reply ≤5 lines.

## Queue after 2a (backfill as agents land; fresh quota check before EACH launch)
1. amortized-potential Ch.9: 177(PODS),015,180,363 full; 274,203 sketches.
2. Wave 3 (NEW chapters — replace stub files, ensure <tool>.bib bg refs):
   coresets-rnla Ch.10: 289,053(PODS),303,349,052,127 — but 053/303 already
   exemplars in exchange-greedy/spectral (R5 allows recurrence under own
   lens; prefer non-reused alternates from plan.json if scores allow);
   information-theory Ch.11: 185(PODS),079,231,279,237 (231 recurs from
   estimation — same rule); communication-complexity Ch.12: 115(PODS),
   243(PODS),357,070 — PODS cap 2 for this chapter only; online-decisions
   Ch.13: 242,094,221,140 hand-picked.
3. After each wave: acceptance greps (CHAPTER-RULES.md checklist) →
   `./build.sh main` → per-chapter commits → quota check.
4. Post-rollout (LAST): overfull polish pass, ch0 refresh (§0.3 trinity
   52/39 vs table 50/38), Index part, `\bookversion{1.0}`, CLAUDE.md runbook
   + memory updates.

## Standing rules (unchanged)
Cost calibration ~1–1.3pt/chapter agent; wave ≈ 5pt + 1pt master. Byte-stable
build (≥4 pdflatex runs after aux wipe; build.sh loops to identical md5
twice). Vision loop: pdftoppm -r 110 → Read → analyze_image (per-URL
signatures; 400 = stale → re-Read). Sections from x.0 via per-chapter
`\setcounter{section}{-1}`. Exactly 3 box semantics. Master reads only
CLAUDE.md/index/report + ≤120-line spot checks; theory/ + digests are
subagent-only. Old chapters' [?] citation warnings are expected until their
rewrite lands.
