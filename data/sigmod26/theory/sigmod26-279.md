# sigmod26-279 — Benchmarking Differentially Private Tabular Data Synthesis: [Experiments & Analysis]

from=tex flag=True score=14 stmts=12 proofs=0 chars=168471
kinds: {"definition": 3, "theorem": 6, "lemma": 3}
counts: {"np_hard": 0, "lower_bound": 1, "upper_bound": 0, "big_o": 6, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 7, "invariant": 0, "convergence": 4, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 1, "learned": 0}

## Statements
**Theorem .** For any pair of attributes $(A_i, A_j)$, the KL divergence error of conditional estimation is always no larger than that of independent estimation. Formally, we have ( [A_i, A_j] \|\; [A_i, A_j] . ) ≤ ( [A_i, A_j] \|\; [A_i] [A_j] . ) Here $ [A_i, A_j]$ is defined in Equation~( [ref] ).

**Definition R\'enyi DP~\cite{mironov2017renyi.** We say that an algorithm $ A $ satisfies $(α, )$-R\'enyi DP ($(α, )$-RDP) if and only if for any two neighboring datasets $D$ and $D'$ \[ D_ α ( A (D)|| A (D')) ≤ , \] where $D_ α (Y||N) = 1 α-1 ln E _ x ~ N [ Y(x) N(x) ]^ α $.

**Definition Differential Privacy.** An algorithm $ A $ satisfies $( ,δ)$-differential privacy ($( ,δ)$-DP) if and only if for any two neighboring datasets $D$ and $D'$ and any $T Range ( A )$, we have $$ A (D) T ≤ e^ \, A (D') T + δ. $$

**Theorem Composition.** Let $f: D R _1$ be $(α, _1)$-RDP and $g: R _1 × D R _2$ be $(α, _2)$-RDP respectively. Then the mechanism defined as $(X,Y)$, where $X ~ f(D)$ and $Y ~ (D, f(D))$, satisfies $(α, _1 + _2)$-RDP.

**Lemma .** Assuming that \[ P_1(z) = Σ_x p(x)P_1(z|x) \;\;\; and \;\;\; P_2(z) = Σ_x p(x)P_2(z|x), \] we have \[ (P_1(z) \;\|\; P_2(z) ) ≤ Σ_x p(x) (P_1(z|x) \;\|\; P_2(z|x) ) \]

**Definition Sensitivity.** Let $f: D R ^k$ be a vector-valued function of the input data, then the $ _2$ sensitivity of $f$ is defined as \[ _f = max_ D D' f(D) - f(D') _2 \]

**Theorem Post-Processing.** Let $f: D R _1$ is $(α, )$-RDP, and $g: R _1 R _2$ is an arbitrary randomized mapping. Then $g f$ is also $(α, )$-RDP.

**Theorem .** If $f$ is an $(α, )$-RDP mechanism, then it also satisfy $ ( + log 1/δ α - 1 , δ )$-DP for any $0 < δ < 1$.

**Lemma .** For any $α > 1$, rare value merge satisfies $(α, α _2 )$-R\'enyi differential privacy.

**Theorem .** The Exponential Mechanism defined above satisfies $ (α, α ε^2 8 )$-RDP for $ α > 1$.

**Lemma .** For any $α > 1$, PrivTree satisfy $(α, α _1 )$-R\'enyi differential privacy.

**Theorem .** The Gaussian Mechanism defined above satisfies $ (α, α 2 σ^2 )$-RDP.

## Proofs
## Bound sentences
- Formally, this method can be expressed as $ Uniform Bin (x) = x - x_ h $, where $x_ $ is the lower bound of the attribute's domain, and $h$ is the length of the uniform interval determined by the bin number.
