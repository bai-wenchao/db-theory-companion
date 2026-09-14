# batch_w4a — queue3 lines 53-65 (scores 15-13)

### sigmod26-085 — Efficient Influential Community Search over Dynamic Graphs
domain: graph-db
props: correctness | upper-bound
tools: adversarial-construction
modeling: Influential communities via k-core keynodes; maintenance recast as ICD-order (per-k-core vertex order) upkeep under edge insert/delete; cost measured output-sensitively by order difference diff_k and relative boundedness vs recomputation. Mild pdf noise (table fragment inside Thm 3.7).
properties: Correctness of insertion/deletion order maintenance (Thms 5.2, 5.6); time O(Σ_k vol(diff_k)+|N(diff_k,G_k)|·log|V_k|) (Thms 5.3, 5.7); prior ICP algorithms proved relatively unbounded (Thm 3.7).
usage: Keynode iff remaining degree ≥ k (Lemma 4.2) reduces index maintenance to order maintenance; unboundedness of prior work motivates the diff-sensitive bound.
role: design-driver — the diff-based complexity target shapes the incremental algorithms.
quote: "Given a graph G, its ICD-order O, and a set of edges ΔG to be inserted into G, Algorithm 2 is relatively bounded with respect to the ICP maintenance algorithm." (Thm 5.4)

### sigmod26-087 — Efficient Meta-subgraph Instance Search over Large Heterogeneous Information Networks
domain: graph-db
props: hardness | upper-bound
tools: reduction | duality | moment-analysis
modeling: Meta-subgraph M defined by edge-type adjacency over an HIN schema; instances are type-preserving injective mappings; performance target is output-sensitive O*(|Ans*|). Some pdf noise in Defn 2.2 preamble.
properties: Deciding M-instance existence is NP-complete (Lemma 2.3, reduction from k-clique); worst-case bounds O*(|Ans*_edge|) and O(|E(HM')|·|Ans*_star|) (Lemmas 4.2–4.3); Finner-inequality size bound on bag counts.
usage: Hardness motivates backtracking with pre-pruning; Finner's (generalized Hölder) inequality bounds star-bag sizes; an LP over weighted vertex cover picks cost-minimal star bags.
role: design-driver — hardness plus output-sensitive cost model steer pruning and bag selection.
quote: "The problem of deciding whether an M instance exists is NP-complete." (Lemma 2.3)

### sigmod26-245 — Towards Selecting Informative Alternative Relational Query Plans for Database Education
domain: query-optimization
props: hardness | approximation-ratio
tools: reduction | exchange-greedy
modeling: Plans as trees; three distances — normalized subtree kernel (LogiPln), normalized edit distance (PhyOpr), L1 cost — blended into Dist; informativeness U(Π) = min pairwise Dist (MaxMin); b-tips selects top-k plans, i-tips adapts to user ratings.
properties: b-tips NP-hard (Thm 3.4); LogiPln distance is a metric (Lemma 4.3); refined Dist satisfies triangle inequality (Lemma 4.8); greedy selection is a 2-approximation (Thm 5.1).
usage: Triangle inequality is exactly what licenses the factor-2 guarantee of the greedy/heap algorithm; kernel and edit distances quantify learner-perceived plan differences.
role: design-driver — metric structure and approximability dictate the selection algorithms.
quote: "b-tips is a 2-approximation algorithm if the distance satisfies the triangle inequality (Lemma 4.8)." (Thm 5.1)

### sigmod26-262 — A Fast, Mergeable, and LDP Compatible Sketch for Counting Distinct Values in Fully Dynamic Tables
domain: cardinality-estimation | privacy-dp
props: privacy-guarantee | error-bound
tools: estimation-theory | moment-analysis
modeling: FM/HLL-style cardinality sketch generalized to base-G registers, updated by mod-G hashing so deletions are supported; per-user GRR perturbation before aggregation gives LDP; merging is register-wise union; estimator from zero-register fraction.
properties: Exact register distribution (Thm 2); asymptotic unbiasedness and limiting relative variance via the dilogarithm Li2 (Thms 3, 6); perturbation mechanism is ε-DP (Thm 4); merged sketches keep a computable distribution (Thm 5).
usage: Binomial occupancy calculations yield closed-form variance (compared to HLL's 1.079/m) and drive the optimal register base G under a memory budget.
role: design-driver — variance and privacy analysis select parameters G, w, and the noise rate.
quote: "The estimator n̂* is asymptotically unbiased, that is, lim_{m→∞} E(n̂*) = n." (Thm 3)

### sigmod26-280 — Beyond Vector Search: Querying With and Without Predicates
domain: ann-vector-search
props: hardness | approximation-ratio
tools: reduction
modeling: Vector search augmented with predicates: proximity graph plus AND/OR predicate graph plus M cross-edges; quality = maximum hop distance from non-predicate to predicate nodes; cross-edges selection asks which M edges minimize it.
properties: Cross-edges selection is NP-hard (Thm 6.1, from Dominating Set); Algorithm 6 is a 2-approximation (Thm 6.2) via Lemma 6.1's lower bound; any numerical range predicate is covered by ≤2 dyadic OR-nodes (Thm 5.1).
usage: Hardness justifies approximation; the two-node dyadic covering theorem bounds predicate routing to logarithmic hops.
role: design-driver — approximation guarantee and covering theorem shape the index construction.
quote: "Given a graph G, a node set S in G, and an integer M, the cross-edges selection problem is NP-hard." (Thm 6.1)

### sigmod26-334 — MAVIS: Materialized View for Subgraph Matching
domain: graph-db
props: correctness | hardness
tools: reduction | induction
modeling: View pattern partitioned into super-nodes forming a tree (minimum connected tree partitioning); materialized view stores per-super-node candidate matches with factorized super-edges grouped by port vertices; queries rewritten to reuse materialized super-nodes.
properties: View is complete and tight — no invalid candidates (Thm 5.1); tree-shaped views eliminate invalid candidates (Thm 3.1); materialized super-nodes preserve all partial matches (Thm 6.3); tree partitioning and view-usage rewriting are NP-complete/NP-hard.
usage: Completeness by contradiction against dual-simulation filtering; NP-hardness of rewriting (from exact cover) motivates greedy isomorphism-function selection.
role: design-driver — completeness/tightness requirements dictate the tree partitioning and factorized storage.
quote: "(1) Completeness: We can retrieve all the match results of V with the materialized view. (2) Tightness: There is no invalid candidate in our materialized view." (Thm 5.1)

### sigmod26-340 — P2FedRec: Privacy-Preserving and Personalized Federated Recommendation via Relationship Awareness
domain: privacy-dp
props: privacy-guarantee
tools: dp-composition
modeling: Two-server federated recommender; threat model with honest-but-curious non-colluding servers and users; privacy notions: ε-edge LDP on adjacency lists, pseudo-anonymity, IND-CPA homomorphic encryption plus 2-of-2 additive secret sharing with Beaver triples.
properties: Four theorems: data-level privacy against users (inner-product indistinguishability) and servers (IND-CPA + information-theoretic sharing); edge-level privacy against users; noisy local graph satisfies ε-edge LDP against servers (likelihood ratio ≤ e^{εa+εd}).
usage: LDP proof is a direct probability-ratio computation mixing randomized-response flips and Laplace degree noise; DP post-processing immunity imported (Thm 2.1).
role: design-driver — privacy budgets calibrate the noise injection at each protocol component.
quote: "The noisy local graph holds ε-edge local differential privacy against the servers." (Thm 6.4)

### sigmod26-021 — Analysis of Shuffling Beyond Pure Local Differential Privacy
domain: privacy-dp
props: upper-bound | lower-bound | tightness
tools: clt-normal-approx | dp-composition | concentration-ineq
modeling: Single-message shuffled mechanism S∘Rⁿ for local randomizers beyond pure LDP; privacy profile δ(ε) via hockey-stick/blanket divergence with blanket mass γ; asymptotic regime n→∞, ε_n from ω(n^{-1/2}) to O(√(log n/n)).
properties: CLT asymptotic expansion of blanket divergence (Lemma 3.2); privacy profile sandwiched between shuffle-index curves χ_lo, χ_up (Cor 3.4); delta band ε_n ≈ (1/χ)√(log n/n) (Thm 3.5); iff condition for asymptotic tightness (Thm 3.8); near-linear FFT accountant with rigorous error (Thm 4.2).
usage: CLT expansion gives the leading φ(χε√n) term; shuffle index χ = √(γ/σ) from the amplification RV's variance; concentration bounds control FFT truncation.
role: theory-as-contribution — PODS-style analysis; the bounds and their tightness are the paper.
quote: "we derive a simple structural necessary and sufficient condition on the local randomizer under which the blanket divergence yields an asymptotically optimal characterization of shuffling." (Thm 3.8 discussion)

### sigmod26-082 — Efficient and Effective Biclique Counting with Local Differential Privacy
domain: privacy-dp | graph-db
props: privacy-guarantee | error-bound
tools: dp-composition | estimation-theory
modeling: Bipartite graph under ε-edge LDP: each vertex perturbs its neighbor list by randomized response; motif transformation probabilities form a transition matrix T between true and noisy motif counts; estimate solves n̂ = n′ × T⁻¹.
properties: Inclusion-pattern-corrected estimate is unbiased (Thm 4); common-neighbor product estimator f1 unbiased (Thm 5); global sensitivity Δ(f1) ≤ γ^{p−1} calibrates Laplace noise (Thm 6); sequential/parallel composition and post-processing imported (Thms 1–3).
usage: Matrix inversion de-biases RR noise; sensitivity bound sizes Laplace noise per release; composition theorems track the total privacy budget.
role: design-driver — unbiasedness and sensitivity analysis determine the perturbation and estimation pipeline.
quote: "the estimator f1 = Σ_{v∈N(u1)} Π_{j>1} φ(v,u_j) is an unbiased estimator of the number of common neighbors of u1, u2, ..., up" (Thm 5)

### sigmod26-220 — Shielding PII to Prevent Re-identification and Preserve Utility
domain: security | privacy-dp
props: hardness | approximation-ratio | privacy-guarantee
tools: reduction | exchange-greedy
modeling: Anonymization as a game on a risk graph over PII: protector picks actions with utility loss and privacy risk under thresholds (τ0, ε0, U0); attacker modeled as membership-inference distinguisher between adjacent datasets; DPP = feasible-strategy problem.
properties: DPP NP-complete (Thm 1, from set cover); SHIELD's mechanism satisfies ε0-DP against all information-theoretic membership-inference attacks (Thm 2); each action never decreases privacy nor increases utility (Thm 3); greedy RUC loses at most H(Rmax)·U* utility (Thm 4).
usage: Weighted-set-cover-style marginal-cost analysis gives the harmonic bound; DP proof reduces the attack family to binary distinguishers.
role: design-driver — hardness motivates the greedy heuristic whose approximation guarantee certifies it.
quote: "The RUC heuristic (Algorithm 1) produces a solution p^RUC whose total utility loss U^RUC satisfies U^RUC ≤ H(Rmax)·U*, where H(k) is the k-th harmonic number." (Thm 4)

### sigmod26-322 — GraphTwin: Cache-Centric Bit-Level Graph Representation for Fast and Exact Graph Queries
domain: graph-db | storage-compression
props: correctness | hardness
tools: reduction | exchange-greedy
modeling: Graph encoded as k bitmaps (GT-vectors) of maximal-independent-set memberships; edge queries answered by one bitwise AND (non-edge certificate) with adjacency-list fallback; generation = choosing k independent sets maximizing non-edge coverage.
properties: AND ≠ 0 certifies non-adjacency — no false negatives (Thm 1); hybrid framework exact (Thm 2); generation NP-hard and submodular (Thm 3, from MaxIS); N(u) ⊆ N(v) implies bitwise subset (Thm 4).
usage: Independent-set structure gives a sound 1-cycle non-edge certificate; submodular coverage analysis (1−1/e greedy impractical) motivates the diversified-MIS heuristic GTWICE; Thm 4 prunes set-inclusion queries.
role: design-driver — exactness theorems dictate the hybrid bitwise/adjacency-list layout.
quote: "The hybrid framework guarantees exact results for all edge queries: (1) No false negatives: Non-edges resolved by GT-vectors are always correct. (2) No false positives: Edges unresolved by GT-vectors are verified exactly via the adjacency list." (Thm 2)

### sigmod26-098 — Fair-Count-Min: Frequency Estimation under Equal Group-wise Approximation Factor
domain: streaming | fairness
props: price-of-x | probabilistic-guarantee
tools: balls-bins-hashing | concentration-ineq
modeling: Count-min sketch with group-aware semi-uniform hashing; fairness = equal expected group-wise approximation factor; achieved by column partitioning with w_g proportional to group size (n_g/n)·w; price of fairness = additive-error difference vs standard CM.
properties: Proportional allocation is group-fair (Thm 1); exact expected approximation factors (Lemmas 1–2); unbiased group-size estimation with Hoeffding tail 2exp(−2mε²) (Lemma 3); column computation in O(n log² n) (Lemma 4); PoF < 0 for d=1 (Lemma 5).
usage: Balls-in-bins occupancy expectations equate the two groups' errors and size the split; monotonicity (Prop 1) enables binary search for w_g1.
role: design-driver — the equal-error equation directly determines column allocation; fairness analysis certifies.
quote: "A CM sketch with a group-aware semi-uniform hash function h(·) is group-fair, if the number of bins w_g allocated to each group is proportional to the ratio of element types from that group." (Thm 1)

### sigmod26-213 — Scalable Clustering Over High Dimensional Vector Streams
domain: streaming
props: correctness | upper-bound
tools: + angular triangle inequality
modeling: Clusters = vector sets with pairwise angular diameter ≤ θ (validity invariant); per-cluster reference vector with boundary angle θ_r = θ − max angle to reference; safe region = spherical cone; stream supports vector/value/dimension updates.
properties: Insertion inside the safe region preserves cluster validity (Lemma 1); monotonicity of the spherical-cosine combination f(β,φ) (Lemma 2) supports angle lower bounds; per-insert cost O(kd + (1−α)nd).
usage: Angular triangle inequality makes deletion/expiry constant-time (validity unaffected by removal); trig monotonicity lets bucket search skip unpromising references.
role: design-driver — the boundary-angle invariant defines the incremental insertion test.
quote: "If ∠(v, r_j) ≤ θ − max_{v_i∈C_j} ∠(v_i, r_j) = θ_r_j then for any v_i ∈ C_j, ∠(v, v_i) ≤ θ." (Lemma 1)
