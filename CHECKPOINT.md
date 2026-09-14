# CHECKPOINT — 2026-09-14 15:45 (wave 1 = 3/4 done; QUOTA TRIPPED, idling)

Weekly 40% ≥ soft 39.9% (3d bound) at 15:34 → policy enforced: estimation
agent killed (mid-write, file UNTOUCHED — still pre-pilot 153 lines, builds
fine), no further subagent launches. Next relief: day 4 completes
~15:05 9/15 → bound 54.14% (headroom ~14pt).

## Cost calibration (IMPORTANT for wave planning)
Chapter-revision agents cost **~1–1.3pt each** (750–850-line rewrites, 27–37
tool uses), NOT the 0.4–0.5pt of note batches. Wave 1 (4 agents + master)
≈ 5pt total (35%→40% in 25 min). Plan around ~5pt/wave + 1pt master.

## State
- Committed this round: `82a2550` ToC right-align (vision-verified),
  `22a74ae` frequency chapter order (reductions = Ch.1), `0613ec7` bib
  seeding (all 12 chapters' `-all.bib` hold their planned exemplar corpus
  entries verbatim from refs.bib — agents only add classic bg refs),
  `9592cb1` reduction, `f16bdc0` induction, `1998330` adversarial-construction.
- Wave 1 acceptance: 3/3 revised chapters PASS (opener/objectives/boxes/
  recap/bib-tail/\citep-only/keys-resolve/PODS≤1; anatomy = \paragraph{
  Problem./Guarantee./How …/What it buys.}). One build error found+fixed:
  induction had a text-mode `\eopm` → `\eop` (amsmath \tag error).
- Full book: `./build.sh main` → **123pp, 0 errors, 21 overfulls, 76
  unresolved citations — ALL in unrevised chapters** (estimation 20,
  dp-composition 18, online-decisions 12, spectral 11, exchange-greedy 10,
  amortized 5). Revised chapters resolve 100%. 9 overfulls sit in the 3
  new chapters (cosmetic; polish pass AFTER all waves, before ch0 refresh).
- estimation-theory agent was killed mid-rewrite; its context is resumable
  via SendMessage to its task (don't relaunch fresh — resume is cheaper).
  If resuming fails: relaunch with the wave-1 prompt (exemplars 115(PODS),
  231, 102, 373, 293, 377; note the current draft has an env-form reachbox
  workaround that R3 replaces).

## Resume (in order, after quota GO)
1. `python3 scripts/quota_check.py` — GO when headroom > ~4pt (a full wave
   + margin). Expected ~15:05 9/15.
2. Resume/relaunch estimation-theory (Ch.4), THEN wave 2 (dp-composition
   Ch.6: 298,178(PODS),337,263,073,214; exchange-greedy Ch.7:
   053(PODS),200,031,009,224,229; spectral-matrix Ch.8:
   038(PODS),303,235,190,101,265; amortized-potential Ch.9:
   177(PODS),015,180,363,274,203) — same agent prompt template as wave 1.
   If headroom < 9pt at wave-2 gate, split: 2 chapters now, 2 on day 5.
3. Wave 3 (coresets-rnla Ch.10 NEW: 289,053(PODS),303,349,052,127;
   information-theory Ch.11 NEW: 185(PODS),079,231,279,237;
   communication-complexity Ch.12 NEW: 115(PODS),243(PODS),357,070 —
   PODS cap 2; online-decisions Ch.13: 242,094,221,140 hand-picked).
   New-chapter agents: replace stub file, add `<tool>.bib` bg refs;
   `-all.bib` corpus entries already seeded.
4. After each wave: acceptance greps → `./build.sh main` → commit per
   chapter → fresh quota check.
5. Post-rollout (LAST): overfull polish pass, ch0 refresh (reconcile
   §0.3 trinity 52/39 vs table 50/38), Index part, `\bookversion{1.0}`,
   update CLAUDE.md runbook + memory.

## Standing rules (unchanged)
Byte-stable build (≥4 pdflatex runs after aux wipe; `./build.sh` loops
until PDF md5 identical twice). Vision loop: pdftoppm → Read →
analyze_image (per-URL signatures; prefer pdftotext -bbox for geometry).
Sections from x.0 via per-chapter `\setcounter{section}{-1}`. Exactly 3
box semantics; no algorithmblock. Master reads only CLAUDE.md/index/
report + ≤120-line spot checks; theory/ is subagent-only.
