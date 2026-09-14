# batch_w2c — queue2 lines 27-39 (13 papers, consumer w2c)

### sigmod26-385 — WoW: Window-to-Window Incremental Index for Range-Filtering ANNS
domain: ann-vector-search | indexing
props: lower-bound | upper-bound
tools: estimation-theory
modeling: Formalizes RFANNS via a window graph (RNG + window properties) over vector-attribute pairs and hierarchical layers with boosting base o; assumes sequential attribute values and uniformly distributed neighbor selection; defines LID and query selectivity.
properties: Interval bounds on the expected fraction of in-range neighbors at a single hop on the landing layer (cases a-c); pruning-dominance inequality comparing neighbor distances across layers.
usage: Expectation computations over uniform window placement yield the bounds; case analysis recommends o=4.
role: design-driver — landing-layer selection and boosting-base choice follow directly from the fraction bounds.
quote: "In the landing layer, the expected fraction f_R of in-range neighbors at a single hop on the path is bounded by [intervals in o, l, n']."

### sigmod26-255 — Workload-Aware Incremental Reclustering in Cloud Data Warehouses
domain: workload-tuning
props: upper-bound
tools: amortized-potential + hall-matching
modeling: Sequences of batched ingestions and range queries over micro-partitions; explicit cost model; potential function over boundary partitions.
properties: Total cost O((n+q)log q) + Σ|output_i|/m amortized (O(n) warm start); reclustering of k partitions drops potential by ≥ 4k − O(log q); bipartite input/output matching of size k−3.
usage: Hall's-theorem matching plus summation of potential decreases yields the amortized bound.
role: design-driver — near-optimal query performance with bounded reclustering cost justifies recluster-only-boundary-partitions.
quote: "A reclustering operation of k micro-partitions decreases the potential Φ by at least 4k − O(log q)."

### sigmod26-107 — FGIM: Fast Graph-based Indexes Merging for ANNS
domain: ann-vector-search | indexing
props: + formulation-only
tools: + none-extracted
modeling: Seven clean definitions formalize graph-index merging as multi-objective optimization (saved build cost minus merge cost, QPS, recall); cross/local candidate neighbors defined for merged graphs. Thin extract: definitions only, one empty proof, no bounds.
properties: None stated.
usage: Definitions frame the cross-candidate merging heuristics; no extracted results back them.
role: motivation — formal problem statement preceding the heuristic framework.
quote: "The merge process is formulated as a multi-objective optimization problem: max {B(X) − M(G1,…,Gh), Q(G), R(G)}."

### sigmod26-228 — SQLBarber: LLM-Generated Customized Realistic SQL Workloads
domain: llm-db | benchmark
props: correctness
tools: + wasserstein-distance
modeling: Nine definitions specify workload generation: SQL templates with placeholders, user specifications, cost-aware instantiation targeting a cost distribution matched via Wasserstein distance; correctness = executability plus spec satisfaction. Definitional only; no theorems or proofs extracted.
properties: Correctness criteria defined, not proven.
usage: Definitions scope the system; cost-distribution matching objective drives iterative predicate refinement.
role: motivation — formal problem framing for LLM-based workload generation.
quote: "The system should generate SQL queries with costs that reduce this distance as much as possible within a given time budget."

### sigmod26-302 — Dynamically Detect and Fix Hardness for Efficient ANNS
domain: ann-vector-search | indexing
props: correctness | upper-bound | space-complexity
tools: adversarial-construction + graph-reachability
modeling: Escape Hardness EH(u,v,q,G) = min over paths of max rank along the path; K_h-reachability on induced S-neighboring subgraphs of directed graph indexes.
properties: GreedySearch with list size ≥ EH always visits the target (corollary); 100% accuracy for historical queries without pruning; EH = S reachability characterization; removing any DG edge isolates nodes; at most 2(N_q−1) added edges.
usage: Reachability thresholds localize hard vertex pairs; adversarial edge-removal shows DG minimality.
role: design-driver — the EH matrix detects where bypass edges must be inserted.
quote: "If any edge of DG is removed, there exists a query q such that NG_{2,q} contains only two isolated nodes."

### sigmod26-354 — Regular Expression Indexing for Log Analysis
domain: indexing
props: correctness
tools: + selectivity-monotonicity
modeling: n-gram bit-vector inverted index over logs; gram selectivity σ estimated from workload frequency. The np_hard signal is cited related work on optimal subset selection (noise).
properties: Bit filtering never drops a potentially matching log line (correctness lemma, case analysis over n-gram presence); any literal containing a σ-selective bigram has selectivity ≤ σ.
usage: Containment argument proves filter safety; monotonicity observation guides gram selection.
role: design-driver — selectivity observations steer index construction.
quote: "Suppose a bigram g has selectivity σ. Then, any string literal s containing g has selectivity at most σ."

### sigmod26-044 — Causal Search for Skylines (CSS): Causally-Informed Selective De-Correlation
domain: query-optimization + skyline-queries
props: + correlation-analysis
tools: estimation-theory + causal-dag-reasoning
modeling: Edge-labeled causal DAG over attributes; causal paths, tuple dominance, skyline, and conditioning operator; closed-form covariance/correlation computations for fork/chain/collider structures under linear models with Gaussian latents.
properties: Observation/corollary that conditioning on mediators/forks eliminates negative correlations and conditioning on colliders boosts positive ones; no formal theorems.
usage: Covariance algebra over causal structures selects which attributes to condition on before skyline search.
role: design-driver — the causal graph dictates the de-correlation conditioning choices.
quote: "Negative correlations can be eliminated by conditioning on the mediator/fork attributes with originally negative impact."

### sigmod26-299 — DiskJoin: Large-scale Vector Similarity Join with SSD
domain: ann-vector-search | storage-compression
props: hardness
tools: reduction
modeling: Vector similarity self-join on SSD formalized as Minimum Edge Cover with Cache (MECC): find a minimum-length load/evict sequence covering all edges of a graph with a capacity-C cache; bucket-ordering subproblem.
properties: MECC is NP-hard.
usage: Polynomial reduction from Independent Set with LIFO eviction and cache size |V|−T+1.
role: motivation — hardness justifies the approximate two-stage decomposition (edge ordering + eviction policy).
quote: "We show that the decision version of MECC can be reduced from independent set (IS)."

### sigmod26-282 — Brook-2PL: Deadlock-Free Two-Phase Locking for High-Contention Workloads
domain: transactions
props: consistency | correctness
tools: + wait-for-cycle-construction
modeling: Transaction chopping into pieces; SC-graph (sibling/conflict edges) and SLW-graph over locking hops under a deadlock-free 2PL variant.
properties: SC-cycle-free chopping yields an acyclic serialization graph, i.e., conflict-serializability; absence of SLW-cycles implies deadlock-freedom.
usage: Contradiction proofs: a serialization cycle would force an SC-cycle; any wait-for deadlock cycle yields an SLW-cycle.
role: design-driver — cycle-freeness conditions are the protocol's safety and liveness criteria.
quote: "A set of transactions is deadlock-free if, in their [SLW-graph], no SLW-cycle exists."

### sigmod26-359 — SAQ: Vector Quantization via Code Adjustment and Dimension Segmentation
domain: ann-vector-search | storage-compression
props: error-bound | probabilistic-guarantee | asymptotic-optimality
tools: concentration-ineq | estimation-theory
modeling: Quantization codebooks (CAQ) with dimension segmentation; inner-product distance estimation over quantized codes, positioned relative to RaBitQ.
properties: Unbiased estimator with tail P[error > threshold] ≤ 2e^{−c0ε0²}; ε < 2^{−B}·c/√D with >99.9% probability (asymptotically optimal in B); CAQ codebook equivalent to RaBitQ's.
usage: Tail bounds certify per-segment lower-bound distance pruning with confidence 1−1/m².
role: design-driver — guarantees underwrite code adjustment and staged pruning.
quote: "With a probability of at least 1−exp(−c0ε0²), the error bound of the estimator satisfies P[…] ≤ 2e^{−c0ε0²}."

### sigmod26-036 — Beyond Relational: Semantic-Aware Multi-Modal Analytics with LLM-Native Query Optimization
domain: llm-db | query-optimization
props: + heuristic-hypotheses
tools: + none-extracted
modeling: Two hypotheses (not theorems): model capability (a stronger model also answers correctly) and operator independence (upgrading one operator's model improves overall quality regardless of other allocations). Thin extract; approx_ratio signals are quality-cost tradeoff prose (noise).
properties: None proven.
usage: Hypotheses license the model-allocation heuristic in LLM-native query optimization.
role: motivation — stated assumptions left unproven.
quote: "If a model m returns a correct answer y to x, any model m+ that is more powerful than m also returns the right answer y."

### sigmod26-173 — On Efficient Approximate Aggregate Nearest Neighbor Queries over Learned Representations
domain: ann-vector-search | aqp
props: error-bound | probabilistic-guarantee | sample-complexity
tools: concentration-ineq
modeling: Aggregate NN over learned representations answered by two-phase sampling with a pilot sample; error split into sampling tolerance ε_S and NN-selection tolerance ε_NN, parameterized by neighborhood density.
properties: For AVG/VAR/SUM/COUNT/PCT: P[|agg_S − agg_D| ≤ ε_S + ε_NN] ≥ 1−α given explicit lower bounds on sample size s and pilot size s_p (Hoeffding-style ln(2/α) terms).
usage: Concentration bounds directly size the main and pilot samples per aggregate function.
role: design-driver — sample sizes follow from the bounds.
quote: "The approximation error satisfies P[|agg_S − agg_D| ≤ ε_S + ε_NN] ≥ 1−α."

### sigmod26-287 — Categorical Data Clustering via Value Order Estimated Distance Metric Learning
domain: + categorical-clustering
props: space-complexity | upper-bound + finite-convergence
tools: + monotone-descent-finiteness
modeling: Alternating outer/inner loops (OCL) over partitions Q and value orders O minimizing objective L(Q,O); finite discrete state space.
properties: Inner and outer loops each converge to a local minimum in finite iterations (strictly decreasing objective over finite states); time O(EInks + Enks), space O(ns + nk + ks).
usage: Monotone improvement plus state-space finiteness gives convergence; straightforward accounting yields the complexities.
role: appendix-foundation — standard post-hoc algorithm analysis.
quote: "OCL algorithm converges to a local minimum in a finite number of iterations."
