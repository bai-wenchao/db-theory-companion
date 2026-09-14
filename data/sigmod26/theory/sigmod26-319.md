# sigmod26-319 — GenJoin: Conditional Generative Plan-to-Plan Query Optimizer that Learns from Subplan Hints

from=tex flag=False score=1 stmts=0 proofs=0 chars=118582
kinds: {}
counts: {"np_hard": 0, "lower_bound": 1, "upper_bound": 0, "big_o": 5, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 1, "sketch": 0, "cost_model": 2, "cardinality": 9, "learned": 6}

## Statements
## Proofs
## Bound sentences
- When considering inference time as a variable amount of time with a lower bound (e.g., because the encoding requires an EXPLAIN call that is on the order of 50 milliseconds), then the LQO should improve the execution time by at least the same amount to not become slower than the classical optimizer.
