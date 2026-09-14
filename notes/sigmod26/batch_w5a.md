# batch_w5a — queue3 lines 105-116 (scores 5-4); all pdf-derived extracts

### sigmod26-088 — Efficient Vector Index Merging in Vector Databases
domain: ann-vector-search | indexing
props: asymptotic-optimality | upper-bound
tools: induction | exchange-greedy
modeling: Merging s HNSW indexes as a sequence of pairwise merges; cost of one merge dominated by linear scan of the larger index (size N_i) times forward-search width λ = O(log N). Merge orderings counted as full binary merge trees.
properties: (2s−3)!! distinct merge orders (Lemma 6.1, structural induction on tree leaves); Theorem 6.2 — greedy large-first pairwise merging minimizes total merge time under the λ = O(log N) cost model, proven by induction with per-pair cost comparison. Observations 1–2 (backward-edge sufficiency, small λ) are empirical, not proven.
usage: Induction over merge trees plus greedy-choice cost comparison yields the merge-scheduling policy; combinatorial count of orders frames the search space.
role: design-driver — the optimality theorem dictates the large-first merge order inside HNSW-Merger.
quote: "The optimal merge ordering that minimizes total merge time in a sequence of pairwise merges is to repeatedly merge the two largest indexes at each step." (Thm 6.2)

### sigmod26-138 — Improving Range Scan Performance in LSM-trees with Group Caching
domain: caching-scheduling | storage-compression
props: probabilistic-guarantee | error-bound
tools: concentration-ineq
modeling: Cached-group benefit S(t) as a sum of weighted block-reuse indicators s_i B_i(t) over LSM levels with a dependency graph of degree Δ ≤ L−1; per-block expectation b_i(t) ∈ [0,1].
properties: Variance bound V ≤ s_max·E[S(t)] via b_i(1−b_i) ≤ b_i (Lemma A.2); two-sided multiplicative tail bound P[|S(t)−μ| ≥ εμ] ≤ 2exp(−ε²μ / (2L·s_max(1+ε/3))) by mapping a Janson/Chernoff-type theorem with b = s_max, plus union bound. Extract captured proofs but not the theorems they prove (noisy pdf extraction).
usage: Dependency-graph concentration certifies that group caching delivers its expected benefit with high probability across workloads.
role: appendix-foundation — tail-bound analysis backs the cache design; stated theorems not visible in extract.
quote: "P[𝑆(𝑡) ≥ (1+𝜀)𝜇] ≤ exp(−𝜀²𝜇 / (2𝐿 𝑠_max(1+𝜀/3))) ... combining both tails with a factor of 2 completes the proof."

### sigmod26-250 — Variational Inference for De Finetti Logic
domain: uncertain-data
props: correctness
tools: bayesian-posterior | + knowledge-compilation (d-DNNF/SDD circuits)
modeling: De Finetti Logic programs as ground PPDL theories over exchangeable dice; posterior over parameters Θ given constraints Φ and atoms A; lineage compiled to "upSDD" circuits (d-DNNF subclass built from positive sentential decompositions).
properties: Theorem 1 — the exact posterior is an affine combination of products of Dirichlet densities, summing over satisfying draw sequences of a Pólya-Eggenberger urn (conjugacy); ELBO maximization via stochastic variational inference replaces intractable KL minimization. No convergence-rate result captured.
usage: Dirichlet conjugacy plus circuit-based enumeration of DSat partitions makes the posterior tractable enough for SVI gradients.
role: design-driver — the posterior characterization and circuit structure define the variational inference algorithm.
quote: "The posterior density 𝑝(Θ|Φ, A) can be computed as an affine combination of products of Dirichlet densities." (Thm 1)

### sigmod26-315 — Focus! Fast On-disk Concurrency-control Using Sketches
domain: transactions | storage-compression
props: correctness
tools: sketching-theory
modeling: TicToc-style timestamp validation where on-disk read/write timestamps are stored approximately (sketched); approximation treated as an operation that never decreases a timestamp (Property 1), correctness argued from lock discipline.
properties: Lemma 3 — every timestamp increases monotonically in physical time under approximate storage, and every write to key k increases k's write timestamp. Proof by case analysis over get/put/commit paths, locks, and atomic max-updates. Serializability itself is inherited from TicToc, not reproven. Signal counts (approx_ratio 9, θ 4) are text noise.
usage: Invariant-preservation argument showing lossy timestamp storage cannot break monotonicity, licensing compact on-disk CC state.
role: design-driver — the monotonicity lemma is the safety certificate for the sketch-based storage layout.
quote: "Each timestamp increases monotonically in physical time in TicToc with approximate timestamp storage. Furthermore, every write to a key 𝑘 causes 𝑘's write timestamp to increase." (Lemma 3)

### sigmod26-330 — LLM-Powered Interactive Graph Search
domain: graph-db | llm-db
props: correctness
tools: + graph-reachability (free; nothing in taxonomy fits)
modeling: Interactive Graph Search over a classification hierarchy H: identify target concept with minimum oracle interactions; relaxes the perfect-oracle assumption to error-prone LLM oracles; introduces ambiguous and overlapping nodes.
properties: Theorem 3.1 (monotonicity) — if Q_r(q)=Yes then all ancestors answer Yes; if Q_r(q)=No then all descendants answer No; short reachability proof. Claim 3.1 explains why binary-search and greedy IGS fail on ambiguous/overlapping nodes (informal). Thin formal content overall.
usage: Monotonicity licenses ancestor/descendant pruning of the search space during LLM-guided traversal.
role: design-driver — monotonicity theorem underpins the pruning strategy of the interactive search.
quote: "For a node 𝑞 ∈ 𝑉, if 𝑄𝑟(𝑞) = Yes, then ∀𝑤 ∈ anc(𝑞), 𝑄𝑟(𝑤) = Yes. Conversely, if 𝑄𝑟(𝑞) = No, then ∀𝑤 ∈ des(𝑞), 𝑄𝑟(𝑤) = No." (Thm 3.1)

### sigmod26-367 — Stochastic Submodular Data Forgetting
domain: + machine-unlearning (free; no taxonomy fit)
props: approximation-ratio | correctness
tools: exchange-greedy | estimation-theory
modeling: Data forgetting as budgeted subset selection: maximize retained utility f(D′) over |D′| ≤ B under a query distribution Q; f lifted to its multilinear extension F for continuous stochastic maximization.
properties: Theorem 5.1 — f is non-negative, monotone, submodular, giving a (1−1/e) polynomial-time guarantee via greedy/lazy-greedy. Theorem 5.2 — f is doubly-stochastic and ∇F admits a double-stochastic estimator needing no more terms than the single-stochastic one. Theorem 5.6 — the independent (Jaccard) case is exactly solvable by top-B scores.
usage: Submodular greedy guarantee plus double-stochastic gradient estimates (DepDF) avoids O(nB) costly objective evaluations; exact top-B scoring (IndepDF).
role: design-driver — theorems select between dependent and independent forgetting algorithms.
quote: "The Problem 1 admits a solution with (1 − 1/e) approximation guarantee to the optimal one in polynomial time." (after Thm 5.1)

### sigmod26-037 — Bound-Tightened Densest Subgraph Discovery on GPU
domain: graph-db
props: correctness | approximation-ratio
tools: peeling-dyadic
modeling: Densest k-clique subgraph: vertices carry clique-core numbers κ_k(v); density of optimum D* related to the clique-core density ρ_core; iterative peeling removes vertices at each core level.
properties: Every vertex of an optimal D* participates in at least ρ(D*) k-cliques, so ρ(D*) ≥ ρ_core and vertices with κ_k(v) < ρ_core can be pruned safely; correctness of concurrent atomic-decrement updates during warp-centric peeling. Extract's "proof" mixes argument with GPU algorithm description (noisy); upper/lower-bound counts come largely from surrounding text.
usage: Clique-core peeling bounds tighten the density search interval and drive GPU-parallel pruning.
role: design-driver — core-based bounds shape the peeling kernels and the search-space reduction.
quote: "By definition, every vertex 𝑣 ∈ 𝐷* must participate in at least 𝜌(𝐷*) 𝑘-cliques in the induced subgraph 𝐺(𝐷*). Since the densest clique core achieves density 𝜌_core, we have 𝜌(𝐷*) ≥ 𝜌_core."

### sigmod26-050 — Concurrent Path-Copying Update to Tree Structures
domain: indexing | transactions
props: correctness | lower-bound
tools: amortized-potential
modeling: Path-copying versioned trees updated concurrently by worker threads; versions form a unidirectional dependency order; hybrid BeTree with lower B+Trees of order b and height h.
properties: Lemma 4.1 — the update algorithm is non-blocking and starvation-free; Property 4.2 — a parent node's version is never earlier than its children's, so subtrees of committed nodes can skip dependency checks. Theorem 5.1 — a second root split requires amortized Ω(b^{h+2}) insertions, via potential Φ(T) = b^{h(T)}(sz(T)−b) that increases by 1 per insert and resets on splits.
usage: Potential-function amortization quantifies rebuild rarity; version-ordering invariant enables the dependency-check skip optimization.
role: design-driver — amortized rebuild bound justifies the hybrid upper/lower-tree architecture.
quote: "For a lower B+Tree of order 𝑏 and height ℎ, triggering the second root split requires amortised Ω(𝑏^{ℎ+2}) insertions. Hence, BeTree rebuilds are rare." (Thm 5.1)

### sigmod26-063 — cuRPQ: GPU-Based Regular and Conjunctive Regular Path Queries
domain: graph-db
props: correctness
tools: none captured (definitional; + automaton traversal free)
modeling: Formal RPQ/CRPQ semantics (vertex pairs joined by label sequences matching a regular expression; homomorphism semantics for CRPQs); GPU traversal organized by product automaton over graph slices, with "checkpoint sets" at static-hop boundaries as resumable frontiers.
properties: No theorems or proofs — extraction captured only definitions and design discussion. Qualitative argument that DFS with memory-limited hop bounds misses valid paths and yields incorrect results, motivating BFS-style bounded expansion; single bound sentence merely cites worst-case optimal joins from related work. Thin extract.
usage: Definitions frame the correctness requirement (no missed pairs under hop limits) that the slicing/checkpoint design targets.
role: motivation — problem formalization and incorrectness of DFS-under-bounds motivate the GPU framework; no proved results captured.
quote: "DFS-based traversal can easily exceed these bounds, leading to missed valid paths and ultimately incorrect results."

### sigmod26-131 — HotHash: Hotness-Aware Consistent Hashing for Cloud Databases
domain: caching-scheduling | + consistent-hashing/partitioning (free)
props: probabilistic-guarantee | upper-bound
tools: clt-normal-approx | concentration-ineq
modeling: Query load on nodes as accumulation of binomial random variables over hotness-weighted data segments; node groups of sublinear size; load imbalance I, cache hit rate C, and transmission cost T as the analyzed quantities.
properties: Theorem 5.1 — load imbalance I is at most ≈ √(n/(c/m²)) (mangled pdf math), small for m<2; node load balanced in expectation. Theorem 5.2 — cache hit rate at least 1 − c/(n+N) and transmission cost bounded by n(c+N). Derivations use normal approximation of binomials, independence, and Chebyshev's inequality.
usage: Binomial→normal approximation plus Chebyshev tail control quantifies balance and cache-hit guarantees of the hotness-aware placement.
role: design-driver — the two theorems certify the scheme's balance and cache benefits; math heavily mangled by pdftotext (noisy).
quote: "This shows that the load on each node is balanced in expectation. ... We then show a lower bound on its cache hit rate in Theorem 5.2."

### sigmod26-167 — NeurBench: Benchmark Suite for Learned Database Components with Drift Modeling
domain: benchmark | + learned-components (free)
props: correctness
tools: delta-method
modeling: Drift modeling for benchmark generation as a controlled diffusion/reverse process conditioned on drift variables: reverse distribution p(x_{t−1}|x_t, x_drift) approximated via Pr(x_drift|x_t) and its gradient.
properties: Theorem 1 — the controlled reverse distribution is approximable by a perturbed Gaussian N(x_t; μ + Σ∇_{x_t}Pr(x_drift|x_t), Σ); proof Taylor-expands the log-density around μ and completes the square (following Sohl-Dickstein-style diffusion arguments). No error bound stated; benchmark itself is empirical. Signal counts (learned 46, cardinality 3) are topical, not theoretical.
usage: Taylor-expansion (delta-method-style) argument validates gradient-guided perturbation of the reverse Gaussian for drift injection.
role: appendix-foundation — one borrowed approximation theorem underpins the benchmark's drift-generation component; the paper is otherwise an [Experiments & Analysis] artifact.
quote: "𝑝(x_{t−1}|x_t, x_drift) can be approximated by N(x_t; 𝜇 + Σ·∇_{x_t} Pr(x_drift|x_t), Σ)." (Thm 1)

### sigmod26-225 — SmartRabbit: An Interactive Query Processor
domain: query-optimization
props: correctness
tools: + operator-timing model (free; inception/completion points)
modeling: Interactive execution defined semantically: a non-empty prefix of R(Q) is emitted strictly before a latency-optimized blocking execution completes. Each operator gets temporal markers — inception point ip (first possible output) and completion point cp (all outputs guaranteed); plans structured around a "fulcrum" attribute inducing sorted emission.
properties: Lemma 2.1 (blocking characterization) — for an operator edge p→c, c is blocking on p iff ip_c ≥ cp_p; equivalence stated with the definition (no captured proof). Fulcrum-ordered emission yields correct incremental results (claimed, not proven in extract).
usage: The iff-characterization identifies pipeline breakers and guides fulcrum/access-path selection for interactive plans.
role: design-driver — the blocking lemma and fulcrum concept drive the interactive plan construction and dual-plan coordination.
quote: "For an edge 𝑝 → 𝑐 between operators, 𝑐 is blocking on 𝑝 if and only if ip_𝑐 ≥ cp_𝑝." (Lemma 2.1)
