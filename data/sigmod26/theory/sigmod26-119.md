# sigmod26-119 — GEM: A Native Graph-based Index for Multi-Vector Retrieval

from=tex flag=False score=2 stmts=1 proofs=0 chars=291377
kinds: {"definition": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 4, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 5, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 3, "competitive": 0, "worst_case": 0, "sketch": 4, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition Similarity score.** Given two sets of vectors $A, B R ^d$, the similarity score is defined as the sum of the maximum similarity between each vector in $A$ and all vectors in $B$. Formally, CH (A, B) = Σ_ a A max_ b B Sim (a, b), where cosine similarity or $L_2$ distance are typically used as the default choices for $ Sim (·, ·)$ in prior work.

## Proofs
## Bound sentences
- Consider a search path that is currently at vertex $P_1$, then the distance from $P_1$ to its neighbor $P_2$ has a predictable upper bound: $CH(Q, P_2) ≤ EMD(Q, P_2) ≤ EMD(Q, P_1) + EMD(P_1, P_2)$.
