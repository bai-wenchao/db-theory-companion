# sigmod26-047 — CoDec: Prefix-Shared Decoding Kernel for LLMs

from=tex flag=False score=2 stmts=0 proofs=0 chars=111901
kinds: {}
counts: {"np_hard": 2, "lower_bound": 1, "upper_bound": 2, "big_o": 6, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
## Proofs
## Bound sentences
- In this section, we first formulate the optimization problem of task division and scheduling, which is np-hard, and propose a heuristic solution through pruning.
- The above problem is an advanced parallel task scheduling problem~ [cite] , which is NP-hard.
- This monotonicity and the inequality in Equation~ [ref] can be used to determine the lower bound of the cost (denoted as $cost_l$) through binary search.
- Therefore, we can narrow down the search space by setting the upper bound of the division number of each KV cache node as [display] where $C_ est (n_q[i], n[i])$ is the estimated execution time defined in Section~ [ref] .
- Moreover, we formulate the optimization problem of task division and scheduling, unfortunately, it is NP-hard.
