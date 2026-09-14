# batch_pilot — sigmod26, top-8 flagged ids (score desc), 2026-09-13
Source: data/sigmod26/theory/<id>.md extracts; tags from CLAUDE.md taxonomy.

### sigmod26-038 — Bounding the Fragmentation of B-Trees Subject to Batched Insertions
domain: indexing
props: lower-bound | convergence-rate | correctness
tools: spectral-matrix | induction | reduction
modeling: Capacity-B B-tree blocks receive insertion batches of size r; block-size counts follow a linear matrix recurrence with a Metzler transition matrix, each batch hitting a size-proportional random block — generalizing Yao's even-split model.
properties: Recurrences converge to the spectral projection at dominant eigenvalue r (Perron–Frobenius); limiting fullness ≥(1/2+δ)B for r≤(1/2−ε)B, ≥7/12·B for 0.21B≤r<0.5B, exact 2ir(H₂ᵢ−Hᵢ)/B when r∈(B/(2i),B/(2i−1)], and ≥2/3·B in large-batch regimes.
usage: Spectral (Jordan/Perron–Frobenius) analysis proves convergence; eigenvector arithmetic yields the fullness bounds; regime analysis selects even/uneven/TargetSplit algorithms.
role: design-driver — proven fullness per batch-size regime dictates which split strategy to deploy.
quote: "For r ∈ (B/(2i), B/(2i−1)], the expected final fullness of the deferred even split strategy is 2ir(H₂ᵢ − Hᵢ)/B, where Hₖ is the k-th harmonic number."

### sigmod26-012 — Acyclic Graph Pattern Counting under Local Differential Privacy
domain: privacy-dp | graph-db
props: privacy-guarantee | error-bound | lower-bound
tools: concentration-ineq | estimation-theory | reduction
modeling: Graph dispersed across N nodes, each seeing only its neighborhood; output must satisfy edge-local DP. Counts k-line walks, k-paths (node-distinct), and acyclic k-edge patterns via multi-round aggregation with Laplace noise scaled by running maxima.
properties: Estimators are unbiased and ε-edge-LDP; error Õ(√(N·d^{k−1})) w.p. 1−β for walks, Õ(√(N·d^k)) for paths/patterns; variance lower bound Ω(N^{k+1}) for an RR-style estimator; communication O(N²) (walks) / O(M+N) (patterns).
usage: Parallel/basic DP composition, Laplace concentration, Chernoff on effective degrees, Chebyshev for sampling error; random marking reduces path counting to walk counting.
role: design-driver — privacy–utility analysis shapes the round structure and marking protocol.
quote: "The k-round mechanism satisfies E[M(G,ε)] = W_k, and with probability at least 1−β, |M(G,ε) − W_k| ≤ kγ√N(d(G)+γ)^{k−1} = Õ(√(N·d(G)^{k−1}))."

### sigmod26-015 — AeroSketch: Near-Optimal Time Matrix Sketch Framework for Streams
domain: streaming | sketching
props: error-bound | space-complexity | probabilistic-guarantee
tools: sketching-theory | spectral-matrix | amortized-potential
modeling: Row-stream matrix sketching under relative covariance error ‖AᵀA−BᵀB‖² ≤ ε‖A‖²_F; persistent historical queries, sliding window of N updates (norm bound R), and distributed sites. Frequent Directions with SVD replaced by power/simultaneous iteration; snapshots dumped per dyadic threshold θ.
properties: Space O((d/ε)log R), amortized update time O((d/ε)·log d·log R) — near-optimal against a known time lower bound; success probability ≥99/100, amplifiable to 1−δ; distributed communication O((md/ε)·log‖A‖_F).
usage: FD decomposability composes per-site sketches; iteration error bounds give the whp guarantee; amortization over every-ℓ-updates SVD yields the time bound.
role: design-driver — provably avoiding exact SVD while keeping FD error/complexity guarantees is the core contribution.
quote: "ML-AeroSketch solves [sliding-window matrix sketch tracking] with space O((d/ε)·log R) and amortized time O((d/ε)·log d·log R) per update, with success probability at least 99/100."

### sigmod26-070 — Deterministic Lower Bounds for k-Edge Connectivity in the Distributed Sketching Model
domain: graph-db | distributed-query
props: lower-bound | upper-bound
tools: adversarial-construction | communication-complexity | reduction
modeling: Distributed sketching model: each of n nodes sends one sketch to a referee that decides k-edge connectivity deterministically. Hardness via a new 3-party simultaneous-message problem, UniqueOverlap (support-s ternary vectors with a single XOR-differing index).
properties: Worst-case sketch length Ω(k) bits for any super-constant k ≤ γ√n — first super-polylogarithmic deterministic bound for a connectivity decision problem; UniqueOverlap deterministic one-way complexity Ω(m) for s=Θ(m); complementary s−1-bit protocol when s>m/3.
usage: Probabilistic-method set families plus pigeonhole partitions create indistinguishable neighborhood pairs; reduction and a simulation of the sketching algorithm by the three parties transfer the hardness.
role: design-driver — the lower-bound program dictates the graph construction, the communication problem, and the simulation.
quote: "Every deterministic algorithm that decides k-edge connectivity on n-node graphs in the distributed sketching model has a worst case message length of Ω(k) bits."

### sigmod26-018 — An Efficient Streaming Algorithm for Approximating Graphlet Distributions
domain: graph-db | streaming
props: upper-bound | error-bound | probabilistic-guarantee
tools: concentration-ineq | coupling-dominance | estimation-theory
modeling: Edge stream; the k-graphlet distribution is approximated in L∞. Two phases: compute a (1+ε)-approximate degree-dominating order from sampled subgraphs, then estimate isomorphism-class probabilities with per-class counters (Horvitz–Thompson) instead of rejection sampling.
properties: DD order in O(1/c) passes and Õ(n^{1+c}) memory w.p. 1−1/n; distribution error ≤α w.p. 1−δ using O(k^{O(k)}/(α⁴M)·ln(1/δ)) passes and M words; memory near-optimal against a pass/memory lower bound.
usage: Chernoff plus union bounds control bad events; stochastic-dominance coupling equates one-pass and multi-pass sampling; conditioning on denominator concentration handles ratio estimators.
role: design-driver — pass/memory/error analysis motivates the counters-over-rejection redesign.
quote: "The L∞ distance between p̂ and the k-graphlet distribution of G is at most α, with probability at least 1−δ; preprocessing uses O(1/c) passes and Õ(n^{1+c}) bits."

### sigmod26-079 — DP-S4S: Select-Join-Aggregate Query Processing with User-Level DP
domain: privacy-dp | aqp
props: privacy-guarantee | error-bound
tools: concentration-ineq | information-theory
modeling: User-level DP over select-join-aggregate queries: users contribute tuples to a join result; Poisson sampling of join tuples at rate q plus truncation at τ; both pure and Rényi DP; ℓp-error framework over scalar/vector outputs.
properties: Exact sampling-amplification formula for user-level DP (binomial mixture over witness-user contributions); scalar error Õ(√(n/q)+1/q+τ*(T)(1+1/(qε*))) w.p. 1−β; RDP smooth-sensitivity mechanism for vector queries with noise scale set by roots of h(t)=0.
usage: Rényi-divergence convexity and Bernstein/Chernoff bounds drive amplification and error proofs; SVT searches the truncation threshold.
role: design-driver — the amplification theorem dictates sampling rate and privacy-budget allocation.
quote: "Algorithm 2 satisfies (ε,0)-DP; with probability 1−β its error is Õ(√(n/q) + 1/q + τ*(T) + τ*(T)/(qε*))."

### sigmod26-068 — Defense against Poisoning Attacks under Shuffle-DP
domain: privacy-dp | security
props: robustness-stability | privacy-guarantee | error-bound
tools: peeling-dyadic | concentration-ineq | + dp-composition
modeling: Shuffle-DP (randomizer–shuffler–analyzer) with up to k̂ corrupted users injecting poisoned messages; any union-preserving query Q with a generic base protocol error Error_ℓp(P_Q,·); hierarchical detection levels aggregate single users, √n-blocks, then doubling-size groups.
properties: SUSDP error O(n·Error+γ), BSDP O(√n·Error+γ), HSDP/OHSDP O(log n·Error+γ), all w.p. 1−β and preserving (ε,δ)-DP; k-attacker bound O(k·log n·Error+γ(k)); O(log n) extra messages per user.
usage: Parallel/basic composition and post-processing give privacy; union bounds and triangle inequality track per-level error; dyadic group sizes yield the log n bound.
role: design-driver — the hierarchical detection structure is engineered to meet the error/privacy bounds.
quote: "With probability at least 1−β, the total error is bounded by O(k·log n·Error_ℓp(P_Q, ε/log n, δ/log n, β/n) + γ_ℓp(Q, k·log n·log(1/δ)))."

### sigmod26-009 — Accelerating Maximum Common Subgraph Computation by Exploiting Symmetries
domain: graph-db
props: correctness | upper-bound
tools: exchange-greedy | + automorphism-group
modeling: Maximum common induced subgraph (NP-hard) solved by branch-and-bound (McSplit-style) over vertex mappings; modular symmetry = vertices with identical neighborhoods, shown equivalent to transposition automorphisms; variable- and value-symmetry rules prune symmetric branches.
properties: Breaking variable or value symmetry preserves correctness and completeness; positive/negative symmetry are mutually exclusive; symmetry detection in O(n²) time and O(n) space via neighborhood hashing; pruning bound |M|+Σ min(|V_l|,|U_l|).
usage: Swap/exchange arguments map any pruned branch to an earlier lexicographic branch; the automorphism characterization identifies symmetry classes.
role: design-driver — completeness theorems license the symmetry-based pruning that yields the speedup.
quote: "Variable symmetry breaking does not violate the correctness or completeness of the MCIS solution."
