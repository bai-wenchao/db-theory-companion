### sigmod26-294 — DAG of DAGs: Order-Fairness Made Practical
domain: consensus-replication | transactions
props: correctness
tools: reduction | + quorum-threshold arithmetic
modeling: BFT transaction ordering: n replicas, f faulty, fairness parameter γ; local-order messages induce a weighted majority graph; Condorcet cycles collapsed via condensation graph; global order built on Narwhal/Tusk certificates of availability. Pdf-derived extract with page-header noise.
properties: Order-fairness (γn replicas receiving t before t' ⇒ t' never ordered before t), safety, liveness; acyclicity of the pruned global-order graph; quorum lemmas on fixed/pending transactions.
usage: Weight-threshold counting over local-order messages (n−2f vs n(1−γ)+f) proves each lemma; safety reduced to Narwhal/Tusk; cycle-encapsulation keeps the condensation DAG acyclic.
role: design-driver — pruning/edge-selection rules are shaped so the fairness, safety and liveness proofs go through.
quote: "DoD guarantees data-dependent order-fairness. … DoD guarantees safety. … DoD guarantees liveness."

### sigmod26-305 — Efficient ANNS via Hemi-Sphere Centroids Graph
domain: ann-vector-search
props: upper-bound | correctness
tools: induction | + sphere-to-tangent-plane geometry (Yao ray packing, Gauss-Bonnet)
modeling: ANNS under cosine similarity on the unit sphere; MRNG graph index; Monotonic Search Network (MSNET) framework where greedy best-first search follows strictly increasing similarity.
properties: MRNG-CS is an MSNET (search reaches any query without backtracking); maximum out-degree bounded by a constant C_{d−1} independent of N, matching the Euclidean bound in R^{d−1}; minimum geodesic angle between out-edges ≥ π/3.
usage: Rays on S^{d−1} mapped one-to-one to a Euclidean tangent hyperplane, applying Yao/Fu's K(d−1,φ) ray-packing lemma; Gauss-Bonnet gives the angle bound; induction proves monotone-path search.
role: design-driver — the constant-degree property under cosine similarity dictates the HSC graph construction.
quote: "For any MRNG constructed using cosine similarity as the measure, the maximum out-degree is bounded by a constant C_{d−1} that is independent of the number of vertices."

### sigmod26-081 — Efficient Anchored Densest Subgraph Discovery
domain: graph-db
props: approximation-ratio | convergence-rate | lower-bound
tools: peeling-dyadic | + convex optimization (Frank-Wolfe/FISTA analysis)
modeling: Anchored densest subgraph under NR-density, formulated as a quadratic program QP(G,A) and an equivalent unconstrained-relaxed QP′; solved by Frank-Wolfe (FDP) and accelerated FISTA (PASTA); novel k-r-core enables graph reduction. Noisy pdf extract — mangled exponents and table fragments inside statements.
properties: OPT(QP)=OPT(QP′); gradient Lipschitz constant L_f ≤ 2(|A|+1)·Δ(G)·vol(R); ADS contained in ⌈ρ_R⌉-r-core; k-r-core existence gives density lower bound; (1+ε)-approximation with fewer iterations than FDP.
usage: Curvature/Lipschitz bounds feed standard Frank-Wolfe/FISTA convergence theorems to get iteration counts; peeling-style r-core reduction shrinks the search space provably safely.
role: design-driver — relaxation, acceleration and core-reduction choices are derived from the convergence analysis.
quote: "The ADS D = G[S*] must be contained within G[V(M*) ∪ A], where ρ*_R is the NR-density of the ADS D."

### sigmod26-142 — Kangaroo: Lossless Floating-Point Compression
domain: storage-compression | time-series
props: correctness
tools: + monotone-subsequence (T-LSIS/T-LNDS) structure on leading-zero arrays
modeling: Floating-point time series compressed by XOR against a dynamically chosen reference after bit-erasure; cost model over an LZ-history array of leading-zero counts; search space partitioned into complete/incomplete "hops"; IEEE 754 bit-level representation.
properties: No reference inside an incomplete hop beats its boundary; only complete-hop left endpoints can beat right endpoints; the optimal reference lies in the boundary set B_i (all other candidates proven non-optimal); erasure preserves the exponent; erasure parameter α uniquely reconstructible (losslessness).
usage: Leading-zero inequalities via longest-increasing-subsequence conditions prune reference selection to O(1)-maintained boundaries; IEEE-754 bit arithmetic proves erasure invertibility.
role: design-driver — optimality and unique-decodability theorems justify the dynamic reference and erasure machinery.
quote: "Then the α can be uniquely reconstructed as: α = ⌊(52 − E′ − trail v′) lg 2⌋."

### sigmod26-010 — Accelerating Triangle-Connected Truss Community Search
domain: graph-db
props: correctness
tools: + equivalence-class partitioning and transitivity of k-triangle connectivity
modeling: k-truss and triangle-connected k-truss community (k-TTC) search; internal/marginal/external k-triangle taxonomy; EquiTree index of supernodes (k-truss equivalence classes) linked by superedges; tensor-based implementation over heterogeneous hardware.
properties: Processing order of triangles does not affect EquiTree construction (index is deterministic); supernode membership follows trussness equality plus connectivity; after one refinement round maximal active supernodes become static and are never reactivated (termination).
usage: Transitivity of k-triangle connectivity shows supernodes/superedges are order-independent, licensing parallel out-of-order tensorized construction; monotone trussness ordering proves refinement stops.
role: design-driver — order-independence is precisely what enables the parallel/heterogeneous implementation.
quote: "The processing order of triangles does not affect the construction of the EquiTree index."

### sigmod26-137 — Improving LZ4 for Effective Compression and Efficient Query
domain: storage-compression
props: upper-bound | lower-bound | correctness
tools: + case analysis over hash-table and block-run invariants
modeling: LZ77/LZ4 matching formalized via Mat/Max definitions over a sequence alphabet; compressed data as b blocks of m bytes with inter-block dependency chains; LZV compressor plus CIS compressed-data query with auxiliary jump arrays.
properties: Hash-table lookup finds the maximal match position (no missed matches); match finding O(l²), LZV compression O(ln); worst-case retrieval of the last element requires Ω(b); CIS query O(b); block count b ≤ m/3.
usage: Run-structure case analysis (matched elements in runs ≥ 4) proves hash coverage; aggregating per-block costs ∑(m_i²+u_i) ≤ l·n; dependency-chain chaining gives the query lower bound that CIS matches.
role: design-driver — CIS is designed to match the Ω(b) worst-case compressed-data query bound.
quote: "In the worst case, retrieving the last element D[n−1 : n−1] from C requires at least O(b) time."

### sigmod26-180 — ORDER: Optimal Routing with Path Indexing in Exchange Graph
domain: + DeFi exchange order routing
props: upper-bound | correctness
tools: amortized-potential | sketching-theory
modeling: Exchange graph with ordered edge groups (parallel swap venues ordered by weight, each with capacity); path selection as min-weight paths with bottleneck capacity; prioritized bucket index with an active top-K heap and reserve buckets; KLL quantile sketch sets the admission threshold. Application-track paper.
properties: On-demand bottleneck capacity is exact; no reserve path can dominate an active path (bucket-order invariant); provably safe early stopping of rebuilds; results invariant to K; amortized per-selection cost O(|P|/T + 1 + (K/T)·log K); optimal K exists by quasi-convexity.
usage: Contradiction proofs on the global weight ordering validate lazy maintenance; epoch decomposition (scan + heap build + per-selection heap ops) yields the amortized bound.
role: design-driver — bucket hierarchy and lazy updates are engineered around the domination invariants and amortized analysis.
quote: "For any two indices i < i′, no path in B_i′ has a strictly smaller ordering key than a path in B_i."

### sigmod26-073 — Differentially Oblivious Multi-way Join
domain: join-algorithms | privacy-dp
props: privacy-guarantee | upper-bound | asymptotic-optimality
tools: dp-composition | + smooth-sensitivity (local sensitivity) analysis
modeling: Access-pattern leakage formalized via full-oblivious and "advised FO" algorithms; differential obliviousness (ε,δ)-DO; multi-way joins with maximum boundary T_E(I); smooth upper bounds built by dropping boundary attributes (RST) and incorporating degrees (EST); residual-linear join class; fractional hypertree width w.
properties: Meta-algorithm is (ε1+ε2, δ1+δ2)-DO by composition; DOJoin is (ε,δ)-DO in O((N^w + |Q(I)| + RRS(I))·log N) time; on residual-linear joins (line, star, hierarchical) this asymptotically matches the Ω(N + max_E T_E) lower bound.
usage: FO join evaluation leaks only input size plus a DP-noisy join-size bound; RST/EST lemmas establish smoothness of the sensitivity bound; hybrid construction picks the cheapest valid smooth bound per subset.
role: theory-as-contribution — the DO guarantee with matching complexity is the paper's core result.
quote: "Algorithm 3 runs in O((N^w + |Q(I)| + RRS(I)) · log N) time under data complexity, where w is the fractional hypertree width of the join query."

### sigmod26-169 — Nucleus Decomposition Revisited: A Counting-Based Approach
domain: graph-db
props: correctness
tools: + combinatorial counting over clique-path encodings
modeling: (r,s)-nucleus decomposition via a Clique Path Index: each path has mandatory hold vertices and optional pivot vertices; every k-clique is encoded by a unique path; s-connectivity links r-cliques through induced s-cliques; supports dynamic edge updates.
properties: Unique path encoding of k-cliques; number of s-cliques lower-bounds the number of surviving pruned paths; clique-removal updates preserve soundness and completeness (each surviving clique encoded on exactly one subpath); connectivity of r-cliques within a path.
usage: Binomial counting over hold/pivot vertices yields per-path clique counts; case-split path updates (hold-hold/hold-pivot/pivot-pivot edges) keep the encoding exact under edge deletion.
role: design-driver — index construction and incremental maintenance algorithms are built directly on the encoding theorems.
quote: "Then |K_s| ≥ |P_s|. Moreover, ∑_{P∈P_s} |V_h(P)| ≤ s |K_s|."

### sigmod26-013 — Adaptive Outlier Detection over Data Stream
domain: streaming
props: correctness
tools: + hypercube min/max distance-bound geometry on a quadtree
modeling: Distance-based outliers D(n,k,r) over sliding windows; relaxed R-OD with relaxation parameter ρ (ρ-neighbors, ρ-inliers); quad-tree index with node side lengths; k-nodes and node distance lower bounds e(l_k). Lemma 2 is an empty pdf-extraction stub; math partially mangled.
properties: If e(l_k) > r all objects in a small node are outliers, if ≤ r they are ρ-inliers (100% precision; missed outliers still have k neighbors within (1+ρ)r); k-nodes have zero lower bound; kNNs of descendants of k-nodes are contained in the node neighborhood; full detection reduces to maintaining k-node neighborhoods.
usage: Hypercube min/max distance arithmetic turns node-level bounds into bulk inlier/outlier verdicts, pruning per-window recomputation.
role: design-driver — the index and pruning rules follow directly from the node-bound theorems.
quote: "If e(l_k) > r, all objects in e are outliers; if e(l_k) ≤ r, all objects in e are ρ-inliers."

### sigmod26-027 — ASSS: Adaptive Stratified Sampling for Shapley-like Values
domain: sampling
props: lower-bound | sample-complexity | probabilistic-guarantee
tools: estimation-theory | concentration-ineq | dp-optimality
modeling: Shapley-like values as weighted coalition-game values; estimation by Monte Carlo sampling stratified by coalition size; generalized stratification as a partition of {1..n}; two adaptive variants — stratify after sampling (ASSS-A) and before (ASSS-B); compared to GELS. Statement-heavy extract, no proofs captured.
properties: Static stratified sampling needs Θ(n² log n) samples (harmonic-sum lower bound); stratification matching unstratified proportions provably reduces variance, with exact variance gap; optimal stratification is consecutive, solvable by DP in O(Ln²); ASSS fills L strata with Ω(L² log L) samples, unbiased w.p. > 1−1/n²; Var(ASSS) ≤ Var(GELS); (ε,δ) bounds via CLT, Chebyshev, Hoeffding.
usage: Variance decomposition and unbiasedness arguments; DP over layer boundaries for optimal stratification; concentration inequalities convert variance into (ε,δ) sample sizes.
role: design-driver — the adaptive stratification scheme is designed around the Θ(n² log n) barrier and variance-dominance conditions.
quote: "E[m_n] ≥ n(n−1) ∑_{k=1}^n 1/k ≈ n²(ln(n) + γ) = Θ(n² log n)."

### sigmod26-179 — Order-based Algorithms for Core Maintenance in Bipartite Graphs
domain: graph-db
props: lower-bound | upper-bound | correctness
tools: adversarial-construction | + order-invariant (BD-Order) maintenance
modeling: Bipartite (α,β)-core (c-pair) maintenance under edge insertions/deletions; locally persistent algorithm model; BD-Order vertex orders per α-level with lack values and supports; AFF/CHANGED change sets quantify update scope.
properties: Insertion updates are unbounded for locally persistent algorithms (adversarial two-update construction), while deletions are bounded — an asymmetry theorem; insertion algorithm runs in O(|N1(AFF)|·|N2(AFF)|) (near-bounded); deletion in O(|CHANGED|+|N1(CHANGED)|); both algorithms update c-pairs and orders correctly.
usage: Order-position necessary/sufficient conditions (lack values, monotone paths in the order) prune candidate sets; the adversarial construction separates insertion from deletion complexity.
role: design-driver — boundedness asymmetry motivates the order-based candidate identification that the algorithms build on.
quote: "Updating these bi-cores after inserting an edge (u,v) is unbounded under the model of locally persistent algorithms."

### sigmod26-205 — Recursive Querying of Neural Networks via Weighted Structures
domain: + querying neural networks as weighted structures
props: hardness | upper-bound
tools: mso-logic | reduction | + finite-model theory (Immerman-Vardi, pebble games)
modeling: Feedforward networks as finite weighted structures; FO(SUM) aggregation logic extended with inflationary fixpoints (IFP(SUM)), functional vs loose fixpoint semantics shown equivalent; scalar fragment sIFP(SUM); reduced networks with polynomially bounded reduced weights; classes K(m,d) of bounded I/O dimension and depth.
properties: FO(SUM) simulates FO(R_lin,f) at fixed depth; normal form for IFP(SUM); sIFP(SUM) evaluates in polynomial time (XP parameterized by expression length); a PTIME query inexpressible in IFP(SUM) even with 0/1 weights (CFI + bijective pebble games); sIFP(SUM) captures PTIME on polynomially-bounded-reduced-weight classes; deciding whether an FNN computes a non-zero function is NP-hard already on K(1,1).
usage: Fixpoint semantics over aggregate terms define recursion on weights; pebble-game/CFI constructions prove inexpressibility; a 3-SAT reduction encodes assignments into network inputs; Immerman-Vardi yields the capture theorem.
role: theory-as-contribution — PODS-style expressiveness and complexity results are the paper.
quote: "It is NP-hard to decide if an FNN N ∈ K(1,1) computes a non-zero function, that is, if f_N(x) ≠ 0 for some x ∈ R."
