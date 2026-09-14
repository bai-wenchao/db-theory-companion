# sigmod26-318 — Gem: Scalable Monotonic Graph Processing Beyond Billion-Scale on a Single Machine

flag=False score=1 stmts=0 proofs=0 chars=115496
kinds: {}
counts: {"np_hard": 0, "lower_bound": 9, "upper_bound": 9, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 16, "competitive": 0, "worst_case": 0, "sketch": 116, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
## Proofs
## Bound sentences
- The upper bound 𝑈 𝐵(𝑠𝑟𝑐 → 𝑣) is a close estimate that is greater than or equal to 𝐷𝐼𝑆𝑇 (𝑠𝑟𝑐 → 𝑣).
- The lower bound 𝐿𝐵(𝑠𝑟𝑐 → 𝑣) is a close estimate that is less than or equal to 𝐷𝐼𝑆𝑇 (𝑠𝑟𝑐 → 𝑣).
- Triplion uses the triangle inequality to compute the upper bound as 𝑈 𝐵(𝑠𝑟𝑐 → 𝑑𝑒𝑠𝑡) = 𝐷𝐼𝑆𝑇 (𝑠𝑟𝑐 → ℎ) + 𝐷𝐼𝑆𝑇 (ℎ → 𝑑𝑒𝑠𝑡), based on precomputed distances to hub vertices.
