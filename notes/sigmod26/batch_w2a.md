### sigmod26-371 — The Space-Time Complexity of Sum-Product Queries
domain: join-algorithms
props: upper-bound | space-complexity | conditional-lower-bound
tools: induction | adversarial-construction
modeling: Sum-product queries (CQs over semirings) evaluated by nested plan classes — pseudo-trees, cached pseudo-trees, tree decompositions, recursive pseudo-trees — each with recursively defined space/time exponents; classes compared via a plan-domination preorder.
properties: Correctness lemmas for recursive solve/cache algorithms; O(|D|^t)-time, O(|D|^s)-space bounds per class; strict-dominance separations via witness path queries; conjectured Triple-k-Clique space-time lower bound over the tropical semiring.
usage: Induction over trees and elimination orders; AGM/fractional-edge-cover bounds on intermediates; explicit witness-query constructions; heavy/light partitioning for sublinear-space plans.
role: theory-as-contribution — the space-time hierarchy of plan classes is the result.
quote: "For any ε > 0, no algorithm can solve this problem over the tropical semi-ring in space S=O(|E|^k4−ε) and time T=O(|E|^k2)."

### sigmod26-289 — Clustering with Set Outliers and Applications in Relational Clustering
domain: + clustering-outliers
props: approximation-ratio | hardness | probabilistic-guarantee
tools: reduction | coresets-geometry
modeling: k-center clustering with set (hyperrectangle/family) outliers, approximation quality as an (α,β,γ) triple over centers/outliers/cost; relational variant where points are tuples of an acyclic join accessed via counting/sampling oracles; bounded doubling-dimension metrics.
properties: Polytime (2,2,O(1)) and (2+ε,2f,2+ε)-approximation theorems with explicit runtimes; UGC-based inapproximability of (1,f−ε,γ); coreset reduction to O(min{n,k²z,km}) points; w.h.p. guarantees for join-based algorithms.
usage: LP feasibility plus greedy rounding with weight-charging arguments; Set-Cover reductions via line-point encodings; coresets shrink instances; randomized repetition over join samples.
role: theory-as-contribution — approximation algorithms and hardness for a new outlier model.
quote: "If the Unique games conjecture is true, there exists no (1, f−ε, γ)-approximation algorithm that runs in polynomial time for the problem, where f = o(log n)."

### sigmod26-307 — Efficient Exact Resistance Distance Computation on Small-Treewidth Graphs
domain: graph-db
props: correctness | upper-bound | space-complexity
tools: spectral-matrix | induction
modeling: Exact resistance distance via pseudo-inverse of the graph Laplacian; Gaussian elimination ordered along a heuristic tree decomposition; labels store columns of the shrinking inverse (Schur complements); complexity parameterized by decomposition height h_G and max degree d_max.
properties: Correctness of index construction (rank-1 update formula); construction O(n·d_max·h_G²); label size O(n·h_G); single-pair query O(h_G), single-source O(n·h_G); label sparsity via cut and vertex-hierarchy properties.
usage: Block-matrix inversion/Schur complements derive elimination formulas; induction on eliminated node sets; random-walk interpretation for the cut property; subtree-contiguous traversal for lookup.
role: design-driver — correctness and height-parameterized bounds shape the labelling scheme.
quote: "Algorithm [index-building] has a time complexity of O(n · d_max · h_G^2)."

### sigmod26-298 — Differentially Private Explanations for Clusters
domain: privacy-dp
props: privacy-guarantee | error-bound | upper-bound
tools: dp-composition
modeling: Cluster explanations as attribute selections scored by interestingness/sufficiency/diversity over cluster-vs-dataset distributions; DP under one-tuple neighboring datasets; pipeline of per-cluster top-k exponential mechanisms, global combination, noisy histograms.
properties: Overall (ε_CandSet+ε_TopComb+ε_Hist)-DP by sequential/parallel composition plus post-processing; new scores with sensitivity exactly 1 (triangle-inequality proofs); TV/JSD interestingness shown to have sensitivity ≥ 1/2; exponential-mechanism utility bound.
usage: Composition/post-processing calculus assembles the end-to-end privacy proof; direct sensitivity analyses (L1 histogram algebra, binary-entropy limits) justify replacing standard divergences with low-sensitivity scores.
role: design-driver — sensitivity analysis dictates which quality scores are privately usable.
quote: "Given a clustering function f: ..., alg:gen_global_explanation is (ε_CandSet + ε_TopComb + ε_Hist)-DP."

### sigmod26-350 — Query Answering Under Volume-Based Diversity Functions
domain: + diverse-query-answering
props: approximation-ratio | hardness | correctness
tools: exchange-greedy | reduction
modeling: Answer diversity as volume: each tuple maps to a set β(t), diversity δ_Ω(S)=μ(∪β(s)); DiverseSet/DiverseTopk problems over CQ answers with tree-decomposition-compatible rankings (fractional hypertree width); generalizes multi-attribute diversity.
properties: δ_Ω always monotone submodular ⇒ (1−1/e) greedy approximation; NP-hard even singleton case (Hamiltonian path, independent set); MaxCoverage gives (1−1/e) inapproximability unless P=NP; O(k·|Q|·|D|) approximation for acyclic CQs; distance-based diversity shown non-submodular.
usage: Measure-algebra submodularity proof; combinatorial reductions; marginal diversity evaluated as a tropical-semiring sum-product query; ranked enumeration with compatible rankings for preprocessing.
role: theory-as-contribution — new diversity framework with matching tractability/approximability frontier.
quote: "Let Ω be any volume assignment over a universe U of possible solutions. Then δ_Ω is always monotone and submodular."

### sigmod26-264 — A Unifying Algorithm for Hierarchical Queries
domain: provenance | uncertain-data
props: correctness | upper-bound | hardness
tools: induction | reduction | + semiring-provenance
modeling: Hierarchical self-join-free BCQs over "twomonoid"-annotated databases (two commutative monoids with absorbing 0); provenance trees as canonical annotations; one elimination algorithm instantiated to bag-set repair maximization, counting k-subsets, and tuple-independent probabilistic evaluation.
properties: Correctness via decomposable-provenance invariant (pairwise disjoint supports); linear number of ⊕/⊗ operations; O((|D_ex|+|D_re|)·θ²) time; dichotomy: non-hierarchical queries make repair-decision NP-complete / W[1]-hard parameterized.
usage: Variable-elimination rules (private variables, duplicate atoms) with invariant induction; homomorphism φ commuting with monoid operations transfers provenance to each application; bipartite-clique reduction for hardness.
role: theory-as-contribution — a unifying algebraic framework with per-problem complexity dichotomy.
quote: "Then, the output of Algorithm [hierarchical] on Q and D_φ is the φ-mapping of the output of Algorithm [hierarchical] on Q and D₊."

### sigmod26-375 — Tractability Frontiers of the Shapley Value for Aggregate Conjunctive Queries
domain: provenance
props: hardness | upper-bound
tools: reduction | + shapley-axioms
modeling: Shapley value of a fact for aggregate queries αQ (sum/max/min/median/quantile) with "localized" value functions applied at head positions; exogenous/endogenous fact split; tractability boundary drawn at hierarchical vs q-hierarchical CQs.
properties: Dichotomy: polynomial-time computation iff Q hierarchical (max/min/sum with localized functions), otherwise #P-complete for some localized function; #P-completeness for concrete queries; closed-form Shapley formulas for special average/quantile cases.
usage: #Set-Cover and permanent reductions via databases whose Shapley values encode coverage counts; Shapley linearity/symmetry/dummy axioms to decompose; injective transformations shifting value functions across aggregation.
role: theory-as-contribution — a tractability frontier for Shapley over aggregate CQs.
quote: "If Q is [hierarchical], then φ(f, A_α) is computable in polynomial time ... Otherwise, there is a localized [value function] such that computing φ(f, A_α) is #P-complete."

### sigmod26-259 — A Bouquet of Results on Maximum Range Sum: General Techniques and Hardness Reductions
domain: spatial
props: approximation-ratio | conditional-lower-bound | probabilistic-guarantee
tools: concentration-ineq | reduction
modeling: Maximum Range Sum — placing a d-ball/interval to maximize covered weight; static, dynamic (amortized update), colored (count distinct colors), and batched (many query lengths) variants; approximation-vs-update-time tradeoffs.
properties: Randomized (1/2−ε)-approximation for static/dynamic with O(ε^{-2d-2} log n) amortized update, whp; (1−ε)-approx and exact algorithms for colored disks; conditional Ω(mn)/Ω(n²) lower bounds from (min,+)-convolution hardness, near-matching trivial upper bounds.
usage: Grid-shifted random sampling of points with Chernoff plus union bound for weighted-depth concentration; guard-point encodings reduce (min,+)-convolution to batched MaxRS; trapezoidal maps for exact colored enumeration.
role: theory-as-contribution — approximation and conditional lower bounds across MaxRS variants.
quote: "Assuming that (min,+)-convolution on sequences of length n requires Ω(n²) time, the batched MaxRS problem on n points and m query interval lengths requires Ω(mn) time."

### sigmod26-303 — Effective Clustering for Large Multi-Relational Graphs
domain: graph-db
props: correctness | error-bound | probabilistic-guarantee
tools: spectral-matrix | randomized-nla
modeling: Multi-relational graph clustering as normalized-cut trace maximization over a doubly stochastic multi-relational affinity; closed-form S* = (1/(1+α))(I − α/(1+α)S)^{-1} approximated by truncated Neumann series; relaxation of discrete cluster indicators. Extract mildly noisy (leftover draft comments; NP-hardness mentions are related-work context).
properties: Equivalence of the doubly-stochastic objective with weighted k-means; spectral-norm truncation-error bound via eigengaps; CountSketch preserves trace/Frobenius norms with probability ≥ 1−δ; N-cut NP-hardness cited as motivation.
usage: Neumann series with Lidskii/Courant–Fischer eigenvalue arguments; Sinkhorn–Knopp scaling (Birkhoff–von Neumann) for a symmetric doubly stochastic affinity; CountSketch for scalable norm estimation.
role: design-driver — spectral guarantees justify the scalable pipeline.
quote: "If S_ω is doubly stochastic and Z=Y^T, optimizing [the relaxed objective] is equivalent to optimizing Σ_k Σ_{v_i∈C_k} ‖z_i − c^(k)‖²₂, where c^(k) is the center of cluster C_k."

### sigmod26-337 — N2E: Reducing Node-Differential Privacy to Edge-Differential Privacy for Graph Analytics
domain: privacy-dp | graph-db
props: privacy-guarantee | error-bound | probabilistic-guarantee
tools: dp-composition | + LP-rounding
modeling: Node-DP vs edge-DP on graphs; N2E pipeline: privately approximate maximum degree via SVT over sensitivity-monotonic queries (exact or LP-relaxed node deletion), clip the graph, then run any edge-DP mechanism converted to node-DP by group privacy; benchmarked by down-neighborhood optimality.
properties: N2E satisfies (ε,δ)-node-DP; with probability ≥1−β, error equals intrinsic query error plus edge-DP error after clipping O(log(log(Δ/β))/ε) nodes; LP rounding gives factor-3 node-deletion approximation; clipping is distance-preserving (edge distance ≤ τ+k).
usage: Sequential composition, group privacy, post-processing; SVT over sensitivity-1 monotone queries at logarithmic scale; LP rounding of the (x_v,y_e) relaxation.
role: theory-as-contribution — a reduction framework with end-to-end privacy and error guarantees.
quote: "The N2E framework satisfies (ε, δ)-node-DP."

### sigmod26-290 — Codd's Theorem for Databases over Semirings
domain: provenance
props: correctness | + inexpressibility
tools: induction | adversarial-construction
modeling: K-relations over semirings extended with monus (truncated subtraction) and support; basic relational algebra and calculus with semiring semantics (quantifiers as sums over the universe); domain independence; zero-sum-free/positive semiring classes; the bag semiring N.
properties: Codd equivalence over zero-sum-free (resp. positive) semirings: RA-expressible ⟺ domain-independent calculus ⟺ calculus; active-domain definability; division is inexpressible in BRA over the bag semiring; equivalence fails without zero-sum-freeness.
usage: Structural induction translating expressions ↔ formulas; multiplicity-growth counting (support ≤ n^{l(E)}, multiplicities ≤ p_E(n)·2^{l(E)}) against a 2^n division counterexample.
role: theory-as-contribution — a classical theorem transported to semiring-annotated databases.
quote: "There is no expression of basic relational algebra BRA that defines the division operation ÷ on N-databases."

### sigmod26-306 — Efficient Defective Clique Enumeration and Search with Worst-Case Optimal Search Space
domain: graph-db
props: upper-bound | tightness | correctness
tools: induction | adversarial-construction
modeling: Maximal k-defective clique enumeration (subgraphs missing ≤ k edges) via BK-style branch search over (S,C,X) instances; size-q search variant with colorful cores/degeneracy; parameters n, m, degeneracy δ; classical pivoting generalized to defective cliques.
properties: Search-tree size O(3^{n/3}·n^k), runtime O(m·3^{n/3}·n^k); degeneracy-aware O(n·3^{δ/3}·(δC)^{k+2}); matching Ω(3^{n/3}·n^k) worst-case output size (Moon–Moser construction) gives worst-case optimality for constant k; correctness of pivoting and pruning rules.
usage: Branching-vector induction over search-tree instances; Moon–Moser-style witness graphs for the output lower bound; colorful-degree core arguments for size bounds.
role: theory-as-contribution — worst-case-optimal search space is the headline result.
quote: "The worst-case output size of maximal k-defective clique enumeration is Ω(3^{n/3}·n^k) when k is a constant."

### sigmod26-278 — Bag Semantics Query Containment: The CQ vs. UCQ Case
domain: query-optimization
props: hardness | upper-bound
tools: reduction | + polynomial-inequality-encoding
modeling: Bag-semantics query containment — whether Q_s(D) ≤ Q_b(D) for all databases, with homomorphism counts as bag values; CQ-vs-UCQ and multiplicative-approximation variants; polynomials encoded as queries via "CQ-ization" over planets/trips/foggy structures. Noisy: symbols heavily dropped, but statements inferable.
properties: CQ-vs-UCQ decidability shown equivalent to the CQ-vs-CQ case; UCQ-vs-CQ containment undecidable; (1+ε)-multiplicative approximate containment undecidable for every rational ε>0; Π^P_2 lower-bound context from prior work.
usage: Undecidability by reduction from universally quantified polynomial inequalities; homomorphism-count products over disjoint-variable query components realize polynomial values; engineered structures control the counts.
role: theory-as-contribution — mapping the decidability frontier of bag-semantics containment.
quote: "For each rational ε > 0 the following problem is undecidable: Given are Boolean CQs β_s and β_b. Does (1+ε)·β_s ⊑ β_b?"
