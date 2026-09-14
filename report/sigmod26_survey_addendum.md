# SIGMOD'26 survey — full-corpus addendum

*Baseline: `report/sigmod26_survey.md` (100 notes, arXiv-reachable subset).
This addendum covers the full corpus: 385/385 papers fetched (229 ACM-only camera-ready PDFs via
CDP Chrome), 226 flagged, **228 tagged notes** — waves 3–5 added batches w3a–d, w4a–d, w5a–b
(128 new papers). Aggregates from `index/sigmod26_tags.md` (228 papers, authoritative).
Cohort splits and PODS carvings were computed for this addendum by re-parsing the notes
(split on `^### `, trim `+ free` suffixes); commands cited inline. Papers cited as `sigmod26-NNN`.*

## 1. What changed at full coverage

Properties (baseline 100 → full 228, `index/sigmod26_tags.md`):

- correctness 32 → **98** — #2 → **#1** (43% of papers)
- upper-bound 34 → 75 — #1 → #2
- probabilistic-guarantee 21 → 42 — #3 stable
- hardness 16 → 36 — #5 → #4 (2.25×, exactly the corpus-growth rate)
- error-bound 20 → 35 — grows only 1.75× (under-represented in the new mass)
- lower-bound 15 → 31; privacy-guarantee 14 → 26; approximation-ratio 11 → 26 (now tied #7–8)
- space-complexity 13 → 24
- tightness 2 → 11 — **5.5×**: the matching-lower-bound culture scales
- from zero: competitive-ratio 2, regret-bound 2, io-cost-bound 2, price-of-x 1, completeness-recall 1

One-line interpretations:

- **Headline flip: correctness overtakes upper-bound.** The baseline's "provably fast beats
  provably right" was an artifact of the theory-heavy sample. The ACM-only cohort proves its
  algorithms correct (51% of its papers) far more often than it bounds them (32%).
  Full-corpus answer to R2: *first correct, then fast.*
- **Hardness 16→36 at flat share (16%)** — NP-hardness is exactly as dense in the ACM-only mass;
  it is the standard license for heuristics in community-search/repair/mining papers
  (sigmod26-283, sigmod26-224, sigmod26-316).
- **The baseline's "never used" taxonomy slots all activated** — competitive-ratio
  (sigmod26-242 ski rental, sigmod26-094 ML-oracle enumeration), regret-bound (sigmod26-140
  bandit discretization, sigmod26-221 windowed repair), io-cost-bound (sigmod26-147,
  sigmod26-323 learned indexes), price-of-x (sigmod26-098 fair Count-Min). "SIGMOD'26 theory
  is not about online ratios" was a sample-size artifact — though at 2 papers each these remain
  niches, entering through systems doors (when-to-adapt, when-to-stop) not classic online algorithms.
- **Tools**: reduction 23→52 (#1 stable; 22–23% of papers in both cohorts), concentration 22→39
  (share 22%→17%), induction 19→37, estimation 13→28, dp-composition 8→18.
  **exchange-greedy 4→17 is the big riser** (4.25× — greedy submodularity/Set-Cover certificates
  in the ACM systems mass); dp-optimality 2→7, balls-bins-hashing 1→5.
- **Domains**: graph-db 13→56 (now 25% of all notes — the dominant dialect); storage-compression
  ~→14, indexing 6→15, time-series →8, spatial →9 are new cross-tab columns; llm-db 9→13 only.
- **Roles**: design-driver 54%→66%, theory-as-contribution 34%→25% (§2, §3).
- **Extraction totals**: 2,405 statements (663 theorems, 761 lemmas, 649 definitions) and
  1,130 proofs (`index/sigmod26_index.md` "Statements by kind"; proofs = Σ`n_proof` in
  `index/sigmod26_index.csv`), vs 1,284/665 at baseline; `regret` signal 1→6 papers,
  `competitive` 0→5 (same files).

## 2. The bias test: arXiv subset vs ACM-only cohort

Cohorts (by `grep -c '^### sigmod26-'` over the two batch-file sets):

- **A** = pilot + 01_10 + 11_20 + 21_30 + 31_40 + w2a–d — **100 notes**, mostly arXiv-TeX extracts.
- **B** = w3a–d + w4a–d + w5a–b — **128 notes**, all CDP-fetched ACM camera-ready PDFs.

| dimension | A (n=100) | B (n=128) | verdict |
|---|---|---|---|
| flag rate at extraction | 98/156 = 63% | 128/229 = 56% | mild skew, held |
| mean flagged score | 27.2 | 16.4 | arXiv ≈ 1.7× denser |
| theory-as-contribution role | 34% | 18% (23) | held, ~2× |
| design-driver role | 54% | 76% (97) | — |
| top property | upper-bound 34% ≈ correctness 32% | correctness 51% (66) ≫ upper 32% (41) | **inverted mix** |
| statistical props (prob+error) | 41% | 27% | over-sampled in A |
| concentration-ineq | 22% | 13% | over-sampled in A |
| exchange-greedy | 4% | 10% | under-sampled in A |
| reduction | 23% | 22% | identical |
| graph-db share | 13% | 34% (43) | under-sampled in A |
| llm-db share | 9% | 3% (4) | over-sampled in A |
| formalization-only props line | 11/100 | 7/128 (5%) | thin share halved |

(Shares from the cohort parser over concatenated batch files; roles via
`grep '^role:' | cut -d' ' -f1 | sort | uniq -c` per cohort.)

**Verdict: the old caveat was right about depth, wrong about direction, and partly mis-attributed.**

- **Held (depth).** The arXiv cohort really is theory-denser: 63% vs 56% flag rate, 1.7× mean
  score, 2× theory-as-contribution share. The venue-wide share of results-first theory is
  lower than the baseline reported.
- **Inverted (mix).** The ACM-only mass is not diluted theory — it carries a *different* theory
  (graph-systems correctness, combinatorial greedy, amortized maintenance) that **changed the
  #1 property**. The bias was in *which* theory, not only *how much*.
- **Mis-attributed.** 18 of cohort A's 100 notes are PODS articles (§3) — a chunk of the
  "arXiv theory-friendly skew" was **PODS contamination** inside PACMMOD Vol 4. Excluding PODS,
  cohort A's mean score drops 27.2→21.3; the residual arXiv-vs-ACM gap (21.3 vs 16.4) is real
  but modest.

## 3. PODS contamination

- **The entire PODS'26 section is inside the corpus.** PACMMOD Vol 4 No 2 is the PODS issue —
  confirmed by its own editorial inside the corpus (sigmod26-184, "PACMMOD, V4, N2 (PODS),
  May 2026"). Every article with DOI 10.1145/3801890–3801919 — **29 research articles** besides
  the editorial — was fetched as "sigmod26", and **all 29 are among the 228 noted papers**
  (12.7% of notes; DOI band from `data/sigmod26/papers.jsonl`).
- Consumer agents marked only 5 as PODS/PODS-style (`grep -i pods notes/sigmod26/*.md`):
  sigmod26-021, 049, 135, 205, 253. The DOI band completes the list, adding sigmod26-004,
  011, 038, 053, 070, 104, 109, 114, 115, 136, 141, 155, 166, 175, 177, 178, 185, 222, 227,
  232, 241, 243, 244, 247.
- **The baseline survey's flagship exhibits were PODS papers all along**: sigmod26-136
  (continual-release lower bounds), 175 (trimmed-moment sketching), 114 (FPT hypertree width),
  222 (adorned Datalog), 243 (join-project sampling), 244 (maintaining CQs) all sit in the band.
- **13 of the current top-20 score table and 21 of the top-50 are PODS**
  (`index/sigmod26_index.csv`).
- **With PODS removed (n=199, parser re-count)**: correctness 92 (46%) is still #1 — **the
  correctness flip survives the carve-out and is a genuine SIGMOD-proper fact**; upper-bound 56,
  probabilistic-guarantee 38, hardness 34, error-bound 33. But the limits cluster collapses:
  lower-bound 31→19, tightness 11→4; theory-as-contribution 57→30 (25%→15% of papers);
  query-optimization 20→11, join-algorithms 10→4, privacy-dp 26→20; dp-composition 18→13,
  adversarial-construction 22→14. hardness×reduction stays the #1 pair either way (32→30).
- Directionally: **PODS carries the lower-bound/tightness culture and most of the QO/join
  theory enclave; SIGMOD-proper carries correctness, probabilistic certification, and greedy
  approximation.**

## 4. Updated domain cross-tabs & playbook deltas

Biggest domains (tags.md DOMAIN×PROPS / DOMAIN×TOOLS), and what w3–w5 added:

- **graph-db 13→56** — correctness 36, upper-bound 25, hardness 9; reduction 14, induction 12.
  The ACM-only mass is graph-*systems*: community/biclique search (sigmod26-283 NP-hard + no-APX,
  sigmod26-372 worst-case O(m·1.348^n), sigmod26-158 O(m·α^n + nβ)), core maintenance
  (sigmod26-179 insertion-unbounded vs deletion-bounded asymmetry, sigmod26-006, sigmod26-257),
  and correctness-of-index lemmas everywhere. The baseline graph dialect (WOJ enumeration,
  labelling schemes) is now a minority wing.
- **privacy-dp 13→26** — privacy-guarantee 24, error-bound 12; dp-composition 18/26 = 69%
  (deeper monoculture than baseline's 62%). New ACM-side privacy is pipeline *accounting*
  (sigmod26-348 RDP graph synthesis, sigmod26-195 PATE-style LLM distillation, sigmod26-340
  LDP federated recommendation, sigmod26-082 LDP biclique counting), not new mechanisms.
- **streaming 8→23** — upper 10, space 9, correctness 8; estimation-theory 9. Split between a
  pure-theory wing (sigmod26-314 state-change optimality, sigmod26-247 ℓp sampling) and
  estimator systems (sigmod26-199 duplicate-aware KLL "never worse" guarantee, sigmod26-362).
- **ann-vector-search 14→25** — prob 10, upper 7. New papers are correctness/structure-oriented
  (sigmod26-305 constant-degree sphere graphs, sigmod26-083 monotone OOD routing,
  sigmod26-088 optimal merge order): the CLT culture is now only half the domain.
- **New cross-tab columns**: storage-compression 14 (correctness 8: sigmod26-142 lossless FP,
  sigmod26-137 LZ4, sigmod26-116 compare-less compaction), indexing 15, time-series 8, spatial 9,
  transactions 6, consensus-replication 5 — all dominated by component-correctness lemmas.

**(prop,tool) playbook reshuffle**: correctness×reduction 17 enters the top-8 at #7;
error-bound×estimation-theory 16 joins the #8 tie with privacy-guarantee×dp-composition 16;
upper-bound×adversarial-construction (baseline #7 with 9) grows to 13 but drops to #11.
Risers just outside: hardness×exchange-greedy 10, approximation-ratio×exchange-greedy 9,
upper-bound×amortized-potential 10 (all ≤4 at baseline).
Full top-8 (tags.md): hardness×reduction 32, correctness×induction 29,
probabilistic×concentration 25, upper×induction 21, upper×reduction 20, error×concentration 18,
correctness×reduction 17, privacy×dp-composition / error×estimation 16 each.

**New recipes from w3–w5 exemplars** (none in the baseline playbook):

1. **Rare-event bounding by potential function** (× amortized-potential — sigmod26-223,
   sigmod26-050, sigmod26-110, sigmod26-180). Define Φ rising O(1) per cheap operation and
   resetting on the expensive event; frequency follows: GK sketch size ≤ 2s·ln(n/s+2)
   (sigmod26-223); a second BeTree root split needs amortized Ω(b^{h+2}) insertions
   (sigmod26-050). The ACM systems mass's favorite proof that rebuilds/compression are free.
2. **NP-hard selection → exchange-greedy with a certificate** (× exchange-greedy —
   sigmod26-224, 367, 220, 245). Reduce from Set Cover / k-median, prove metric-or-submodularity,
   inherit the factor: log-guarantee chunk merging for long-context QA (224), (1−1/e) data
   forgetting (367), harmonic H(R_max) PII shielding (220), 2-approximation via triangle
   inequality (245).
3. **Ski-rental competitive analysis for when-to-commit decisions** (× competitive-analysis —
   sigmod26-242, sigmod26-094). Cast a tuning choice as rent-vs-buy: adapt-after-⌊α⌋ is
   2-competitive with a closed-form golden-ratio threshold α=0.618 (242); ML-oracle confidence
   thresholds earn competitive ratios vs offline OPT (094).
4. **Regret certification of windowed/bandit online modes** (× online-regret — sigmod26-221,
   sigmod26-140). Bound regret by exponential window decay (online repair R_n ≤ n·e^{−β(W+1)},
   221) or reduce the search to a K-armed bandit and inherit O(K√(T log T)) (140).

## 5. New taxonomy gaps & new findings

New topics outside the vocabulary (all forced into `+ free` tags):

- **machine-unlearning** — sigmod26-367 (budgeted submodular data forgetting).
- **knowledge-compilation** — sigmod26-250 (d-DNNF/SDD circuits underpin the De Finetti-logic
  posterior; the corpus's first knowledge-compilation paper).
- **DeFi routing** — sigmod26-180 (exchange-graph order routing with KLL-sketch admission;
  an application-track paper with amortized-potential proofs).
- **neural-network querying** — sigmod26-205 (IFP(SUM) over weighted structures; sIFP captures
  PTIME via Immerman–Vardi; CFI + pebble-game inexpressibility — a PODS article).
- Suggested additions to the taxonomy: `unlearning`, `knowledge-compilation`, `finance-routing`,
  `nn-querying`.

Baseline gaps that persist: semiring-algebra (264/290/371), LP-rounding, confidence-sequences
(236/293), causal-graph. Two baseline "tagging misses" fixed themselves at scale:
`group-symmetry` now used (sigmod26-004 automorphism trees) and `moment-analysis` 0→3
(sigmod26-262 dilogarithm variance, sigmod26-247). Still zero uses: `bootstrap-resampling`,
`fixed-point-contraction`; `latency-throughput-bound` is the only never-used property left.

New free-text recurrences from w3–w5 (tag candidates): branching-recurrence analysis
(sigmod26-158 with α≈1.3954, sigmod26-308 with λ_s<2 — the graph-enumeration community's
shared calculus), min-plus TTF algebra (325), Ising/QUBO energy encodings (329), GPU work-span
analysis (118), closed-form cost models (146, 323, 147), entropy/capacity gating of
LM-approximated predicates (237).

Surprising patterns:

- **RDP/f-DP/zCDP accounting arrives en masse**: 5 of the new privacy papers use Rényi-style
  calculus (sigmod26-049, 135, 195, 253, 348 — `grep -l 'Rényi\|RDP\|zCDP' notes/sigmod26/*.md`)
  vs 3 in the baseline (079, 127, 279). Privacy proofs are shifting from pure (ε,δ) sums to
  divergence arithmetic.
- **PODS-style enclave at the top of the score table**: 13 of the top-20 scores are PODS
  articles; within the new ACM-only mass, the highest scores belong to pure streaming/sketching
  theory (sigmod26-314 = 63, sigmod26-247 = 54, 357, 241) — a theory stratum far above the
  systems papers (scores 5–15).
- **Systems papers' component-correctness lemma culture**: the modal B-cohort paper proves one
  or two preservation/monotonicity/safety lemmas certifying a single module, then moves on —
  monotone approximate timestamps (315), comparison-free merge correctness (116),
  order-independent index construction (010), sharing-safety of reused blocks (035),
  lazy-checkpoint soundness (331). This is *why* correctness is #1: thousands of small
  invariants, not big theorems.
- **Fairness by equation**: sigmod26-098 sizes Count-Min columns so both groups get equal
  *expected* error (price-of-fairness < 0) — calibration as the entire formal content.

## 6. Revised limitations

- **Coverage is closed**: 385/385 fetched (229 ACM-only via CDP, camera-ready), 226 flagged,
  228 noted. The baseline's 60%-missing caveat is retired, replaced by the measured bias test (§2).
- **PODS mixing is the new biggest external-validity threat**: 29/228 notes (12.7%) are PODS'26
  articles; every "SIGMOD'26" claim in both reports is 12.7% PODS by note count and far more by
  theory mass (39% of lower-bound tags, 64% of tightness, 47% of theory-as-contribution roles).
  Cross-venue comparisons must carve out the DOI band 10.1145/3801890–3801919.
- **pdf-derived extraction noise for 248 papers**: unicode-mangled math (explicitly flagged for
  sigmod26-131 "heavily mangled", also 081, 013), captions/table fragments inside statements
  (019, 081, 128, 251), proofs captured without their theorems (138) and theorems without
  proofs (195, 235 in baseline). All of cohort B carries this noise; the 137 TeX extracts do not.
- **No inter-rater check across waves**: ~15 consumer agents wrote 19 batch files with no shared
  calibration; role clauses drifted (tags.md's role section contains mangled entries), and PODS
  was spotted by only 5 of 29 papers' writers.
- **Camera-ready vs preprint divergence**: the 137 TeX-derived extracts are arXiv e-prints
  (possibly v1/v2) while the 248 pdf-derived ones are camera-ready ACM versions — one analysis,
  two document generations.
- **Flag threshold still admits formalization-only papers** (649 definitions corpus-wide);
  the 159 extracted-but-unflagged papers remain unread.

## 7. Bottom line

- **Most-studied property**: correctness (98/228, 43%) — the full corpus flips the baseline
  ranking; SIGMOD'26 theory is first about proving the artifact right, with upper-bound (75)
  the strong second. The flip survives removing PODS (92/199).
- **Most-used tools**: the trinity holds — reduction (52), concentration (39), induction (37) —
  but the riser is exchange-greedy (4→17), the certificate of choice for NP-hard selection;
  statistical tools (concentration/estimation/CLT) shrink from ~35% to ~25% of papers.
- **Strongest domain dialects**: graph-db (56; hardness → exact branch-and-bound → index
  correctness), privacy-dp (26; dp-composition 69% monoculture, now Rényi-flavored),
  streaming/sketching (35; unbiased estimator + matching lower bound), ann-vector (25; split
  between CLT certification and structural correctness).
- **Playbook headline**: hardness×reduction (32) and correctness×induction (29) are the twin
  workhorses; new recipes: amortized-potential event bounding, greedy-with-certificate,
  ski-rental adapt decisions, bandit/decay regret windows.
- **Theory's role**: design-driver even more dominant at full coverage (66%; 76% in the ACM-only
  cohort) — but that hides two strata: a PODS/pure-theory enclave (13 of the top-20 scores) and
  a systems mass proving one component lemma per paper.
- **The old bias caveat, resolved**: the arXiv skew was real in depth (1.7× score, 2×
  results-first share) but wrong in kind — the ACM-only mass supplied the correctness surge and
  the combinatorial-greedy dialect; and a third of the baseline's apparent theory-friendliness
  was PODS contamination inside Vol 4, now fully bounded at 29 papers.
