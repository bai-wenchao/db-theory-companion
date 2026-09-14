# sigmod26-127 — HeteroFedSyn: Differentially Private Tabular Data Synthesis for Heterogeneous Federated Settings

from=tex flag=True score=18 stmts=12 proofs=3 chars=107623
kinds: {"definition": 6, "theorem": 6}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 3, "big_o": 16, "omega": 1, "theta": 0, "approx_ratio": 0, "whp": 1, "regret": 0, "dp": 4, "invariant": 0, "convergence": 2, "competitive": 0, "worst_case": 4, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition .** ( ($ε$, $δ$)-Differential Privacy ). An algorithm $ M $ satisfies ($ε,δ$)-DP,where $ε, δ ≥ 0$, if and only if for any neighboring datasets $D$ and $D'$ that differ in one element, and any possible outputs $ R Range( M )$, we have \[ [ M (D) R ] ≤ e^ ε [ M (D') R ] + δ.\]

**Theorem .** ~ [cite] For any pair of attributes $(A_i, A_j)$, the KL divergence of conditional estimation is no larger than that of independent estimation: KL \! (P_ ij \,\|\, P_ ij ) \; \; KL \! (P_ ij \,\|\, P_i P_j ), where \[ P_ ij = Σ_ A P( A)\, P(A_i A)\,P(A_j A). \]

**Definition .** (Zero-Concentrated Differential Privacy (zCDP)). A randomized mechanism $ M $ satisfies $ $-zCDP with parameter $ > 0$ if, for all neighboring datasets $D$ and $D'$ differing in a single element, and for all $α > 1$, we have: \[ D_ α ( M (D) \| M (D')) ≤ α, \]

**Theorem .** (Unbiased estimation of $ InDif2 _ a,b $). $ \|z_ a,b -z_ a*b \|_2^2 - [ kασ_2^2 + ασ_1^2 (s_b\| M_a\|_2^2+s_a\| M_b\|_2^2 ) - s_a s_b α^2 σ_1^4 ]$ is an unbiased estimator of the square of $ InDif2 _ a,b $, where $α= Σ_i n_i^2 n^2 $.

**Definition .** (Gaussian Mechanism). Given a function \( f: D R ^d \), the Gaussian Mechanism adds Gaussian noise to ensure differential privacy. Specifically, the Gaussian Mechanism is defined as: \[ M (D) = f(D) + N (0, σ^2 I), \]

**Theorem .** (Privacy Guarantee for 2-Way Marginals) Let $ M_ a,b ^ c_i P_ a,b -M_ a,b ^ c_i' P_ a,b _2 _2, a,b \ 1,..., d\ , b>a, i \ 1,..., c\ $. Then for any $ _2>0$, $z_ a,b $ is $ _2$-zCDP if $σ_2 _2√ d(d-1) 4 _2 $.

**Definition .** (Composition of zCDP~ [cite] ) For a sequence of mechanisms \( M _i\) satisfying \( _i\)-zCDP for \(i = 1, 2, , k\), their composition $ M = ( M _1, M _2, , M _k)$ satisfies $Σ_ i=1 ^ k _i -zCDP $.

**Theorem .** (Privacy Guarantee for 1-Way Marginals). Let $ M_a^ c_i -M_a^ c_i' _2 _1, a \ 1,..., d\ $, $i \ 1,..., c\ $. Then for any $ _1>0$, $ M_a$ is $ _1$-zCDP if $σ_1 _1√ d 2 _1 $.

**Theorem .** (Bounding $ _2$). Let $ _2$ be the $ _2$ sensitivity for adding noise to the $2$-way marginals. We have \[ _2 max_ 1 i s_as_b √ Σ_ j=1 ^k P_ a,b [i, j]^2 \]

**Definition .** (zCDP to $(ε, δ)$-DP) If a mechanism \( M \) satisfies \( \)-zCDP, then it also satisfies \((ε, δ)\)-DP for any \(δ > 0\) and: \[ ε ≤ + 2√ log(1/δ) . \]

**Definition .** If a mechanism \( M : D R \) satisfies \((ε, δ)\)-DP, then for any function \(g: R R' \), the mechanism \( g M \) remains \((ε, δ)\)-DP.

**Theorem .** (Bounding $ _1$). Let $ _1$ be the $ _2$-sensitivity for adding noise to the $1$-way marginals. We have $ _1 1$.

## Proofs
**Proof.** Denote the count of items on attribute $a$ as $a_1,..., a_ s_a $. Assume that we add one sample to the dataset of participant $c_i$, the value of attribute $a$ belongs to the $j^ th $ item $a_j$. Additionally, the number of sample held by each participant $n_i$ should larger than $1$. Then we have & _1=max M_a^ c_i - M_a^ c_i' _2 \\ &=max √ Σ_ i=q, q≠ j ^ s_a ( a_q n_i - a_q n_i+1 )^2+( a_j n_i - a_j+1 n_i+1 )^2 \\ &=max √ Σ_ i=q, q≠ j ^ s_a a_q^2 n_i^2(n_i+1)^2 + (a_j-n_i)^2 n_i^2(n_i+1)^2 \\ &=max 1 n_i(n_i+1) √ Σ_ i=q ^ s_a a_q^2+n_i(n_i-2a_j) \\ & √ 2 n_i 1

**Proof.** Denote the count of items on attribute $a$, $b$ as $a_1,..., a_ s_a $ and $b_1,..., b_ s_b $, respectively. Then the domain size of $2$-way marginal on attribute $a$ and $b$ is $s_as_b$, denote the count of items as $c_1,...,c_ s_as_b $. Assume we add one sample to the $i^ th $ user's datasets, the value of attribute $a$ and $b$ belong to $i_0^ th $ and $j_0^ th $ items, respectively. We have _2&=max M_ a,b ^ c_i P_ a,b -M_ a,b ^ c_i' P_ a,b _2 \\ & max M_ a,b ^ c_i -M_ a,b ^ c_i' _2 _ 1 i s_as_b √ Σ_ j=1 ^k P[i, j]^2 (based on [cite] ) \\ &=√ Σ_ (i,j)≠(i_0,j_0) ( c_ i,j n_i - c_ i,j n_i+1 )^2+( c_ i_0,j_0 n_i - c_ i_0,j_0 +1 n_i+1 )^2 \\ & _ 1 i s_as_b √ Σ_ j=1 ^k P[i, j]^2 max_ 1 i s_as_b √ Σ_ j=1 ^k P[i, j]^2 .

**Proof.** We first recall the setup and notations. Each client $c_i$ has a dataset of size $n_i$ with $n=Σ_i n_i$. Each client sends the following to the server: 1-way marginals $n_i (M_a^ c_i +G_a^ c_i )$ with $G_a^ c_i ~ N(0,σ_1^2 I_ s_a )$; 2-way marginals $z_ a,b ^ c_i =n_i (M_ a,b ^ c_i P_ a,b +G_ a,b ^ c_i )$ with $G_ a,b ^ c_i ~ N(0,σ_2^2 I_k)$. Define $M_a = 1 n Σ_i n_i M_a^ c_i $, $G_a = 1 n Σ_i n_i G_a^ c_i $, $G_ a,b = 1 n Σ_i n_i G_ a,b ^ c_i $, and $α= Σ_i n_i^2 n^2 $. Then we have $$G_a~ N(0,ασ_1^2 I_ s_a ),$$ $$G_ a,b ~ N(0,ασ_2^2 I_k).$$ Server aggregates $$ M_a= 1 n Σ_i n_i(M_a^ c_i +G_a^ c_i )=M_a+G_a,$$ $$z_ a,b = 1nΣ_i z_ a,b ^ c_i =M_ a,b P_ a,b +G_ a,b .$$ We then analyze $E [\|z_ a,b -z_ a*b \|_2^2 ]$, where &z_ a,b -z_ a*b =(M_ a,b -M_a× M_b)P_ a,b \\ &+ (G_ a,b -(M_a× G_b)P_ a,b -(G_a× M_b)P_ a,b -(G_a× G_b)P_ a,b ). Since $G_a$, $G_b$, and $G_ a,b $ are independent, mean-zero Gaussians and independent of $P_ a,b $, we have & E [\|z_ a,b -z_ a*b \|_2^2 ]=E [\|(M_ a,b -M_a× M_b)P_ a,b \|_2^2 ]\\ &+ E [\|G_ a,b \|_2^2 ] + E [\|(M_a× G_b)P_ a,b \|_2^2 ] + E [\|(G_a× M_b)P_ a,b \|_2^2 ]\\ &+ E [\|(G_a× G_b)P_ a,b \|_2^2 ]. We then evaluate each variance term. We use two useful properties: $ E\|xP\|_2^2=\|x\|_2^2$ (Johnson-Lindenstrauss Lemma~ [cite] ), and $\|u× v\|_2^2=\|u\|_2^2·\|v\|_2^2$. Then we have $$ E\|(M_ a,b -M_a× M_b)P_ a,b \|_2^2=\|M_ a,b -M_a× M_b\|_2^2, $$ $$ E\|G_ a,b \|_2^2=kασ_2^2, $$ $$ E\|(M_a× G_b)P_ a,b \|_2^2 = E\|M_a× G_b\|_2^2 =\|M_a\|_2^2· E\|G_b\|_2^2 =\|M_a\|_2^2· s_bασ_1^2. $$ Similarly, $$ E\|(G_a× M_b)P_ a,b \|_2^2 =\|M_b\|_2^2· s_aασ_1^2, $$ $$ E\|(G_a× G_b)P_ a,b \|_2^2 = E\|G_a\|_2^2\, E\|G_b\|_2^2 =s_a s_bα^2σ_1^4. $$ Therefore, &E [\|z_ a,b -z_ a*b \|_2^2 ]=\|M_ a,b -M_a× M_b\|_2^2\\ &+kα\,σ_2^2+ασ_1^2 (s_b\|M_a\|_2^2+s_a\|M_b\|_2^2 ) + s_a s_b\,α^2σ_1^4. Since $ M_a = M_a + G_a$, we have $ E\| M_a\|_2^2=\|M_a\|_2^2+s_aασ_1^2$. Similarly, $ E\| M_b\|_2^2=\|M_b\|_2^2+s_bασ_1^2$. Therefore, we have &E [\|z_ a,b -z_ a*b \|_2^2 ] =\|M_ a,b -M_a× M_b\|_2^2\\ & +kα\,σ_2^2+ασ_1^2 (s_b E\| M_a\|_2^2+s_a E\| M_b\|_2^2 ) - s_a s_b\,α^2σ_1^4. The Unbiased estimator is $ InDif2 ^ 2 _ a,b = \|z_ a,b -z_ a*b \|_2^2 - [ kασ_2^2 + ασ_1^2 (s_b\| M_a\|_2^2+s_a\| M_b\|_2^2 ) - s_a s_b α^2 σ_1^4 ]$ where $α= Σ_i n_i^2 n^2 $, and we have $ E [ InDif2 ^ \,2 _ a,b ] =\|M_ a,b -M_a× M_b\|_2^2 = InDif2 _ a,b ^2.$

## Bound sentences
- Next, we provide the upper bound on the sensitivity $ _1$ of the $1$-way marginal in the:delta_1 .
- We provide an upper bound on the sensitivity $ _2$ in the:delta_2 .
