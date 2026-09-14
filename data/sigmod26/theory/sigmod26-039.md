# sigmod26-039 — Breadcrumb Filters: Fast Fully Featured Filters

flag=False score=1 stmts=0 proofs=0 chars=102468
kinds: {}
counts: {"np_hard": 0, "lower_bound": 2, "upper_bound": 0, "big_o": 0, "omega": 3, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 4, "convergence": 0, "competitive": 0, "worst_case": 4, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
## Proofs
## Bound sentences
- This suggests the following open problem: For space-efficient filters, do you have to sacrifice performance to support enumerability? 1 Space efficiency of a filter is the ratio of its size and the information-theoretic lower bound, i.e. the space efficiency of a filter instance of size 𝑆 bits with  …
- The numerator, 𝑛 log 𝜀 −1 , represents the information-theoretic minimum space required [17], while the denominator reflects the actual space used.
- All the filter designs we consider (except the Bloom filter with 1.44𝑛 log 𝜀 −1 space usage) incur an overhead of Ω(𝑛) bits beyond the lower bound.
