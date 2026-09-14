# sigmod26-167 — NeurBench: A Benchmark Suite for Learned Database Components with Drift Modeling: [Experiments & Analysis]

flag=True score=4 stmts=1 proofs=1 chars=114089
kinds: {"theorem": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 1, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 3, "learned": 46}

## Statements
**Theorem 1.** The controlled reverse distribution 𝑝 (x𝑡 −1 |x𝑡 , xdrift ) is able to be approximated using Pr(xdrift |x𝑡 ) and its gradient at x𝑡 , or ∇x𝑡 Pr(xdrift |x𝑡 ).

## Proofs
**Proof.** For Equation (3), the first part is approximated by a Gaussian model, while the second part can be simplified using conditional independence, which transforms the equation to: 𝑝 (x𝑡 −1 |x𝑡 , xdrift ) ≈ 𝑧N (x𝑡 ; 𝝁, Σ)Pr(xdrift |x𝑡 ), where 𝑧 is the normalizing factor. Next, as proven by Dickstein et al. [50], we can perform Taylor expansion around 𝝁 to further approximate 𝑝 (x𝑡 −1 |x𝑡 , xdrift ) so that a perturbed Gaussian distribution can be used to model it: log 𝑝 (x𝑡 −1 |x𝑡 , xdrift ) ≈ log N (x𝑡 ; 𝝁, Σ) + log Pr(xdrift |x𝑡 ) 1 ≈ − (x𝑡 − 𝝁) ⊤ Σ−1 (x𝑡 − 𝝁) + (x𝑡 − 𝝁) · 𝑔 + 𝐶 2 1 = − (x𝑡 − 𝝁 − Σ · 𝑔) ⊤ Σ−1 (x𝑡 − 𝝁 − Σ · 𝑔) + 𝐶 2 = log N (x𝑡 ; 𝝁 + Σ · 𝑔, Σ), where 𝑔 = ∇x𝑡 Pr(xdrift |x𝑡 ), and the constant term 𝐶 can be ignored. In other words, 𝑝 (x𝑡 −1 |x𝑡 , xdrift ) can be approximated by N (x𝑡 ; 𝝁 + Σ · ∇x𝑡 Pr(xdrift |x𝑡 ), Σ). □

## Bound sentences
