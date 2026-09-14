### sigmod26-229 — Stress-Testing Causal Claims via Cardinality Repairs
domain: data-cleaning
props: hardness
tools: reduction | exchange-greedy
modeling: Database with treatment T, outcome O, confounders; ATE as causal estimand. Repairs are deleted tuple sets or conjunctive-equality patterns; decision version asks whether ≤n deletions move ATE into [target−ε, target+ε]. Tuple influence = ATE change on deletion. Mildly noisy pdf extract (prose interleaved with statements).
properties: CaRET (tuple removal) NP-complete via SUBSET-SUM reduction; pattern-removal variant also NP-complete for AVG and ATE, even without confounders.
usage: NP-completeness motivates influence-scored greedy heuristics (SubCure-tuple/pattern) with sampling and periodic influence recomputation instead of exact optimization.
role: design-driver — hardness propositions directly justify the heuristic algorithms.
quote: "Problem 1 and Problem 2 are NP-complete for AVG and ATE."

### sigmod26-236 — Task Cascades for Efficient Unstructured Data Processing
domain: llm-db
props: hardness | probabilistic-guarantee
tools: reduction | concentration-ineq
modeling: LLM cascade stages as (document fraction f, model m, operation o, thresholds) with a token-caching cost model; surrogate operations approximate the oracle task; accuracy target α with failure probability δ. Noisy: "Theorem 1.1" captured is a figure caption.
properties: Optimal task-cascade construction is NP-hard (reduction from MSSC where cascade cost equals set-cover objective); threshold-adjustment algorithm returns a cascade meeting Pr(Acc < α) ≤ δ.
usage: NP-hardness motivates heuristic cascade assembly; a concentration-based estimator (Hoeffding-style, Waudby-Smith–Ramdas) plus union bounding over adjustment iterations certifies end accuracy.
role: design-driver — the accuracy guarantee shapes the threshold-adjustment loop.
quote: "Algorithm 3 returns a cascade 𝜋∗ with Pr(Acc(𝜋∗) < 𝛼) ≤ 𝛿."

### sigmod26-235 — TaCo: Subspace Collision for High-dimensional Approximate Nearest Neighbor Search
domain: ann-vector-search
props: probabilistic-guarantee | error-bound
tools: spectral-matrix | concentration-ineq
modeling: Data covariance Σ̂ with orthonormal subspace maps B_j; subspace-collision (SC) score modeled as binomial collision count; greedy balanced eigensystem partition maximizing log-det. Statement capture failed (stmts=0), proofs carry the content.
properties: Distance preservation (1−ε)‖oᵢ−o_z‖² ≤ ‖B⊤(oᵢ−o_z)‖² ≤ ‖oᵢ−o_z‖² under orthogonal projection; SC-score separation of query-near vs query-far objects via binomial KL/Chernoff bound; eigenvector allocation optimal by interlacing.
usage: Poincaré separation (Cauchy interlacing) proves the eigensystem allocation solves the log-det problem; projection non-expansiveness plus Chernoff bound justify collision-based candidate selection in k-ANNS.
role: design-driver — the optimization solution and separation analysis directly define the index/query algorithms.
quote: "∥B⊤(𝑜𝑖−𝑜𝑧)∥² ≥ (1−𝜀)∥𝑜𝑖−𝑜𝑧∥² ... yields ∥B⊤(𝑜𝑖−𝑜𝑗)∥² < ∥B⊤(𝑜𝑖−𝑜𝑧)∥²."

### sigmod26-201 — Rollbaccine: Herd Immunity against Storage Rollback Attacks in TEEs
domain: consensus-replication | security
props: consistency | correctness
tools: induction
modeling: Histories with invocations/responses, happens-before ordering, sequential histories and reads-see-writes; durable cuts over primary/backup writes ordered by writeIndex; rollback-attack threat model; Matchmaker-Paxos-style reconfiguration by ballots.
properties: Linearizability of durable execution under rollback attacks (constructive sequential history); backups form a durable cut containing all completed synchronous writes; reconfiguration safety across ballot changes.
usage: Constructive sequential-history linearizability argument; writeIndex monotonicity for cut durability; induction on ballot differences for reconfiguration.
role: appendix-foundation — formal definitions and proofs certify the storage/replication guarantees; systems benchmarks carry the paper.
quote: "To prove that DE is linearizable, we must construct a sequential history S that respects reads-see-writes ... By definition, DE is linearizable."

### sigmod26-076 — Distribution-Aware Exploration for Adaptive HNSW Search
domain: ann-vector-search
props: probabilistic-guarantee | + asymptotic-normality
tools: clt-normal-approx | estimation-theory
modeling: Full Distance List (FDL) for inner-product distances; i.i.d.-across-dimensions assumption on embeddings (empirically supported; Lindeberg relaxation and correlation-aware variance discussed); adaptive ef = minimum ef achieving user-specified expected recall; distances sampled from 2-hop neighborhood.
properties: FDL of inner-product distances converges in distribution to Normal with explicit mean ΣqᵢE[vᵢ] and variance Σqᵢ²Var(vᵢ) as d→∞.
usage: CLT-derived distance distribution lets ESTIMATE-EF choose ef meeting expected recall dynamically, replacing the user-supplied ef parameter.
role: design-driver — the distributional limit directly powers the Ada-ef search algorithm.
quote: "the full distance list 𝐹𝐷𝐿𝐼𝑃(q, V) converges in distribution to a normal distribution as 𝑑 → ∞ ... 𝜎²𝐼𝑃 = Σ qᵢ² Var(vᵢ)."

### sigmod26-165 — MultiVis-Agent: Multi-Agent Framework with Logic Rules for Cross-Modal Data Visualization
domain: llm-db
props: correctness | robustness-stability
tools: induction
modeling: Logic-rule framework (CR/TE/EH/RC) over multi-agent executions; parameter domains partitioned into valid/invalid; error-recovery function with finite retry cap; execution traces with state transitions and loop invariant counter(sᵢ)=i. Noisy extract: theorem statements embedded inside proofs; formalism is procedural (bounded retries, iteration caps) rather than deep.
properties: Parameter safety by exhaustive case analysis; bounded error recovery within finite T_e; guaranteed termination with |σ| ≤ T_max = 10 iterations; system reliability as conjunction of the three.
usage: Case analysis over parameter vectors, strong induction with retry bounds, loop invariants plus well-ordering to force termination.
role: design-driver — theorems back the deterministic rule system that constrains LLM agent decisions.
quote: "All execution sequences 𝜎 ∈ Σ ... terminate within a maximum of 𝑇𝑚𝑎𝑥 = 10 iterations."

### sigmod26-043 — Causal Explanations for Disparate Trends: Where and Why?
domain: fairness
props: hardness
tools: reduction
modeling: Pearl causal model with DAG, unconfoundedness and overlap assumptions, backdoor adjustment; patterns as conjunctions of equality predicates defining subpopulations; CATE-based disparity Δ(φ); selection problem with budget k, support threshold σ, similarity threshold τ, total-disparity bound B.
properties: The top-k disparity-explanation selection decision problem is NP-hard via reduction from Independent Set; hardness holds w.r.t. number of explanations, itself exponential in attribute count.
usage: Hardness justifies Apriori-based subpopulation mining heuristic over candidate patterns instead of exact selection.
role: design-driver — NP-hardness motivates the heuristic mining algorithm.
quote: "determining whether ∃Φ ⊆ Φ𝑐 s.t. |Φ| ≤ 𝑘, ∀𝜙ᵢ ∈ Φ, 𝑠𝑢𝑝𝑝𝑜𝑟𝑡(𝜙) ≥ 𝜎 ... and Σ𝜙∈Φ Δ(𝜙) ≥ 𝐵 is NP-hard."

### sigmod26-204 — RAIRS: Optimizing Redundant Assignment and List Layout for IVF-Based ANN Search
domain: ann-vector-search
props: + closed-form expected loss
tools: + uniform-sphere geometric integration
modeling: IVF lists with centroids c, c′; queries uniformly distributed on a hypersphere of radius l_m around point x; residuals r = c−x, r′ = c′−x; loss L(c′,c,Q) measures regret of the second (redundant) list versus the ideal.
properties: Closed form L(c′,c,Q) ∝ ‖r′‖² + λr⊤r′ for uniform queries — the second list should lie in the inverse-residual direction; λ=0 degenerates to nearest-second-list.
usage: Expectation over the hypersphere evaluated by decomposing vectors into parallel/orthogonal components and computing trigonometric integrals over surface area; the theorem directly yields the AIR selection metric.
role: design-driver — the derived closed form IS the redundant-assignment strategy.
quote: "𝐿(𝑐′, 𝑐, 𝑄) ∝ ||𝑟′||² + 𝜆𝑟⊤𝑟′ where 𝑟 = 𝑐 − 𝑥, 𝑟′ = 𝑐′ − 𝑥, and 𝜆 > 0 is a constant factor."

### sigmod26-101 — Fair Data Pre-Processing with Imperfect Attribute Space
domain: fairness
props: identifiability
tools: spectral-matrix
modeling: Latent causal model: one latent attribute X₀ with τ states, d≥4 observed attributes in four groups, conditional independence of groups given (X₀,X₄), X₀ ⊥ X₄; group cardinalities κᵢ ≥ 2; fairness policy defined on the latent-augmented DAG with parameters θ* fit to data.
properties: Local parameters generically identifiable up to a global permutation of latent states when at least two groups have cardinality ≥ τ (tensor-decomposition identifiability condition).
usage: Conditioning on each X₄=j slice yields per-slice latent-class models; tensor-decomposition identifiability plus the shared mixing distribution forces one consistent global permutation; θ₄ read from observed conditionals.
role: design-driver — identifiability licenses estimating the latent fairness policy from observed data.
quote: "the local parameters 𝜃𝵢 of each 𝑋𝵢 are generically identifiable up to a global permutation of the latent states."

### sigmod26-215 — ScaleDoc: Scaling LLM-based Predicates over Large Document Collections
domain: llm-db
props: probabilistic-guarantee | generalization-bound
tools: concentration-ineq
modeling: LLM-predicate scores with thresholds (l,r); proxy sample S′ of size pN; empirical functional T_{S′}(l,r) tracking oracle disagreement against positive-class mass F⁺; accuracy target α, confidence δ.
properties: Sample condition T_{S′}(l,r) ≤ (1−α)F⁺_{S′} − ε implies P[Acc_S(l,r) ≥ α] ≥ 1−δ; margin ε shrinks with sample size and score variances.
usage: Bernstein inequality on i.i.d. indicator means with variance-aware margins, union bound at δ/2; discretization in threshold search acts as a conservative buffer over ε.
role: design-driver — the variance-driven margin justifies contrastive learning of low-variance proxy scores.
quote: "if the sample condition satisfies T_{𝑆′}(𝑙,𝑟) ≤ (1−𝛼)𝐹_{𝑆′}⁺ − 𝜖, then the true accuracy satisfies 𝑃[Acc𝑆(𝑙,𝑟) ≥ 𝛼] ≥ 1−𝛿."
