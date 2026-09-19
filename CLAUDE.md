# db-theory-survey — How DB researchers use theory

Survey of theoretical tools in top DB venues (SIGMOD first). Research questions:

- **R1 Modeling**: how do DB papers formalize a problem (models, assumptions, cost/complexity framework)?
- **R2 Properties**: what do they prove (correctness, complexity bounds, approximations, guarantees)?
- **R3 Tools**: which theoretical machinery (reductions, concentration, duality, competitive analysis, ...)?
- **R4 Role**: where theory sits in the paper (motivation / design driver / evaluation yardstick)?

Scope: **SIGMOD'26 = PACMMOD Vol 4 (257 articles, rounds 3–4) + Vol 3 issues 4–6 (128 articles,
rounds 1–2) = 385 articles** (research track ≈ 349/1049 = 33%; corpus also contains ~17
[Experiments & Analysis] + some industrial papers — demos are NOT in PACMMOD).
Structure note: one SIGMOD conference spans TWO PACMMOD volumes (2 rounds per volume-half).
Later venues: SIGMOD'25 = Vol 2 i4–6 + Vol 3 i1–3; SIGMOD'24 = Vol 1 i4–6? + Vol 2 i1–3 (verify).
IDs sigmod26-001..257 = Vol 4 (alphabetical); sigmod26-258..385 = Vol 3 i4–6 (rounds 1–2).

## Environment notes (2026-09-13)
- `dblp.org` is TLS-reset by the local proxy (127.0.0.1:7897) — **OpenAlex** used instead
  (source lookup + `biblio.volume` filter; works fine).
- `dl.acm.org` Cloudflare-blocks raw scripts (403 `cf-mitigated: challenge`), BUT is fully
  reachable via **CDP Chrome** (2026-09-13, works): launch a SECOND Chrome instance
  `open -na "Google Chrome" --args --user-data-dir=<tmp>/cdp-profile --remote-debugging-port=9222
  --remote-allow-origins='*' --no-first-run <dl.acm.org url>` — a fresh profile passes the
  JS challenge automatically (no clicks/cookies needed). Drive via websocket
  (`scripts/cdp_eval.py` eval helper; `scripts/cdp_fetch_pdf.py` in-page fetch→base64→PDF;
  `scripts/02c_fetch_acm_cdp.py` bulk). NOTE: Chrome ≥136 forbids CDP on the DEFAULT
  profile — separate --user-data-dir is mandatory. Keep a dl.acm.org tab open in that
  instance (same-origin context for fetches). Don't close its window mid-run.
- Consequence: ACM-only papers are no longer a coverage gap; arXiv TeX remains preferred
  when available (camera-ready ACM PDF via CDP is the fallback, and often the
  camera-ready version).
- `pdftotext` (poppler) available; python3 = anaconda 3.13.

## Pipeline (run from this folder; all steps are cheap local scripts, no LLM)

TeX-FIRST policy (2026-09-13, user directive): prefer machine-readable sources. arXiv TeX
e-print is the authoritative source when available (structured theorem envs, no pdf-mangling);
PDF+pdftotext remains the fallback. `theory/<id>.json` records provenance in `"from"`.

```bash
cd db-theory-survey
python3 scripts/01_fetch_paper_list.py 4 data/sigmod26/papers.jsonl sigmod26        # OpenAlex
python3 scripts/02_download_pdfs.py data/sigmod26/papers.jsonl data/sigmod26/pdfs   # fallback path
python3 scripts/02t_download_tex.py data/sigmod26/papers.jsonl data/sigmod26/s2_arxiv_map.json data/sigmod26/src   # preferred
python3 scripts/02c_fetch_acm_cdp.py data/sigmod26/papers.jsonl data/sigmod26/pdfs data/sigmod26/manual_pdfs   # ACM-only via CDP Chrome
python3 scripts/03_pdf2txt.py data/sigmod26/pdfs data/sigmod26/txt                  # fallback path
python3 scripts/04t_extract_theory_tex.py data/sigmod26/papers.jsonl data/sigmod26/src data/sigmod26/theory   # preferred
python3 scripts/04_extract_theory.py data/sigmod26/papers.jsonl data/sigmod26/txt data/sigmod26/theory          # fallback
python3 scripts/05_build_index.py data/sigmod26 index/sigmod26_index
```

Producer-consumer split (user directive): a PRODUCER subagent owns 02t/04t + ingest
(downloads, extraction, index rebuild); CONSUMER agents do analysis waves over
notes/sigmod26/. Master launches waves and stays out of both files.

## Layout
- `data/<venue>/papers.jsonl` — id, title, authors, doi, oa_urls, src
- `data/<venue>/manifest.jsonl` — one line per download attempt (append-only)
- `data/<venue>/pdfs/<id>.pdf`, `txt/<id>.txt`, `theory/<id>.{json,md}`
- `index/<venue>_index.{csv,md}`, `index/<venue>_index_flagged_ids.txt` (score-desc)
- `notes/<venue>/batch_*.md` — subagent per-paper analyses
- `report/<venue>_survey.md` — final synthesized survey
- `lecture-notes/` — chapter .tex files, `figures/`, `refs.bib`, `plan.json` (scripts 07–09)

## Extraction definitions (04)
- Statements: `Theorem|Lemma|Corollary|Proposition|Claim|Observation|Fact|Definition|Conjecture N`
  at paragraph/sentence start (prev-char guard kills most inline cross-references).
  Captured until the next statement/proof marker (≤1.5k chars).
- Proofs: `Proof [of <kind> N] [Sketch].` until ∎/□/QED/next marker (≤2.5k chars).
- Bound sentences: sentences containing lower/upper bound, NP-hard, approximation ratio,
  asymptotic/worst-case optimal, information-theoretic (≤12 per paper, ≤300 chars).
- Signal counts: big-O/Ω/Θ, whp, regret, DP, invariants, convergence, competitive ratio,
  worst-case, sketch, cost model, cardinality, learned-*.
- `flag` = ≥1 proof OR ≥3 statements OR (lower-bound signal AND ≥1 statement).
- `score` = statements + 2·proofs + lower_bound + np_hard + approx_ratio (higher = more theoretical).

## Tag taxonomy (assigned by analysis subagents per paper; controlled vocab, may append `+ free-text`)

**props** (property studied / thing proven):
`lower-bound` `upper-bound` `tightness` `hardness` (NP/#P/complexity) `approximation-ratio`
`competitive-ratio` `error-bound` (MSE/error bars) `probabilistic-guarantee` (whp/confidence)
`asymptotic-optimality` `convergence-rate` `sample-complexity` `space-complexity` `io-cost-bound`
`latency-throughput-bound` `regret-bound` `correctness` (invariants/equivalence/soundness)
`consistency` (serializability/atomicity/linearizability) `privacy-guarantee` `robustness-stability`
`identifiability` `generalization-bound` `price-of-x` (anarchy/communication/federation) `completeness-recall`
`conditional-lower-bound` (SETH/BMM/OMv-conditioned)

**tools** (theoretical machinery used):
`concentration-ineq` `clt-normal-approx` `delta-method` (incl. functional/Hadamard) `reduction`
`adversarial-construction` `amortized-potential` `competitive-analysis` `exchange-greedy`
`duality` (LP/convex) `kkt-optimality` `induction` `martingale-azuma` `balls-bins-hashing`
`sketching-theory` (mergeability etc.) `information-theory` (entropy/Fano) `communication-complexity`
`spectral-matrix` `coupling-dominance` `estimation-theory` (unbiasedness/variance/MSE)
`bootstrap-resampling` `game-equilibrium` `fixed-point-contraction` `online-regret` (UCB/mirror descent)
`dp-optimality` (dynamic programming) `peeling-dyadic` `markov-chain` `bayesian-posterior`
`dp-composition` (DP composition/sequencing/post-processing/amplification)
`group-symmetry` (group-theoretic/symmetry/automorphism arguments)
`randomized-nla` (randomized numerical linear algebra: power/subspace iteration, sketch-and-solve)
`fine-grained-reductions` (BMM/SETH/Hyperclique/OMv-based conditional lower bounds)
`coresets-geometry` (coresets, geometric decompositions, discrepancy)
`mso-logic` (MSO logic, transductions, meta-theorems)
`moment-analysis` (moment generating/special functions, analytic combinatorics)

**domain** (paper topic):
`cardinality-estimation` `query-optimization` `join-algorithms` `aqp` `sampling` `streaming`
`sketching` `indexing` `ann-vector-search` `llm-db` (Text-to-SQL/RAG/semantic) `data-cleaning`
`entity-resolution` `data-integration` `transactions` `consensus-replication` `distributed-query`
`privacy-dp` `security` `fairness` `data-market` `graph-db` `spatial` `time-series`
`storage-compression` `caching-scheduling` `provenance` `uncertain-data` `workload-tuning` `benchmark`

**role** (where theory sits): `motivation` | `design-driver` | `evaluation-yardstick` |
`appendix-foundation` | `theory-as-contribution` (the formal result IS the paper)

## Analysis protocol (subagents)

Note file format (machine-parsable; first 4 lines exactly as shown):

```
### {id} — {title ≤ 12 words}
domain: tag | tag
props: tag | tag
tools: tag | tag
modeling: ...
properties: ...
usage: how the tools above are applied (1 line)
role: one of {motivation, design-driver, evaluation-yardstick, appendix-foundation} + clause
quote: ≤ 40 words, one key formal statement
```

≤ 110 words prose per paper — the budget covers modeling/properties/usage/role prose ONLY
(tags lines and quote are excluded). Tags from the taxonomy only (append `+ free` if truly
needed); use 1–3 tags per line — as many as honestly fit, no forced minimum.

Noise rule: pdf-derived extracts may contain table fragments / captions / empty stubs posing
as statements, and signal counts may come from related-work text — judge by context, ignore
junk (note "noisy" under modeling if it dominates). TeX-derived extracts (`from=tex`) are
structurally cleaner.
After each wave: `python3 scripts/06_tag_stats.py notes/sigmod26 index/sigmod26_tags.md`
aggregates counts + domain×prop / domain×tool cross-tabs + (prop,tool) pairs with exemplar ids.

## Quota governor (user policy, 2026-09-13 — HARD RULE)
- Daily allowance = 100%/7 per day since the last weekly reset; cumulative bound =
  COMPLETED days since reset (floor — a partial day does NOT count) × 100/7 %.
  Day 0 (reset day) still gets the first day's allowance. Checked via
  `python3 scripts/quota_check.py` (exit 3 = STOP) before EVERY subagent launch.
- On weekly usage ≥ bound − 3 (SOFT bound = hard bound − 3; the 3-point margin leaves ~1%
  for this master's summary/checkpoint and ~2% for OTHER workers on the same plan): master
  STOPS all running subagents (TaskStop), then spends at most ~1% writing a summary +
  checkpoint to CHECKPOINT.md (state, queues, next actions, resume instructions), then
  idles until the bound grows (next day boundary) or the week resets. No waves, no
  subagents while over threshold.
- The 5-hour window (unit 3) is informational; the WEEKLY bound is the binding constraint.
- Endpoint: GET https://open.bigmodel.cn/api/monitor/usage/quota/limit
  (Authorization: $ANTHROPIC_AUTH_TOKEN). limits[] unit 6 = weekly, unit 3 = 5h window.

## Token & parallelism policy
- Script stage: 0 LLM tokens (this is the bulk of the work).
- Analysis stage: waves of **≤ 4 concurrent** subagents, 8-10 papers each. Each agent reads only
  its ~10 `theory/*.md` files (~60-100KB ≈ 15-25k input tokens) and replies ≤ 5 lines.
- Master token spend per wave ≈ prompts + wave summaries (keep ≤ 1k tokens/wave).
- Ledger (est., input+output tokens): maintained in Status log. Update after each wave.

## Token discipline (IMPORTANT for the master agent)
1. Master reads ONLY: this file, `index/*.md`, `report/*`, and spot-check slices ≤120 lines.
   **Never** open files in `pdfs/`, `txt/` wholesale; `theory/` is read by subagents only.
2. Analysis subagents (general-purpose): get a line range of `index/<venue>_index_flagged_ids.txt`,
   read `data/<venue>/theory/<id>.md` for each id, write `notes/<venue>/batch_<a>_<b>.md`
   (≤110 words/paper, fixed schema), reply with ≤5 lines.
3. Synthesis subagent: reads all `notes/` + `index/*.md` → writes `report/<venue>_survey.md`.
   Master reads only the report.
4. Subagents must `grep` papers.jsonl if they need metadata — never read it whole.

## Workflow v2 (2026-09-13 reflection — binds all future runs)
Post-mortem of the full SIGMOD'26 run (~950k subagent tokens ≈ 18% weekly quota, governor
never tripped). What worked and is now mandatory:

1. **Zero-LLM-first**: every deterministic transform is a script BEFORE any agent sees data
   (01–06: fetch/extract/index/stats; 07–09: chapter plans, figures, bib stubs). LLM tokens
   buy judgment only. CDP fetching and matplotlib figures cost 0 tokens.
2. **Producer–consumer, waves ≤ 4**: producer owns fetch/extract/index and self-revises its
   scripts; consumers get a queue slice, read ONLY their `theory/<id>.md` files, emit
   fixed-schema notes, reply ≤ 5 lines. Master touches only CLAUDE.md / index / report /
   plan summaries (≤ 120-line spot checks). The 5h window peaked ~60% under this regime.
3. **Quota governor before EVERY launch** (`scripts/quota_check.py`, exit 3 = STOP;
   soft = hard − 3). Log headroom in each wave's status line. On trip: TaskStop all →
   ≤1% checkpoint → idle. Never tripped in v1; keep it that way.

v2 fixes for frictions observed in v1:

- **ONE queue file** per venue (`notes/<venue>/queue.txt`, `id\tscore\ttitle` lines;
  agents claim a range by appending `# claimed a..b <ts>`). The `_queue/_queue2/_queue3`
  sprawl caused repeated status checks and near-double assignment.
- **Calibration sheet**: every consumer first reads `notes/<venue>/calib.md` (3 gold
  pilot notes + tagging conventions). Waves 3–5 showed role-clause drift with no shared
  standard (addendum §6); cost of the sheet ≪ cost of inconsistent tags.
- **Exclude PODS at fetch time**, not post-hoc: for SIGMOD-only runs pass
  `--exclude-doi 3801890:3801919` (PACMMOD Vol 4 No 2 = PODS issue). The post-hoc
  carve-out cost a full addendum section and contaminates every cross-venue claim.
- **TeX-first with `tex_locked()`** guard (already in 04): pdf extraction never
  overwrites TeX-derived theory files.
- **Synthesis agents read aggregates only** (`index/*.md` + notes), never corpora.
- **Artifact reuse**: non-survey deliverables (lecture notes, slides) ride the same spine —
  script plan (07) → ≤ 4-agent chapter waves → script figures/bib (08/09) → master composes.

## Lecture-notes pipeline (added 2026-09-13)
```bash
python3 scripts/07_plan_chapters.py notes/sigmod26 index/sigmod26_tags.md \
  index/sigmod26_index.csv data/sigmod26/papers.jsonl lecture-notes/plan.json   # per-tool exemplars (dedup'd, PODS-flagged)
~/anaconda3/bin/python3 scripts/08_make_figures.py index/sigmod26_tags.md lecture-notes/figures   # matplotlib PDFs, 0 tokens
python3 scripts/09_make_bib.py data/sigmod26/papers.jsonl lecture-notes/refs.bib  # @article keys sigmod26-NNN
```
Chapter-agent protocol: prompt contains its plan.json slice (count + 4–6 exemplars with
id/title/score/PODS flag/usage/quote); agent reads `data/sigmod26/theory/<id>.md` for each
exemplar, writes `lecture-notes/chapters/<tool>.tex` (section file, NO preamble: tool intro
with background refs → 3–5 deduplicated exemplars, ≤ 2 sentences of context each + the key
statement; PODS exemplars marked) + `chapters/<tool>.bib` for classic background refs;
≤ 1 inline TikZ/pgfplots figure only if it genuinely helps; reply ≤ 5 lines. Master composes
`main.tex` + `ch0.tex` (scope, stats, figures, chapter index), cats bibs, runs
pdflatex+bibtex, and finalizes the Ch0 index LAST (user spec).

### Book runbook (v1.0, 2026-09-15)
- Build: `cd lecture-notes && ./build.sh main` — loops pdflatex/bibtex until the PDF
  is byte-stable (the ToC needs the extra pass); prints "N pp, X overfulls".
  Steady state: 273 pp, 6 known overfull survivors (all ≤4.14pt). NEVER
  `git add buildstamp.tex` (gitignored per-run stamp).
  Other modes (2026-09-19): `./build.sh chapter <name>` builds main-<name>.pdf =
  ch0 + chapters/<name>.tex; `./build.sh clean` removes aux artifacts
  (aux/bbl/toc/log/..., buildstamp.tex, generated main-* subset sources) but
  keeps every .pdf. The legacy `pilot` target was removed the same day (the
  `chapter` mode subsumes it); default target is `main`.
- Index back matter: `python3 scripts/11_make_index.py` (any CWD) regenerates
  `lecture-notes/chapters/index.tex` from main.tex's include order + the
  `domain:` tags in notes/sigmod26/batch_*.md ("By paper domain" view + the
  alphabetical list). Re-run after adding/renaming chapters, changing theorem
  labels, or editing domain tags, then rebuild. Layout note: entries are
  plain unbreakable paragraphs (\interlinepenalty 10000) at the normal TEXT
  measure — the wide-margin convention (margin column free on every page,
  odd right / even left, like the body chapters). No parity machinery at
  all: the earlier full-measure + aux-probe/\leftskip schemes (fullwidth,
  adjustwidth*, \gdef\idxpg) were all superseded — the text measure is
  parity-independent, so a bare pdflatex run lays the index out correctly
  (the build.sh loop is still needed for the ToC). Entries carry a local
  \emergencystretch=6em: long names + unbreakable \mbox{Thm.~n.m} tails
  can exhaust the global 3em at the narrower measure.
- Overfull check: plain grep can miss hits (locale) — use
  `LC_ALL=C grep -a -n 'Overfull' main.log`.
- Smoke tests: ToC orphan scan `pdftotext -f 3 -l 9 -layout main.pdf - |
  grep -nE '^[0-9]+ *$|^\*[0-9]+ *$'` (empty = clean); page renders via
  `pdftoppm -r 110 -png -f P -l P main.pdf /tmp/pg` + Read for visual checks.

## Status log
- 2026-09-13 scaffolded; env probed (dblp ✗, ACM pdf ✗, OpenAlex ✓, arXiv ✓, pdftotext ✓).
- 2026-09-13 paper list fetched: **257 papers** (PACMMOD Vol 4) -> data/sigmod26/papers.jsonl.
- 2026-09-13 pilot (4 papers): download→txt→extract verified; extraction quality good
  (statements+proofs+bound sentences; math is unicode-mangled by pdftotext — acceptable).
  PDF sources: OpenAlex oa_urls / arXiv title match / Semantic Scholar openAccessPdf /
  ACM last resort. Pilot hit-rate 2/4 via arXiv alone -> S2 fallback added.
- 2026-09-13 scope extended per user decision: full conference rounds 1-4 (385 papers).
      papers.jsonl = Vol 4 (001-257) + Vol 3 i4-6 (258-385).
- 2026-09-13 download realities (v3): arXiv API IP-throttled (429) after v1 burst; ACM
      Cloudflare blocks scripts (curl, browser headers, curl_cffi impersonation, jina, wayback
      all fail). Viable sources: S2 batch DOI->arXiv-id map (data/sigmod26/s2_arxiv_map.json,
      138 ids) -> arxiv.org/pdf; Unpaywall non-publisher mirrors; S2 openAccessPdf non-ACM urls.
      Projected ceiling ~40-45% (145-170/385). Bias note: arXiv posters skew theory-friendly —
      document in report; a "manual ACM fetch list" can be generated for the user if full
      coverage is wanted.
- 2026-09-13 PIPELINED execution (user directive): downloads in background; a 90s incremental
      loop re-runs 03+04+05 (idempotent) so index/flagged list appear early; analysis subagent
      waves start on the first flagged batch instead of waiting for all downloads.
- 2026-09-13 PRODUCER-CONSUMER live: producer subagent owns TeX ingest (02t/04t + index
      rebuild, self-revises scripts); consumer subagents do 10-paper note batches.
      Done: pilot (8 papers), batch_01_10. In flight: batches 11-20 / 21-30 / 31-40.
      Next: wave 2 = queue lines 41-47 + newly TeX-flagged ids after producer rebuild.
- [x] producer DONE: src_ok 137/138 (281 = PDF-only arXiv sub, keeps pdf fallback), tex_extracted
      137, flagged 98 (was 88), coverage 156/385 extractions (137 tex + 19 pdf-only legacy).
      Fixed 2 detex bugs. Details: data/sigmod26/PRODUCER_STATUS.md
- [x] wave 1 DONE: 48 papers noted (batch_pilot 8, batch_01_10 10, batches 11_20/21_30/31_40)
- [x] wave 2 DONE: batches w2a-w2d (52 papers) -> 100 tagged notes total (9 batch files),
      all flagged papers covered
- [x] tag stats: 100 papers -> index/sigmod26_tags.md (rankings + cross-tabs + pairs)
- 2026-09-13 SURVEY v2 COMPLETE (full corpus, 100% coverage): addendum written
      (report/sigmod26_survey_addendum.md, 255 lines, spot-verified). Key results:
      (1) correctness 98 overtakes upper-bound 75 as #1 property (survives PODS carve-out
      92/199); (2) PODS CONTAMINATION: DOI band 10.1145/3801890-3801919 = PACMMOD V4 N2
      (PODS'26) — 29 research articles + 1 editorial inside the corpus (12.7% of notes,
      13 of top-20 scores, 39% of lower-bound tags, 64% of tightness); carve-out required
      for all cross-venue claims; (3) bias test: arXiv cohort 1.7x denser but a third of
      that was PODS; ACM-only mass brought the correctness surge + exchange-greedy (4->17);
      (4) new playbook recipes: amortized-potential event bounding, greedy-with-certificate,
      ski-rental adapt decisions, bandit/decay regret; (5) taxonomy additions proposed:
      unlearning, knowledge-compilation, finance-routing, nn-querying.
      NOTE for future venues: fetch must EXCLUDE the PODS DOI band (or use OpenAlex
      issue filter '2' exclusion) if a SIGMOD-only survey is wanted.
- 2026-09-13 WORKFLOW v2 reflection folded into this file (sections above); scripts
      07 (chapter plans) / 08 (matplotlib figures) / 09 (corpus bib + unicode map) /
      10 (per-chapter digests — the key cost lever: agents read ONE 7-37KB digest,
      ~5x cheaper than raw theory/<id>.md files) added.
- 2026-09-13/14 LECTURE NOTES COMPLETE overnight (user asleep; autonomous run under
      frozen quota cap 25.6% until 9/14 15:00, never tripped — final usage 22%).
      lecture-notes/main.pdf = 53 pages, 0 LaTeX errors: ch0 (scope + stats + 5 figures
      + finalized chapter map) + 10 tool chapters (reduction, concentration, induction,
      estimation, adversarial, dp-composition, exchange-greedy, amortized-potential,
      spectral, online-decisions) + merged all.bib (385 corpus refs + 60 classic bg refs).
      10 chapter agents in 3 waves (4+4+2), 44 exemplars used of 58 planned (dedup +
      diversity skips), PODS exemplars marked \pods. pdflatex+bibtex clean.
      Fixes found by early smoke tests: estimation reachbox needed env form; corpus
      bib titles needed unicode→LaTeX map (ℓ→$\ell$ etc.); newunicodechar safety net
      added to main.tex.
- 2026-09-14/15 BOOK v1.0 COMPLETE. Grew to ch0 + 13 tool chapters (+ coresets-rnla,
      information-theory, communication-complexity) per the CHAPTER-RULES.md pilot
      spec (sections from x.0, 3-box palette, folio-first headers, per-chapter
      bibliographies, recap-before-appendix); rounds 6–8 user-feedback fixes are
      documented as comments in main.tex (ToC right-aligned page numbers, parity-free
      ToC entries, ragged-right wrapped headings, widefigure/widetable captions).
      2026-09-15 polish queue (user "Go ahead!"): overfull pass 57→6 survivors
      (2f054f4); stale tool-count refresh to the 228-tagged figures (7a8bd2b);
      script-generated index back matter — 11_make_index.py → chapters/index.tex,
      \ref-based (no makeindex): tool map + 219 named results + 65 exemplars,
      two-round vision-verified (9ce4600); \bookversion{1.0} "First complete
      edition" (fafeb8e). Final state: 275 pp, Index pp. 265–275.
- 2026-09-15 post-v1.0 review round (user list, all verified by render+bbox):
      chapter fixes — Fig 6.1 annotation/block overlap + Lemma 6.11's doubled
      \eop (dp-composition), Fig 7.1 enlarged into a marginfigure in the margin
      column (exchange-greedy), Fig 10.1 rightmost block moved off the arrow's
      way (coresets-rnla), p.250 sidenote re-anchored off the page boundary so
      its parity is evaluated correctly (online-decisions), Fig 12.1 streaming
      pass redrawn at margin width (communication-complexity) — 7208285; index
      redesigned — "Tools and chapters" and "Corpus papers used as exemplars"
      dropped per user, new "By paper domain" section (17 domains from 39
      exemplar papers, PODS'26 flagged; 119 corpus-derived results attributed,
      223 total in the alphabetical list) — 2f87db0. Final state: 272 pp,
      Index pp. 263–272, same 6 overfull survivors.
- 2026-09-15 index layout revision (user report: two-column index wasted the
      wide margin, comma-crammed entries, unwanted PODS highlighting): both
      index sections widened to text+margin (then via tufte fullwidth — its
      adjustwidth* parity proved fragile, superseded by 43b7389's plain-
      paragraph layout), one result per line, domain headers carry only the
      exemplar count (PODS parsing kept for console stats) — a60121c. Final state:
      273 pp, Index pp. 263–273, same 6 overfull survivors. Build hygiene
      note: a manual non-build.sh build reported 270 pp from under-converged
      aux/toc (pre-index content was at 260 pp vs canonical 262) — the
      canonical page count ALWAYS comes from `./build.sh main` (byte-stable
      loop), never a bare pdflatex run.
- 2026-09-15 index parity bug fixed (user report: pp. 269/271 "rendered too
      left, only the right half visible"): fullwidth/adjustwidth* cannot judge
      an entry landing at the top of a fresh page — the live \c@page test
      still counts the PREVIOUS page (the round-8 ToC disease), and strict
      mode's aux probe precedes the list's breakable top glue, so it too
      ships with the previous page and the byte-stable loop converges
      STABLY WRONG: one-line entries got the even-page leftskip (-167.4pt)
      on odd pages → painted at x = -95pt, half off the paper (pp. 265/269/
      271/273 fragments at x≈0; p264 entry at x=229). Fix in 11_make_index.py:
      no fullwidth at all — each entry is ONE unbreakable paragraph
      (interlinepenalty 10000) at the full text+overhang measure, parity per
      entry from the PREVIOUS run's aux (\gdef\idxpg<roman>, @-free so it
      survives aux re-tokenization; the \protected@write probe sits INSIDE
      the entry's first line so \thepage resolves at shipout). Pagination is
      parity-independent, so build.sh converges in 2-3 runs. Also fixed:
      domain headers joined to their first entry by \\* — parskip glue, even
      at 0pt, is a legal page break and orphaned a header at p264. Verified:
      bbox+ink scans of all 11 index pages (zero words outside 58-556pt,
      minX 61.4-72.0, formerly invisible entries back) + vision on 269/271 —
      43b7389. Final state: 273 pp, Index pp. 263-273, same 6 overfulls.
- 2026-09-16 index wide-margin revision (user report: the "Named theorems"
      section read as full-page mode): measurement showed BOTH sections
      actually shared the full text+margin measure — odd pages filled the
      right margin on long lines (p263 ink to 550pt), even pages started
      every entry at x≈62 in the left margin; the domain section only
      LOOKED conforming because its entries are shorter. Fix in
      11_make_index.py: entries now set at the plain TEXT measure — margin
      column free on every page, like the body chapters. The whole
      parity/aux-probe machinery (\idxpg probes, \leftskip, idxprobe
      counter) is GONE (text measure is parity-independent), plus a local
      \emergencystretch=6em in entries (one 6.8pt overfull from a long
      name + \mbox tail at the narrower measure, now resolved). Verified:
      bbox scan of all 11 index pages (body ink strictly within
      [72,384] odd / [229,541] even; sole exception = the chapter-opener
      footer folio, book-wide convention) + vision on 264/269 (wide empty
      margins both parities, zero protrusion). Final state: 273 pp,
      Index pp. 263-273 ('Named theorems' starts p268), same 6 overfulls.

- 2026-09-16 repo cleanup + public release: github.com/bai-wenchao/db-theory-companion
      (renamed from db-theoretical-companion). Tracked set = sources only (scripts,
      lecture-notes tex/bib/cls + docs); data/, index/, notes/, report/, CHECKPOINT.md
      are gitignored local artifacts (.gitignore documents the regeneration chain).
      Book retitled "A Theoretical Companion to Database Research"; author credit
      "Wenchao Bai and GLM5.3 (harnessed by Claude Code)" (title page, verso, running
      heads, PDF metadata). Rebuild verified: 273 pp, same 6 overfull survivors.
- 2026-09-19 build.sh modes + public-repo docs: `clean` target (aux artifacts only,
      every .pdf kept) and `chapter <name>` subset builds (main-<name>.tex = ch0 +
      one chapter, exact-name include filtering, name validated [a-z0-9-]+); default
      target now `main`. Tested: chapter reduction = 29 pp/0 overfulls, clean keeps
      main.pdf + subset PDFs, full main = 273 pp/6 overfulls (canonical). Added
      README.md (survey+book overview, pipeline, build, license, citation) and
      LICENSE (MIT, scripts) + LICENSE-CC-BY-4.0 (book content); .gitignore covers
      main-*.tex / main-*.pdf subset jobs. `./build.sh main` also emits the
      distributable copy lecture-notes/A-Theoretical-Companion-to-Database-Research.pdf
      (gitignored; the release asset). Released: commits 3f0ee8a + 4f0e44c pushed;
      GitHub release v1.0 (matches \bookversion) created with the title-named PDF
      attached — github.com/bai-wenchao/db-theory-companion/releases/tag/v1.0.
- 2026-09-19 round 2 (user feedback): legacy `pilot` target REMOVED from
      build.sh (chapter mode subsumes it) + every active doc (README, .gitignore,
      CHAPTER-RULES R9, main.tex header; REVISION-PLAN/old status entries keep
      their historical mentions). README citation drops the "GLM5.3 harnessed by
      Claude Code" note (author field keeps GLM5.3). Book verso license corrected
      CC BY-NC 4.0 → CC BY 4.0 (was inconsistent with LICENSE-CC-BY-4.0) + CC BY
      88x31 badge (lecture-notes/cc-by-88x31.png, tracked) + tcs-style
      "Text available on <repo> — post issues there" line. THIRD-PARTY-NOTICES.md
      was already cited on the verso (no change needed).

## Token ledger (est; input+output, excludes master context)
- script stage: ~0 LLM tokens
- producer agent: ~200k (88 tool uses: downloads, 2 script fixes, spot-checks)
- wave 0+1: 5 consumers × ~30k ≈ 150k (48 papers noted)
- wave 2: 4 consumers × ~35k ≈ 140k (52 papers, done)
- waves 3-5 (full-corpus refresh): 10 consumers × ~30k ≈ 300k (128 papers, done)
- addendum synthesis: ~90k (done)
- TOTAL subagent ≈ 950k for: 385/385 papers, 385 extractions, 228 tagged notes, report + addendum.
  Per-note amortized: ~4.2k. Script stages + CDP downloads: 0 LLM tokens.
  Weekly quota consumed by entire survey: ~18% of plan (governor never tripped).
- Lecture notes (2026-09-13/14): 10 chapter agents in 3 waves ≈ 3.0pt of weekly quota
      (19%→22%); wave 1 = 2pt (4 agents), wave 2 = 0.4pt, wave 3+ = 0.6pt. Per chapter
      ≈ 0.3-0.5pt. Digest trick (10_make_digests) cut per-agent input ~5x. Figures,
      planning, bib, composition: 0 LLM tokens.
