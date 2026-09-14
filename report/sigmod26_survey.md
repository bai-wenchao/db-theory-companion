# SIGMOD'26 theory-usage survey

*Sources: 100 per-paper notes (`notes/sigmod26/batch_*.md`), machine-aggregated tags (`index/sigmod26_tags.md`), theory-signal index (`index/sigmod26_index.md`). Papers cited as `sigmod26-NNN` with a ≤6-word title hint; every claim traces to tags/notes. Where counts could conflict, `index/sigmod26_tags.md` (machine-aggregated) is authoritative over any reading of notes.*

## 1. Executive summary

- **Theory is a design activity at SIGMOD'26, not decoration.** Of 100 tagged papers, 54 use theory as a *design-driver* — the theorem is engineered into the algorithm/protocol — and 34 are *theory-as-contribution*, where the bounds themselves are the paper. Pure motivation (7), appendix-foundation (4), or evaluation-yardstick (1) roles are rare.
- **The property DB researchers care most about: provable cost bounds.** Upper bounds (34 papers) narrowly beat correctness (32); with probabilistic guarantees (21) and error bounds (20), the "fast, right, and accurate whp" cluster dominates everything else.
- **The toolbox trinity: reduction (23), concentration inequalities (22), induction (19)** — roughly one workhorse per property cluster (hardness/lower bounds, statistical guarantees, correctness/upper bounds). Estimation theory (13) and adversarial constructions (12) round out the top five.
- **Privacy is the biggest single theory vertical**: privacy-guarantee (14 papers) is the largest domain-specific property, powered almost entirely by DP composition (8 of 13 privacy-dp papers) plus sensitivity analysis; its lower-bound wing is the most technically aggressive work in the corpus (sigmod26-136).
- **Each domain has a distinct theoretical dialect**: DP papers speak composition algebra; query-optimization/join papers speak width measures, LP duality, and induction; ANN/vector papers speak asymptotic statistics (CLT, concentration as d→∞); LLM-DB papers mostly *formalize*, then certify sampling with concentration bounds.
- **Matching lower bounds are a badge of honor**: 15 papers prove lower bounds (3 conditional), typically paired with near-matching uppers — e.g. sigmod26-166 (near-optimal PageRank), sigmod26-243 (join-project sampling), sigmod26-178 (pure-DP histograms).
- **Eight (property, tool) pairs do most of the work** (93 pair-instances): the two workhorses are correctness×induction (16) and hardness×reduction (15).
- **Newest machinery arrives via LLM cost control**: anytime-valid confidence sequences (Waudby-Smith–Ramdas) appear in exactly the LLM-cascade papers sigmod26-236 and sigmod26-293 — an import from outside classical DB theory.
- **~11% of flagged papers are formalization-only** (definitions, no theorems), concentrated in LLM-systems and indexing papers — theory as problem statement, with results living in experiments.
- **Caveat up front**: this is the arXiv-reachable, theory-friendly ~26% of SIGMOD'26; 229 ACM-only papers are absent and the skew is toward theory (§2, §10).

## 2. Corpus & method

- **Corpus**: 385 articles = PACMMOD Vol 4 (257, rounds 3–4; ids 001–257) + Vol 3 issues 4–6 (128, rounds 1–2; ids 258–385). Research track ≈33%, plus ~17 [Experiments & Analysis] and some industrial papers.
- **Pipeline (TeX-first, zero LLM tokens in extraction)**: OpenAlex paper list → arXiv TeX e-print download (title match, difflib ≥ 0.82) → structured extraction of theorem/lemma/proof environments, bound sentences, and signal counts → per-paper score → subagent analysis notes (≤110 words/paper, fixed schema) → tag aggregation. PDF+pdftotext is the fallback; `theory/<id>.json` records provenance in `"from"` (tex vs pdf).
- **Coverage**: 156/385 papers have extractions (137 arXiv-TeX + 19 pdf-only); 107 show some theory signal; 98 flagged (≥1 proof OR ≥3 statements OR lower-bound signal + statement); **100 tagged notes** cover the flagged set in full (early batches ran against a preliminary flagged list of 88).
- **Extraction yield**: 1,284 statements (463 lemmas, 403 definitions, 302 theorems, 68 propositions, 61 corollaries, 33 claims) and 665 proofs corpus-wide.
- **Signal prevalence** (papers mentioning, not proving): big-O 96, upper-bound language 85, worst-case 73, approximation-ratio 64, lower-bound language 62, whp 27, np-hard 21, DP 16, learned-* 12, regret 1.

> **Coverage bias (read this before any number below).** `dl.acm.org` Cloudflare-blocks scripts, so arXiv is the only scalable source. Papers with arXiv preprints skew theory-friendly, and extracted text may be the preprint, not camera-ready. The **229 papers with no extraction are ACM-only** and systematically absent from every count — treat all shares as describing the theory-leaning subset, not SIGMOD'26 at large. The true venue-wide theory share is lower than reported here.

**How to query the artifact:**

| Question | Where |
|---|---|
| Title/authors/DOI for an id | `grep sigmod26-NNN data/sigmod26/papers.jsonl` (never read whole file) |
| How theoretical is paper N / which are most theoretical | `index/sigmod26_index.md` (top-30 table) + `index/sigmod26_index.csv` `score` column; ranked ids in `index/sigmod26_index_flagged_ids.txt` |
| Raw theorems/proofs/bound sentences of paper N | `data/sigmod26/theory/NNN.md` (provenance in `NNN.json`) |
| Per-paper R1–R4 reading, tags, key quote | `notes/sigmod26/batch_*.md` |
| Aggregate rankings, domain cross-tabs, (prop,tool) pairs with exemplars | `index/sigmod26_tags.md` (regenerate: `python3 scripts/06_tag_stats.py notes/sigmod26 index/sigmod26_tags.md`) |
| Synthesis (this file) | `report/sigmod26_survey.md` |

## 3. R1: How problems are modeled

Recurring formalization patterns, with exemplars:

1. **Resource-triple cost model for dynamic problems** — preprocessing time / amortized update time / enumeration delay is the standard frame for incremental maintenance and dynamic query evaluation.
   - sigmod26-155 (heavy-light join maintenance): costs parameterized by a new "maintenance width" mw(Q).
   - sigmod26-244 (maintaining CQs): amortized update time + delay, classified by hypergraph height/dimension.
   - Also sigmod26-232 (dynamic subset sampling over joins), sigmod26-371 (space/time exponents per plan class), sigmod26-255 (reclustering potential).
2. **Width measures as the complexity interface** — query difficulty compressed into one parameter against which both algorithms and lower bounds are stated.
   - sigmod26-141 (Jaguar): target bound is submodular width subw(Q,Δ,n) under degree constraints.
   - sigmod26-114 (FPT hypertree widths): tractability parameterised by k + rank + max arity.
   - Also 222 (edge-cover width for Datalog size bounds), 233 (width-1 plans ↔ acyclicity), 350 (fhtw-compatible rankings).
3. **Restricted-access oracle models over virtual inputs** — clustering/sampling/counting over a join output *without materialization*, via count/sample/report/degree oracles.
   - sigmod26-104 (relational clustering): oracles over boxes, N = |q(D)| never materialized.
   - sigmod26-243 (join-project sampling): property-testing access (tuple test, sample, degree queries).
   - Also 289 (relational clustering with outliers), 191 (indexes with degree bounds).
4. **DP neighborhood algebras** — the central modeling act is choosing the neighboring relation and budget structure.
   - sigmod26-136 (continual release): event- vs item-level, incremental vs fully dynamic.
   - sigmod26-337 (N2E): node-DP reduced to edge-DP via private degree capping.
   - Also 263 (per-record budgets ε(r)), 012 (edge-local DP across N nodes), 163 (w-event LDP), 079 (user-level DP over joins).
5. **Stream models with memory as the priced resource** — turnstile/insert-delete updates, passes, words of space, unbounded or skewed streams.
   - sigmod26-175 (trimmed statistics): linear sketches under a condition on top-k vs tail mass.
   - sigmod26-231 (Sublime): a size function W(·) trades expected error against memory on unbounded streams.
   - Also 115 (noisy streams, "mismatch ambiguity" ηp), 015 (sliding-window matrix sketches), 377 (hypergraph streams, reservoirs).
6. **Asymptotic-dimension distributional assumptions** — iid-across-dimensions embeddings, uniform queries on a hypersphere, doubling dimension; results stated as d→∞ limits.
   - sigmod26-076 (adaptive HNSW): FDL of inner-product distances converges to Normal as d→∞.
   - sigmod26-378 (TRIM): rotation-invariant models pin down the distribution of triangle bounds; distance concentration as d→∞.
   - Also 204 (uniform queries on a sphere → closed-form loss), 103/349 (doubling dimension), 359 (quantization tail bounds).
7. **Adversarial input models** — corrupted users, Yao-minimax hard distributions, engineered hard instances.
   - sigmod26-068 (poisoning under shuffle-DP): up to k̂ corrupted users inject messages.
   - sigmod26-227 (oblivious subspace embeddings): Yao's minimax fixes a hard distribution over orthonormal columns.
   - Also 166 (r-padded instances with hidden splits), 070 (UniqueOverlap 3-party problem).
8. **Semantic constraints and unproven regularity assumptions** — modeling by assumption rather than theorem.
   - sigmod26-382 (document extraction): "compliant document" assumptions license field inference.
   - sigmod26-258 (3D entity resolution): an (ε,δ)-discrepancy band assumed to hold across matching pairs.
   - Also 036 (model-capability and operator-independence hypotheses, explicitly unproven), 044 (causal-DAG conditioning).
9. **Annotation algebras** — semiring/"twomonoid"-annotated databases as the semantic base for provenance, repair, and probabilistic evaluation.
   - sigmod26-264 (unifying hierarchical queries): two commutative monoids; one elimination algorithm instantiates repair maximization, counting, and probabilistic evaluation.
   - sigmod26-290 (Codd over semirings): RA ⟺ domain-independent calculus over zero-sum-free semirings.

Cross-cutting observation: modeling choices are aggressively *engineered so the proof closes* — sigmod26-095 shapes epochs and deterministic commit so a 1SR induction goes through; sigmod26-103 designs its pruning rule so routing convergence and bounded degree are provable; sigmod26-163's budget split exists to make windowed composition work. The model is a design artifact, not a neutral description.

## 4. R2: Properties studied

Ranked list (papers proving/studying each property):

1. upper-bound — 34
2. correctness — 32
3. probabilistic-guarantee — 21
4. error-bound — 20
5. hardness — 16
6. lower-bound — 15
7. privacy-guarantee — 14
8. space-complexity — 13
9. approximation-ratio — 11
10. consistency — 4
11. conditional-lower-bound — 3
12. asymptotic-optimality, tightness, sample-complexity, convergence-rate, robustness-stability — 2 each
13. identifiability, generalization-bound — 1 each

- **Top cluster — the guarantee quartet**: upper-bound (34) + correctness (32) + probabilistic-guarantee (21) + error-bound (20). **Answer to "what property do DB researchers care most": a worst-case bound on cost, with correctness essentially tied** — i.e. "my algorithm is provably fast and provably right", and if approximate, "accurate with probability 1−δ". Space-complexity (13) extends the same instinct to memory; the streaming/sketching and join papers are its carriers (sigmod26-175, 231, 371, 232).
- **The limits cluster**: hardness (16) + lower-bound (15) + conditional-lower-bound (3) + tightness (2) — 36 tag instances establishing what cannot be done, and the culture is to pair limits with matching or near-matching uppers (136, 166, 243, 178, 259, 349, 306). Conditional lower bounds lean on k-clique/BMM/OMv (sigmod26-244), (min,+)-convolution (sigmod26-259), and Hyperclique/SETH (sigmod26-109).
- **Privacy-guarantee (14)** is the largest domain-specific property — essentially the entire privacy-dp vertical, always paired with an error/utility bound (9 papers).
- **Approximation-ratio (11)** splits between classic combinatorial approximation (350: (1−1/e) submodular diversity; 289: (2,2,O(1)) clustering with outliers; 254: (2+ε) set multi-cover) and sampling/ANN approximation (243, 175, 115).
- Rare birds: identifiability once (sigmod26-101, latent fairness attributes via tensor decomposition); generalization-bound once (sigmod26-215, LLM predicates); robustness-stability twice (sigmod26-068 poisoning, sigmod26-165 agent retries).
- Consistency (4) is confined to transactions/replication: sigmod26-095 (one-copy serializability), sigmod26-201 (linearizability under rollback attacks), sigmod26-333 (autoscaling invariants), sigmod26-282 (deadlock-freedom) — all proved by pure lemma-chain induction.
- In the taxonomy but never used: competitive-ratio, regret-bound, price-of-x, io-cost-bound, latency-throughput-bound, completeness-recall — SIGMOD'26 theory (in this subset) is not about online adversarial performance ratios or communication prices (communication-complexity *is* used, as a lower-bound tool, 3 papers).

## 5. R3: Tools used

Ranked list:

1. reduction — 23
2. concentration-ineq — 22
3. induction — 19
4. estimation-theory — 13
5. adversarial-construction — 12
6. dp-composition — 8
7. amortized-potential — 6, spectral-matrix — 6
8. duality, information-theory, exchange-greedy — 4 each
9. peeling-dyadic, sketching-theory, communication-complexity, clt-normal-approx, coresets-geometry — 3 each
10. game-equilibrium, randomized-nla, coupling-dominance, dp-optimality, delta-method — 2 each
11. martingale-azuma, fine-grained-reductions, balls-bins-hashing, kkt-optimality — 1 each

- **Top-cluster interpretation — three workhorses, one per property cluster.** Reduction (23) + adversarial construction (12) power hardness and lower bounds; concentration (22) + estimation theory (13) power probabilistic and error guarantees; induction (19) + amortized potential (6) power correctness and upper bounds. The classical DB-theory core loop is exactly this triad; heavier machinery (duality 4, information theory 4, communication complexity 3) is seasoning, not substance.
- **dp-composition (8) is a domain monoculture**: 8 of 13 privacy-dp papers use it — composition + post-processing calculus *is* the field's proof technique (298, 263, 163, 337, 136, 127, 178, 079). The interesting privacy papers are interesting *in their composition algebra* (e.g. 263's per-record budgets via geometric budget partitions).
- **Spectral/matrix analysis (6)** splits between storage structure — sigmod26-038 (Perron–Frobenius convergence of B-tree occupancy recurrences) — and similarity/learned structures (303 multi-relational clustering, 235 eigensystem partition, 015 sketch residuals, 307 Laplacian elimination).
- **Duality (4)** lives almost entirely inside query evaluation: LP duality certifies output-size bounds in sigmod26-222 and sigmod26-185 (the PANDA algorithm literally executes the dual Shannon-flow proof), selects view trees in sigmod26-155, and rounds the convexified cover in sigmod26-254.
- **Imports from outside classical DB theory** (explicit in notes):
  - **Anytime-valid inference**: Waudby-Smith–Ramdas betting/empirical-Bernstein confidence sequences as sequential stopping rules for LLM cascades — sigmod26-293, sigmod26-236.
  - Cryptographic hardness: hCLWE (SIVP/GapSVP) underwrites covert DP backdoors — sigmod26-123.
  - Tensor-decomposition identifiability from latent-class models — sigmod26-101.
  - Yao's minimax principle — sigmod26-227.
  - MSO transductions / finite-model theory (Bojańczyk–Pilipczuk lifted) — sigmod26-114.
  - Mechanism-design economics: hazard-rate dominance, KKT optimality — sigmod26-355.
- **Notable absences**: online-regret/UCB — zero uses (corpus-wide "regret" signal: 1 paper) despite learned-* signals in 12 papers; martingale arguments once (sigmod26-166, Azuma–Hoeffding on Monte-Carlo error); competitive analysis, bootstrap, Bayesian-posterior, Markov-chain, fixed-point tags — zero uses. SIGMOD'26 theory is frequentist and worst-case, not Bayesian or competitive.

## 6. Domain cross-tabs

Template question answered per domain: *what properties/tools are preferred in domain XXX?*

**privacy-dp (13 papers)**
- Properties: privacy-guarantee (13/13), error-bound (9), lower-bound (3), upper-bound (3), probabilistic-guarantee (2).
- Tools: dp-composition (8), concentration-ineq (4), estimation-theory (4), reduction (3).
- Preferred pattern: decompose the pipeline into mechanisms → per-mechanism sensitivity analysis → sequential/parallel composition + post-processing → error bound showing utility survives (sigmod26-298 cluster explanations, sigmod26-263 per-record DP, sigmod26-163 streaming LDP). The lower-bound wing imports fingerprinting codes and InnerProduct reductions (sigmod26-136, continual release).

**query-optimization (13 papers)**
- Properties: upper-bound (9), correctness (5), approximation-ratio (2), hardness (2).
- Tools: induction (5), duality (3), reduction (3), fine-grained-reductions (1).
- Preferred pattern: define a width/size measure, prove evaluation or maintenance bounds by induction, use LP duality (fractional edge covers, polymatroids) for tightness — sigmod26-222 (adorned Datalog size bounds), sigmod26-233 (width-1 plans ↔ acyclic), sigmod26-155, sigmod26-141, sigmod26-185.

**join-algorithms (8 papers)**
- Properties: upper-bound (8/8 — every join paper proves one), correctness (5), conditional-lower-bound (2), space-complexity (2).
- Tools: induction (4), adversarial-construction (2), duality (2), amortized-potential (2), communication-complexity (1).
- The same width-measure + delay-aware dialect as query-optimization, plus conditional lower bounds via k-clique/OMv (sigmod26-244) and a space-time hierarchy over plan classes (sigmod26-371).

**ann-vector-search (14 papers — largest domain)**
- Properties: probabilistic-guarantee (6), upper-bound (4), error-bound (3), space-complexity (2).
- Tools: concentration-ineq (4), estimation-theory (3), coresets-geometry (2), clt-normal-approx (2), adversarial-construction (2).
- Preferred pattern: distributional assumption (iid dimensions or doubling dimension) → CLT/concentration tail bound → confidence-parameterized pruning, recall certification, or sample sizing — sigmod26-076 (CLT-adaptive HNSW), sigmod26-378 (p-relaxed triangle bounds), sigmod26-359 (quantization tail bounds), sigmod26-173 (pilot-sized aggregate sampling). But the domain is bimodal: several systems papers are definitional-only (381, 107, 267) and one pair proves graph-size lower bounds (sigmod26-349).

**graph-db (13 papers)**
- Properties: upper-bound (7), correctness (6), lower-bound/probabilistic-guarantee/error-bound (4 each) — the most balanced profile in the corpus.
- Tools: concentration-ineq (3), adversarial-construction (3), induction (3).
- Spans worst-case-optimal enumeration (sigmod26-306, 3^{n/3}·n^k defective cliques), labelling schemes (sigmod26-307, treewidth-parameterized resistance distances), dominance-based pruning (sigmod26-291), expressiveness (sigmod26-339, = FO[TC]), and query-complexity optimality (sigmod26-166, PageRank).

**llm-db (9 papers — the semantic/LLM-query domain)**
- Properties: probabilistic-guarantee (3), correctness (3), hardness (2), robustness-stability (1), generalization-bound (1).
- Tools: concentration-ineq (3), reduction (2), induction (1).
- Split personality: 3 papers are definitional-only (sigmod26-030 code synthesis, sigmod26-228 workload generation, sigmod26-036 multi-modal analytics), while the strongest import *statistical certification* — anytime-valid sequences to stop LLM cascades (sigmod26-293, sigmod26-236), Bernstein margins for proxy predicates (sigmod26-215). Classical complexity appears as NP-hardness of cascade construction (sigmod26-236) or agentic scheduling (sigmod26-086); logic soundness backs LLM-generated test oracles (sigmod26-029); rule systems get termination proofs (sigmod26-165).

**streaming (8) + sketching (5), for completeness**
- Properties: space-complexity (5), error-bound (4), lower-bound (3), upper-bound (3); sketching adds space-complexity (4), error-bound (3).
- Tools: estimation-theory (5), concentration-ineq (4), dp-composition (2), sketching-theory (3).
- House style: unbiased estimator + explicit variance + memory lower bound, usually near-matched — sigmod26-377 (hypergraph triangles), sigmod26-231 (error–space tradeoff with entropy lower bound), sigmod26-175 (trimmed moments).

## 7. Playbook: property × tool

Top eight (prop, tool) pairs from `index/sigmod26_tags.md` — recipes of the form "to establish property X, use tool Y, as in paper <id>".

1. **correctness × induction (16)** — To certify an algorithm/protocol correct, define a state invariant and prove preservation by induction over epochs, eliminations, or recursion depth.
   - Exemplar: sigmod26-095 (epoch-based OCC) — skeleton: availability lemma (PoA ⇒ a correct replica holds the batch) → uniform-order lemma → per-epoch serializability → induction over epochs ⇒ global one-copy serializability.
   - Also sigmod26-141 (Jaguar: recursion soundness via invariant + induction), sigmod26-333 (invariants per reconfiguration transaction type), sigmod26-282 (no SLW-cycle ⇒ deadlock-free, by contradiction).
2. **hardness × reduction (15)** — To show a problem intractable, encode a canonical NP/#P-complete problem (clique, Subset-Sum, Independent Set, vertex cover, set cover) into a database instance.
   - Exemplar: sigmod26-219 (table overlap discovery) — tables as hypergraphs; maximum-clique reduction gives NP-hardness *and* O(|V|^{1−ε}) inapproximability.
   - Also sigmod26-022 (AOD repair via Subset-Sum), sigmod26-229 (cardinality repairs), sigmod26-278 (polynomial-inequality encoding ⇒ undecidability of bag containment).
3. **probabilistic-guarantee × concentration-ineq (13)** — To whp-certify a randomized algorithm, bound each bad event with Chernoff/Hoeffding/Bernstein, union-bound over events; ε, δ double as accuracy knobs and sample-size formulas.
   - Exemplar: sigmod26-166 (single-source PageRank) — Monte-Carlo discovery + Chernoff/union bound; martingale-difference error control with Azuma for the additive variant.
   - Also sigmod26-173: "P[|agg_S − agg_D| ≤ ε_S + ε_NN] ≥ 1−α" with sample sizes read straight off the Hoeffding terms.
4. **upper-bound × induction (11)** — To bound runtime/space, find a monotone measure (potential, recursion depth, alternation depth) that each step decreases by a constant factor; depth × per-step cost is the bound.
   - Exemplar: sigmod26-233 (succinct plan representations) — structural induction + ear-removal acyclicity characterizes width-1 plans, enabling O(|E(H)|³) meta-decompositions.
   - Also sigmod26-114 (elimination forests with a Dealternation Lemma bounding alternation depth for FPT width checks).
5. **error-bound × concentration-ineq (11)** — To bound estimator error: prove unbiasedness, compute variance, convert to a tail bound, propagate through estimator arithmetic.
   - Exemplar: sigmod26-231 (Sublime) — geometric-series epoch analysis + Markov/Chebyshev tracks the error–space tradeoff, matched against an entropy-incompressibility memory lower bound.
   - Also sigmod26-008 (stratified join sampling): Chebyshev propagation through stratum arithmetic + functional delta method for asymptotic optimality of the allocation.
6. **upper-bound × reduction (10)** — To get an algorithmic upper bound, reduce the task to one with a known worst-case-optimal routine (join evaluation, index probe, LP).
   - Exemplar: sigmod26-191 (Poisson sampling over acyclic joins) — algebraic rewriting to nested semijoins + geometric probe sequences ⇒ O(|db| + k log|db|).
   - Also sigmod26-243 (heavy/light partition reduces uniform sampling to index lookups); sigmod26-337 (reduces node-DP to edge-DP with error inflated only logarithmically).
7. **upper-bound × adversarial-construction (9)** — To prove a bound *tight*, build the worst-case instance family and analyze the algorithm on it; the same construction usually yields the matching lower bound.
   - Exemplar: sigmod26-306 (defective clique enumeration) — Moon–Moser-style witness graphs show the O(3^{n/3}·n^k) search space is worst-case optimal.
   - Also sigmod26-244 (color-coding families encoding k-clique into update sequences), sigmod26-166 (r-padded hard instances), sigmod26-070 (UniqueOverlap simulation).
8. **privacy-guarantee × dp-composition (8)** — To prove end-to-end DP: split the pipeline into mechanisms, per-mechanism sensitivity analysis, sequential/parallel composition + post-processing, budget allocated across stages.
   - Exemplar: sigmod26-298 (DP cluster explanations) — "alg:gen_global_explanation is (ε_CandSet + ε_TopComb + ε_Hist)-DP"; sensitivity analysis (triangle-inequality proofs, replacing standard divergences with sensitivity-1 scores) dictates which quality scores are privately usable.
   - Also sigmod26-178 (geometric mechanism + four-case dominance analysis, matching the Balcer–Vadhan ℓ∞ lower bound — the corpus's cleanest tight result).

## 8. Role of theory

Distribution across the 100 tagged papers (each paper's dominant role):

| Role | # | Share |
|---|---|---|
| design-driver | 54 | 54% |
| theory-as-contribution | 34 | 34% |
| motivation | 7 | 7% |
| appendix-foundation | 4 | 4% |
| evaluation-yardstick | 1 | 1% |

- **Design-driver dominance (54%) is the headline**: the formal result shapes the artifact. Pruning rules are designed so convergence is provable (sigmod26-103); privacy budget splits exist to make composition close (sigmod26-163); cascade thresholds are set by concentration bounds (sigmod26-293); a derived closed form *is* the index-assignment strategy (sigmod26-204); a variance-driven margin justifies the training objective (sigmod26-215). Protocol designs are contorted so an induction succeeds (sigmod26-095, sigmod26-333).
- **theory-as-contribution (34%)**: a full third of tagged papers are results-first — dichotomies (sigmod26-109 min/max CQs, sigmod26-278 bag semantics), tractability frontiers (sigmod26-375 Shapley over aggregate CQs, sigmod26-350 diversity), space-time hierarchies (sigmod26-371), a pure lower-bound paper (sigmod26-227), classical theorems transported to new settings (sigmod26-290 Codd over semirings). These papers monopolize the top of the score table.
- **The residual roles are marginal (12 papers combined)**: motivation-only (sigmod26-219, sigmod26-299, sigmod26-086, sigmod26-130 — hardness cited to license heuristics; sigmod26-107, sigmod26-228 — formal framing before a heuristic system; sigmod26-036 — assumptions stated and used unproven), appendix-foundation (sigmod26-201, sigmod26-279, sigmod26-287, sigmod26-381 — proofs or definitions certifying/scaffolding a systems contribution), and exactly one evaluation-yardstick (sigmod26-267 — the OPT cache policy as a theoretical baseline for disk reads). In this corpus, if a paper has theory, it *uses* it; theory is rarely mere framing or afterthought.
- Caveat: papers whose extracts contain only definitions were still assigned design-driver or motivation roles — the "theory" there is formalization, not results (see §9). Discounting those, the design-driver share softens to roughly 45%.

## 9. Other findings

- **Thin-extract share — theory as formalization-only (11/100)**: sigmod26-107 (graph-index merging), sigmod26-228 (LLM SQL workloads), sigmod26-036 (multi-modal analytics), sigmod26-207 (learned cost model), sigmod26-258 (3D entity resolution), sigmod26-267 (out-of-core graphs), sigmod26-365 (substring cardinality), sigmod26-381 (GPU filtered search), sigmod26-030 (function synthesis), sigmod26-312 (temporal IR), sigmod26-358 (column annotation) contain definitions but no proven theorems. They cluster in llm-db (030, 228, 036), ann/vector systems (107, 381, 267), and indexing/data-integration (365, 312, 258, 358). Formalization frames the system; the evidence is experimental.
- **Taxonomy gaps (free-text tags that recurred)**:
  - semiring/provenance algebra — sigmod26-264, 290, 371 (3 papers; no controlled tag).
  - LP relaxation + rounding — sigmod26-289, 337, 254 (only partially caught by `duality`).
  - causal-DAG reasoning — sigmod26-043, 044.
  - anytime-valid confidence sequences — sigmod26-236, 293.
  - doubling-dimension/covering geometry — sigmod26-103, 349, 289 (partial overlap with `coresets-geometry`).
  - one-off gems: Wasserstein distance (228), Hall's matching (255), reservoir-sampling lemmas (377), automorphism groups (009), uniform-sphere integration (204).
  - Suggested additions: `semiring-algebra`, `lp-rounding`, `confidence-sequences`, `causal-graph`.
- **Tagging misses**: `group-symmetry` and `moment-analysis` sit unused in the taxonomy while note-writers reached for free-text equivalents (sigmod26-009 "+ automorphism-group", sigmod26-196 "+ special-function moment analysis") — the controlled vocabulary and the free text drifted apart. `fine-grained-reductions` was tagged once (sigmod26-244) though sigmod26-109 uses the same machinery under free text.
- **Noise observations**: definitions are 403/1,284 (31%) of captured "statements", so statement counts overstate theorem density; pdf-derived extracts bleed prose/captions into statements (185, 123, 229, 005, 278, 312, 258) and contain empty proof stubs (107, 267, 381); one paper's statements failed to capture entirely while its proofs carried the content (sigmod26-235); `np_hard` signals can come from related work rather than results (flagged as noise in 354, 303); score components double-count (a paper rich in bound *sentences* scores high without proportionally more proofs).
- **Surprising findings**:
  - Regret/online-learning machinery is essentially absent (1 corpus signal, 0 tag uses) even though 12 papers mention learned components — learning enters SIGMOD'26 theory through concentration bounds, not regret analysis.
  - The transactions/consistency cluster (095, 201, 333, 282) proves exclusively by induction and lemma chains — zero probabilistic machinery anywhere near serializability.
  - The newest inferential machinery in the corpus (e-values, anytime-valid confidence sequences) enters precisely at the LLM-cost boundary — statistical testing deployed to decide *when to stop calling an LLM*.
  - Corpus-wide whp language appears in 27 papers but Bayesian tools in zero — the theory culture is fully frequentist.
  - The top of the score table reconstructs the classic theory enclaves: privacy under continual release (sigmod26-136), trimmed-moment sketching (sigmod26-175), hypertree-width FPT (sigmod26-114), space-time join hierarchies (sigmod26-371).

## 10. Limitations & next steps

- **Coverage bias is the main threat to external validity**: 229/385 papers (60%) have no extraction because ACM blocks scripted access; the 156 extracted skew toward arXiv-posting (theory-friendly) authors. All shares describe the theory-leaning subset; the true SIGMOD'26 theory share is lower. Extracts may be preprints rather than camera-ready versions.
- **Flagging bias**: the flag threshold (proof/statement counts) plus definition-heavy extracts means some "tagged" papers carry formalization only, while genuinely light-theory extracted papers are under-sampled — the 58 extracted-but-unflagged papers were never read closely.
- **Depth limits**: ≤110 prose words per paper; quotes and judgments come from extracts, not full papers; role and tags are one analyst's call per paper (no double-coding, no inter-rater check).
- **Aggregate caveats**: property/tool counts are per-paper tags, not per-theorem; a paper proving many theorems counts once; free-text tags are excluded from rankings by construction (§9 shows what that hides).
- **Next steps**:
  1. Generate a manual-fetch list for the 229 ACM-only papers (download attempts are logged in `data/sigmod26/manifest.jsonl`); browser-session or institutional-access fetching would close the largest gap and let the bias be measured, not just asserted.
  2. Extend the pipeline to SIGMOD'25 (Vol 2 i4–6 + Vol 3 i1–3) and SIGMOD'24 (Vol 1/2 — volume split to verify) for a longitudinal view; all scripts are venue-parameterized (`01`–`06`).
  3. Fold the §9 free-text recurrences into the tag taxonomy and re-run `scripts/06_tag_stats.py` for consistent cross-venue comparisons.
  4. Optional: a cheap abstract-only classification pass over the 229 absent papers to quantify how theory-friendly the missing mass actually is.
