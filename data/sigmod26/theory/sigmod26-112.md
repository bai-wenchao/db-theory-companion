# sigmod26-112 — FLEA: Frequency-based Lossless Encoding Algorithm for Periodic Time Series

flag=True score=3 stmts=0 proofs=1 chars=79943
kinds: {}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 4, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 9, "cardinality": 0, "learned": 0}

## Statements
## Proofs
**Proof.** The squared magnitude of 𝑅𝑘 = 𝑛1 (13) 𝑗𝑘 𝑗=0 𝜖 𝑗 𝜔𝑛 is given by: Í𝑛−1 𝑛−1 1 ∑︁ 𝜖 𝑗 𝜔𝑛𝑗𝑘 |𝑅𝑘 | = 2 𝑛 𝑗=0 2 ! 𝑛−1 ∑︁ ! 𝜖𝑙∗𝜔𝑛−𝑙𝑘 . 𝑙=0 Taking the expectation and applying the uncorrelated error assumption, which implies E[𝜖 𝑗 𝜖𝑙∗ ] = 0 for 𝑗 ≠ 𝑙 and E[|𝜖 𝑗 | 2 ] = |𝜖 𝑗 | 2 (since 𝜖 𝑗 is deterministic for a given input), all off-diagonal terms vanish: 𝑛−1 𝑛−1 1 ∑︁ ∑︁ E[𝜖 𝑗 𝜖𝑙∗ ]𝜔𝑛𝑗𝑘 𝜔𝑛−𝑙𝑘 E[|𝑅𝑘 | 2 ] = 2 𝑛 𝑗=0 𝑙=0 = 𝑛−1 ∑︁ 𝑛−1 1 1 ∑︁ 2 𝑗𝑘 − 𝑗𝑘 |𝜖 | 𝜔 |𝜖 𝑗 | 2 . 𝜔 = 𝑗 𝑛 𝑛 𝑛 2 𝑗=0 𝑛 2 𝑗=0 □

## Bound sentences
