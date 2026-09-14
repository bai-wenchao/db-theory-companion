# sigmod26-197 — PTO: A Workload-driven Predictive Table Optimizer for Lakehouse Systems

flag=False score=0 stmts=0 proofs=0 chars=98374
kinds: {}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 3, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 3, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 7, "learned": 0}

## Statements
## Proofs
## Bound sentences
- The reason for observing case (a) consistently is that 95% tail is long enough for sort cluster size estimation using Good Turing heuristic to converge earlier (i.e., below 0.1% upper bound of sample rate for all the SF 10K tables). 3.2.5 Discretizing TFS and RGS.
- (2) FIXED SAMPLING : We take the upper bound of the sampling rate (0.1%) used in our GoodTuring implementation and repurpose it as fixed sampling rate on each table to measure the number of sort clusters and average distinct sort cluster size.
