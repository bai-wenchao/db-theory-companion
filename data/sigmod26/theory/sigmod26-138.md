# sigmod26-138 — Improving Range Scan Performance in LSM-trees with Group Caching

flag=True score=5 stmts=0 proofs=2 chars=97873
kinds: {}
counts: {"np_hard": 0, "lower_bound": 5, "upper_bound": 3, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 1, "worst_case": 3, "sketch": 2, "cost_model": 0, "cardinality": 0, "learned": 1}

## Statements
## Proofs
**Proof.** Since 0 ≤ 𝑏𝑖 (𝑡) ≤ 1, we have 𝑏𝑖 (𝑡) (1 − 𝑏𝑖 (𝑡)) ≤ 𝑏𝑖 (𝑡). Thus ∑︁ ∑︁ 𝑉 ≤ 𝑠𝑖2𝑏𝑖 (𝑡) ≤ 𝑠 max 𝑠𝑖 𝑏𝑖 (𝑡) = 𝑠 max E𝑆 (𝑡). 𝑖 ∈𝐴 □

**Proof.** We prove the upper tail; the lower tail follows by applying the same argument to −𝑆 (𝑡) and then using a union bound. Map Theorem A.1 with 𝑍 = 𝑆 (𝑡) and 𝑌𝑖 = 𝑠𝑖 𝐵𝑖 (𝑡). By construction, the dependency graph degree satisfies Δ ≤ 𝐿 − 1. Moreover,  𝑌𝑖 − E𝑌𝑖 = 𝑠𝑖 𝐵𝑖 (𝑡) − 𝑏𝑖 (𝑡) ≤ 𝑠𝑖 ≤ 𝑠 max, so we can set 𝑏 = 𝑠 max . Using the quadratic form in Theorem A.1 with deviation 𝑡 = 𝜀 E𝑆 (𝑡) and writing 𝜇 = E𝑆 (𝑡) yields    𝜀2𝜇2  . P 𝑆 (𝑡) ≥ (1 + 𝜀)𝜇 ≤ exp − 2(Δ + 1) 𝑉 + 𝑠 max𝜀𝜇/3 By Lemma A.2 and Δ + 1 ≤ 𝐿,  2(Δ + 1) 𝑉 + 𝑠 max𝜀𝜇/3 ≤ 2𝐿 𝑠 max 𝜇 (1 + 𝜀/3). Substituting gives   P 𝑆 (𝑡) ≥ (1 + 𝜀)𝜇 ≤ exp −  𝜀2 𝜇 . 2𝐿 𝑠 max (1 + 𝜀/3) 2 The claimed upper-tail bound follows with 𝜃 = 2𝐿 𝑠max𝜀 (1+𝜀/3) . The lower tail is identical, and combining both tails with a factor of 2 completes the proof. □

## Bound sentences
