# batch_w3a — queue3 lines 1-13 (scores 63-35)

### sigmod26-314 — Finding Heavy-Hitters with Optimal State Changes
domain: streaming | sketching
props: upper-bound | lower-bound | tightness
tools: concentration-ineq | estimation-theory | adversarial-construction
modeling: Insertion-only stream as frequency vector; cost measured in the state-change model (memory writes) alongside space; (ε, ℓk)-heavy-hitters with constant success probability.
properties: O(log³n) space and O(√n·log³n) state changes for ℓ2 (Thm 3); O(ε⁻¹log(1/ε)·n^{1−1/k} polyloglog n) state changes for k∈[1,2] (Thms 4/20); Ω(n^{1−1/k}ε⁻¹log(1/ε)) state-change lower bound (Thms 6/21), optimal up to loglog factors.
usage: Morris/Morris+ counters with sub-gamma tails (Lemma 22, exp(−cR)); competing-pairs counting plus Markov for counter survival; dyadic subsampling (Lemmas 13/14); exponential max-stability (Prop 15) for Fk tracking; lower bound from crafted streams with one repeated item.
role: theory-as-contribution — the state-change upper and lower bounds are the paper's results.
quote: "Let k ∈ [1, ∞). Suppose that an algorithm solves the (ε, ℓk)-heavy-hitter problem with probability at least 3/4. Then this algorithm must use at least Ω(n^{1−1/k} ε^{-1} log(1/ε)) state changes." (Thm 6)

### sigmod26-247 — Optimal Streaming Algorithms for ℓp Sampling, the Forget Model, and Beyond
domain: streaming | sampling
props: upper-bound | space-complexity | probabilistic-guarantee
tools: estimation-theory | sketching-theory | moment-analysis
modeling: Stream as frequency vector; ℓp-sampler outputs i with Pr[i=j] = |f_j|^p/‖f‖_p^p ± 1/poly(n); α-RFDS forget model: post-forget vector g satisfies ‖g‖_p ≥ (1−α)‖f‖_p; also general contracting operations.
properties: One-pass ℓp sampler in Õ(log n log(1/ε)) space (Thms 1.1/3.2), optimal up to polyloglog; Fp estimation under α-RFDS in Õ(ε^{−2/(1−α)} log²n) space (Thms 4.1/4.2/5.1); heavy hitters under contractions (Thms 6.1–6.3).
usage: Exponential rescaling z_i = f_i/e_i^{1/p} tracked via BPTree, CountSketch, AMS sketches; Taylor-series estimator for x^p; geometric-mean estimator over p-stable sketches; Chebyshev and union bounds.
role: theory-as-contribution — optimal space bounds for ℓp sampling and forget-model Fp estimation are the results.
quote: "For any constant p ∈ (0, 2], there is a one-pass streaming algorithm that runs in space Õ(log^{c(p)} n log(1/δ)) ... Pr[i = j] = |f_j|^p / ‖f‖_p^p ± 1/poly(n)." (Thm 1.1)

### sigmod26-357 — Representation Obliviousness and Pseudodeterminism in Streaming Algorithms
domain: streaming | sketching
props: lower-bound | space-complexity | tightness
tools: communication-complexity | reduction
modeling: Defines pseudodeterministic (canonical output w.p. ≥ 2/3) and representation-oblivious (output distribution invariant on Rk-equivalent stream orderings) algorithms; ROPD = both; studies F0/Fk estimation space.
properties: Any one-pass ROPD (ε,δ)-approximation of F0 needs Ω(n) space (Thm 3.1); t(n)-pass needs Ω(n/t(n)) (Thm 4.1), tight via deterministic partition algorithm (Obs 4.3); BJKST, AMS, linear-sketch Fk algorithms are representation oblivious (Thms 5.1/5.4, Obs 5.3); NVGMPC only 1/3-oblivious (Thm 5.2).
usage: Reduction chain from ROPD F0 estimator to ROPD Promise-Union protocol to PD Disj protocol, contradicting CC(Disj)=Ω(m); canonical-value and output-distribution arguments.
role: theory-as-contribution — new algorithmic restrictions with matching space lower bounds.
quote: "Let ε, δ ≤ 1/3. Any ROPD streaming algorithm that (ε, δ)-approximates F0 requires Ω(n) space (where n is the size of the universe)." (Thm 3.1)

### sigmod26-177 — Optimal Enumeration of Regular Pattern Matches
domain: indexing
props: upper-bound | asymptotic-optimality
tools: induction | amortized-potential
modeling: Text of length n; regular pattern with variables separated by fixed strings; output all valid embeddings; measures preprocessing, delay, space. Mild extraction noise (duplicated glyph runs).
properties: O(n+|S|) preprocessing, constant delay, O(n+min{|S|,n^k}) space (Thm 1.1); amortized constant delay with O(n) preprocessing (Thm 1.2); worst-case constant delay (Thm 1.3); dynamic index with O(n log n) preprocessing (Thm 1.4).
usage: Left/right-canonical embeddings; epoch partition of intervals; suffix array/tree ranges, radix sort, range-max structure for O(1) delay; counting bound Σ(|O_i|−1) ≤ min{kn,|S|} (Lemma 3.4); segment tree for the dynamic case.
role: theory-as-contribution — constant-delay enumeration bounds are the paper.
quote: "We can enumerate the set S of all valid embeddings of α in T with constant delay, after a preprocessing running in O(n + |S|) time. The used space is O(n + min{|S|, n^k})." (Thm 1.1)

### sigmod26-241 — Tight Lower Bounds for ℓ2 Sampling
domain: streaming | sketching
props: lower-bound | tightness
tools: clt-normal-approx | adversarial-construction | spectral-matrix
modeling: Linear sketches of the frequency vector; (ε,δ)-ℓ2-sampler with frequency estimation; measures sketching dimension and bit complexity for poly(n)-sized entries.
properties: (ε,δ)-ℓ2-sampler with frequency estimation needs sketching dimension Ω(ε⁻¹log²n + 2ε⁻¹log n) and Ω(log³n + 2ε⁻¹log²n)/ε bits (Thm 1.1); matches known upper bounds up to log factors.
usage: Sketch rows modeled as Gaussian location mixtures with recovery impossibility via posterior/MAP bounds; leverage scores with dyadic decomposition; Yao's principle with payout-game expected-score arguments; discrete-Gaussian lattice rounding.
role: theory-as-contribution — the sketch-dimension lower bound is the result.
quote: "An (ε, δ)-ℓ2-sampler with frequency estimation requires a sketching dimension of at least Ω((1/ε)log²n + (2/ε)log n). Moreover, storing such a sketch for vectors with poly(n) sized entries requires Ω((log³n + (2/ε)log²n)/ε) bits." (Thm 1.1)

### sigmod26-011 — Acyclic Conjunctive Regular Path Queries are no Harder than Corresponding Conjunctive Queries
domain: graph-db
props: upper-bound | tightness
tools: reduction | induction
modeling: Acyclic CRPQs over an edge-labeled graph of size N; output-sensitive data complexity with OUT = output size; combinatorial setting (no fast matrix multiplication). Some proof bodies stubbed in extraction.
properties: Acyclic CRPQ answered in O(N + N·OUT^{1−1/max(fn-fhtw(Q),2)} + OUT) (Thm 3.1), matching the best combinatorial acyclic-CQ bound (Thm 3.2); cannot improve without improving CQ combinatorial algorithms (Prop 2.18).
usage: Reduces acyclic CRPQ to constantly many free-leaf CRPQs (Lemma 3.4) via bound-connected components and NFA product graphs; bottom-up tree evaluation with Δ=OUT^{1−1/ℓ} restrictions; heavy/light splitting; induction.
role: theory-as-contribution — the worst-case query-evaluation bound is the result.
quote: "Let Q be any acyclic CRPQ, and G be an input edge-labeled graph of size N. Then, Q over G can be answered in time O(N + N·OUT^{1−1/max(fn-fhtw(Q),2)} + OUT) in data complexity, where OUT is the output size." (Thm 3.1)

### sigmod26-053 — Coresets for Robust Query Optimization
domain: query-optimization
props: approximation-ratio | sample-complexity | probabilistic-guarantee
tools: concentration-ineq | exchange-greedy | coresets-geometry
modeling: (ε,τ,δ|W)-coreset for plan risk under a workload distribution; τ-risk = Pr_{s∼U_Q}[Pnl(π,s)>τ]; plans and sampled queries as the ground set.
properties: Greedy cover samples O((κ*/δ²)ln N ln δ⁻¹) queries, returns coreset of size O(κ* ln δ⁻¹) whp (Thm 3.5); LocalInference risk ≤ Risk*+4ε w.p. 1−2δ (Thm 4.1); combined risk+neighborhood-cost coresets (Thms 4.5/4.8); worst-case α-coresets via bucketing/hyperplane arrangements.
usage: Hoeffding plus union bounds (Lemmas 3.1–3.2); greedy coverage with exponential termination (Lemma 3.4); global↔local risk transfer (Lemma 4.2); Markov argument (Lemma 4.6).
role: theory-as-contribution — coreset existence and sampling guarantees for robust plan selection.
quote: "There exists an algorithm that samples O((κ*/δ²) ln(N) ln(δ⁻¹)) queries from W and computes ... a set C ⊆ Π of size O(κ* ln δ⁻¹) such that, with high probability, C is a (c₁ε, τ, c₂δ|W)-coreset for risk." (Thm 3.5)

### sigmod26-153 — LSHAlign: All-Pair Near-Duplicate Text Alignment via Locality-Sensitive Hashing
domain: entity-resolution
props: correctness | upper-bound
tools: balls-bins-hashing | induction
modeling: Sequences hashed by concatenated LSH functions g=(h_1..h_m); tight intervals defined via left/right tightness; skyline of positions; expected-case analysis under random hashes (random-permutation assumption).
properties: Algorithm 1 generates exactly all tight intervals in O(n) expected time with O(log n) expected stack (Thms 1/2; E[|S(r)|]=O(log r), Lemma 7); expected number of tight intervals O(nm) (Thm 4); O(mn) expected alignment (Thms 5/7); rectangles partition collision-free subsequences (Lemma 8/Thm 6).
usage: Monotone-stack skyline updates proved by induction; probability s/(s+1), s/(s+2) union-bound tightness computations; rectangle partition guarantees completeness (no missed near-duplicates).
role: design-driver — tightness/skyline lemmas justify the alignment pipeline and its complexity.
quote: "Given a text T with length n, and a hash function g = (h1, . . . , hm) ∈ G, the expected number of tight intervals in T under g is O(nm)." (Thm 4)

### sigmod26-004 — A Logical View of GNN-Style Computation and the Role of Activation Functions
domain: graph-db
props: + expressivity-separation
tools: induction | adversarial-construction | group-symmetry
modeling: MPLang logic capturing (Σ∪{id})-GNNs numerically; A-MPLang = activation-free fragment; walk-equivalence of graphs as the expressiveness yardstick.
properties: A-MPLang normal form as linear combination of walk counts (Thm 4.2); Boolean closure properties (Props 4.5–4.7); eventually-constant activations collapse to Boolean (Thm 5.5); ReLU strictly more expressive than Boolean MPLang (Thms 6.1/6.8).
usage: Walk-equivalent graph pairs witness inexpressibility (Cor 4.3, Ex 4.4); red-blue symmetric trees with structural induction on function shape (Lemmas 6.6/6.7) yield the ReLU separation.
role: theory-as-contribution — expressiveness characterizations and separations are the results.
quote: "For any set of uneven eventually constant activation functions Σ, rational ReLU-MPLang numerically strictly contains rational Σ-MPLang on k-coloured graphs." (Thm 6.1)

### sigmod26-154 — Maintaining Biconnected Components in Streaming Graphs
domain: streaming | graph-db
props: correctness | upper-bound
tools: induction
modeling: Sliding window of θ edges over a graph stream; maintain biconnected components (BCCs) under insertion and expiry; measures index space and update/query time.
properties: BCCs in nested sub-windows are nested or edge-disjoint (Lemma 4.1); Backward BCC Forest is BCC-equivalent to the window graph with O(n) space (Lemma 4.5), O(n) query (Thm 4.1); O(1) deletion (Thm 5.1); O(h·h_t) insertion (Thm 5.2).
usage: Maximum spanning tree by timestamps; a new edge plus MST path yields one cycle and one new internal node; Swing/Swipe operators preserve BCC-equivalence (Lemmas 5.7/5.8), proved by invariant induction.
role: design-driver — equivalence-preservation lemmas justify the index design and bounds.
quote: "The BBF, viewed as a graph weighted by node timestamps, is BCC-equivalent to the graph within the current window, viewed as a graph weighted by edge arrival timestamps." (Lemma 4.5)

### sigmod26-372 — Theoretically and Practically Efficient Maximum Biclique Search
domain: graph-db
props: upper-bound | correctness
tools: duality | reduction
modeling: Maximum edge biclique in a bipartite graph with per-side size constraints (τ_U, τ_V); branch-and-bound over subinstances; worst-case time via recursion-tree recurrences.
properties: Pivot-based branching into d_u+1 subinstances (Thm 3.1), improved by dropping dominated non-neighbors (Thms 3.2/3.3); degree-ordering upper bounds (Lemmas 3/4/10) computable in linear time (Thms 3.5/4.2); worst-case O(m·1.348^n) and O(m·1.381^n) (Thms 3.6/4.3).
usage: Duality between maximum edge biclique and minimal vertex cover of the complement maximizing |U\S_U|×|V\S_V| (Thm 4.1); closed forms for near-complete and low-complement-degree graphs (Thm 3.4, Lemmas 7/8); progressive bounding schedule (Lemma 11); density-based hybrid.
role: theory-as-contribution — worst-case complexity guarantees are a headline contribution alongside practice.
quote: "The problem of finding the maximum edge biclique in G such that each side has cardinality no less than τ_U and τ_V is equivalent to the problem of finding a minimal vertex cover (S_U, S_V) of Ḡ such that |U\S_U| × |V\S_V| is maximized." (Thm 4.1)

### sigmod26-102 — Fast Estimation of Pairwise Biharmonic Distance on Graphs
domain: graph-db
props: error-bound | probabilistic-guarantee | upper-bound
tools: estimation-theory | spectral-matrix | concentration-ineq
modeling: Biharmonic distance β(s,t) = b_st^⊤L†b_st via the Laplacian pseudoinverse; exact computation O(n³); pivot-based reformulations; (ε,δ) approximation guarantees.
properties: Reduced-Laplacian identities express β via L_v^{-1} (Lemmas 3.1–3.3, Thm 3.5); BackPush error bounded by Σπ^v·r_max (Lemma 4.2); FastWalk unbiased estimators via walk collisions (Lemma 5.1); FastTree (ε,δ) guarantee with ω_t = O(d_v²Δ²log(2n/δ)/ε²) trees (Thm 6.3).
usage: Absorbing-random-walk interpretation of L_v^{-1}; pushback invariant by induction (Lemma 4.1); unbiased tree-sampling estimators via electrical networks/Kirchhoff (Lemma 6.1, Cor 6.2); Chernoff-Hoeffding plus union bounds.
role: design-driver — matrix identities and concentration analysis justify the three estimators.
quote: "If ω_t = d_v²Δ²log(2n/δ)/(2ε²), FastTree ... samples ω_t trees and the corresponding estimators satisfy that for each node u, |x_a(u) − x̃_a(u)| ≤ ε and |x_b(u) − x̃_b(u)| ≤ ε." (Thm 6.3)

### sigmod26-373 — Time-Critical Influence Minimization via Node Blocking
domain: graph-db
props: hardness | approximation-ratio | probabilistic-guarantee
tools: concentration-ineq | exchange-greedy | estimation-theory
modeling: TIC diffusion with edge delays; activation-duration-weighted influence spread with deadline T; choose k blocker nodes to minimize spread; possible-world sampling.
properties: TCIM is NP-hard and inapproximable within any constant factor unless P=NP (Thm 3.3); D(·) is #P-hard (Thm 3.4) and monotone non-submodular (Thm 3.5); submodular surrogates D_L ≤ D ≤ D_U ≤ D_U' (Lemmas 4.1–4.8) enable greedy guarantees.
usage: Reverse-score sample sets (GRS/TRS) with unbiased coverage estimators (Lemma 5.8); concentration bounds (Lemma 6.4) set the sample threshold θ_max (Lemma 6.5); union bounds give the end-to-end approximation guarantee.
role: design-driver — hardness and surrogate-submodularity results shape CBFM and its guarantee.
quote: "Given 0 ≤ ε, δ ≤ 1, CBFM returns B* satisfies: Pr[D(B*) ≥ τ(1 − 1/e − ε)·D(B_o)] ≥ 1 − 3δ." (Thm 6.7)
