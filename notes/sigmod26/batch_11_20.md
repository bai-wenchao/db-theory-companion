### sigmod26-244 — Towards Parameterized Hardness on Maintaining Conjunctive Queries
domain: join-algorithms | query-optimization
props: conditional-lower-bound | upper-bound
tools: fine-grained-reductions | adversarial-construction
modeling: Dynamic maintenance of conjunctive queries under single-tuple updates; cost = amortized update time plus enumeration delay. Queries classified by relational-hypergraph height k and dimension d; hardness conditioned on combinatorial k-clique, BMM, OuMv conjectures. TeX extract, clean.
properties: Height-k / dimension-d queries need Ω(|D|^{1−1/max(k,d)−ε}) amortized update time — first super-square-root lower bounds for free-connex queries; q-hierarchical ≡ height 1 ≡ dimension 1; matching upper bound for star queries via generalized H-index ≤ |D|^{1/d}.
usage: Reductions encode k-cycle detection (color-coding hash families) and OuMv tensors into update sequences, so faster maintenance breaks the underlying conjecture.
role: theory-as-contribution — the parameterized conditional lower bounds and the height/dimension taxonomy are the paper.
quote: "Assuming combinatorial k-clique conjecture, no dynamic combinatorial algorithm can maintain Q with amortized update time O(|D|^{(k−1)/k−ε}) and support constant delay enumeration for any constant ε > 0."

### sigmod26-115 — Frequency Moments in Noisy Streaming and Distributed Data under Mismatch Ambiguity
domain: streaming | sampling
props: approximation-ratio | space-complexity | lower-bound
tools: concentration-ineq | communication-complexity | estimation-theory
modeling: Fp estimation on noisy streams where mismatch ambiguity ηp bounds symbol-level noise vs ground truth; single-pass space (words) and coordinator-model communication as costs; (ε,δ)-approximation semantics.
properties: One-pass (ε+O(ηp), 0.01)-approximation using O(m^{1−1/p}/ε²) words; Ω(m^{1−1/p}/ε^{1/p})-bit space lower bound for O(1)-pass (ε+Cηp, 0.48)-approximations; three-round distributed protocol in the coordinator model with k sites.
usage: Ordered p-clique sampling estimator with truncation controls expectation/variance (Hölder, Chebyshev, plus a Renyi-style inequality); DISJ communication-complexity reduction yields the space lower bound.
role: theory-as-contribution — upper and lower bounds under the new noise model are the results.
quote: "Any O(1)-pass ((ϵ + Cηp), 0.48)-approximation algorithm for computing Fp on any noisy data stream of length up to m needs Ω(m^{1−1/p}/ϵ^{1/p}) bits of space."

### sigmod26-185 — PANDAExpress: A Simpler and Faster PANDA Algorithm
domain: join-algorithms | query-optimization
props: upper-bound | asymptotic-optimality | correctness
tools: information-theory | duality
modeling: Disjunctive datalog rules evaluated under degree constraints; Shannon-flow inequalities over polymatroids certify output-size bound B = ∏ Nδ^{wδ}; runtime benchmarked against fractional hypertree width and submodular width. Pdf-derived extract, mildly noisy (discussion prose inside some statements).
properties: Model of size O(B) computable in O(N log N + B log N); recovers O(N^{fhtw} log N) and O(N^{subw} log N) with constant-delay enumeration; execution-tree invariants (a)–(e) carry correctness; LP solved in polynomial time with reset-lemma pruning of dominated constraints.
usage: LP duality picks optimal weights; a sub-probability-measure / geometric-mean construction turns each Shannon-inequality proof step into recursive hyperplane partitioning; potential |D|+|M|+3|S| bounds recursion depth.
role: theory-as-contribution — the algorithm literally executes the Shannon-flow proof; matching subw/fhtw bounds is the result.
quote: "PANDAExpress can compute a model Σout for the DDR (8) of size ∥Σout∥ = O(B) in time O(N log N + B log N) where B = ∏δ Nδ^{wδ}."

### sigmod26-231 — Sublime: Sublinear Error & Space for Unbounded Skewed Streams
domain: streaming | sketching
props: error-bound | space-complexity | lower-bound
tools: estimation-theory | information-theory | concentration-ineq
modeling: Frequency-estimation sketches (CMS, Count Sketch, MG) on unbounded skewed streams with deletions; a size function W(·) (sublinear power N^α/ε or linear N/ε) trades expected error E(N) against memory; VALE variable-length counter encoding. TeX extract but captions/author blocks bleed into proofs (mild noise).
properties: Expected error O(1)·εN^{1−α} or log²N·ε, within constant/log factors of an upfront-allocated sketch; unbiased CS variant with matching variance bound; memory ≈ d·W(N)·(4.41+1.26 log₂(N/W(N))); Ω(N/E(N)·[log 1/δ + log log(N/E(N))]) memory lower bound, nearly matched.
usage: Geometric-series epoch analysis over expansions; Markov/Chebyshev for confidence; Jensen for encoding length; entropy incompressibility argument proves the lower bound.
role: design-driver — expansion thresholds and encoding are chosen to provably track the error–space tradeoff; experiments validate.
quote: "Such a sketch must use at least N/E(N) · [Ω(log 1/δ + log log(N/E(N))) − Θ(1)] bits of memory at some point in time while processing a stream."

### sigmod26-123 — GPM: Gaussian Pancake Mechanism for Undetectable DP Backdoors
domain: privacy-dp | security
props: privacy-guarantee | lower-bound | upper-bound
tools: reduction | adversarial-construction
modeling: Supply-chain backdoor replaces the Gaussian mechanism by hCLWE-noise "pancake" mechanism; computational (PPT) vs statistical (backdoor-key-holding) adversaries; privacy cost measured by (ε,δ)-DP breach. Pdf-derived extract, mildly noisy (prose fragments inside statements).
properties: Covertness — GPM outputs computationally indistinguishable from GM for polynomially many queries; with key w, privacy loss ε ∈ Θ(1/β²) (so ε > 10⁴ in practice) while a statistical upper bound ε ∈ Θ(γ√(β²+γ²)Δ/βσ) still holds; distinguishing attack succeeds with probability ≥ 1−2Φ(−cγ|t|/β).
usage: Covertness by reduction to hCLWE hardness (SIVP/GapSVP vs BQP); Gaussian c.d.f. analysis of peak misalignment along w; Weyl equidistribution over random w for the average-case bound.
role: theory-as-contribution — the covertness theorem and privacy-loss bounds are the paper.
quote: "With constant probability over sampling w ←$ S^{d−1}, M is not (ε,δ)-DP where ε ∈ Θ(1/β²) for any 0 < δ ≤ 0.5."

### sigmod26-232 — Subset Sampling over Joins
domain: sampling | join-algorithms
props: correctness | upper-bound | space-complexity
tools: amortized-potential | induction
modeling: Subset (per-tuple-probability) sampling over acyclic join results without materialization; per-relation decomposable weight functions; static index, one-shot, and dynamic (single-tuple insertions) settings; costs = space, preprocessing, expected query time, amortized update time. Pdf-derived but statements clean.
properties: Index of O(N log N) space, O(N log N log log N) preprocessing, O(1+μΨ log N) expected query; one-shot in O(min(N log N log log N + μΨ log N, N log²N + μΨ)); dynamic variant with O(log³N log log N) amortized updates; samples exact or 2^k-factor-uniform.
usage: Light / near-uniform weight-bucket decomposition with meta-index batched rejection sampling and geometric jumps; strong induction proves direct-access distinctness; FFT convolution plus power-of-two approximated statistics keep dynamic counts consistent.
role: theory-as-contribution — complexity guarantees are the contribution; implementation explicitly left to future work.
quote: "There exists an index D of size O(N log N) that can be built in O(N log N log log N) time, such that each subset sampling query can be answered in O(1 + μΨ log N) expected time."

### sigmod26-141 — Jaguar: A Primal Algorithm for Conjunctive Query Evaluation in Submodular-Width Time
domain: join-algorithms | query-optimization
props: upper-bound | correctness
tools: amortized-potential | induction | + shortest-path reduction
modeling: CQ evaluation under degree/statistics constraints via a primal set function g maintained under cardinality, monotonicity, and statistics invariants; target bound is the submodular width subw(Q,Δ,n); data complexity. TeX extract, clean.
properties: Jaguar correctly computes Q(D0) in O(N^{subw(Q,Δ,n)+ε}+OUT) with O(N^{subw+ε}) preprocessing and constant-delay enumeration; truncation lemma turns any monotone g into a polymatroid h ≤ g respecting the statistics; Calibrate runs in linear time.
usage: Calibrate is revealed as a shortest-path algorithm on a weighted subset graph; a log-relation-size potential decreases by ε across heavy edges, bounding recursion depth; induction establishes soundness of recursive calls.
role: theory-as-contribution — correctness plus the subw-time guarantee are the paper.
quote: "Jaguar (Algorithm 1) correctly computes Q(D0) in time O(N^{subw(Q,Δ,n)+ε} + OUT) in data complexity, and supports constant-delay enumeration of the output tuples."

### sigmod26-227 — Sparsity-Dimension Trade-Offs for Oblivious Subspace Embeddings
domain: sketching
props: lower-bound | space-complexity
tools: adversarial-construction | game-equilibrium | concentration-ineq
modeling: Oblivious subspace embeddings: random Π ∈ R^{m×n} preserving (1±ε)-norms on every fixed d-dimensional subspace with probability 1−δ; trade-off between row count m and column sparsity s (relevant to in-DB linear regression). TeX extract, clean.
properties: For 3 ≤ s ≤ ~(1/2)ε⁻¹, m ≥ Ω(d²/(ε² s^{1+O(δ)} log¹³ s)); general regime bound Ω((d/(εs))^{1+1/(⌊(4+o(1))εs⌋+1)}·s^{−O(δ)}), improving Nelson–Nguyễn's Ω(d^{1+1/(16εs+4)}) in both d and ε.
usage: Yao's minimax principle fixes a hard distribution over orthonormal columns; a "great collision lemma" (greedy algorithm) finds many large-inner-product column pairs whp; pigeonhole/averaging and negative-correlation concentration convert collisions into norm distortion.
role: theory-as-contribution — pure lower-bound paper.
quote: "Any (ϵ, δ)-subspace-embedding Π must have at least Ω((d/(ϵs))^{1+1/(⌊(4+o(1))ϵs⌋+1)} · s^{−O(δ)}) rows, if the column sparsity s satisfies 3 ≤ s ≤ O(ϵ^{−1} log d)."

### sigmod26-155 — Maintaining Queries under Updates Using Heavy-Light Partitioning
domain: join-algorithms | query-optimization
props: upper-bound | correctness
tools: duality | induction
modeling: Incremental maintenance of join queries under single-tuple updates via heavy/light partitioning of join-variable values; costs = preprocessing, amortized update time, enumeration delay; new "maintenance width" mw(Q) defined via degree configurations, view trees, and an LP objective. TeX extract, clean.
properties: Any join query maintainable with O(N^{1+mw}) preprocessing, amortized O(N^{mw}) updates, O(1)-delay enumeration; mw(Q) ≤ dw(Q) (dynamic width); Loomis-Whitney-k achieves O(N^{1/2}) updates; hierarchical queries O(1); path-query times conditionally optimal (OMv, subw conjectures).
usage: Delta views upper-bounded through "guarding queries" computed under acyclic degree constraints (PBD bound); per-configuration view trees selected by the LP objective; case analysis over degree configurations; induction for enumeration correctness.
role: theory-as-contribution — the width measure and the update-time theorem are the core.
quote: "Any join query Q can be maintained with O(N^{1+mw(Q)}) preprocessing time, amortized O(N^{mw(Q)}) single-tuple update time, and O(1) enumeration delay."

### sigmod26-127 — HeteroFedSyn: Differentially Private Tabular Data Synthesis for Heterogeneous Federated Settings
domain: privacy-dp
props: privacy-guarantee | + unbiased estimation
tools: dp-composition | estimation-theory | randomized-nla
modeling: Horizontal federated tabular synthesis against an untrusted server; clients send Gaussian-noised 1-way marginals and randomly projected (Gaussian matrix) 2-way marginals; zCDP privacy accounting; utility via greedy dependency-driven marginal selection. TeX extract, clean.
properties: Each released mechanism is ρ-zCDP with explicit ℓ2 sensitivities (Δ1 ≤ 1; Δ2 bounded by max projected column norms), converted to (ε,δ)-DP; the squared InDif² dependency score admits an unbiased estimator from noisy projected marginals, with exact variance-correction terms.
usage: zCDP additivity plus post-processing for budget allocation across marginals; expectation calculations strip projection and noise bias; random projection compresses 2-way marginals before release; greedy selection trades noise error against dependency error.
role: design-driver — privacy proofs and unbiasedness justify each pipeline stage; experiments measure utility.
quote: "z_{a,b} − ‖z_{a∗b}‖²₂ − [kασ₂² + ασ₁²(s_b‖M̂_a‖²₂ + s_a‖M̂_b‖²₂) − s_a s_b α²σ₁⁴] is an unbiased estimator of the square of InDif²_{a,b}."
