# sigmod26-143 — KVD rive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference

from=tex flag=False score=2 stmts=0 proofs=0 chars=97681
kinds: {}
counts: {"np_hard": 1, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 2, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
## Proofs
## Bound sentences
- Given a total GPU cache budget $M$, the objective is: \[ max_ \ w_ l,h \ Σ_ l,h Benefit _ l,h (w_ l,h ) s.t. Σ_ l,h Cost _ l,h (w_ l,h ) ≤ M. \] This allocation problem is a variant of the multiple-choice knapsack problem (MCKP), which is NP-hard in general.
