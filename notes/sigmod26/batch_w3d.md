### sigmod26-253 — Weighted Fourier Factorizations for Private Marginal Queries
domain: privacy-dp
props: error-bound | tightness | privacy-guarantee
tools: spectral-matrix | kkt-optimality | concentration-ineq
modeling: Workloads of marginal/product queries over a product universe as workload matrix W; mechanisms are factorizations LR=W answering Fourier strategy queries under μ-GDP; error = weighted-average or maximum squared error; noise sampled via FFT. PODS paper; pdf-derived with interleaved footers, statements clean.
properties: Exact error formulas for the Fourier factorization (Thms 8/12/16); optimality among all factorization mechanisms for weighted and max-variance error; matching lower bound on γ_F(P^{1/2}W) (Thm 18) — near-tight; near-linear noise-sampling time.
usage: First-order optimality (KKT) conditions on the weight LP pin p* so average weighted error equals max variance; operator norms ∥PL∥_F, ∥R∥_{1→2} carry the γ2 machinery; Gaussian concentration lifts variance to max-error.
role: theory-as-contribution — the optimal mechanism plus matching lower bound is the paper.
quote: "In Section 3.3 we show that the error bound of Lemma 9 is also optimal among all factorization mechanisms."

### sigmod26-024 — Approximate DBSCAN via Density-Biased Sampling and Kernel Density Estimation
domain: spatial | sampling
props: probabilistic-guarantee | correctness
tools: estimation-theory
modeling: DBSCAN clusters as connected components of a cluster graph; sampled set D_i as a minimal connected dominating set; ε-neighborhood size computed via uniform-kernel KDE (exact identity, Lemma 4.3); assumes independent points and uniformly distributed KDE error. np_hard/approx_ratio signal counts come from related-work text — noisy.
properties: Every point of D_i is core; union of ε-neighborhoods of D_i equals the cluster; lower bounds on P_same (correct merge through k core points) and P_diff (correct separation; =1 for well-separated clusters) for LDBS-KDE.
usage: Case analysis over candidate-selection events plus independence yields per-pair merge/separation probabilities; the KDE identity reduces core-point tests to density estimates.
role: design-driver — dominating-set and KDE lemmas justify the sampling scheme; probability bounds quantify its accuracy.
quote: "P_same ≥ (3/4) · ((d+2)l² / (8πε²·(d+1)²))^(k+1)"

### sigmod26-214 — Scalable Privacy-Preserving Shortest Path via 2-Hop Labeling in MPC
domain: graph-db | privacy-dp
props: correctness | privacy-guarantee
tools: induction | dp-composition
modeling: Graph split across two MPC parties (secret sharing + HE); per-party 2-hop labels; an abstract combined boundary graph kept secret-shared; edge-weight-level DP (neighbors differ by ℓ1 weight 1) with Laplace noise on the Bellman-Ford loop count.
properties: Boundary and combined boundary graphs preserve global shortest distances (Lemmas 4.4, 5.2); oblivious Bellman-Ford terminates correctly under a DP-noised, truncated loop count that never under-counts rounds; mechanism satisfies (ε,δ)-DP (Thm 5.4).
usage: Optimal-substructure induction over boundary decompositions proves distance preservation; truncated Laplace mechanism analysis gives privacy with guaranteed convergence.
role: design-driver — preservation lemmas shape the boundary-graph protocol; the privacy theorem certifies pruning.
quote: "Theorem 5.4 (Privacy Guarantee). The above mechanism satisfies (𝜖, 𝛿)-differential privacy."

### sigmod26-242 — To Adapt or Not to Adapt, That is the Ski Question
domain: sketching | caching-scheduling
props: competitive-ratio | probabilistic-guarantee
tools: competitive-analysis | adversarial-construction
modeling: Deciding when to adapt a filter to repeated false positives cast as ski rental: each false positive costs C_DB (rent), adapting costs C_RM (buy), ratio α=C_RM/C_DB; adversarial sequence of k false positives.
properties: For α≥1, adapt-after-⌊α⌋ is optimal and 2-competitive; for α<1, equating candidate ratios gives threshold α=0.618 — adapt immediately (ratio 1+α) vs on second occurrence ((2+α)/(1+α)); filter augmentation bounds false positives whp (Lemma 6).
usage: Worst-case ratio analysis over adversarial input sequences; importing whp bounds for strongly adaptive filters composes the guarantees.
role: theory-as-contribution — optimal competitive strategies for the adapt decision are the contribution.
quote: "For 𝛼 < 1, the optimal strategy is to adapt immediately when 𝛼 < 0.618 and adapt on the second occurrence otherwise."

### sigmod26-348 — PrivAGS: Differentially Private Attributed Graph Synthesis
domain: privacy-dp | graph-db
props: privacy-guarantee | hardness | correctness
tools: dp-composition | reduction | markov-chain
modeling: Attributed graph synthesis under Rényi DP: Gaussian mechanisms across four pipeline phases (communities, dependency graph, attributes, edges); dependency structure cast as an optimized inference structure (OIS) minimizing noise power; MCMC edge generation targeting a cohesiveness distribution Π.
properties: Overall (α,ε)-DAE RDP with ε=ε1+ε2+ε3+ε4 (Thm 1); bounded Gaussian threshold mechanism is (α,ε2)-RDP (Thm 2); OIS is NP-hard via 3-Partition (Thm 3); Markov chain converges to Π, irreducible and aperiodic (Thm 4, Lemmas 1-2).
usage: RDP composition across phases; likelihood-ratio Rényi divergence bound for thresholding; reduction for hardness; irreducibility/aperiodicity certify the sampler.
role: design-driver — privacy accounting and NP-hardness (motivating heuristics) shape each pipeline stage.
quote: "Our solution satisfies (𝛼, 𝜀)-DAE RDP, where 𝜀 = 𝜀1 + 𝜀2 + 𝜀3 + 𝜀4."

### sigmod26-190 — PJsim: Towards Precise and Scalable Graph Similarity
domain: graph-db
props: correctness
tools: spectral-matrix
modeling: Node-pair graph similarity defined by a Lyapunov-type matrix equation XS + SX^T = 2(1−c)I_n built from random-walk structure; solutions computed exactly, truncated, or via decomposition. Signal counts (approx_ratio, convergence) partly from surrounding prose.
properties: Vectorization (X⊕X)Vec(S)=2(1−c)Vec(I_n) with closed-form inverse (Thm 3.1, Cor 3.1.1); invertibility since eigenvalues of X⊕X lie in [2(1−c),2]>0; Neumann-series truncation, eigendecomposition, and Schur-based block back-substitution yield solvers.
usage: Kronecker-sum eigenvalue analysis, Neumann expansion, and real Schur decomposition replace direct O(n^6) vectorized inversion.
role: design-driver — the linear-algebraic reformulation is the algorithm.
quote: "The vectorized PJsim similarity matrix has the direct closed-form solution: Vec(𝑆^PJ) = 2(1−𝑐)(𝑋⊕𝑋)^{−1}Vec(𝐼𝑛)"

### sigmod26-362 — SieveSketch: A Fine-grained and Adaptive Sketch Framework for Accurate Frequency Estimation
domain: sketching | streaming
props: error-bound | probabilistic-guarantee
tools: balls-bins-hashing | estimation-theory
modeling: Three-tier (cold/warm/hot) frequency sketch; cold items in few-bit counters with round-based adaptive sampling probability p_i and halving on overflow; error split into hash-collision part β_h and scaling part β_c.
properties: Round trigger thresholds n_i from counter-occupancy probabilities (Thm 1); increments unbiased under binomial thinning (Lemma 1); scaling error β_c ≤ 2^{i−1}−1 (Lemma 2); per-item and whole-sketch accuracy Pr(1−2^{i−1} ≤ f̂−f ≤ ε‖f‖₁) ≥ 1−Σ P_fp (Thms 2-3).
usage: Occupancy/binomial analysis sets sampling triggers; worst-case collision accounting yields the probability tail bound.
role: design-driver — theorems calibrate the adaptive-scaling module and certify its accuracy.
quote: "Pr(1 − 2^{i−1} ≤ f̂_{u_i} − f_{u_i} ≤ 𝜖‖f‖₁) ≥ 1 − Σ_{j=t−𝜖‖f‖₁}^{t} P_fp(w₁, k₁, j)"

### sigmod26-128 — High-Throughput k Nearest Neighbors Search in Road Networks
domain: spatial | graph-db
props: correctness | upper-bound | space-complexity
tools: induction | dp-optimality
modeling: Road network recursively split by balanced vertex cuts into a cut tree inducing partial order ≺; index stores local shortest distances, local kNN, and convex neighbors per vertex; dynamic object updates. Noisy pdf extract (parameter tables inside statements); no proofs extracted.
properties: Global dist(v,u)=min over cut vertices of lsd sums (Thm 4.3); local kNN from convex neighbors' lists (Thm 5.1); index size O(Σ|S(v)|); construction O((m log n + w(m+n log n)) log n); incremental-polynomial kNN queries; updates O(|P(o)|·k·ℓ_max) and O(|P(o)|·k).
usage: Cut-tree decomposition reduces global distances and kNN to precomputed local quantities; complexity bounds certify construction, query, and update costs.
role: design-driver — locality theorems are the index's foundation.
quote: "dist(𝑣, 𝑢) = min_{𝑐∈P(𝑣)∩P(𝑢)} lsd(𝑐,𝑣) + lsd(𝑐,𝑢), where lsd(𝑐,𝑣) and lsd(𝑐,𝑢) are stored in our index."

### sigmod26-301 — DRPQ: Distributed Evaluation of Regular Path Queries On Streaming Graphs
domain: graph-db | streaming
props: correctness | completeness-recall
tools: + dfa-product-graph
modeling: Streaming graph as timestamped edge sequence with sliding-window snapshot semantics; RPQ compiled to a DFA evaluated over a product graph; partial matches grouped into Partially Matched Query Tasks (PMQTs) over timestamped rooted digraphs, distributed to workers; PMQT similarity via (bucketed) vector dot products.
properties: Processing multiple PMQTs generates all correct query results (Thm 1); overall distributed evaluation is correct and complete (Thm 2), by timestamp-subset reuse arguments.
usage: Definitions formalize the task; subset-inclusion reasoning validates task decomposition and cross-worker reuse; vector similarity heuristically groups tasks.
role: design-driver — the PMQT formalism and correctness results underpin the distributed design.
quote: "Theorem 2. The query results obtained from DRPQ are correct and complete."

### sigmod26-195 — Prism: Private Relational Data Synthesis with Language Models
domain: privacy-dp | llm-db
props: privacy-guarantee
tools: dp-composition
modeling: PATE-style DP distillation: teacher LLMs vote per token, votes perturbed with Gaussian noise; the privatized transcript (noisy ranges, histograms) trains a student that emits synthetic relational data; Rényi-DP accounting. Extract captured proofs only (statement headers missed).
properties: Gaussian-CDF false-positive/negative probabilities for noisy thresholding; ℓ2 sensitivities: vote gap ≤2, histogram √2; per-round RDP cost with adaptive composition and budget stopping; end-to-end (ε(δ),δ)-DP via RDP→DP conversion plus post-processing immunity.
usage: Sensitivity analysis and the Gaussian/RDP calculus compose privacy loss across the pipeline.
role: design-driver — privacy accounting is built into each distillation round.
quote: "Since differential privacy is preserved under arbitrary post-processing, these steps incur no additional privacy cost."

### sigmod26-224 — Skyline Retrieval meets Set-Cover Chunk Merging for Long-Context LLM QA
domain: llm-db
props: hardness | approximation-ratio
tools: reduction | exchange-greedy | adversarial-construction
modeling: Long-context QA as retrieval plus merging: queries decomposed into extraction meta-queries; chunks scored on presence (φ) and semantic (ω) dimensions; chunk merging formalized as minimum-cost coverage of meta-queries under a token budget.
properties: Merge problem NP-hard via cost-preserving reduction from Weighted Set Cover (Thm 3.8); greedy gain-per-cost step satisfies G_{t+1} ≥ r_t/OPT (Lemma 3.10, the efficiency lemma behind the logarithmic guarantee); presence and semantic dimensions complementary (Lemma 3.4).
usage: WSC reduction proves hardness, motivating greedy merging; an averaging argument against an optimal cover bounds each greedy step.
role: design-driver — hardness plus greedy guarantee justify the merge heuristic.
quote: "The meta-query merge problem is NP-hard via a polynomial-time, cost-preserving reduction from Weighted Set Cover (WSC)."

### sigmod26-310 — Estimating Biclique Counts with Accuracy Guarantees
domain: graph-db
props: error-bound | probabilistic-guarantee
tools: estimation-theory
modeling: (p,q)-bicliques counted via "zstar" structures: every biclique contains exactly one h-zstar (h=p), giving sample space Δ(G); two-stage design — build a BC-Shadow sample space, then uniform zstar sampling governed by a stopping rule.
properties: Unbiased estimator (|Δ|/|T|)ΣX(Z) (Thm 2); zstar sampling time O(|E|+p·d_max) (Thm 3); with probability ≥1−δ, relative error ≤ε (Thm 4).
usage: Zstar uniqueness makes indicator sampling unbiased via linearity of expectation; the stopping-rule theorem converts samples into (ε,δ) accuracy.
role: design-driver — the guarantee shapes the sample-space/estimator split.
quote: "𝑐𝑝,𝑞(𝐺) = (|Δ(𝐺)|/|𝑇|) Σ_{𝑍∈𝑇} 𝑋(𝑍) is an unbiased estimator for the count of (𝑝,𝑞)-bicliques in 𝐺."

### sigmod26-351 — Query Optimization for Database-Returning Queries
domain: query-optimization
props: correctness
tools: induction | + block-cut-forest
modeling: Database-returning queries optimized via semi-join programs; join-graph acyclicity (α- vs JG-); cyclic graphs handled by biconnected-block decomposition, block enumeration problems (BEP), and folding vertex cuts into single nodes; heuristic selectivity-based cost model C_Decompose.
properties: Horizontal semi-join order independent of the tree root (Lemma 4.1); a folded vertex cut becomes a cut vertex (Lemma 6.3); recursive algorithm solves the tree-folding enumeration problem (Thm 6.4); TVC benchmark query family defined.
usage: Induction over subtrees and blocks proves order-invariance and folding correctness; cost heuristics choose folds and roots.
role: design-driver — structural join-graph theory directly yields the TDFold/TDRoot optimizers.
quote: "Then, the solution returned by Algorithm 5 is a solution for the TFEP of 𝐺[𝐵]."
