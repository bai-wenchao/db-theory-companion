### sigmod26-178 — Optimal Pure Differentially Private Sparse Histograms in Deterministic Linear Time
domain: privacy-dp
props: privacy-guarantee | error-bound | tightness
tools: dp-composition | estimation-theory | coupling-dominance
modeling: Pure-DP histogram release: n user elements over domain [d], neighboring histograms, (ε,δ)-indistinguishability; utility as (α,β)-simultaneous ℓ∞ accuracy; goal is deterministic linear time. Geometric-noise sampling with tail padding.
properties: 2ε-DP guarantee; ℓ∞ error Θ((1/ε)·ln d), asymptotically optimal, matching the Balcer–Vadhan lower bound Ω(min{(1/ε)ln d, n}); O(n+k) deterministic running time.
usage: Four-case distribution-dominance analysis over neighboring supports plus DP composition proves privacy; geometric-mechanism estimator accuracy carries through to per-coordinate utility.
role: theory-as-contribution — the optimal pure-DP mechanism with matching error bounds is the paper.
quote: "The utility guarantee of Theorem 4.1 is an ℓ∞ bound and is asymptotically optimal, matching the lower bound Ω(min{1/ε ln d, n}) of Balcer and Vadhan."

### sigmod26-022 — Analyzing Deviations from Monotonic Trends through Database Repair
domain: data-cleaning
props: hardness | approximation-ratio
tools: reduction | dp-optimality | adversarial-construction
modeling: Aggregate order dependencies (AOD): repair = minimum tuple deletions so aggregate α over groups satisfies a monotonic trend; optimum is a maximum monotonic subset. TeX extract drops some math glyphs; statements remain interpretable.
properties: NP-hardness for general α via Subset-Sum reduction; polynomial-time solvable for bounded aggregates; pseudo-polynomial (weakly polynomial) for sum/average; greedy heuristic suffers Ω(n) approximation ratio on adversarial instances.
usage: DP over group/aggregate-value states with greedy upper-bound pruning computes optimal repairs without sacrificing optimality; adversarial databases separate greedy from optimum.
role: design-driver — the complexity map dictates which aggregates get exact DP algorithms and where heuristic pruning enters.
quote: "While the general case is NP-hard, several practically relevant aggregates admit polynomial-time solutions."

### sigmod26-151 — Local Stability of Rankings
domain: uncertain-data + ranking-robustness
props: hardness | probabilistic-guarantee | sample-complexity
tools: reduction | concentration-ineq
modeling: k-SBtf(D): the set of attribute refinements ε that move tuple t's rank by at most k; local stability measured as the volume ratio of the stable zone within the reasonable-changes region RC; tuple-independent ranking functions.
properties: Computing k-SBtf is #P-hard (unless FP = #P) via a parsimonious #DNF reduction; Hoeffding-based Monte Carlo verification: N = (1/2η²)ln(1/δ) samples confirm α-stability with probability 1−δ.
usage: Hardness justifies sampling; the concentration bound sets sample budgets in the two-phase construct/verify LStability algorithm and its volume estimation.
role: design-driver — #P-hardness motivates the sampling-based approximation algorithm.
quote: "Unless FP = #P, there is no polynomial-time algorithm for computing k-SBtf(D) given a database D, a tuple t ∈ D, a ranking function f, and a value k."

### sigmod26-095 — Epoch-based Optimistic Concurrency Control in Geo-replicated Databases
domain: transactions | consensus-replication
props: consistency | correctness
tools: induction
modeling: Crash-failure model tolerating f failures; geo-replicated epochs with Proof-of-Availability (f+1 acknowledgements), consistent cuts agreed via consensus, deterministic conflict graph + MWIS + deterministic locking; single-copy serial history Sser.
properties: PoA implies a correct replica stored the batch; all correct replicas observe identical batch order per epoch; per-epoch serializable commit; induction over epochs yields One-Copy Serializability (1SR).
usage: Lemma chain (availability → uniform order → deterministic serialization) plus epoch-by-epoch induction proves the global theorem.
role: design-driver — PoA, epochs, and deterministic commit are shaped so the 1SR induction goes through.
quote: "At each epoch, the same set of transactions is ordered to be executed in a serializable manner among all correct replicas ... Minerva guarantees One-Copy Serializability (1SR)."

### sigmod26-008 — Accelerating Approximate Analytical Join Queries over Unstructured Data with Statistical Guarantees
domain: aqp | sampling
props: error-bound | convergence-rate | probabilistic-guarantee
tools: concentration-ineq | clt-normal-approx | delta-method
modeling: Stratified importance sampling over join cross-products with proxy similarity scores W and pilot/main budget split (b1, b2); MSE framework for COUNT/SUM/AVG under an oracle predicate O(s); blocking-and-sampling (BaS) regime.
properties: Recall targets met with probability p via normal-approximation upper bounds on stratum counts; estimated allocation's MSE converges to the optimal at rate O(b1^{-1/2}); BaS asymptotically outperforms or matches the prior WWJ estimator.
usage: Chebyshev bounds on sample mean/variance propagate through arithmetic operations; Hadamard differentiability (functional delta method) underwrites the asymptotic guarantees.
role: design-driver — budget allocation and blocking choices are derived from the MSE convergence analysis.
quote: "The MSE with the estimated minimizer β̂* converges to that with the true minimizer β* at the rate O(b1^{-1/2})."

### sigmod26-219 — Shape-Agnostic Table Overlap Discovery: A Maximum Common Subhypergraph Approach
domain: data-integration
props: hardness | approximation-ratio
tools: reduction
modeling: Tables encoded as hypergraphs (cells = nodes, rows/columns = hyperedges); shape-agnostic overlap under row/column permutations equals the maximum common subhypergraph problem; overlap size = common node count.
properties: Encoding correctness (maximum overlap ↔ maximum common subhypergraph); NP-hardness via maximum-clique reduction; inapproximability within O(|V|^{1−ε}) for any ε > 0 unless P = NP, via the approximation-preserving reduction.
usage: Permutation-invariance construction proves the encoding sound; clique reductions transfer both hardness and inapproximability, motivating exact and heuristic practical solvers.
role: motivation — hardness results justify approximate and practical overlap-discovery algorithms.
quote: "The maximum common subhypergraph problem is NP-hard to approximate within a factor of O(|V|^{1−ε}) for any ε > 0 in polynomial time."

### sigmod26-203 — RadixGraph: A Fast, Space-Optimized Data Structure for Dynamic Graph Storage
domain: graph-db | storage-compression
props: space-complexity | upper-bound
tools: dp-optimality | amortized-potential | balls-bins-hashing
modeling: Radix-tree vertex index over an ID universe; layer fanouts a_i chosen to minimize expected space, with n vertex IDs modeled by hypergeometric occupancy; log/snapshot edge segments with periodic compaction.
properties: DP computes optimal fanouts g(l−1,x) in O(nlx²) time and O(lx) space; amortized O(1) edge insert/update/delete; total index space O(2^{a0} + ngα + ng) via geometric-series layer accounting.
usage: The occupancy model yields the space objective; dynamic programming over layer splits minimizes it; amortized counting of compaction costs bounds update time.
role: design-driver — structure parameters are directly optimized by the formal space-cost model.
quote: "Under a single-threaded execution model, the amortized time complexity of edge insertion, update and deletion is O(1)."

### sigmod26-103 — Fast-Convergent Proximity Graphs for Approximate Nearest Neighbor Search
domain: ann-vector-search
props: upper-bound | space-complexity
tools: coresets-geometry | induction
modeling: Points in a metric space of doubling dimension d; α-convergent graph built by an α-reducible pruning rule (δ(p,u) > α·δ(p,v) + (α+1)τ); greedy routing / beam search; diameter Δ, minimum distance 1.
properties: Out-degree O((ατ)^d log Δ); greedy routing finds the exact NN in O(log_α Δ) hops when δ(q,v*) ≤ τ, otherwise an (α/(α+1)^{-1} + ε)-ANN; construction O(n²·((ατ)^d log Δ + log n)).
usage: Doubling-dimension ball covers over dyadic rings bound out-degree; per-hop distance shrinking by factor α bounds the routing path length.
role: design-driver — the pruning rule is designed so routing convergence and bounded degree are provable.
quote: "The α-CG G has space O(n · (ατ)^d log Δ) and can be constructed in O(n² · ((ατ)^d log Δ + log n)) time."

### sigmod26-163 — MTSP-LDP: Multi-Task Streaming Data Publication under Local Differential Privacy
domain: privacy-dp | streaming
props: privacy-guarantee | correctness
tools: dp-composition | estimation-theory
modeling: Per-user streaming publication under w-event LDP: w-neighboring stream variants; privacy budget split ε/2 statically across the window and ε/2 dynamically allocated; perturbed counts with explicit noise-variance accounting.
properties: Discrepancy estimator unbiased and ε-LDP by post-processing immunity; sliding-window variance estimator unbiased; total budget within any window of length w bounded by ε, hence w-event ε-LDP per user.
usage: Expectation/variance calculations with noise-variance corrections establish unbiasedness; windowed budget composition proves the privacy theorem.
role: design-driver — the budget-allocation scheme is engineered around sliding-window composition.
quote: "The total privacy budget consumed within any sliding window of length w does not exceed ε ... MTSP-LDP satisfies w-event ε-LDP for each user."

### sigmod26-191 — Poisson Sampling over Acyclic Joins
domain: sampling | join-algorithms
props: upper-bound | correctness
tools: + algebraic query rewriting (nested semijoin algebra)
modeling: Acyclic join queries rewritten into two-phase nested-semijoin expressions; CSR/USR random-access indexes with degree bound deg_Q(db); Poisson sampling queries, including free-connex projections; measured in data complexity.
properties: Linear-time index construction with O(log|db|) (USR) or O(log|db| + deg) (CSR) access; Poisson sampling over acyclic joins and free-connex projections solved in O(|db| + k log|db|).
usage: Rewriting to flat nested relations plus geometric probe sequences into the index yield the complexity theorem.
role: theory-as-contribution — the linear-plus-logarithmic sampling complexity bound is the headline result.
quote: "Poisson sampling over acyclic joins, as well as over free-connex projections of such joins, can be solved in time O(|db| + k log |db|) in data complexity."
