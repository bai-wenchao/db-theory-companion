# sigmod26-321 — GraphMatch: Subgraph Query Processing on Steroids

flag=False score=1 stmts=0 proofs=0 chars=90963
kinds: {}
counts: {"np_hard": 0, "lower_bound": 1, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 9, "sketch": 0, "cost_model": 0, "cardinality": 2, "learned": 0}

## Statements
## Proofs
## Bound sentences
- We propose GraphMatch, a hardware-accelerated subgraph query processing system based on worst-case optimal joins (WCOJ).
- In related work, there are two main approaches to this workload: backtracking[16, 70] and join-based subgraph query processing [2, 53] that employ worst-case optimal joins (WCOJs).
- Join-based Subgraph Query Processing Worst-case optimal joins (WCOJ), as shown in Algorithm 1, guarantee a runtime complexity in the worst-case output cardinality of the algorithm [32, 55, 67].
- Compact path index ✓ ✓ ✓ ✓ ✓ ✓ Candidate space ✓ ✓ ✓ ✓ ✓ ✓ Compact embedding cluster index ✓ ✓ ✓ ✓ ✓ ✓ Trie ✓ ✓ ✓ ✓ ✓ ✓ Adjacency lists ✓ ✓ ✓ ✓ ✓ ✓ Encoded trie ✓ ✓ ✓ ✓ ✓ ✓ Adjacency lists ✓ ✓ ✓ ✓ ✓ ✓ Compressed sparse row ✓ ✓ ✓ ✓ ✓ ✓ Partitioned compressed sparse row ✓ ✓ ✓ ✓ ✓ ✓ Compressed sparse r …
- Overall, we observe that with 80% cache hit rate, the performance reaches the same baseline for each number of input sets, thereby denoting a lower bound set by the cycles the hardware needs to perform the intersection itself.
- We preserve the worst-case optimal number of intermediate results.
