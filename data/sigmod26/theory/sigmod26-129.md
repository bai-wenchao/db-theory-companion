# sigmod26-129 — HIRE: A Hybrid Learned Index for Robust and Efficient Performance under Mixed Workloads

from=tex flag=False score=2 stmts=0 proofs=0 chars=194813
kinds: {}
counts: {"np_hard": 0, "lower_bound": 3, "upper_bound": 0, "big_o": 10, "omega": 0, "theta": 0, "approx_ratio": 3, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 5, "sketch": 0, "cost_model": 7, "cardinality": 0, "learned": 54}

## Statements
## Proofs
## Bound sentences
- At each internal node, consults both the primary child list and a small log of newly added child node pointers to identify the lower-bound candidate node whose key range provides the tightest lower bound for the $k_q$.
- Between the candidate node ending at 90 (from the log) and the one ending at 82 (from the primary list), the latter provides a tighter lower bound for the key 56 and is selected for the next step in the traversal.
