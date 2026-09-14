# sigmod26-080 — Dynamic Flat Filter: A Unified Framework for Scalable and Stable Fingerprint-Based Filters

flag=False score=2 stmts=0 proofs=0 chars=96114
kinds: {}
counts: {"np_hard": 0, "lower_bound": 1, "upper_bound": 1, "big_o": 0, "omega": 3, "theta": 1, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 6, "sketch": 1, "cost_model": 0, "cardinality": 1, "learned": 0}

## Statements
## Proofs
## Bound sentences
- Therefore, when amortized over a segment’s 𝑚 · 𝑏 slots (and normalized by the load factor 𝛼), the directory contributes only a small bits-per-key overhead under typical segment sizes—typically below 0.1 bits-per-key in our experiments (§6.8). 5.2 False Positive Rate We now derive an upper bound on t …
- This matches the asymptotic stability achieved by InfiniFilter and Aleph Filter and is consistent with the Ω(log log 𝑛) lower bound for dynamic approximate membership [38]. 5.3 Time Cost We evaluate the time complexity of operations in DFF by considering the segment-local cost and the directory rout …
