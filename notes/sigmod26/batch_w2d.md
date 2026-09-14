### sigmod26-086 — Efficient LLM Serving for Agentic Workflows
domain: llm-db | caching-scheduling
props: hardness | upper-bound
tools: reduction
modeling: Agentic-workflow serving modeled as scheduling a tree (TRT) of LLM operators under an inter-operator dependency graph, with a cost-based heuristic and makespan-style objective.
properties: NP-hardness via reduction from parallel-machine makespan scheduling; theorem bounds scheduler time at O(|V_int|·c_max³ + |E'|·d), proved by phase analysis (traversals, Σ O(k²) per node).
usage: The reduction places exact optimization out of reach, licensing the heuristic; the proof is constructive complexity accounting over the recursion.
role: motivation — hardness plus the polynomial-time scheduling theorem justify the cost-based heuristic design.
quote: "The time complexity of the scheduling algorithm (Algorithm 1) is O(|V_int| · c_max³ + |E'| · d)."

### sigmod26-207 — Reqo: Learning-Based Cost Model for Robust, Explainable Query Optimization
domain: query-optimization
props: + none-proven (definitional only)
tools: + none (definitional only)
modeling: Formalizes context-based hint generation over plan subgraphs, explainability of a learned cost model as a subgraph-contribution function E, and subplan patterns (SPP) from postorder relation sequences. No theorems, proofs, or bound sentences in extract.
properties: None proven; the definitions fix operationally what "explainable" and context-aware mean for a black-box cost model.
usage: Definitions structure the LCM architecture and its explanation interface; theory stays at the formalization level.
role: design-driver — formal definitions of explainability and context-aware hints shape the system.
quote: "A LCM is considered to be explainable if it quantifies the contribution of sg to C_learned(p) via a function E."

### sigmod26-258 — 3dSAGER: Geospatial Entity Resolution over 3D Objects
domain: entity-resolution | spatial
props: + none-proven (definitional only)
tools: + none (definitional only)
modeling: Defines 3D objects as polygon meshes (closed surfaces, shared edges), property vectors, a componentwise division operator, and an (ε,δ)-systematic discrepancy condition: a stable ratio r_g bounds a geometric property across most known matching pairs.
properties: The discrepancy condition is an assumed regularity, not a proven guarantee; it licenses ratio-based filtering between indexed and candidate sets.
usage: Formal geometry definitions feed the matching pipeline; the discrepancy band turns geometric ratios into a pruning filter.
role: design-driver — object and discrepancy definitions structure the ER pipeline.
quote: "There exists a ratio r_g such that at least a (1−δ) fraction of the known matching pairs satisfy r_g − ε ≤ g(P1) g(P2) ≤ r_g + ε."

### sigmod26-365 — SSCard: Substring Cardinality Estimation using Suffix Tree-Guided Learned FM-Index
domain: cardinality-estimation
props: + none-proven (thin extract)
tools: + none (thin extract)
modeling: Substring cardinality estimation via a suffix-tree-guided learned FM-index; defines the "starting character" (first suffix matching a pruned-tree path) and BWT L-triples (char, position, rank) as estimation units. Extract holds definitions only — no proofs or bound sentences, though heavy big-O/cardinality signals suggest complexity analysis lives in prose. Thin extract.
properties: None captured.
usage: The two definitions pinpoint where suffix-tree pruning hands off to the learned FM-index component.
role: design-driver — definitions carve the workload split between tree lookup and learned estimation.
quote: "A char P[i] is the starting character, if the suffix started from P[i] matches a path in T, and no suffix started from P[k] (k<i) matches any path in T."

### sigmod26-381 — VecFlow: A High-Performance Vector Data Management System for Filtered-Search on GPUs
domain: ann-vector-search
props: + none-proven (problem definitions only)
tools: + none
modeling: Formalizes filtered NNS/ANNS: labeled points in R^D, query with label set, goal is top-k recall under the label constraint at minimal search time. Noisy: the captured "Proof" is an empty stub; no theorems or bounds in extract.
properties: None proven; the recall/time trade-off is the stated objective, not an established result.
usage: Definitions frame the filtered-search workload the GPU system is built for.
role: appendix-foundation — preliminaries-style problem definitions, no formal results.
quote: "The goal of ε-filtered-NNS is to design an algorithm that answers a given query point q ... by maximizing the recall of finding the top-k closest points while minimizing the search time."

### sigmod26-005 — A Principled Solution to the Disjunction Problem of Diagrammatic Query Representations
domain: + query-languages (no taxonomy fit)
props: correctness
tools: induction
modeling: TRC safety conditions extended to disjunction for relational diagrams; syntactic fragments TRC¬∃∧ / TRC¬∃∧∨; pattern equivalence (same atoms, equivalent structure) as the fidelity criterion for diagrammatic syntax. Noisy: pdf-derived; the Theorem 3 statement is mangled with appendix prose.
properties: Lemma: TRC formulas with ∨/→/∀ admit pattern-equivalent disjunction-free rewrites in polynomial steps. Lemma 10: the four safety conditions yield relational completeness and domain independence, via constructive RA→safe-TRC translation and induction on operators.
usage: Equivalence-preserving syntactic translations show diagrams lose no expressiveness while remaining safe.
role: theory-as-contribution — the logic results about the diagrammatic representation are the paper.
quote: "The four conditions given in Section 3.2 are a valid safety restriction, i.e. the resulting safe TRC fragment is relationally complete and every safe TRC query is domain-independent."

### sigmod26-029 — Automated Discovery of Test Oracles for Database Management Systems Using LLMs
domain: llm-db | + dbms-testing
props: correctness
tools: + contradiction-counterexample
modeling: Conjunctive query templates (CAQs) with placeholders and constraints; instantiations substitute valid SQL snippets; two CAQs equivalent iff all instantiations are semantically equivalent — the oracle's foundation.
properties: Proof by contradiction that rewriting queries with expression-defined virtual columns preserves semantics: a constructed counter-database transfers, via unique-row-reference and null-preserving properties (outer joins).
usage: The equivalence theorem certifies generated query pairs as sound test oracles — no false-positive bug reports.
role: design-driver — soundness of the virtual-column rewrite underpins the LLM-driven oracle generation.
quote: "The core of this proof is establishing that for any query Q_k, the results Q_k(D) and Q_k'(D') are identical."

### sigmod26-030 — Automating Database-Native Function Code Synthesis with LLMs
domain: llm-db
props: + none-proven (definitional only)
tools: + none
modeling: Formalizes database-native function synthesis: generate unit functions satisfying spec S that integrate into database D, passing all test cases T without compliance errors; a function = declaration + unit functions + referenced modules. Noisy: the lone "bound sentence" is an experimental-results summary, not theory.
properties: None proven; success is defined by integration and test-case passage.
usage: The definition fixes the synthesis goal and success criterion for the agent pipeline.
role: design-driver — the formal task definition drives the decomposition into code-synthesis agents.
quote: "Database native function synthesis aims to generate the codes of necessary function units that satisfy S and can be successfully integrated into D."

### sigmod26-130 — HONEYBEE: Efficient Role-based Access Control for Vector Databases via Dynamic Partitioning
domain: ann-vector-search | security
props: hardness
tools: exchange-greedy
modeling: RBAC formalized as (U, R, D, UA, PA) with permissions as union over roles; index partitioning across the role hierarchy posed as a Mixed-Integer Nonlinear Program balancing memory against per-role search cost.
properties: The MINLP is NP-hard (combinatorial space, nonlinear constraints) — asserted, no reduction detailed in extract; a greedy heuristic spans strategies from post-filtering to per-role indices under memory budgets.
usage: Hardness licenses the greedy partitioning family; the formal RBAC model supplies the access constraints.
role: motivation — NP-hardness of the partitioning MINLP motivates the greedy strategy spectrum.
quote: "This problem is a Mixed-Integer Nonlinear Program (MINLP), which is NP-hard due to its combinatorial search space and nonlinear constraints."

### sigmod26-267 — ACGraph: An Efficient Asynchronous Out-of-Core Graph Processing Framework
domain: graph-db | caching-scheduling
props: lower-bound
tools: + none (thin extract)
modeling: Thin extract: no statements, an empty proof stub (noise), convergence signals likely from iterative computation. The only theory artifact is treating the OPT (full future knowledge) cache policy as a theoretical lower bound on synchronous disk-read volume.
properties: No proven bounds in extract; the OPT lower bound is invoked, not established here.
usage: OPT anchors comparison of cache replacement strategies across buffer sizes.
role: evaluation-yardstick — the OPT policy serves as a theoretical lower-bound baseline for disk reads.
quote: "As the OPT policy assumes full future access knowledge (albeit unrealistic), it serves as a theoretical lower bound for the disk read volume under synchronous execution."

### sigmod26-358 — Retrieve-and-Verify: A Table Context Selection Framework for Accurate Column Annotations
domain: data-integration | + column-annotation
props: + none-proven (definitional only)
tools: + none
modeling: Formalizes column type annotation (CTA) and column property annotation (CPA) as prediction tasks over a table, plus context verification: select the context subset S maximizing a quality score φ(S, t) for annotating target t.
properties: None proven; the argmax selection is the framework's formal objective.
usage: Definitions separate the annotation tasks from the context-selection problem the two-stage pipeline solves.
role: design-driver — the subset-selection formalization shapes the retrieve-and-verify framework.
quote: "Column context verification aims to identify the subset S that maximizes the quality score, i.e., S = argmax φ(S, t), where φ evaluates the effectiveness of S for annotating t."

### sigmod26-384 — WaveStitch: Flexible and Fast Conditional Time Series Generation With Diffusion Models
domain: time-series
props: correctness
tools: + none (elementary set-inclusion)
modeling: Defines solution sets by loss thresholds: real data (zero loss), δ-self-guidance set, δ-stitch set, and δ-conditional set, with conditional loss the sum of both and all losses non-negative.
properties: Proposition: X_real ⊆ X_cond^0 ⊆ X_cond^δ ⊆ X_self^δ — a chain of inclusions proved from non-negativity and the loss decomposition.
usage: The inclusion chain shows joint conditional training dominates its components — no trade-off between the two objectives.
role: design-driver — the nesting result justifies training on the combined conditional loss.
quote: "We have the following chain of inclusions: X_real ⊆ X_cond^0 ⊆ X_cond^δ ⊆ X_self^δ."

### sigmod26-312 — Fast Indexing for Temporal Information Retrieval
domain: indexing | + temporal-ir
props: + none-proven (cost-model framing)
tools: + none
modeling: Time-travel IR query formalized: return objects whose validity interval overlaps the query interval and whose description contains all query elements (set semantics). Slicing optimization: under a user-set cap on index-size growth from entry replication, minimize expected query processing cost. Noisy: statement embeds running-example prose (pdf-derived).
properties: No bounds proven in extract; the size/cost trade-off is an optimization framing.
usage: The cost model drives the choice of index slicing.
role: design-driver — constraint-bounded cost minimization shapes the index layout.
quote: "A time-travel IR query returns all objects in O whose interval overlaps with [q.t_start, q.t_end] and their description contains all elements in q.d."
