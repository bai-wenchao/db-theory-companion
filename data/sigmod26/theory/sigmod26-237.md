# sigmod26-237 — The Case For Language Model Approximated LIKE Predicate

flag=True score=3 stmts=1 proofs=0 chars=119700
kinds: {"theorem": 1}
counts: {"np_hard": 0, "lower_bound": 1, "upper_bound": 1, "big_o": 22, "omega": 0, "theta": 0, "approx_ratio": 3, "whp": 0, "regret": 0, "dp": 0, "invariant": 1, "convergence": 2, "competitive": 0, "worst_case": 4, "sketch": 0, "cost_model": 1, "cardinality": 31, "learned": 4}

## Statements
**Theorem 5.** 1 (Entropy of a LIKE Pattern). Given a LIKE pattern of length 𝑥 with 𝑝 underscore ("_") and 𝑞 percent ("%") wildcards over alphabet Σ, no two percent signs adjacent, and a maximum generated-string length of 𝑚, the pattern entropy 𝐻 (P) is: ! 𝑚−𝑥+𝑞 ∑︁ 𝑠 + 𝑞 − 1 𝑠 𝐻 (P) = 𝑝 ln |Σ| + ln |Σ| (2) 𝑞−1 𝑠=0 The proof is detailed in Appendix I.1.

## Proofs
## Bound sentences
- Within our framework, 𝑀 represents an abstracted upper bound on the total task complexity 𝐻 (W) that the model can reliably internalize.
- This leads to the following lower bound on the success probability:     𝑀 𝛼 |𝜃 | 𝑝 ≥ 𝑐 · min 1, = 𝑐 · min 1, (4) 𝐻 (W) 𝐻 (W) This assumption provides a tractable, albeit simplified, link between model scale and task complexity, enabling the derivation of sampling bounds.
