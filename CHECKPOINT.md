# CHECKPOINT — 2026-09-15 16:1x (BOOK v1.0 SHIPPED; polish queue complete)

## State: everything DONE
Survey (385 papers, 228 tagged, report + addendum) and the lecture-notes
book are complete. Book = ch0 + 13 tool chapters + script-generated Index,
`\bookversion{1.0}` "First complete edition", 275 pp, 0 errors, 0 undefined
refs, 6 known overfull survivors (all ≤4.14pt), byte-stable.

## Polish queue — all items closed (2026-09-15, user "Go ahead!")
1. [x] Overfull pass 57→6, vision-verified — `2f054f4`.
2. [x] ch0/tool count refresh to 228-tagged figures — `7a8bd2b`.
3. [x] Index back matter, script-first: `scripts/11_make_index.py` →
   `chapters/index.tex` (\ref-based, no makeindex): tool map (14) + named
   results (219) + corpus exemplars (65, 12 PODS). Two vision rounds; fixes
   = \clearpage before the results section (orphaned heading), \mbox around
   every ref unit (no "Chap-ter" splits), em-dash ties (no dangling dash at
   line end). Layout vision-verified — `9ce4600`.
4. [x] `\bookversion{1.0}` + "First complete edition" — `fafeb8e`.
5. [x] CLAUDE.md: book runbook (§ Book runbook) + status log entry; memory
   refreshed; this checkpoint = final.

## Runbook
Book build/verify/index-regeneration/smoke-test commands live in CLAUDE.md
(§ Book runbook). Highlights: `./build.sh main` (byte-stable loop);
`python3 scripts/11_make_index.py` after any chapter/label change;
`LC_ALL=C grep -a -n 'Overfull' main.log`; ToC orphan scan via pdftotext.

## Standing rules (unchanged, for any future venue run)
Quota governor HARD rule (`scripts/quota_check.py` before EVERY subagent
launch, exit 3 = STOP); the 9/15-only 80%-of-weekly override EXPIRED with
the day — original rule applies. Waves ≤ 4 concurrent; producer-consumer
split; master reads only CLAUDE.md/index/report + ≤120-line spot checks;
theory/ + digests subagent-only. Commits: Conventional Commits +
Co-Authored-By trailer; never `git add` buildstamp.tex (gitignored).
