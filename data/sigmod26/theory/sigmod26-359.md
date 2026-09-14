# sigmod26-359 — SAQ: Pushing the Limits of Vector Quantization through Code Adjustment and Dimension Segmentation

from=tex flag=True score=6 stmts=2 proofs=1 chars=100826
kinds: {"lemma": 2}
counts: {"np_hard": 0, "lower_bound": 4, "upper_bound": 1, "big_o": 12, "omega": 0, "theta": 0, "approx_ratio": 9, "whp": 2, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Lemma Estimator and Error Bound.** The estimator of inner product is unbiased because : E ( o _p, q _p ) = o _p, q _p o _p, o _p . With a probability of at least $1-exp(-c_0ε_0^2)$, the error bound of the estimator satisfies P \ | o _p, q _p' o _p, o _p' - o _p', q _p' | > √ 1 - o _p, o _p' ^2 o _p, o _p' ^2 · ε_0 √ D - 1 \ ≤ 2e^ -c_0 ε_0^2 where $c_0$ is a constant and $ε_0$ is a parameter that controls the probability of failure of the bound.

**Lemma .** $ D _ CAQ $ of CAQ is equivalent to $ G _r$ in RaBitQ.

## Proofs
**Proof.** From Lines 6-11 of Algorithm [ref] , the dimensions of $ x $ take values from $ \ -v_ max + · (i + 0.5) i [2^ B - 1] \ $. Thus, we have $$ D _ CAQ = \ -v_ max + · (i + 0.5) i [2^ B - 1] \ ^ D . $$ With $ = 2 · v_ max / 2^B$, dividing the vectors in $ D _ CAQ $ by $v_ max $ gives $ \ -(2^B -1)/ 2 + i \, | \, i [2^ B - 1] \ ^D$, which matches the unnormalized codebook $ G $ of RaBitQ in Eq.~ [ref] . The normalization only changes the norm of the codewords but not the direction, and we have discussed that the norms of the codewords do not affect the estimated inner product.

## Bound sentences
- With >99.9\% probability, we have $ε < 2^ -B · c_ ε / √ D $ where $c_ ε =5.75$ This is asymptotically optimal as the error scales with $2^ -B $.
- Instead, approximate distance estimates or distance bounds can filter out most unlikely candidates (e.g. if a lower bound exceeds the current best NN distance).
- Moreover, we can even obtain a lower bound of the estimated distance with almost no computation.
- We can use $ Est _v( Seg )$ to predict a lower bound of the contribution of each stage to the final inner product with confidence $1- 1 m^2 $.
- As $m$ increases, the confidence in the lower bound distance produced by the estimator increases, though it is likely that candidates are pruned.
- Observing that padding yields inferior accuracy, extended RabitQ (E-RabitQ) uses codewords on the unit sphere after projection and is shown to be asymptotically optimal in accuracy~ [cite] .
