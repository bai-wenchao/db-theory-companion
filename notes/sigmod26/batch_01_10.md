# batch 01-10 — sigmod26 (queue lines 1-10)

### sigmod26-136 — Improved Lower Bounds for Privacy under Continual Release
domain: privacy-dp | streaming
props: lower-bound | upper-bound | privacy-guarantee
tools: reduction | adversarial-construction | dp-composition
modeling: (ε,δ)-DP mechanisms under continual release (event/item-level; incremental/fully dynamic) maintaining max matching, degree histogram, k-core, and monotone symmetric norms over T steps, n vertices; accuracy = additive + multiplicative error.
properties: Incremental exact lower bounds α = Ω(min{T^a, n^b}) (Thm 1) via InnerProduct reductions with extendable bitwise-AND gadgets; item-level fully-dynamic η·α tradeoffs (Thm 5) via fingerprinting codes on 1-Way-Marginals (n = Ω(d/ε)); upper bounds via SVT, continual counting, composition, (1+ζ)-approximate IncSNE with polylog error.
usage: Gadgets embed inner-product queries into graph streams; packing/reidentifiable-distribution arguments yield sample-complexity bounds; binary-tree mechanisms plus composition give near-matching upper bounds.
role: theory-as-contribution — the lower/upper bounds themselves are the paper.
quote: "Any (ε,δ)-DP incremental mechanism ... for maintaining the size of the maximum matching, degree histogram, or core number of a vertex must have additive error α = Ω(min{T^a, n^b})."

### sigmod26-175 — On Sketching Trimmed Statistics
domain: streaming | sketching
props: upper-bound | approximation-ratio | space-complexity
tools: concentration-ineq | sketching-theory | peeling-dyadic
modeling: Turnstile stream updates an n-dimensional frequency vector; linear sketch S ∈ R^{r×n}; goal: (1±ε)-estimate Fp of top-k, trimmed-k, and thresholded frequency subvectors under condition a_k² ≥ (ε/log n)^c·‖x_{−k}‖²/k.
properties: poly(log n/ε)-space sketches for p ≤ 2 (Thms 4.1/5.1); poly(log n/ε)·n^{1−2/p} space for p > 2 (Thm 6.1); corollaries for thresholded Fp, Ky-Fan norms, and estimating k itself.
usage: Geometric level sets with random threshold ζ; dyadic subsampling isolates Θ(log n/ε²) survivors; CountSketch/heavy-hitter identification; Chernoff plus union bound over levels.
role: theory-as-contribution — the space-accuracy tradeoffs are the results.
quote: "there exists a linear sketch that uses poly(log n/ε) bits of space and estimates Σ_{i=1}^k |a_i|^p up to a (1±ε) multiplicative factor with high constant probability."

### sigmod26-114 — FPT Parameterisations of Fractional and Generalised Hypertree Width
domain: query-optimization
props: upper-bound | approximation-ratio
tools: induction | + MSO-transductions / elimination forests (finite-model theory)
modeling: Hypergraphs H with rank r(H) and maximum predicate arity Δ(H); decision problems fhw(H) ≤ k, ghw(H) ≤ k parameterised by k + rank + Δ, via "manageable" width functions over fractional covers of subhypergraphs; also discretized adaptive width F_δ.
properties: First FPT algorithms deciding fractional/generalised hypertree width ≤ k; FPT for discretized adaptive width; factor-2 FPT approximation for relaxed F*_δ-width.
usage: MSO transductions lift Bojańczyk–Pilipczuk; elimination forests with a Reduced-Hypergraph Dealternation Lemma bound alternation depth; conflict-graph coloring and neutral-swap/pigeonhole arguments; induction over forests.
role: theory-as-contribution — the parameterized-tractability results are the paper.
quote: "it is fixed-parameter tractable to check ghw(H) ≤ k and fhw(H) ≤ k parameterised by k, rank(H), Δ(H)."

### sigmod26-222 — Size Bound-Adorned Datalog
domain: query-optimization
props: upper-bound | hardness | correctness
tools: induction | reduction | duality
modeling: Recursive Datalog Π rewritten into non-recursive EDB-adorned programs via relaxation functions (id, g_out, g_k, g_min); an adornment is a safe rule bounding derivations; edge-cover width ew(q^ρ); EDB relations ≤ N tuples.
properties: Rewriting equivalence (Thm 3.13); bounded programs recursively enumerable (Cor 4.8); AGM-style |q^ρ| ≤ N^{ew} (Thm 5.5); minimal integral edge-cover width (Thm 5.8); #ADORNMENTS #P-hard (Thm 5.11); Stirling-number adornment counts; FPT evaluation O(f(Π)^{fcghw}·|Π|·N^{ew·fcghw}) (Thm 7.4).
usage: Induction on generalized proof-tree depth; canonical-database witnesses for minimality; #PP2CNF reduction for hardness; fractional edge covers (LP) for size bounds.
role: theory-as-contribution — the rewriting theory and size bounds are the paper.
quote: "Let Π be an EDB-bounded datalog program ... Then every IDB relation q^ρ has size |q^ρ| ≤ N^k, where k is the fractional edge cover width of q^ρ."

### sigmod26-243 — Towards Output-Optimal Uniform Sampling and Approximate Counting for Join-Project Queries
domain: join-algorithms | sampling
props: lower-bound | upper-bound | approximation-ratio
tools: concentration-ineq | reduction | communication-complexity
modeling: Matrix, star, chain join-project queries; input size N, output size OUT; property-testing access (tuple test, sample, degree queries); tasks: uniform sampling and ε-approximate counting.
properties: Matrix: Õ(N) index, O(N/√OUT) sampling, O(ε^{−2.5}√(N·OUT)) counting (Thms 2.3/3.8); star: O(N/OUT^{1/k}) (Thms 5.1/5.2); chain: Õ(N) counting (Thm 6.1). Lower bounds Ω(N/√OUT), Ω(N/OUT^{1/k}) via 2-/k-party set disjointness (Thms 4.2/5.4); combinatorial (BMM/listing) barriers (Thms 4.3/5.5); 3-chain Ω(min{N², N/OUT²}), 4-chain Ω(N).
usage: Hybrid heavy/light partition, Hoeffding intersection estimation, geometric search on OUT, Markov/Chebyshev median amplification, negative-hypergeometric rejection; coupon-collector reductions from listing hardness.
role: theory-as-contribution — matching upper/lower bounds are the paper.
quote: "any randomized algorithm that ... outputs an O(1) approximation of OUT with high probability requires at least Ω(N/√OUT) time."

### sigmod26-109 — Fine-Grained Dichotomies for Conjunctive Queries with Minimum or Maximum
domain: query-optimization
props: lower-bound | upper-bound
tools: reduction | + fine-grained hypotheses (BMM, Hyperclique, SETH)
modeling: Self-join-free acyclic free-connex CQs with min/max aggregation; tasks: enumeration, direct access, counting; targets quasilinear preprocessing with logarithmic access / constant delay.
properties: Tractability when no chordless k-path (k ≥ 3) between relevant variables: predicate elimination via strict partial orders on maximally-branching join trees; quasilinear direct access (Lemma 8); linear-preprocessing constant-delay enumeration (Lemmas 9/10). Otherwise conditional impossibility under Hyperclique and SETH, giving full dichotomies.
usage: Reductions from triangle/hyperclique detection prove hardness; order partitioning and join-tree rearrangement give algorithms; semiring aggregate handling (Lemma 2).
role: theory-as-contribution — the dichotomy theorems are the paper.
quote: "Direct access according to min X is not possible in quasilinear time if Q has a chordless k-path (k ≥ 3) between two variables in X, assuming Hyperclique and Seth."

### sigmod26-166 — Near-Optimality for Single-Source Personalized PageRank
domain: graph-db
props: lower-bound | upper-bound | probabilistic-guarantee
tools: concentration-ineq | martingale-azuma | adversarial-construction
modeling: SSPPR-R (relative error above threshold δ), SSPPR-A (additive ε), STPPR over graphs; arc-centric query model, 2-lift to simple graphs; cost measured in queries vs m, n.
properties: DistWalks solves SSPPR-R in O(min{log n/δ, m + n log n log(mδ/n)}) expected queries (Thm 1), first linear-in-m for dense graphs; SSPPR-A in O(1/ε²); matching lower bounds Ω(min{m₀, log(1/δ₀)/δ₀}), Ω(min{1/ε₀², m₀}), Ω(min{m₀, n₀ log n₀/δ₀}).
usage: Monte-Carlo discovery with Chernoff and union bound; martingale-difference error control with Azuma–Hoeffding; lower bounds via r-padded hard instances with hidden splits, Bayes likelihood-ratio switching.
role: theory-as-contribution — the query-complexity optimality is the paper.
quote: "DistWalks solves the SSPPR-R query within O(min{log(n)/δ, m + n·log n·log(mδ/n)}) queries in expectation."

### sigmod26-104 — Faster Relational Algorithms Using Geometric Data Structures
domain: query-optimization | spatial
props: approximation-ratio | probabilistic-guarantee
tools: concentration-ineq | + randomized geometric decompositions (BBD trees, coresets, ε-samples)
modeling: k-center/k-median/k-means clustering over join output q(D) without materialization; relational oracles (count/sample/report/represent-rectangle) over axis-aligned boxes; N = |q(D)|; γ = black-box routine's guarantee.
properties: Randomized BBD tree built lazily over q(D); k-center (2√d+ε) then (1+ε)γ in O(kN log²N + k log⁴N) w.p. ≥ 1−1/N (Thms 5.1/5.2); k-means (84+ε) with O(k log³N) centers, then (4+ε)γ via coresets (Thm 6.6); extensions: project-join, cyclic queries via fhw, diversity/fairness.
usage: ε-samples with Chernoff and union bound for randomized centroid shrink; pigeonhole on level sets; binary search on ℓ∞ pairwise distances; coresets before black-box solvers.
role: theory-as-contribution — the approximation guarantees are the results.
quote: "there exists an algorithm that computes S ⊆ q(D) of k points such that u_S(q(D)) ≤ (1+ε)·γ·u_OPT; the running time is O(kN log²N + k log⁴N) with probability at least 1 − 1/N."

### sigmod26-233 — Succinct Structure Representations for Efficient Query Optimization
domain: query-optimization
props: upper-bound | correctness
tools: induction
modeling: Query plans as join pipelines; width w(P) = worst-case intermediate size O(N^{w(P)}); join trees vs induced plans; meta-decompositions (labeled trees) representing all join trees of star queries.
properties: w(P)=1 iff plan induced by a join tree (3.5); width-1 plans exist iff acyclic (3.6); optimal width-1 plan per tree (3.8); relation-dominated queries in O(|db|) (3.9); meta-decomposition in O(|E(H)|³), size O(|E(H)|) (4.8/4.10); exact enumeration (4.12).
usage: Structural induction, ear-removal acyclicity, Prüfer-sequence tree counting; theorems justify restricting plan search to width-1/meta-decomposition space; experiments validate.
role: design-driver — width-1 restriction and linear-evaluation guarantees shape the optimizer design.
quote: "A conjunctive query Q has width-1 query plans if and only if Q is acyclic."

### sigmod26-196 — Privacy Loss of Noise Perturbation via Concentration Analysis of A Product Measure
domain: privacy-dp
props: privacy-guarantee | error-bound
tools: concentration-ineq | + special-function moment analysis (chi/Beta-prime/confluent hypergeometric)
modeling: High-dimensional (ε,δ)-DP via product noise σ_M·R·h (χ₁ radius R, uniform sphere direction h), the polar decomposition of spherically symmetric noise; PLRV studied via random-triangle geometry; L2 sensitivity Δ₂f.
properties: PLRV ≤ R + (Δ₂f/σ_M)(1+1/sin θ) (Prop 1); exact moments of shifted-χ W, Beta-prime U via ₁F₁ hypergeometric functions (Props 2–4, 6); Markov moment bound (Prop 5); explicit (ε,δ) calibration (Thm 1); beats Gaussian for M ≥ 14, Θ(log 1/δ) noise reduction (Cors 1/2); AMP application.
usage: Radon–Nikodym product-measure lemma; exponent-optimized Markov bound; AMP sensitivity/Jacobian bounds; linear DP composition.
role: theory-as-contribution — the privacy-loss analysis machinery is the contribution.
quote: "if σ_M ≥ (Δ₂f/ε)·t, then the product noise achieves (ε,δ)-DP on the perturbed f(x) ... the expected magnitude of our product noise is reduced by a factor of Θ(log 1/δ) relative to the classic Gaussian noise."
