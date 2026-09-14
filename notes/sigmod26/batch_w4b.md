### sigmod26-274 — Approximate Query Processing under Updates
domain: aqp
props: approximation-ratio | upper-bound | lower-bound
tools: amortized-potential | reduction
modeling: Free-connex hierarchical CQs with semiring annotations; updates are (relation, tuple, Δ) tuples; b-approximation defined multiplicatively per tuple annotation. Noisy pdf extract (table fragments inline).
properties: Maintained view is a b^(|T|−|S|−|D|)-approximation; amortized O(log_b M) update time under insertions; constant-delay full and delta enumeration (given semiring cancellativity); cites Ω(√N) fully-dynamic lower bound for non-q-hierarchical CQs.
usage: Splitting the join tree into exact connex and approximated parts trades ratio for update speed; a Boolean-semiring reduction imports the dynamic lower bound.
role: theory-as-contribution — approximation ratio, update and enumeration guarantees are the paper's results.
quote: "For any b > 1, any free-connex query Q(H,F), all auxiliary views can be updated in amortized O(log_b M) time under an insertion-only update sequence."

### sigmod26-093 — Enhancing Local Differential Privacy Accuracy by Exploiting Inherent Uncertainty
domain: privacy-dp
props: privacy-guarantee | correctness
tools: dp-composition
modeling: LDP protocols as pure protocols with support functions (p*, q*); inherent data uncertainty captured by a parameter pair (α, β) bounding conditional probabilities; two-stage perturbation scheme.
properties: Two-stage scheme satisfies ε-LDP (Thm 5.1); selected (α, β) preserves the e^ε probability ratio for all value pairs (Thm 4.2); explicit perturbation parameters p, q (Lemma 4.3).
usage: Exhaustive case analysis over candidate parameter pairs with probability-ratio algebra establishes the privacy bound; uncertainty-aware parameters cut noise for accuracy.
role: design-driver — the ε-LDP proof certifies the accuracy-enhancing two-stage protocol.
quote: "The two-stage perturbation scheme satisfies ε-LDP... Pr(Ã=ã_k|S=s_i)/Pr(Ã=ã_k|S=s_j) ≤ e^ε."

### sigmod26-147 — LINE: A Learned Index with Group-Enhanced Leaves and Cache-Optimized Inner Tree
domain: indexing
props: upper-bound | io-cost-bound
tools: balls-bins-hashing
modeling: Learned index leaves as error-bounded linear models over key positions, grouped into nanos; cost measured in cache misses; worst-case analysis.
properties: Group size upper-bounded by m + ⌈f·k2ε/nano⌉ (Thm 4.1); detected skewed gaps bounded in count (Thm 5.1); leaf point operations without SMOs cost O(1) cache misses (Thm 6.1).
usage: Counting arguments over the model error bound ε bound keys per group; two-choice hashing with stash yields O(1)-cache-miss point lookups.
role: design-driver — cache-cost bounds and group-size calculus shape the leaf layout and SMO policy.
quote: "A leaf point operation without SMOs incurs O(1) cache misses... the number of nanos per group is upper bounded by m + ⌈f·k2ε/nano⌉."

### sigmod26-149 — LM-Tree: A Hybrid Learned Index for Similarity Search in Metric Spaces
domain: indexing
props: correctness
tools: + triangle-inequality pruning
modeling: Metric-space indexing: pivots partition objects by distance-to-center (PDL); sorted distances mapped to storage positions via error-bounded linear models; node merging by pivot gain.
properties: Pivot and subtree pruning never discards qualifying objects for range queries (Thms 1–2); adjacent distances stay within [(1−2ε)/a, (1+2ε)/a] (Thm 3); merge forbidden outside the model's slope range (Thm 4).
usage: Triangle-inequality distance bounds certify no-false-dismissal pruning; linear-model error constrains distance gaps so sorted distances occupy contiguous positions.
role: design-driver — pruning safety and placement invariants govern the learned metric index.
quote: "If d^pc_{v+1} < d(q, e.c) − r_q or d^pc_v > d(q, e.c) + r_q holds, p_v and the objects within its corresponding PDL_v are out of the query range."

### sigmod26-152 — Loom: Weaving PCS-Preserving and Searchable Cloud Backups for Secure Messaging
domain: security
props: privacy-guarantee | correctness
tools: reduction | + simulation-indistinguishability
modeling: Searchable encrypted backup as protocol syntax (Setup/DataUpdate/Search/Rollback); security via game-based definitions with key/test/expose oracles, PPT adversaries, negligible advantage; post-compromise security.
properties: Integrity under collision-resistant hashes (Thm 2); Loom-security Adv_{G'}(A') ≤ Adv_G(A) + negl(λ) assuming one-time IND-CPA, non-committing encryption, random oracle (Thm 3).
usage: A simulator programs the random oracle to emulate updates/search without keyword leakage; hybrid reduction transfers the adversary's advantage.
role: theory-as-contribution — the security definitions and proofs are the paper's core.
quote: "Loom is secure... for any Loom-compatible game G and any admissible PPT A there exists a PPT adversary A′ such that Adv_G′(A′) ⩽ Adv_G(A) + negl(λ)."

### sigmod26-234 — SWMT: A Sliding Window Merkle Tree with Delayed Writes
domain: security | storage-compression
props: correctness | consistency
tools: induction
modeling: Blockchain state as a sliding-window Merkle tree over key-value data; Snapshot-ADS defined by verifiability, write consistency, key-value semantics; pruning and congestion control update parameters (B0, f, C).
properties: SWMT with sliding window and congestion control satisfies Snapshot-ADS (Thm 4.3); parameters stay uniquely determined after pruning (Lemma 4.2); composing SWMT with any Snapshot-ADS remains valid (Thm 4.4).
usage: Induction over block height using window/size invariants proves determinism; set algebra shows pruning never changes the combined key-value set.
role: design-driver — correctness under pruning and layering certifies the delayed-write architecture.
quote: "The SWMT with support for both sliding window and congestion control satisfies the definition of Snapshot-ADS."

### sigmod26-035 — Beyond Maximum Common Subgraph: Maximizing Shared Computation for Multi-Query Subgraph Matching
domain: graph-db
props: correctness
tools: + label-disjoint boundary arguments
modeling: Multi-query subgraph matching via signatures (filter indicators), shared candidates, and blocks with boundaries; reuse across queries sharing isomorphic substructures; NP-hardness of matching cited as background only.
properties: With disjoint labels, block matching is uniquely determined by its boundary mapping (Lemma 5.3); shared blocks admit identical valid matchings across all queries (Lemma 5.6).
usage: Isomorphism plus label-disjointness shows shared-block matchings are context-independent, licensing computation sharing beyond maximum-common-subgraph overlap.
role: design-driver — sharing-safety lemmas underpin the multi-query framework.
quote: "If the mapping of boundary is fixed, the set of valid matchings for each B_Q is identical across all Q ∈ Q."

### sigmod26-060 — CoShap: A Scalable Coalition Growth Approach to Shapley Value Approximation
domain: + shapley-feature-attribution
props: error-bound | probabilistic-guarantee | sample-complexity
tools: estimation-theory | concentration-ineq
modeling: Shapley values decomposed layer-wise by coalition size; estimation as uniform sampling of marginal contributions with variance-aware budget split μ_f across layers and features.
properties: Estimator unbiased (Thm 1); (ε, δ) error bound on the total estimate (Thm 2); budget m ≥ nσ̂²(μ_f² + k(1−μ_f)²)/(δ(εμ_f(1−μ_f))²) (Thm 3); per-feature error O(√(δ/m_i))·σ̂_i (Thm 4).
usage: Linearity of expectation gives unbiasedness; Chebyshev-style variance bounds with union and Taylor steps yield the (ε, δ) guarantee steering allocation.
role: design-driver — variance-aware budget allocation is derived from the error-bound analysis.
quote: "The CoShap algorithm (Algorithm 2) provides an unbiased estimate of the Shapley value for each feature, i.e., E(φ̂_i) = φ_i."

### sigmod26-090 — Enabling Efficient Direct Update on Rule-Based Compressed Graph
domain: graph-db | storage-compression
props: correctness | upper-bound | space-complexity
tools: adversarial-construction
modeling: Graph as a rule grammar (DAG of rules); adjacency lists located via unique (sep, v) delimiters; updates as copy-on-write rewrites of rule chains; worst-case analysis of traversal and unification.
properties: Index correct after rule-folding deletion iff stale entries are removed and later offsets shifted by ℓ(s)−1 (Thm 6); worst-case locating via full binary tree; rule unification O(Σ|D(r)|); rule saving S(r)=f(|r|−1)−|r|.
usage: Delimiter uniqueness pins list starts; a maximal-branching (full binary tree) construction bounds worst-case search; copy-on-write confines changes to one rule chain.
role: design-driver — maintenance correctness conditions and worst-case bounds shape the compressed-update design.
quote: "The index I remains correct after this operation if and only if... stale index entries for the source vertex starting at path offset δ0 are removed [and] entry paths after δ0 shifted by ℓ(s) − 1."

### sigmod26-092 — Enhancing Graph-based Approximate Maximum Inner Product Search via Norm-Adaptive Partitioning
domain: ann-vector-search
props: probabilistic-guarantee | lower-bound
tools: clt-normal-approx
modeling: Random Gaussian queries; inner products q⊤x modeled as independent normals N(0, ‖x‖²); norm ratio γ = r1/r2 quantifies "norm domination"; LSH collision probability via angle.
properties: Probability a larger-norm point wins is (2/π)·arctan(r1/r2) for orthogonal points (L4.1); domination probability ≥ F(γ, n1, n2), near 1 even for tiny high-norm subsets (L4.2); early termination succeeds with probability ≥ 1−δ_L (L6.1).
usage: Gaussian model with independence simplification gives closed-form domination probabilities that set Head/Body/Tail partitions and early-stop thresholds.
role: design-driver — the probability analysis directly determines partitioning and termination rules.
quote: "The probability that x1 has a larger inner product with q than x2 is 2/π · arctan(r1/r2)."

### sigmod26-265 — Accelerating High-Dimensional ANN Search via Skipping Redundant Distance Computations
domain: ann-vector-search
props: probabilistic-guarantee | lower-bound | correctness
tools: randomized-nla | spectral-matrix
modeling: ANN with recall metric; pruning via MS-distance, a monotone lower bound on Euclidean distance from mean/std statistics, refined dimension-by-dimension; random orthogonal projection to d dimensions.
properties: Projected threshold test separates δ(p,q) < τ vs > τ with probabilities p1 > p2 (Thm 4.1); MSL remains a monotone lower bound reaching exact distance, preserved under PCA (Thms 2.5, 5.1).
usage: JL distortion bounds turn distance thresholds into cheap projected-space comparisons; orthogonal-transform invariance enables multiplication-free iterative refinement.
role: design-driver — lower-bound and projection guarantees drive the skip/prune pipeline.
quote: "If δ(p,q) < τ, then Pr(‖A(p−q)‖²₂ < (1+ε)d/D·τ) > p1; if δ(p,q) > τ, then Pr(‖A(p−q)‖²₂ < (1+ε)d/D·τ) < p2."

### sigmod26-317 — Guardrail: Automated Integrity Constraint Synthesis From Noisy Data
domain: data-cleaning
props: correctness | identifiability
tools: + pgm-mec-faithfulness
modeling: Integrity constraints as program sketches over attribute dependencies; validity = local/global non-triviality (statistical dependence); learnability framed via PGMs and their Markov equivalence classes. (Signal counts inflated: "sketch" = program sketch, not sketching theory.)
properties: Faithful PGM ⇒ derived sketch globally non-trivial (Thm 4.1); LNT sketches with fully-connected determinant sets pin directed edges in every DAG of the MEC (Props 2–4).
usage: Conditional-independence and v-structure arguments, by contradiction under faithfulness, characterize which sketches are identifiable from learnable MECs.
role: design-driver — the identifiability characterization dictates the synthesis algorithm.
quote: "If P_D is faithful to G, then the program sketch p[·] that is derived from G is GNT."

### sigmod26-325 — Hops Can be Constrained: Efficient Distance Queries on Time-Dependent Road Networks
domain: spatial
props: correctness | upper-bound | hardness
tools: + min-plus TTF composition
modeling: Time-dependent directed graphs with travel-time functions composed min-plus (⊗); MTTF is the minimum over path TTFs; transit-node routing with access nodes, candidate tables, and 2-hop labels.
properties: TCH query returns the shortest path with single-peak node ordering (Thm 3.2); local filter O(|S|), global query O(|A_max|²|C_max|log²|f_max|) (Lemmas 5.1, 5.3); access-node supersets, 2-hop labels, Voronoi compression preserve correctness (Lemmas 6.3–6.9); NP-hardness cited for transit selection and non-FIFO.
usage: Correctness lemmas verify each index layer; big-O accounting over access/candidate set sizes quantifies query cost.
role: design-driver — correctness-preserving layers build the TD-TNR-CH index.
quote: "The time complexity of processing a global query Q = (s,t,τ) is O(|A_max|²|C_max|log²|f_max|)."
