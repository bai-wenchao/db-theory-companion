# batch_w4c — queue3 lines 79-91 (scores 11-8)

### sigmod26-329 — Large-Scale Multiple Query Optimisation with Incremental Quantum(-Inspired) Annealing
domain: query-optimization
props: correctness
tools: reduction + Ising/QUBO energy modeling
modeling: Multi-query optimisation as balanced bipartitioning: queries are spins, shared plan-savings are edge weights in a partitioning graph; objective is an Ising Hamiltonian H = ωA·HA + HB for quantum(-inspired) annealing, HA enforcing equal plan totals per partition, HB retaining cross-partition savings.
properties: Theorems: minimising HA yields two equal-sized distinct query sets; minimising HB minimises the magnitude of discarded savings; with penalty weight ωA = max accumulated pairwise savings, minimising H obtains balanced partitions. One extracted "Theorem 4" is a caption fragment (noise); np_hard mentions sit in related work.
usage: Energy-penalty dominance: the balance penalty provably outweighs any savings benefit from unbalancing, certifying the encoding is faithful.
role: design-driver — Hamiltonian-correctness theorems underpin the annealing pipeline.
quote: "Minimising 𝐻 = 𝜔A𝐻A + 𝐻B obtains balanced query partitions Í if 𝜔A = max𝑞𝑖∈𝑄(Σ𝑞𝑗∈𝑄,𝑞𝑗≠𝑞𝑖 𝜔i,j)." (Thm 4.5)

### sigmod26-118 — Geld: Load-balanced D-Core Decomposition for Consumer GPUs
domain: graph-db
props: correctness | upper-bound
tools: induction + work-span parallel analysis
modeling: D-core decomposition (out-core numbers per in-degree k) of directed graphs via iterative h-index-style GPU updates; parallel cost formalised in the work-span model.
properties: Theorems: the out-core sequence is monotonically non-increasing and bounded below, hence finite convergence; the fixed point satisfies the core definition (correctness by contradiction); work O(|V|·|E|), span ΣΔk·log|V|.
usage: Monotone-sequence/well-ordering argument for termination, contradiction for correctness, per-vertex degree accounting for the work-span bounds.
role: design-driver — guarantees validate the GPU decomposition before load-balance experiments.
quote: "Under the work-span model, Geld compute the D-core decomposition in |𝑉|·|𝐸| work and Σ max k=1..Δk · log(|𝑉|) span." (Thm 3)

### sigmod26-199 — Quantile Estimation with Duplicates
domain: streaming | sketching
props: error-bound | probabilistic-guarantee | space-complexity
tools: concentration-ineq | estimation-theory
modeling: KLL-style quantile sketch (DupliSketch) for streams with heavy duplication; compactors separate frequent values from duplicate elements; a c-Batched Duplicates stream model formalises batch-level duplication intensity c.
properties: Per-compaction errors are zero-mean with Var ≤ 4^{h−1}, hence sub-Gaussian; Chernoff-style tail gives Pr[|R(x,S)−R(x)| ≥ εN] ≤ δ; error never worse than KLL (Prop 4.2), advantage growing with c (Prop 4.3); required space shrinks as c grows (Prop 4.4); amortised update O(log 1/ε).
usage: Variance/sub-Gaussianity of compaction errors plus a tighter compaction count yield error, space, and time guarantees; experiments verify scaling in c.
role: design-driver — guarantee proofs (never worse than KLL, improving with duplication) drive the design.
quote: "the error of the sketch R(x, S) − R(x) is the sum of the errors from individual compactions and is thus sub-Gaussian." (Lemma 4.1)

### sigmod26-316 — Repairing Spatio-Temporal Data via Spatial and Temporal Dependencies
domain: data-cleaning | spatial | time-series
props: hardness | approximation-ratio | probabilistic-guarantee
tools: reduction | dp-optimality
modeling: Repair cast as minimum-cardinality repair set subject to spatio-temporal speed constraints over n timestamps × m locations; decision version NP-complete (Thm 1); three algorithms: exact DP (STER), beam search width K (STPR), greedy sliding window (STGR).
properties: Exact DP returns optimum in exponential time; beam/greedy run in polynomial / O(nm log m) time with |R′|/|R*| ≤ (2n(m−1)−3m+4)/m; probabilities of hitting the optimum quantified, beam higher than greedy (Props 5/8).
usage: NP-completeness motivates the approximations; worst-case ratio bounds per algorithm; hitting-probability statements rank them.
role: design-driver — guarantees calibrate the accuracy-efficiency trade-off among the three repairors.
quote: "Algorithm 2 returns the repair R′ and X with |R′|/|R∗| ≤ (2n(m−1) − 3m + 4)/m." (Prop 4)

### sigmod26-003 — A Game Theory Approach for Negotiating in Data Marketplaces
domain: data-market
props: + none proved — NE/Pareto/NBS solution concepts defined only
tools: game-equilibrium
modeling: Data-sharing negotiation as a two-player sequential bargaining game with reservation values, status quo payoffs, and strategy parameters (dataset, query, purpose, third-party, duration, price); distributed alternating-proposal protocol with best responses under incomplete information; Nash Bargaining Solution as fair target.
properties: Extract is definitional: game, best response, Nash equilibrium, Pareto optimality, feasible solution, NBS (argmax of payoff-gain product), instantiated as a data-sharing negotiation game. No proofs captured; oracle centralised NBS cited as upper bound on efficiency and fairness.
usage: Game-theoretic solution concept steers the protocol design and serves as evaluation yardstick (closeness of distributed protocol to oracle NBS).
role: design-driver — bargaining formalism structures the protocol; no formal properties of the protocol itself in extract.
quote: "A strategy pair 𝜎̄∗ is a Nash Bargaining Solution (NBS) or fair solution, if (𝜋1(𝜎̄∗), 𝜋2(𝜎̄∗)) = argmax (𝜋1(𝜎̄) − 𝑞1)(𝜋2(𝜎̄) − 𝑞2)." (Def 2.7)

### sigmod26-198 — Qualitative Join Discovery in Data Lakes using Examples
domain: data-integration
props: hardness
tools: reduction
modeling: Join discovery over a data-lake join graph: find weight-optimal join path/tree covering required candidate tables, with semantic tuple-match constraints and tuple-cardinality maximisation (Problems 1-2).
properties: Problem 1 NP-hard by reduction from Minimum-Weight Steiner Tree (join graph ≅ Steiner instance, weights negated, terminals mapped to required tables; budget L by restriction); Problem 2 NP-hard since Problem 1 is a special case (empty example set or θ=0 makes the semantic constraint vacuous).
usage: Hardness justifies heuristic top-k join-path search with an inverted join path index and sketch-based joinability estimation; no approximation guarantees.
role: motivation — complexity results license heuristics; no per-algorithm guarantees.
quote: "Problem 1 is NP-Hard by reduction from the Minimum-Weight Steiner Tree problem." (Prop 1)

### sigmod26-007 — ABFlow: Alert Bursting Flow Query in Streaming Temporal Flow Networks
domain: streaming | graph-db
props: correctness | upper-bound
tools: + residual-network max-flow machinery
modeling: Temporal Flow Network G=(V,E,C,T) with timestamped capacitated edges; alert bursting flow query generalised as suffix flow: maximise flow out of every suffix of a source sequence to a sink sequence; streaming window updates.
properties: Flow-merging lemma (residual flows with disjoint source/sink sets add); SuffixFlow_inc correct in O(|S|·T_MFlow); SRN constraints characterise exactly when a maximum flow is a suffix flow (Lem 6.2); recursive solution correct in O(log|S|·T_MFlow).
usage: Residual-network and flow-conservation deductions; contradictory-augmenting-path removal induces cuts splitting the problem for divide-and-conquer recursion.
role: design-driver — lemmas and theorems scaffold the incremental, recursive, and streaming algorithms.
quote: "SuffixFlowinc returns a suffix flow from S to T in G as the answer to the suffix flow problem in O(|S| · T_MFlow(G)) time." (Thm 5.5)

### sigmod26-083 — Efficient and Robust Out-Of-Distribution Vector Similarity Search with Cross-Distribution Monotonic Graph
domain: ann-vector-search
props: correctness | upper-bound
tools: + geometric monotone-path analysis
modeling: Graph-based ANN index (CDMG) built on database X plus an OOD query sample Q; cross-distribution monotonicity: routing always admits an edge strictly decreasing the OOD query distance, up to relaxation parameter τ.
properties: CDMG guarantees monotonicity via a two-phase ball argument (Lem 1); expected out-degree O(ln|V|) and index size O(|V| ln|V|); construction O(|V||Q| + |Q|log|Q| + |V|²ln|V|); expected search complexity O(|V|^{1/D}(ln|V|)²) for queries distributed as Q (Lem 4).
usage: Deterministic monotone-path existence plus a convex-hull uniformity heuristic bounds expected routing length; complexity = out-degree × path length.
role: design-driver — monotonicity and expected-complexity guarantees justify the construction.
quote: "the CDMG 𝐺(𝑉,𝐸) built on X and Q has expected out-degree 𝑂(2·ln|𝑉|) and expected index size 𝑂(2·|𝑉| ln|𝑉|)." (Lem 2)

### sigmod26-089 — Eliminating Redundant Feature Tests in Decision Tree and Random Forest Inference on SQL Predicates
domain: query-optimization
props: correctness
tools: + hyperplane space-partition argument
modeling: Decision tree/random forest as a partition of R^n by axis-aligned hyperplanes (internal nodes = half-spaces); redundancy patterns defined via homogeneous sibling nodes and implicative ancestor nodes; fix is subtree recombination with hyperplane sliding, judged by an inference-overhead cost model.
properties: Theorems: sliding a semi-infinite slidable hyperplane to its interval endpoint never increases overhead; a finite slidable hyperplane never increases overhead when a sliding option with c_max ≤ c_min exists.
usage: Algebraic manipulation of the overhead difference C′ − C∗ shows every term non-positive — the transformation is sound.
role: design-driver — non-increase guarantees make the redundancy-elimination optimisation safe.
quote: "For one finite slidable hyperplane, if there is a sliding option that satisfies c_max ≤ c_min then the subtree recombination will not increase the overhead." (Thm 2)

### sigmod26-099 — FaaSBoard: Efficient Graph Processing with a Disaggregated Architecture on Serverless Services
domain: graph-db | caching-scheduling
props: correctness + monotonicity (of plan validity)
tools: exchange-greedy
modeling: Serverless graph processing on a disaggregated architecture; the formal core is graph partitioning: place the minimum number of cuts so each partition fits a workload limit (function resource budget). Observations 1-2 are empirical motivation, not formal.
properties: Theorem 1: the greedy rightmost-placement algorithm produces minimal cuts for a given limit; Theorem 2: validity of partition plans is monotone in the limit. Proof of Thm 1 is an exchange argument on the first differing cut; Thm 2's proof omitted.
usage: A small exchange argument certifies the partitioner embedded in the autonomous-elasticity mechanism.
role: design-driver — minor formal core validating one module of a systems paper.
quote: "Optimality: the algorithm produces minimal cuts for a given workload limit." (Thm 1)

### sigmod26-135 — Improved Accuracy for Private Continual Cardinality Estimation in Fully Dynamic Streams via Matrix Factorization
domain: privacy-dp | streaming | cardinality-estimation
props: upper-bound | lower-bound | tightness
tools: spectral-matrix | dp-composition | reduction
modeling: Continual counting under ρ-zCDP on fully dynamic streams (class S_{D,k}: turnstile bound D, ℓ1 bound k); MeanSE/MaxSE error notions; matrix-factorization mechanism with Toeplitz factor matrices; PODS article.
properties: Toeplitz sensitivity ‖RΔ‖₂ ≤ √(kD)·‖R‖₁→₂ (Thm 5.1); square-root factorization achieves MaxSE/MeanSE ≤ (1/πlog e + o(1))√(kD log T), with lower bound ~√(kD log(DT/k)·log T) — tight up to lower-order terms for wide k, D (Thm 5.2); sensitivity sandwich reduces S_{D,k} to alternating S₁,k streams (Thm 5.4).
usage: Summation-by-parts over the monotone Toeplitz kernel (upper bound), probabilistic method (lower bound); exact sensitivity noted NP-hard to compute.
role: theory-as-contribution — the error bounds for private continual cardinality estimation are the result.
quote: "the lower bound indicates that our analysis of the square-root factorization is tight up to lower order terms for a wide range of values of k and D." (Thm 5.2 discussion)

### sigmod26-146 — LICO: An SIMD-Aware High-Performance Learned Inverted Index Compression Framework
domain: storage-compression
props: upper-bound
tools: + ε-PLA bit-cost modeling (theorem imported, calibrated)
modeling: ε-PLA (piecewise linear approximation) of sorted posting-list keys; total bits = L(K|ε)·b_seg + n⌈log₂(2ε+1)⌉, trading segment count against residual width; SIMD-aware decoding and query operators.
properties: Theorem (cited from prior learned-compression work [9]): expected segment count L(K|ε) ∝ nσ²/ε², σ² = key-gap variance; coefficient C calibrated by least squares over sampled posting lists (C = 0.10997), giving a closed-form optimal error bound ε. Extract thin; proofs deferred to appendix.
usage: Differentiating the calibrated bit-cost model w.r.t. ε yields the optimal error-bound configuration; calibration itself is empirical.
role: design-driver — cost model selects ε; theory imported rather than extended.
quote: "the expected number of segments 𝐿(K | 𝜖) needed to fit an 𝜖-PLA on {(𝑖, 𝑘𝑖)} is 𝐿(K | 𝜖) ∝ 𝑛𝜎²/𝜖², where 𝜎² is the variance of key gaps." (Thm 4.1)

### sigmod26-158 — Maximal Biclique Enumeration with Improved Worst-Case Time Complexity Guarantee
domain: graph-db
props: correctness | upper-bound
tools: reduction + branching-recurrence analysis
modeling: Maximal biclique enumeration in bipartite graphs with size constraints τL, τR; output-sensitive complexity measured against β = number of maximal bicliques; branch-and-bound with pivots over candidate/excluded vertex sets.
properties: 2-biplex case: O(m + nβ) via complement structure (bicliques ↔ maximal independent sets of a max-degree-2 graph, paths/cycles); general: IPS enumerates in O(m·α^n + nβ), α ≈ 1.3954 = largest root of x⁴−2x−1 = 0; inclusion-exclusion variant O(nγ²·α^γ + γβ), strictly better on sparse graphs.
usage: Linear recurrences per branching case with growth rates from characteristic equations; complement-graph reduction for the structural lemma.
role: theory-as-contribution — the improved worst-case output-sensitive bound is the headline.
quote: "IPS enumerates all maximal bicliques in G in O(m · α^n + n · β) time, where α (≈ 1.3954) is the largest positive real root of x⁴ − 2x − 1 = 0." (Thm 3.2)
