### sigmod26-052 — Constrained Shortest Path Finding on Terrain Surfaces
domain: spatial
props: hardness | approximation-ratio | upper-bound
tools: reduction | induction | coresets-geometry
modeling: CPTS: shortest s–t path on a terrain surface visiting all points-of-interest; decision version; algorithm builds a (1+ε)-geodesic spanner graph over terminals, with aspect ratio α and doubling-like parameter β.
properties: NP-hardness via ETSP reduction (Thm 2); spanner preserves geodesic distances within (1+ε) (Thm 3); edge-count/weight/termination lemmas (O(log α·σ^2β) edges); 2-approximation via MST pre-order walk; O(ε^{-1}k^{2β}·N log²N) time, O(ε^{-1}k^{2β}+N) space.
usage: Contradiction and induction for spanner lemmas; triangle-inequality charging; Kruskal MST plus pre-order traversal gives the factor 2.
role: design-driver — spanner construction and its guarantees shape the whole algorithm.
quote: "It holds that dg(u,v) ≤ dG(u,v) ≤ (1+ε)·dg(u,v), where dG(u,v) is the shortest distance between u and v on G."

### sigmod26-110 — FIRAS: A Framework for Interval Range Search and Sampling
domain: indexing | sampling
props: upper-bound | correctness | space-complexity
tools: amortized-potential + Walker's-alias weighted sampling
modeling: Static and evolving interval collections; query result decomposed into disjoint Q1 (1D range) and Q2 (stabbing) parts (Prop 3.1); interval tree plus evolving-domain EDIT with √n-capacity buffers; IRS = uniform sampling of s results.
properties: IT range query O(log n+k) (Lem 2.7); IRS O(log n+s) average / O(log²n+s) worst with O(n) space (Thm 3.3); counting O(log²n); updates O(1) and O(√n)+U(n), amortized O(1) EDIT growth; evolving-case IRS O(√n+s).
usage: Disjoint-case decomposition proofs; per-node average-case analysis over random insertions; amortization over domain doubling; alias structures give O(1) weighted sampling.
role: design-driver — complexity lemmas steer EDIT/buffer design and the space-improvement claims vs SOTA.
quote: "With O(n) space, FIRAS can process an IRS query correctly in O(log n + s) and O(log² n + s) times in the average and worst cases, respectively."

### sigmod26-189 — Periodic Community Search in Temporal Graphs
domain: graph-db | time-series
props: correctness | upper-bound
tools: + monotonicity/case-analysis arguments
modeling: Temporal graph snapshots; k-core time series (binary, length T); Jaccard ε-approximate periodicity and maximal periodic subseries; maximal temporal core set MC(S); vertex time lists; TP-Core index. Clean definitional extract.
properties: Monotonicity of MC under series inclusion (Thm 4.3); incremental non-emptiness generation (Thm 4.4); time-list inclusion for community members (Thm 5.2); recursive sublist-enumeration identities (Thms 5.3, 5.7); iff-characterization of candidate communities (Thm 5.5); index construction complexity analysis.
usage: Contradiction and partition arguments over timestamp sets; monotonicity prunes the enumerated sublists in the vertex-deletion algorithm.
role: design-driver — Theorems 4.3/5.3/5.5 directly generate the VD algorithm's search space and pruning rules.
quote: "Given ... two time indicator series S and S′, if S ≤ S′, then MC^k_q(S′) ⊆ MC^k_q(S)."

### sigmod26-200 — Querying Cohesive Subgraphs in Temporal Graphs
domain: graph-db
props: correctness | upper-bound | space-complexity
tools: amortized-potential | induction | exchange-greedy
modeling: Abstract cohesive-subgraph model (CSM) required to be non-overlapping and monotonic; u–v time windows; Historical-CSM queries recast as a CSM-free spanning-CC query over an affiliated graph/forest, answered as 3-D orthogonal range search.
properties: CC, k-core, connected k-core are non-overlapping monotonic CSMs (Lem 2.3); BuildAF and AFDecomp correctness (Lems 3.6, 3.10); queries O(n+log²m), construction O(m log m), O(m) space for AF-BTAS (Lems 3.12–3.13).
usage: Union-find with inverse-Ackermann amortization; Kruskal-style cycle edge-exchange for the decomposition; induction for correctness; priority search trees for the range queries.
role: design-driver — the monotone-CSM abstraction plus affiliated-forest decomposition enables one unified index.
quote: "The construction of BTAS runs in O(m log m) and BTAS-Index costs O(m) space."

### sigmod26-031 — Balancing Global and Local: Representative Sampling for Large-Scale Vector Data
domain: sampling | ann-vector-search
props: hardness | approximation-ratio | error-bound
tools: estimation-theory | concentration-ineq | exchange-greedy
modeling: Representative sampling as budgeted coverage plus local-fidelity (CostLID) optimization; assumptions (A1)–(A3): uniform neighbor directions, Exp(1) normalized distances, availability probability α; LID estimator as scaled inverse-Gamma sum.
properties: Exact bias/variance/MSE of the LID estimator (Lem 1), fidelity-loss bound via Jensen (Lem 2); progress-probability lower bound 1−exp(−α·m·p_geom) for graph traversal (Thm 1); NP-hardness via metric k-median reduction (Thm 2); submodular fidelity objective with (1−1/e) lazy-greedy guarantee (Thm 3).
usage: Gamma-sum moment identities; (1−p)^m ≤ e^{-mp}; contraction-unrolling greedy analysis; parsimonious k-median reduction.
role: design-driver — estimator MSE and progress-probability theory justify the CostLID objective and greedy sampler.
quote: "Let B be the budget and let A_gre be the size-B output of (lazy-)greedy in Algorithm 2. Then F(A_gre) ≥ (1 − 1/e) max_{|A|≤B} F(A)."

### sigmod26-304 — Efficient and Scalable Directed Densest Subgraph Discovery
domain: graph-db
props: approximation-ratio | convergence-rate | correctness
tools: duality | concentration-ineq + Fujishige min-norm base / FISTA
modeling: Directed density |E(S,T)|/√(|S||T|); (1+ε)-approximation and exact regimes; DP(c) ℓ∞ fractional formulation vs smooth QP(c) weighted-ℓ2 over the base contrapolymatroid of supermodular f(S,T)=|E(S,T)|; wcore-based graph reduction; power-law degree assumptions for whp results.
properties: DDS contained in ⌈ρ*²/4⌉-wcore (Thm 4.2); DP/QP optimal-solution equivalence (Thms 5.2–5.3); FISTA-DDS ε-closeness iteration bound (Thm 5.5); FBAD (1+ε)-approximation in O(Φ√m/ε) iterations, whp O(Φ√(mn)/ε) under power-law degrees (Thm 6.1).
usage: Per-edge Iverson-bracket case analysis for supermodularity; max-flow feasibility construction; Fujishige's theorem transfers ℓ2 optima to ℓ∞; FISTA gap-to-ℓ∞ conversion.
role: theory-as-contribution — equivalence and iteration-rate theorems are the claimed breakthrough over SOTA.
quote: "The optimal solution to QP(c) over B_f also serves as the optimal solution to DP′(c)."

### sigmod26-094 — Enumerating Graph Pattern Matches with ML Oracles
domain: graph-db
props: hardness | competitive-ratio | probabilistic-guarantee
tools: reduction | competitive-analysis | concentration-ineq
modeling: Subgraph-isomorphism match enumeration pruned by an ML oracle M (error rate η) judging partial matches; robustness = F1-based β-robustness; output-polynomial time; EnumP/fewP complexity classes; oracle confidence thresholds δ_F, δ_T.
properties: SubIso is EnumP-complete (Thm 1); no algorithm is both output-polynomial and β-robust unless fewP=P (Thm 2); precision 1 and consistency (Thm 3); recall/robustness bounds with probability ≥1−ε (Thms 4–5); whp output-polynomial runtime (Thm 6); competitive ratios vs offline OPT (Cor 7, Thm 8).
usage: Parsimonious reductions for enumeration hardness; generalized Bonferroni inequality bounds false-prediction impact; cost partition by oracle confidence for the ratios.
role: theory-as-contribution — impossibility plus guarantee theorems for ML-oracle enumeration.
quote: "No algorithm exists for SubIso that is both output polynomial and β-robust for any positive constant β unless fewP = P."

### sigmod26-157 — Mathematical Foundations of Poisoning Attacks on Linear Regression over CDFs
domain: security
props: correctness | upper-bound
tools: exchange-greedy + calculus/convexity
modeling: Linear regression over the cumulative distribution of index keys K; poisoning adds λ points to maximize squared loss E(K∪P); relaxed continuous variant with a multiset poison allocation over keys; single- and multi-point attack settings.
properties: Optimal single-point attacks lie adjacent to keys (Thm 1); prior greedy multi-point attack can be suboptimal (Obs 2); optimal multi-point attacks form chains adjacent to keys (Thm 2); relaxed optimum uses the full budget, supported on K (Thms 3–4); convexity in w (Thm 5) and endpoint/single-key concentration of the optimum (Thm 6); O(n) and O((n+λ)λ) algorithm bounds.
usage: Sign/monotonicity calculus of the loss; contradiction at interval endpoints; move-a-poison exchange arguments; closed-form inner optimum in b.
role: theory-as-contribution — optimality foundations for previously heuristic poisoning attacks.
quote: "The optimal multi-point attack consists only of poison keys that are either adjacent to legitimate keys directly or connected transitively to legitimate keys via chains of neighboring poison keys."

### sigmod26-150 — LMSC: Local Sketch Modularity for Size-Constrained Community Search
domain: graph-db
props: hardness | robustness-stability
tools: reduction | adversarial-construction
modeling: Local Sketch Modularity LSM = l_C/(o_C·|C|^τ): purely local internal/external edge weights with size penalty τ; LMSC problem with query nodes and size constraint [l,h]; free-rider effect formalized; chain-based relaxation CLSM for greedy expansion.
properties: LMSC NP-hard via Set Cover reduction (Thm 1); LSM strictly less free-rider-prone than Luo modularity (Thm 2); no free-rider effect when the community is weak-sense and τ > log_{1+1/h}(h(h−1)/2) (Thm 3); LSM is non-monotone (Thm 4) and non-submodular (Thm 5).
usage: Algebraic comparison of LM/LSM gain differences; worst-case log-ratio bounding for the τ threshold; explicit clique counterexamples for non-monotonicity/non-submodularity.
role: design-driver — objective properties (locality, free-rider threshold, non-submodularity) motivate the greedy and chain-based heuristics.
quote: "LSM does not suffer from local free-rider effect when the identified community is a weak sense community and τ > log_{1+1/h}( h(h−1)/2 )."

### sigmod26-006 — A Unified Framework for Dense Subgraph Maintenance over Dynamic Bipartite Graphs
domain: graph-db
props: upper-bound | space-complexity | correctness
tools: peeling-dyadic | reduction
modeling: Bipartite (α,β)-core maintenance under edge updates via the BCO-index (onion layers); κBCO-index for the k-(r,s)-nucleus by encoding r-/s-cliques as a bipartite graph; "bounded" maintenance = touching only the 1-hop neighborhood of the changed set L_CHG.
properties: Construction O(m·d_max) time, O(n·d_max) space (Thms 1, 3); maintenance O(||L_CHG||¹) (Thms 2, 4–5); (k,rs)-core equals the k-(r,s)-nucleus (Lem 3); bipartite encodings recover k-core ((k,2)-core) and k-truss ((k−2,3)-core) (Cors 1–2).
usage: Counting peeling passes for construction bounds; locality argument — only changed nodes and neighbors visited; clique-counting combinatorics for the encoding equivalences.
role: design-driver — boundedness/locality theorems dictate both index structure and maintenance algorithms.
quote: "Algorithm 4 is bounded by L_CHG and takes O(||L_CHG||¹) time and uses O(n·d_max) space, where L_CHG is the changed part of BCO-index."

### sigmod26-049 — Concurrent Composition for Differentially Private Continual Mechanisms
domain: privacy-dp
props: privacy-guarantee | tightness | lower-bound
tools: dp-composition | reduction | adversarial-construction
modeling: Continual mechanisms as interactive mechanisms with singleton initial state; identifier/verifier IPMs define DP against adaptive adversaries; f-concurrent composition lets the adversary adaptively create and query CMs; discrete-answer-distribution assumption; randomized response RR_{ε,δ} as the calibration primitive. A few table-fragment statements; proofs deferred to full version.
properties: Concurrent composition of CMs inherits exactly the (ε,δ) of composing noninteractive mechanisms (Thms 1.4, 4.7); k-sparse parallel composition results (Thm 5.4, Cors 5.5, 5.7); counterexample: k-sparse composition of (0,δ)-DP CMs fully leaks the bit (Thm 5.2), making Thm 5.4 tight; Rényi-DP and f-DP extensions.
usage: Simulating any (ε,δ)-DP CM by interactive post-processing of RR outputs, dropping prior finiteness/bounded-interaction assumptions; separate composition of RR groups; explicit adversary for impossibility.
role: theory-as-contribution — pure composition theory (PODS); the theorems are the paper.
quote: "The concurrent composition of continual mechanisms Mi that are (εi, δi)-DP ... is (ε, δ)-DP for the same (ε, δ) that holds for composing noninteractive mechanisms."

### sigmod26-257 — Zero-Redundancy Search for Bi-Components in Bipartite Graphs
domain: graph-db
props: correctness | upper-bound | space-complexity
tools: + core-nesting decomposition lattice
modeling: (α,β)-core/component/community search; nesting and overlap relations among bi-cores; predecessor values; bi-clusters (α,β,γ) and γ-groups partitioning components; summary graph (SNodes/SEdges with c-pairs) with an edge-redundancy criterion. Mildly noisy extract — figure fragments interleaved with definitions.
properties: Disjoint-cover theorems: a bi-core equals the union of its γ<α clusters with exact cardinality sum (Thm 1), likewise components via γ-groups (Thm 2); SEdge redundancy characterization (Lem 4); storage O(μn) and search O(|H|), zero redundancy vs prior indexes (Table 1).
usage: Ordering and contradiction arguments over the c-pair lattice; disjointness yields one-copy storage; the redundancy test prunes summary edges.
role: design-driver — partition theorems produce the zero-redundancy index and the O(|H|) search cost.
quote: "(1) C = ⋃_{i=1..k} x_i and (2) |C| = Σ_{i=1..k} |x_i|, where |C| and |x_i| represent the number of vertices in C and x_i, respectively."

### sigmod26-283 — Budgeted Strong Community Search in Heterogeneous Graphs
domain: graph-db
props: hardness | correctness | upper-bound
tools: reduction
modeling: Heterogeneous graph with schema and meta-paths; P-support measure over meta-path instances; Budgeted Strong Community (BSC) containing the query node under degree and P-score thresholds; random-graph baseline G′ for support estimation.
properties: BSC is NP-hard via k-clique reduction (Thm 2.8); the optimization version is not in APX for D[A0]≥4 unless P=NP, via an L-reduction from MSMD_d (Thm 2.9), hence no PTAS (Cor 2.10); StrCom union/containment structure (Lem 2.11, Thm 2.12); P-support upper bound exact for meta-path lengths 3–4 (Thm 4.1); expected degree/support formulas on G′ (Lem 4.2).
usage: Standard and L-reductions with explicit constants (α,β)=(2,2); linearity-of-expectation computations set pruning thresholds.
role: design-driver — hardness plus containment/upper-bound results delimit the algorithm's search space.
quote: "The optimization version of the BSC problem is not in APX for any D[A0] ≥ 4, unless P = NP."
