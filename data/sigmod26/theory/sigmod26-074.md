# sigmod26-074 — DimWeaver: Dimensional Weaved Trajectory Compression

flag=False score=2 stmts=0 proofs=0 chars=89876
kinds: {}
counts: {"np_hard": 0, "lower_bound": 2, "upper_bound": 2, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 12, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 2, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
## Proofs
## Bound sentences
- Considering the 𝑋 dimension, each segment is initially represented by both its upper and lower bound lines (Figure 4) in the form of a tuple: (𝑡𝑠 , 𝑥𝑠𝑙𝑜𝑤𝑒𝑟 , 𝑣𝑙𝑜𝑤𝑒𝑟 , 𝑥𝑠𝑢𝑝𝑝𝑒𝑟 , 𝑣𝑢𝑝𝑝𝑒𝑟 ) Here, 𝑥𝑠𝑙𝑜𝑤𝑒𝑟 and 𝑥𝑠𝑢𝑝𝑝𝑒𝑟 denote the starting points at 𝑡 = 𝑡𝑠 of the upper and lower lines.
- Each resulting group 𝑖 is defined by a new interval [𝑣𝑙𝑜𝑤𝑒𝑟𝑖 , 𝑣𝑢𝑝𝑝𝑒𝑟𝑖 ], where 𝑣𝑙𝑜𝑤𝑒𝑟𝑖 is the maximum lower bound among the group’s segments, and 𝑣𝑢𝑝𝑝𝑒𝑟𝑖 is the minimum of upper bound.
- For each point, it maintains a score that serves as an upper bound on the SED for its neighboring points.
