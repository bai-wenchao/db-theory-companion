# batch_w5b — queue3 lines 117-128 (scores 4-2)

### sigmod26-251 — VecBench: A Controllable Benchmark for Filtered Vector Search
domain: benchmark | ann-vector-search
props: probabilistic-guarantee | error-bound
tools: concentration-ineq
modeling: Filtered search query Q=(q,P,K) over vector+scalar-attribute pairs with predicate-filtered subset; AMMD (averaged squared MMD over scalar-conditioned groups) checks conditional-distribution preservation in synthetic data. Pdf-derived extract: figure captions bleed into the theorem text (mildly noisy).
properties: JL-style expected relative error ε(N,k,δ) ≈ √(4/k·(2 ln N + ln(1/δ))) for Gaussian-projection dimension upscaling: all N² pairwise distances preserved within relative ε at confidence level δ (stated as "probability at least δ", likely 1−δ mangled).
usage: Chi-square concentration per direction plus union bound over N² pairs yields the projection guarantee for benchmark data generation.
role: design-driver — the projection error bound certifies fidelity of synthesized high-dimensional data.
quote: "All pairwise distances in the transformed space satisfy ∥f(u)−f(v)∥²₂ − ∥u−v∥²₂ ≤ ε∥u−v∥²₂, for all u, v ∈ X, where the expected relative error bound is ε(N,k,δ)."

### sigmod26-323 — High Performance or Low Memory? Updatable Learned Index Time-Space Tradeoff
domain: indexing
props: io-cost-bound | space-complexity | robustness-stability
tools: + analytical cost-model derivation (no formal proofs)
modeling: Gapped learned index (LIFT); Observations 2.1/2.2 (not theorems) that time-space-optimized learned indexes like ALEX collapse under duplicated-key and dense-key poisoning attacks (space ACAs); quantitative gap sizing trades memory-access count against space.
properties: No theorems/proofs. Closed-form memory-access-count and lookup-time equations (e.g., L(d) = H(ε) + 2δεd/ω + log₂-term) parameterized by gap density and model error ε; user-defined upper bound T_total on lookup time; inner nodes claimed fully precise after top-down construction.
usage: Cost equations size gaps to meet a user-given time bound under space budget; ACA defense is structural, validated empirically only.
role: design-driver — cost-model equations parameterize the tradeoff; robustness by construction, not proof.
quote: "In memory-based indexes, the memory access count can approximate lookup performance, as the CPU computation overhead is negligible in comparison."

### sigmod26-328 — Integrating Vector Databases across Embedding Models
domain: ann-vector-search | data-integration
props: error-bound
tools: spectral-matrix
modeling: Cross-embedding-model alignment via isometric rigid map f_iso(x)=s·R(x−cX+cY) (rotation, scale, centroid shift) fitted on shared objects; assumes paired spaces share centroids.
properties: Per-point transformation error δ(z) ≤ (α+α*)·‖z−cX+cY‖/σmin(X), with α, α* the Frobenius fit residuals of the two alignments; error grows with distance from centroid and with ill-conditioning (small σmin).
usage: SVD of the translated source matrix, Frobenius-norm expansion, Cauchy–Schwarz and triangle inequalities chain into the bound; σmin serves as conditioning measure.
role: design-driver — the bound certifies when cross-model vector transformation is trustworthy.
quote: "Let σmin(X) be the minimum singular value of X. Assume that X and X̃ (resp. Y and Ỹ) have the same centroid. Then: δ(z) ≤ (α + α*)‖z − cX + cY‖/σmin(X)."

### sigmod26-379 — Understanding and Detecting Query Performance Regression in Index Tuning
domain: workload-tuning | query-optimization
props: + none — empirical observations only
tools: + none — plan ablation procedure
modeling: Query performance regression (QPR) in index tuning characterized as regression patterns RP-1..RP-3 — local plan transformations (new expensive NLJ, aggregation pushdown, bitmap-filter pushdown); Procedure 1 replans with/without new statistics to isolate cardinality-estimation impact.
properties: No formal results. Observation 4: RP-1 (new expensive nested-loop join) accounts for 23 of 28 significant QPRs; new statistics flip optimizer plans via cardinality under- or over-estimation.
usage: Pattern taxonomy plus statistics-ablation grounds a rule-based QPR detector focused on NLJ emergence; fixes via plan forcing.
role: design-driver — Observation 4 directly shapes the pattern-based detector.
quote: "The impact on cardinality estimation due to the introduction of new statistics can be significant enough to change the optimization decision made by the query optimizer." (Obs 3)

### sigmod26-046 — CMANNS: GPU-Accelerated Graph Index Construction for ANNS
domain: ann-vector-search | indexing
props: + pipeline-desynchronization claim
tools: + drift recurrence on inter-block time gap
modeling: Graph-index construction blocks fetch tasks independently from a global queue; per-block wall times t_b(n), inter-block difference Δn = t_b1(n) − t_b2(n) evolves via five stage times T^(k)(i); assumptions: both sequences exist, no global barrier, stage durations vary by task.
properties: Single proof, no named statements: Δn's increments are generically nonzero and never reset, so any two blocks eventually occupy different pipeline stages — desynchronization.
usage: The drift argument justifies the synchronization/barrier mechanism in the disaggregated GPU pipeline; the big-O counts sit in cost discussion, not formal bounds.
role: design-driver — motivates the pipeline synchronization design.
quote: "By (ii), no global barrier resets Δn to zero. Therefore, b1 and b2 occupy different pipeline stages at the same wall time, i.e., blocks desynchronize."

### sigmod26-112 — FLEA: Frequency-based Lossless Encoding for Periodic Time Series
domain: time-series | storage-compression
props: error-bound
tools: estimation-theory
modeling: Periodic series compressed via frequency-domain encoding; per-sample quantization residuals εj treated as deterministic yet uncorrelated across positions; DFT coefficient noise Rk = (1/n)Σ_j εj ω_n^{jk}.
properties: Exact expectation E[|Rk|²] = (1/n²)Σ_j |εj|²: all cross terms vanish under E[εj εl*]=0 for j≠l, so per-coefficient noise energy equals normalized total squared residual, independent of k.
usage: Expectation computation over root-of-unity phases separates signal from noise coefficients, steering frequency-based encoding allocation.
role: design-driver — noise-energy analysis justifies frequency-domain coding choices.
quote: "Applying the uncorrelated error assumption, which implies E[εj εl*] = 0 for j ≠ l ... all off-diagonal terms vanish: E[|Rk|²] = (1/n²) Σ_{j=0}^{n−1} |εj|²."

### sigmod26-116 — From Learning to Recycling: A Log-Structured Learned-Less Index
domain: indexing | storage-compression
props: correctness
tools: induction
modeling: Two sorted SSTables merged by Compare-Less Compaction: SSTn keys placed at monotonic-model-predicted positions in bufKeys[] with linear probing right on collision, then merged against SSTn+1.
properties: Lemma 4.2: merged output mergedKeys[] is non-decreasing, proven by induction on output position; three cases (predicted-position predecessors, collision, current key) each yield the global minimum among remaining keys.
usage: Predictor monotonicity plus per-position case analysis establishes merge correctness without key comparisons — the "compare-less" claim.
role: design-driver — correctness lemma underpins the comparison-free compaction.
quote: "Given two sorted SSTables SSTn and SSTn+1, the Compare-Less Compaction algorithm produces a merged output array mergedKeys[] in non-decreasing order." (Lemma 4.2)

### sigmod26-122 — GoodTP: Trajectory Data Selection via Monte Carlo Tree Search
domain: spatial
props: correctness
tools: reduction
modeling: Trajectory selection as budgeted subset choice S⊆T, |S|=B, versus per-cluster sampling rates αi with partition constraint Σ αi|TCi| = B; MCTS searches the relaxed space (convergence mentions look related-work-sourced — noisy).
properties: Single proof: forward map αi=|S∩TCi|/|TCi| and backward map S=⋃Sample(TCi,αi) preserve feasibility and objective, bijective up to sampling randomness; no optimality guarantee for MCTS itself.
usage: Solution-space equivalence licenses MCTS over sampling-rate strategies instead of discrete subsets without objective change.
role: design-driver — the formulation equivalence justifies the MCTS search space.
quote: "Given any feasible solution S ⊆ T with |S| = B, we construct the corresponding sampling strategy by defining αi = |S∩TCi| / |TCi|."

### sigmod26-237 — The Case For Language Model Approximated LIKE Predicate
domain: llm-db
props: lower-bound | + exact pattern-entropy formula
tools: information-theory
modeling: LIKE pattern (length x, p underscores, q non-adjacent percents, max string length m) gets closed-form entropy via stars-and-bars string counts; LM scale M abstracted as capacity bound on internalizable complexity H(W). Noisy counts (big_o=22, cardinality=31) mostly prose.
properties: Theorem 5: exact H(P) = p ln|Σ| + Σ_s (s+q−1 choose q−1)/|Σ|^s · ln|Σ|; bound sentence: success probability p ≥ c·min(1, M/H(W)), enabling sampling bounds.
usage: Entropy measures predicate difficulty; capacity ratio M/H(W) links model scale to success probability, gating when LM approximation is viable.
role: design-driver — entropy/capacity model decides viable LM-approximated predicates.
quote: "M represents an abstracted upper bound on the total task complexity H(W) that the model can reliably internalize ... a tractable, albeit simplified, link between model scale and task complexity."

### sigmod26-331 — LPStream: Fine-grained Lazy Provenance for Stream Processing
domain: provenance | streaming
props: correctness
tools: + timestamp-interval composition along operator paths
modeling: Provenance of an output tuple wrt. an operator = set of contributing tuples; window semantics bound contributing input timestamps to [to−ws, to] (ws=0 for Filter/Map); a replay checkpoint must (1) cover all contributing tuples, (2) be the latest with monotone timestamps.
properties: Proof (no named statement): choosing the checkpoint with max timestamp tsi < to − WSize satisfies both conditions, WSize the composed window along all derivation paths.
usage: Per-operator intervals compose along paths; latest checkpoint below to − WSize yields sound, latest-possible lazy replay.
role: design-driver — soundness argument certifies lazy checkpoint selection.
quote: "A checkpoint with a timestamp less than to − ws ensures that all contributing input tuples are replayed ... to − WSize represents the possibly smallest timestamp of a contributing tuple."

### sigmod26-069 — Detecting Join Bugs via Join Implication Reasoning
domain: join-algorithms | + engine testing/bug detection
props: correctness
tools: + double-containment bag-semantics argument
modeling: Join results under bag semantics; join-implication identities relate join types under a common predicate (inner, left outer, anti with NULL padding N(·)); a target join's expected result inferred from executions of logically related joins.
properties: Proven identity L ⟕LEFT_P R = (L ⋈INNER_P R) ∪ N(L ⟕ANTI_P R) by mutual bag inclusion, matching vs NULL-padded cases; generality claimed for arbitrary predicates and bag semantics.
usage: Double-containment case analysis validates each oracle identity; identities become differential oracles across join types for bug detection.
role: design-driver — proven join equivalences are the detection mechanism's oracles.
quote: "Combining (1) and (2) we obtain BAG1 = BAG2, i.e. L ⟕LEFT_P R = (L ⋈INNER_P R) ∪ N(L ⟕ANTI_P R)."

### sigmod26-249 — Unseen Anomaly Detection from System Logs
domain: + system-log anomaly detection (AIOps)
props: + none — formalization only
tools: + none
modeling: Log entry as 6-tuple (code file, request ID, event type, invoking file, execution time δ, exception type) with finite predefined event/exception type sets; invariant count (8) hints at behavior invariants over invocation chains. Thin extract: one definition, no theorems or proofs.
properties: None formal; only per-dataset hyperparameter thresholds (confidence lower bound, top-a ratio) for augmentation selection.
usage: Tuple model grounds downstream learned detection; no theory applied beyond the entry formalization.
role: motivation — formal model frames the problem; detection itself is learned and empirical.
quote: "We model each recorded log entry as a 6-tuple (cf, reqID, et, invcf, δ, exc), where cf ∈ CF is the code file in which this log message is generated."
