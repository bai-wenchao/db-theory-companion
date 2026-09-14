# batch_w2b — consumer wave 2b, queue lines 14-26 (13 papers)

### sigmod26-339 — Expressiveness of Languages for Querying Property Graphs in Relational Databases
domain: graph-db
props: correctness | + expressiveness-separation
tools: induction | + FO[TC]-translations-and-locality
modeling: Property graphs encoded as six-relation relational "property graph views"; a query language with a dynamic graph-view constructor, path vs endpoint pattern semantics, compared against FO[TC] and the transitive-closure arity hierarchy.
properties: Expressiveness chain of equalities and strict inclusions culminating in FO[TC]; endpoint/path semantics equivalence; evaluation NL-complete; inexpressibility of alternating-color paths and non-semilinear path lengths.
usage: Bidirectional structural-induction translations prove equivalences; Gaifman-Vardi locality, Presburger arithmetic, and Immerman's collapse theorem establish strict separations.
role: theory-as-contribution — the expressiveness characterization is the paper.
quote: "Corollary (Expressive equivalence). In terms of expressiveness, [the language] = FO[TC]."

### sigmod26-349 — Proximity Graphs for Similarity Search: Construction, Lower Bounds, Euclidean Separation
domain: ann-vector-search
props: lower-bound | upper-bound | probabilistic-guarantee
tools: adversarial-construction | coresets-geometry
modeling: (1+ε)-proximity graphs over n points in metric spaces with doubling dimension λ and aspect ratio Φ; greedy navigation; size, query-time, and construction-cost tradeoffs.
properties: Ω(n log Φ) and Ω(s^d·n) edge lower bounds in doubling metrics regardless of query time; Euclidean upper bound O((1/ε)^λ·n) edges with polylog query time and whp construction.
usage: Covering-net decompositions yield sparse constructions; adversarial point sets give size lower bounds; a log-drop distance-descent lemma bounds greedy query paths.
role: theory-as-contribution — lower/upper bounds and the Euclidean separation are the headline.
quote: "there is a set P of Θ(n) points ... such that any 2-PG for P must have Ω(n log Φ) edges, regardless of the query time allowed."

### sigmod26-382 — Visual Template Inference for Data Extraction from Documents
domain: data-integration + document-extraction
props: hardness | correctness
tools: reduction | + log-likelihood-linearization
modeling: Documents as phrases with location vectors; true/inferred templates as typed node structures; "compliant document" assumptions; row labeling as probabilistic assignment over K/V/KV/M labels.
properties: Row labeling NP-hard via vertex-cover reduction; extraction correctness under correct template inference plus compliance; record-completeness recovery; labeling objective equivalent to a linear form.
usage: Reduction motivates heuristic solvers; perfect-match/partial-match propositions justify alignment-based field inference; log-likelihood linearization enables integer-program labeling.
role: design-driver — hardness and compliance conditions shape the extraction pipeline.
quote: "Theorem. Row labeling is NP-hard."

### sigmod26-293 — Cut Costs, Not Accuracy: LLM-Powered Data Processing with Guarantees
domain: llm-db
props: probabilistic-guarantee | error-bound | lower-bound
tools: concentration-ineq | estimation-theory
modeling: Dataset with proxy scores and LLM-oracle labels; cascade threshold chosen from k sampled labels to meet recall target T with failure probability δ; score-monotone sampling; (α,β)-calibrated proxies.
properties: Any-time confidence sequences bound recall/precision violation probabilities; precision lower bounds for any score-monotone sampling algorithm meeting recall; binomial-tail-adjusted targets correct targets whp; importance-weight variance bounds.
usage: Betting/empirical-Bernstein confidence sequences (Waudby-Smith–Ramdas style) become sequential stopping rules; binomial tail calibration; importance-sampling variance analysis.
role: design-driver — the statistical tests directly drive stopping and threshold choice.
quote: "use at most k oracle calls to find a cascade threshold θ such that P(R_D(θ) < T) ≤ δ"

### sigmod26-377 — Triangle Counting in Hypergraph Streams: A Complete and Practical Approach
domain: streaming
props: correctness | error-bound | space-complexity
tools: estimation-theory | + reservoir-sampling
modeling: Hypergraph stream as edge sequence; memory-bounded reservoir sampling (single or partitioned subsets); hyper-vertex (inner/hybrid/outer) and hyper-edge (CCC/TCC/TTC/TTT) triangle notions.
properties: Unbiasedness of every estimator at any time t; variance upper bounds via sampling ratios; O(M) space; per-element processing time with harmonic-log replacement factor.
usage: Equal-inclusion-probability reservoir lemma underpins unbiasedness; direct variance computation; harmonic-sum accounting bounds replacements.
role: design-driver — estimators engineered so the analysis closes; theorems validate practicality.
quote: "Algorithm [1] provides an unbiased estimate of hyper-vertex triangle count. Specifically, E[ĉ] = c."

### sigmod26-263 — A General Framework for Per-record Differential Privacy
domain: privacy-dp
props: privacy-guarantee | error-bound | probabilistic-guarantee
tools: dp-composition | peeling-dyadic
modeling: Record-dependent privacy budget function ε(r); PrDP/PrLDP definitions; privacy-specified domains forming a geometric budget partition; down-neighborhood optimality as error benchmark.
properties: Parallel/sequential composition and post-processing for PrDP; black-box conversion of any DP/LDP mechanism with error inflated only by O(1/ε_min·log log); count/sum error bounds w.p. 1−β; √n factor in the local model.
usage: Doubling budget partition plus per-slice Laplace; union bounds; composition lemmas; down-neighborhood lower bounds gauge near-optimality.
role: theory-as-contribution — the framework and its guarantees are the contribution.
quote: "|Q̂(D) − Q(D)| ≤ |Q(D)−Q(D')| + Err_M(D', ε_min(D)/4, β/2), where D' is obtained by removing O(1/ε_min(D)·log log(·/β)) records"

### sigmod26-355 — Reliable and Private Utility Signaling for Data Markets
domain: data-market
props: probabilistic-guarantee | privacy-guarantee | + payoff-dominance
tools: game-equilibrium | kkt-optimality
modeling: Seller prices a dataset against buyer valuation distributions F, F0; utility signaling mechanism discloses dataset utility measured on the buyer's test data; hash-challenge verification over k blocks; MPC-based computation.
properties: (t/k, 1−((k−t)/k)^c)-AoI detection guarantee; unique optimal price under log-concavity; price drops and buyer/seller payoffs improve under hazard-rate dominance.
usage: First-order conditions with log-concavity give uniqueness; hazard-rate dominance drives comparative statics; exhaustive purchase-case analysis; hypergeometric challenge probability.
role: design-driver — economic and detection analysis justify the mechanism design.
quote: "Given total number of data blocks be k, number of falsified blocks be t, number of challenged blocks be c, HashVeri_AP achieves (t/k, 1−((k−t)/k)^c)-AoI."

### sigmod26-254 — Weighted Set Multi-Cover on Bounded Universe and Package Recommendation
domain: + package-recommendation
props: approximation-ratio | upper-bound
tools: duality | + piecewise-linear-convexification
modeling: Weighted set multi-cover with universe |G|=O(1) and per-item demands; objective convexified via per-family piecewise-linear convex functions; fair cover and top-k package recommendation as applications.
properties: Exact O(n^{|G|+1}) algorithm; 2-approximation in O(nL(n)); (2+ε)-approximation in O(n log n + L(log W)); naive greedy uses at most |G|·k sets.
usage: LP relaxation of the convexified problem, solved then rounded using a bounded residual r; ε-piecewise-linear convex approximation with O(log·log/ε) pieces speeds the LP.
role: theory-as-contribution — approximation algorithms are the paper; applications secondary.
quote: "there exists a (2+ε)-approximation algorithm for the problem that runs in O(n log n + L(log W)) time"

### sigmod26-363 — SplineSketch: Even More Accurate Quantiles with Error Guarantees
domain: sketching
props: error-bound | correctness
tools: amortized-potential | sketching-theory
modeling: k-bucket quantile sketch with monotone cubic-spline interpolation, split/join operations, protected thresholds, epoch initialization; merge tree for mergeability; Misra-Gries filtering of heavy items.
properties: Invariant that a joinable bucket pair always exists (streaming and merge settings); per-threshold rank error O(log α·n/k), mergeable version O(log(n/k)·n/k); spline lemma P(1/2)∈[0.067,0.933]; O(k log k) maintenance.
usage: Potential function over bucket counters bounds splits; rank error charged along split history; coefficient-feasibility argument for the spline lemma.
role: design-driver — worst-case analysis validates the heuristic split/join policy.
quote: "for any threshold σ_i of the final sketch, ε^n(σ_i) ≤ O(log α·n/k)"

### sigmod26-378 — TRIM: Triangle-Inequality-Based Pruning for High-Dimensional Vector Similarity Search
domain: ann-vector-search
props: probabilistic-guarantee
tools: concentration-ineq | delta-method | clt-normal-approx
modeling: i.i.d. random-vector model in E^d; landmark-based triangle lower bound |δ(l,q)−δ(l,x)|; p-relaxed lower bound function with tunable confidence γ; distance concentration as d→∞.
properties: Strict triangle bound degenerates to zero in probability; rotation invariance pins down the bound statistic's distribution; exact CDF of Z² calibrates the relaxed bound's confidence.
usage: Chebyshev plus delta method prove concentration; CDF transformation calculus derives p; landmark generation equated to product quantization minimizing MSE.
role: design-driver — statistical analysis sets the relaxed pruning parameter.
quote: "g(x,q,l) is a p-relaxed lower bound function if it satisfies P(g(x,q,l) ≤ δ(q,x)²) = p"

### sigmod26-291 — Continuous Subgraph Matching via Cost-Model-based Dynamic Vertex Dominance Embeddings
domain: graph-db
props: correctness
tools: + monotone-vector-dominance
modeling: Dynamic graph as timestamped edge insert/delete stream; continuous subgraph matching maintains per-pattern answer sets; vertex dominance embeddings (label base vector || neighbor-sum vector) indexed in a cell synopsis with MBRs and degree-grouped upper bounds; cost model.
properties: Dominance monotonicity — star-substructure embeddings componentwise dominated by the full star's embedding, preserved under the optimized combination; safe MBR-range and embedding-dominance pruning lemmas (no false dismissals).
usage: Componentwise monotone neighbor sums make dominance order-theoretic, enabling cell and vertex pruning; cost model allocates embedding effort.
role: design-driver — dominance theory certifies the pruning-heavy index.
quote: "any cell C or vertex v_i can be safely pruned, if o'(q_i) does not dominate any portion of cell C or embedding upper bound vector v_i.UB_δ"

### sigmod26-279 — Benchmarking Differentially Private Tabular Data Synthesis: [Experiments & Analysis]
domain: privacy-dp | benchmark
props: privacy-guarantee | error-bound
tools: dp-composition | information-theory
modeling: Benchmark of DP tabular-data synthesis pipelines; Rényi-DP as the accounting formalism; sensitivity, Gaussian/Exponential mechanisms, PrivTree, rare-value merge; quality measured by KL-divergence error of marginal estimates.
properties: Standard RDP toolkit — composition, post-processing, RDP→(ε,δ) conversion, per-mechanism RDP guarantees; KL error of conditional estimation never exceeds that of independent estimation.
usage: RDP accounting assigns budgets across pipeline stages; KL convexity/chain-rule lemma proves the estimation-ordering theorem; no proofs in extract — statements imported from prior work.
role: appendix-foundation — recalled theory scaffolds the benchmark; experiments are the contribution.
quote: "the KL divergence error of conditional estimation is always no larger than that of independent estimation"

### sigmod26-333 — Marlin: Efficient Coordination for Autoscaling Cloud DBMS
domain: transactions | consensus-replication
props: consistency | correctness
tools: induction
modeling: Autoscaling DBMS cluster as system tables (membership, granule-ownership GTable) plus per-node logs; reconfiguration transactions (AddNode, DeleteNode, Migration, RecoveryMigr); invariants D1, I1–I4 with an initial-state hypothesis; compare-and-swap LSN commit.
properties: System-table consistency across nodes; unique granule ownership preserved by every committed transaction; user transactions serialized through the single owner and TryLog CAS.
usage: Invariant-preservation proofs by induction over committed reconfiguration transactions, with case enumeration per transaction type.
role: design-driver — invariants dictate the coordination protocol design.
quote: "The contents of a local [GTable] may diverge slightly from the ground truth, but the local [GTable] must have identical content as the ground truth regarding granules mapped [to] the current node."
