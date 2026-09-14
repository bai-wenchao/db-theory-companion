# sigmod26-221 — SHoTClean: Bridging Soft and Hard Constraints for Multivariate Time Series Cleaning

flag=True score=7 stmts=2 proofs=2 chars=101924
kinds: {"theorem": 2}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 2, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 8, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 3, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Theorem 2.1.** (Optimality of DAG Solution). Let P ∗ be the maximum-weight path in the constructed DAG. Then the corresponding repaired time series X′P ∗ is exactly the optimal solution of arg minX′ Δ(X, X′ ).

**Theorem 4.1.** The regret 𝑅𝑛 of the online algorithm has a theoretical upper bound.

## Proofs
**Proof.** We prove the theorem through three steps below. i) Bijection between Paths and Cleaned Sequences. Let P = (𝑖 0, 𝑖 1, . . . , 𝑖𝑚 ) be any path in the 𝑘 −1 DAG, give the cleaned sequence X′P : ∀𝑗 ∈ (𝑖𝑘 −1, 𝑖𝑘 ), x′𝑗 = x𝑖𝑘 −1 + 𝑖𝑗𝑘−𝑖 −𝑖𝑘 −1 (x𝑖𝑘 − x𝑖𝑘 −1 ). Conversely, any X′ satisfying the hard constraint determines a unique path PX′ . Thus {feasiable X′ } ←→ {𝑝𝑎𝑡ℎ𝑠 P}. ii) Monotonicity of Cost and Weight. Define the interpolation error for any segment (𝑖𝑘 −1, 𝑖𝑘 ) Í 𝑘 −1 Í is Δ(𝑖𝑘 −1, 𝑖𝑘 ) = 𝑖𝑗=𝑖 ||x 𝑗 − x′𝑗 || 2 , so the cost of P is Δ(X, X′P ) = 𝑚 𝑘=1 Δ(𝑖𝑘 −1, 𝑖𝑘 ). Similarly, the 𝑘 −1 +1 Í weight of P is W (P) = 𝑚 𝑠 · 𝛾 (𝑖 − 𝑖 ), with 𝑠 > 0 and 𝛾 (·) strictly decreasing. 𝑖 𝑖 𝑘 𝑘 −1 𝑘 𝑘=1 𝑘 For any 𝑎 < 𝑏 < 𝑐, Δ(𝑎, 𝑐) ≥ Δ(𝑎, 𝑏) + Δ(𝑏, 𝑐), and ΔW = 𝑠𝑏 · 𝛾 (𝑏 − 𝑎) + 𝑠𝑐 · 𝛾 (𝑐 − 𝑏) − 𝑠𝑐 · 𝛾 (𝑐 − 𝑎) > 0. Hence inserting an anchor 𝑏 decreases total cost and strictly increases total weight, e.g., Δ(X, X′P+𝑏 ) < Δ(X, X′P ) and W (P+𝑏 ) > W (P). iii) Equivalence of Objectives. Let P ∗ be a maximum-weight path. If there were P̂ with Δ(X, X′ ) < Δ(X, X′P ∗ ), the step (2) would force W ( P̂) > W (P ∗ ), contradicting the maximality P̂ of P ∗ . Similarly, any strictly higher-weight path than P ∗ would necessarily yield a strictly lower Δ, which is likewise impossible. Therefore, arg minX′ Δ(X, X′ ) = {X′P | P ∈ arg max P ′ W (P ′ )}. □

**Proof.** Let 𝑆𝑛off and 𝑆𝑛on denote the total scores of the offline and online algorithms. The regret is defined as 𝑅𝑛 = 𝑆𝑛off − 𝑆𝑛on . Suppose the offline algorithm connects node x𝑘 ∗ to node x𝑜𝑔 . If 𝑘 ∗ − 𝑜𝑔 ≤ 𝑊 , the online algorithm has access to x𝑘 ∗ and incurs no regret. However, if 𝑘 ∗ − 𝑜𝑔 > 𝑊 , the online algorithm cannot access x𝑘 ∗ and must instead choose some 𝑘ˆ ∈ (𝑜𝑔, 𝑖]. The one-step regret is therefore 𝑟𝑜𝑔 = 𝑠𝑜𝑔 · [𝛾 (𝑘 ∗ − 𝑜𝑔) − 𝛾 (𝑘ˆ − 𝑜𝑔)] ≤ 𝑠𝑜𝑔 · 𝛾 (𝑊 + 1) ≤ 𝑒 −𝛽 (𝑊 +1) . Thus, the total regret 𝑅𝑛 is the sum of individual regrets: 𝑛 𝑛 ∑︁ ∑︁ 𝑅𝑛 = 𝑟≤ 𝑒 −𝛽 (𝑊 +1) = 𝑛 · 𝑒 −𝛽 (𝑊 +1) . (7) 𝑖=1 𝑖=1 Proc. ACM Manag. Data, Vol. 4, No. 1 (SIGMOD), Article 84. Publication date: February 2026. SHoTClean: Bridging Soft and Hard Constraints for Multivariate Time Series Cleaning 84:11 Overall, the average per-step regret is bounded by 𝑅𝑛𝑛 ≤ 𝑒 −𝛽 (𝑊 +1) , indicating that the online algorithm’s performance converges exponentially to that of the offline optimum as 𝑊 increases. □

## Bound sentences
