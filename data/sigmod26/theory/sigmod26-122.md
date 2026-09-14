# sigmod26-122 — GoodTP: An Effective Data Selection Framework for Enhancing Trajectory Similarity Learning via Monte Carlo Tree Search

flag=True score=3 stmts=0 proofs=1 chars=104106
kinds: {}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 4, "omega": 0, "theta": 0, "approx_ratio": 2, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 8, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
## Proofs
**Proof.** We establish equivalence through bijective mapping between solution spaces. (1) Forward Direction (S → 𝜶 ): Given any feasible solution S ⊆ T with |S| = 𝐵, we construct the | S∩T | corresponding sampling strategy by defining 𝛼𝑖 = | T𝐶 𝐶|𝑖 . This construction ensures: (i) 𝛼𝑖 ∈ [0, 1] Í𝑚 𝑖 Í by definition since S∩T𝐶𝑖 ⊆ T𝐶𝑖 , (ii) the constraint 𝑖=1 𝛼𝑖 |T𝐶𝑖 | = 𝑚 |S| = 𝐵 is satisfied 𝑖=1 |S∩T𝐶𝑖 | = Ð due to the partition property, and (iii) objective preservation follows since S = 𝑚 𝑖=1 (SÍ∩ T𝐶𝑖 ). 𝑚 (2) Backward Direction (𝜶 → S): Given any sampling strategy 𝜶 satisfying the constraint 𝑖=1 𝛼𝑖 |T𝐶𝑖 | = Ð𝑚 Í𝑚 𝐵, the solution is S = 𝑖=1 Sample(T𝐶𝑖 , 𝛼𝑖 ). The constraint ensures |S| = 𝑖=1 ⌊𝛼𝑖 |T𝐶𝑖 |⌋ ≈ 𝐵 (exact equality when all 𝛼𝑖 |T𝐶𝑖 | are integers), and objective function preservation follows directly from the construction. (3) Bijectivity: The above two mappings are inverses of each other up to sampling randomness, establishing bijective correspondence between solution spaces. □

## Bound sentences
