# batch_w4d — queue3 lines 92-104 (scores 8-6)

### sigmod26-308 — Efficient Size-Bounded Community Search, Revisited
domain: graph-db
props: upper-bound | correctness
tools: + branching-recurrence analysis (λ_s root of x^{s+2}−2x^{s+1}+1)
modeling: Size-bounded community search: connected subgraph within size bound h maximizing min-degree; feasibility bounded via degeneracy function ∇(|V|,k), diameter bounded when |V| < 2d_min + c, better solutions must contain k_min+1 query neighbors.
properties: Three exact frameworks (SE-MD, BE-MD, SE-MN) return the optimum in O*(min(λ_s^n, n^h)) with λ_s < 2 (Thm 4.4); total complexities O((h−l)·(n+m)·min(λ_s^n, n^h)) variants via call counting (proof).
usage: Lemmas certify safe pruning (distance rule RR2, missing-edge rule RR3) and query decomposition; recurrence-root bound gives the refined branching factor.
role: design-driver — structural lemmas directly shape the reduction rules; theorem certifies exactness.
quote: "SE-MD, BE-MD, and SE-MN identify the optimal solution of SCS in O*(min(λ_s n, n^h)), where ... λ_s < 2 is the largest real root of the equation x^{s+2} − 2x^{s+1} + 1 = 0." (Thm 4.4)

### sigmod26-383 — Visualization-Oriented Progressive Time Series Transformation
domain: time-series
props: correctness | error-bound
tools: induction | + monotonicity/interval-containment argument
modeling: Rasterization V over pixel columns; problem: select subset Q(X) ⊆ X with V(f(Q(X))) = V(f(X)) at any canvas resolution (error-free, M4-style); time-aligned tree (TAT) carries per-node min/max; pixel error E_U = union-minus-intersection of rasterizations under four extreme range combinations.
properties: Parent min/max dominate children (Thm 1, transitivity); E_U covers all erroneous pixels regardless of true extremes γ_k (Thm 2) — exact error containment for progressive refinement.
usage: Monotone tree aggregates enable progressive pruning of point subsets; E_U bounds drive refinement ordering until zero pixel error.
role: design-driver — the two theorems define what the progressive algorithm may safely skip.
quote: "E_U includes all erroneous pixels in the line chart visualization, ensuring that no errors occur outside E_U, regardless of the actual maximum and minimum function values γ_k." (Thm 2)

### sigmod26-019 — Experimental Study of Indexes in Continuous Subgraph Matching
domain: graph-db | benchmark
props: + none proven (definitions only)
tools: + none
modeling: Clean definitional framework: labeled graphs, subgraph isomorphism matching, dynamic graph as initial graph + update stream, CSM query, matching order with left/right neighbors, vertex/edge index as candidate-set materialized view. Noisy bound sentences are experimental settings (150GB memory cap), not theory.
properties: No theorems or proofs; NP-hardness of subgraph matching cited as background only. Purely experimental [E&A] paper.
usage: Definitions fix the vocabulary for taxonomizing CSM index designs and structuring the benchmark comparison.
role: appendix-foundation — formal defs ground the empirical study; no results.
quote: "An index (also known as a materialized view) of a CSM algorithm is a data structure that records candidate set C(u) for each query vertex u in Q." (Def 2.6)

### sigmod26-140 — Interpretable Attribute Discretization
domain: + attribute discretization (data preparation)
props: regret-bound
tools: online-regret | + MDP/Monte-Carlo-Control modeling
modeling: IAD maximizes α-blended semantic (LLM-scored) + black-box utility objective; optimal partition sets = Pareto frontier over (M_sem, M_util); search space reduced by EMD+DBSCAN clustering of partition distribution vectors; OPS cast as finite-horizon MDP solved via Monte Carlo Control.
properties: Scalarized maximizers lie on the Pareto frontier (Def 2); with d=1 and UCB indices, Algorithm 1 reduces exactly to a K-armed bandit inheriting gap-free O(K√(T log T)) and gap-dependent regret (Thm 1); equivalence fails for d>1.
usage: Pareto/MDP abstraction organizes the search; the bandit reduction yields the only provable guarantee, in the single-attribute case.
role: design-driver — formalization shapes the RL search; guarantee is conditional (d=1).
quote: "If (i) d=1 ... and (ii) MCC uses the UCB index ... then our Algorithm 1 becomes a UCB-guided MCC variant and reduces exactly to a stochastic multi-armed bandit with K arms." (Thm 1)

### sigmod26-202 — R2O: Joint Rewriting and Ordering in Distributed Property Graph Queries
domain: distributed-query | graph-db
props: + none proven (completeness asserted in definitions)
tools: + none (definitional framework)
modeling: Property graphs as labeled multigraphs; pattern queries with property constraints under homomorphism semantics; partitioning with replicated endpoints; query decomposition into subqueries executable per-partition without inter-partition joins, recombined by sequential joins. Big-O counts (16) come from cost discussion, not theorems — noisy signal.
properties: Decomposition/execution semantics stated as definitions ([[q_i]]_G = ∪_j [[q_i]]_{F_j}); completeness asserted in prose, no proofs in extract.
usage: Definitions fix the rewriting and ordering search space for the dual-layer (learned) optimizer.
role: appendix-foundation — semantic scaffolding only.
quote: "Each subquery q_i can be independently executed on each partition F_j without inter-partition join operations, i.e., [[q_i]]_G = ∪_{j=1}^n [[q_i]]_{F_j}." (Def 6)

### sigmod26-212 — Robust Fair Influence Maximization under Multiple Community Partitions
domain: fairness | graph-db
props: hardness | approximation-ratio | probabilistic-guarantee
tools: reduction | exchange-greedy | concentration-ineq
modeling: RFIM: maximize robust fair influence ρ(S) over l community partitions, each with linear-aggregation or concave-welfare fair objective; seed budget k; surrogate H^{(c)} monotone+submodular, estimated by RR-set sampling; bicriteria (ratio, budget) solution concept.
properties: NP-hard to approximate within O(n^{1−poly(ε)}) (linear case, Thm 3.1) and O(n^{0.25−ε}) (welfare case), even with relaxed budget (1−δ)ln l·k; S-HIST returns (1−1/e−ε/OPT, ln l+O(1)) bicriteria whp (Thms 4.1/4.2) with certified lower bound; worst-case time O(mnk log n · log^4(1/ε)/ε^6).
usage: Hardness motivates bicriteria relaxation; greedy on submodular surrogate + RR concentration + OPIM-C-style early stopping certify the ratio.
role: theory-as-contribution — inapproximability plus bicriteria guarantee are the core results.
quote: "The RFIM problem is NP-hard to approximate within a factor of O(n^{1−poly(ε)}) by selecting a seed set of size at most (1 − δ) ln l · k." (Thm 3.1)

### sigmod26-221 — SHoTClean: Soft and Hard Constraints for Multivariate Time Series Cleaning
domain: time-series | data-cleaning
props: correctness | regret-bound
tools: dp-optimality | online-regret
modeling: Multivariate repair minimizing cost Δ(X,X′) subject to hard constraints; feasible repairs biject with paths in a DAG; path weight W(P) with strictly decreasing γ makes max-weight path the min-cost repair; online variant restricted to a window W.
properties: Offline optimality via bijection + monotone cost/weight exchange argument (Thm 2.1); online regret R_n ≤ n·e^{−β(W+1)}, per-step ≤ e^{−β(W+1)} — exponential convergence to offline optimum as W grows (Thm 4.1).
usage: DAG longest-path DP yields the exact offline repair; exponential-decay regret justifies bounded-window online cleaning.
role: design-driver — DP structure is the algorithm; regret bound certifies the online mode.
quote: "Let P* be the maximum-weight path in the constructed DAG. Then the corresponding repaired time series X′_{P*} is exactly the optimal solution of arg min_{X′} Δ(X, X′)." (Thm 2.1)

### sigmod26-223 — Sketch-based Secure Query Processing for Streaming Data
domain: streaming | security | sketching
props: space-complexity | upper-bound
tools: amortized-potential
modeling: Secure (enclave-side) quantile query processing over GK sketches with parameter s and stream length n; compression fuses eligible tuple pairs in rounds; sketch count 184 reflects heavy sketch machinery throughout.
properties: GK sketch size ≤ 2s ln(n/s + 2) + 2 via potential function P_{x_i}(n) (Lemma 4.1); all eligible fusions complete within ⌈log s′⌉ compression rounds by geometric halving (Lemma 4.2).
usage: Potential argument bounds steady-state sketch size; halving round bound caps latency of batched compression inside the secure environment.
role: design-driver — round bound dictates the compression triggering policy.
quote: "The size of the GK sketch when running with parameter s is at most 2s ln(n/s + 2) + 2 when the stream length is n." (Lemma 4.1)

### sigmod26-288 — Cleaning Time Series under Seasonal and Trend Constraints
domain: time-series | data-cleaning
props: hardness | correctness
tools: reduction | + greedy set-cover heuristic
modeling: Repair cost Δ(x,x′) minimized subject to seasonal+trend constraints (windowed median trend filter, period-aligned seasonal filter); violation-tolerant filters with component extension for endpoints. Noisy pdf extract (Prop 4 is a contributions fragment).
properties: Decision problem NP-complete via reduction from Set Cover (Thm 1, proof given); constraint computation invariant to single extreme-value violations (Props 1/2); seasonal repair optimal at cost 2 (Prop 3).
usage: Hardness motivates set-cover-inspired iterative minimal repair; invariance props make filters violation-tolerant without error propagation.
role: design-driver — hardness + invariance props shape the repair loop and filter design.
quote: "The problem is NP-complete to determine whether there is a cleaned time series x′ having (1) seasonal and trend constraint η1 ≤ s_i + t_i − x_i ≤ η2 satisfied for each x′_i, (2) the repair cost Δ(x, x′) ≤ τ." (Thm 1)

### sigmod26-133 — Hyra: Byzantine-Resilient Storage with Hierarchical Erasure-Coding
domain: consensus-replication | storage-compression
props: correctness | lower-bound | tightness
tools: + Byzantine worst-case (quorum) counting
modeling: Hierarchical erasure-coded state storage in BFT: n replicas, f Byzantine, RS(n−2f, 2f) top-level code, per-height replica sets agreed via consensus, eventual synchrony assumption for liveness.
properties: Durability invariant — no data chunk permanently lost, recoverable from honest replicas (Lemma 5.1); any recoverability-guaranteeing coding scheme needs redundancy rate ≥ (n−f)/(n−2f), tight at K=n−2f, M=f — Hyra's configuration (Lemma 5.2).
usage: Worst-case counting (f withheld chunks; ≤ n−2f honest committers) proves both the recoverability invariant and optimality of the chosen RS parameters.
role: design-driver — the tight bound dictates the code configuration.
quote: "Under BFT environment with f Byzantine replicas, the redundancy rate of any coding scheme that guarantees recoverability must be at least (n−f)/(n−2f)." (Lemma 5.2)

### sigmod26-134 — IDAP++: Divergence-Aware Pruning with Joint Filter/Layer Optimization
domain: + neural-network pruning (model compression)
props: error-bound | + divergence invariants (scale-invariance, head-additivity)
tools: + matrix-norm (Frobenius) linearity
modeling: Pruning as maximizing layer-wise divergence D_l between consecutive-layer activation tensors under compression constraints; multi-head attention divergence treated additively over independent heads; guarantees quantified on validation set D_val.
properties: D_l invariant to scaling (Lemma 3.1); total attention divergence = sum of head divergences (Thm 3.3, one-line proof via Frobenius linearity and block-diagonal structure); compressed network satisfies ‖N0(x)−N*(x)‖² ≤ Δ_max‖N0(x)‖² ∀x ∈ D_val at maximal sparsity (Thm 3.4).
usage: Invariance/additivity license per-layer, per-head independent pruning scores; the relative error bound caps output drift.
role: design-driver — guarantee built into the pruning constraint.
quote: "For any network N0 compressed with IDAP++, the compressed network N* satisfies: ‖N0(x) − N*(x)‖² ≤ Δ_max ‖N0(x)‖² ∀x ∈ D_val, while achieving maximal sparsity." (Thm 3.4)

### sigmod26-240 — Hubness: A Revisit on Graph-Based Approximate Nearest Neighbor Search
domain: ann-vector-search | benchmark
props: probabilistic-guarantee
tools: markov-chain | + distance-concentration argument
modeling: Greedy graph ANNS modeled as a stochastic process on the index graph; hubness (in-degree skewness S_Nk) induces centrality variance; hubs form absorbing basins; anti-hubs reachable only via low-density gateway sets. Thin extract — proofs truncated, formal derivations deferred to appendices (A.11/A.21).
properties: Negative reachability result: probability of navigating into the gateway set before hub absorption vanishes as skewness intensifies; hub-capture probability approaches one as dimension grows (Lemma 1).
usage: Stochastic-process view + distance concentration explain greedy failure on anti-hubs; hubness lens taxonomizes existing methods by mitigation complexity.
role: motivation — theoretical lens frames the experimental revisit.
quote: "For a search of finite length, the probability of navigating into the low-density gateway set before being absorbed by a hub's basin of attraction vanishes as skewness intensifies." (Lemma 1)

### sigmod26-313 — Fast Optimal Group Steiner Tree Search using GPUs
domain: graph-db
props: correctness
tools: dp-optimality | induction
modeling: Group Steiner Tree: min-weight tree covering all vertex groups Γ of G(V,E,w); GPU-parallel TrimCDP-WB based on dynamic programming with weight-balanced edge splitting and conditional tree merging [37]. Θ/NP-hard/approx counts in header come from related-work context (noise).
properties: TrimCDP-WB returns the exact optimum w(Θ) (Thm 1); proof by leaf-growing/merging induction: uniquely-covered group sets merge without double counting, recovering w(Θ_u)+w(Θ_v)+w(u,v).
usage: DP weight composition over balanced edge cuts proves the GPU schedule computes optimal weight.
role: design-driver — correctness proof certifies the GPU-parallel DP formulation.
quote: "Given a graph G(V, E, w) and a set Γ of vertex groups, TrimCDP-WB can find an optimal solution to Problem 1." (Thm 1)
