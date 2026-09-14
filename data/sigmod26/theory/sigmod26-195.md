# sigmod26-195 — Prism: Private Relational Data Synthesis with Language Models

flag=True score=16 stmts=0 proofs=8 chars=102855
kinds: {}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 24, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 1, "sketch": 0, "cost_model": 0, "cardinality": 6, "learned": 0}

## Statements
## Proofs
**Proof.** For any token 𝜏, let 𝑐 and 𝑐˜ represent its true and noisy vote counts, respectively. Recall that 𝑐˜ = 𝑐 + N (0, 𝜎 2 ), a random variable 𝑋 = 𝑐˜ 𝜎−𝑐 has a distribution of standard Gaussian, i.e., 𝑋 ∼ N (0, 1). Let Φ(·) be the CDF of 𝑋 . Given the threshold 𝜃 , Case 1: False positive. If 𝑐 < 𝜃 and 𝑐˜ > 𝜃 , 𝑐˜ − 𝑐 𝜃 −𝑐 𝜃 −𝑐 𝜃 −𝑐 > ) = Pr(𝑋 > ) = 1 − Φ( ) 𝜎 𝜎 𝜎 𝜎 Case 2: False negative. If 𝑐 > 𝜃 and 𝑐˜ < 𝜃 , Pr(𝑐˜ > 𝜃 ) = Pr( Pr(𝑐˜ < 𝜃 ) = Pr( Therefore, Equation (2) holds. 𝑐˜ − 𝑐 𝜃 −𝑐 𝜃 −𝑐 𝜃 −𝑐 < ) = Pr(𝑋 < ) = Φ( ) 𝜎 𝜎 𝜎 𝜎 □

**Proof.** Disjoint teacher partitions imply that one tuple change affects at most one teacher’s vote, changing both the max and the min by at most 1; hence the difference of their gap is at most 2. Since 𝑟 (·) outputs a scalar, its ℓ2 sensitivity equals this bound. □

**Proof.** Let 𝑒𝜏 be the standard basis √ vector for coordinate 𝜏. One vote change yields Δ𝑐𝑡 of the form 𝑒𝜏𝑏 − 𝑒𝜏𝑎 (valid→valid, norm 2), 𝑒𝜏𝑏 (invalid→valid, norm 1), or −𝑒𝜏𝑎 (valid→invalid, norm √ 1). The worst case is 2. □

**Proof.** By Lemma 2, the ℓ2 sensitivity is Δr = 2. Applying the Gaussian RDP formula (6) yields the result. □

**Proof.** √By Lemma 3, the histogram sensitivity is Δh = 2. Since 𝜎𝑡h is fixed given 𝐻𝑡 , the RDP 2 ( 2) 𝛼 cost is 𝛼2(𝜎 h ) 2 = (𝜎 h ) 2 . 𝑡 □

**Proof.** RDP composes additively under adaptive dependence, because the histogram noise scale 𝜎𝑡h is a deterministic function of the privatized history 𝐻𝑡 , while the range noise 𝜎 r is fixed. □

**Proof.** Consider the distillation mechanism of Prism that, at each round, queries all 𝑘 teachers and accumulates privacy cost under RDP until the target budget is reached. Let 𝑄 denote the total number of token-query rounds executed before the privacy budget is exhausted. By Corollary 1 and the adaptive composition rule of RDP, the overall mechanism satisfies 𝜀 (𝛼)-RDP, where 𝜀 (𝛼) is defined in (7). Applying the standard conversion from RDP to (𝜀, 𝛿)-DP (8) yields that the transcript H = (𝑟˜1, 𝑐˜1, . . . , 𝑟˜𝑄 , 𝑐˜𝑄 ) satisfies (𝜀 (𝛿), 𝛿)-differential privacy for the training dataset 𝐷. □

**Proof.** By Theorem 1, the distillation mechanism of Prism satisfies (𝜀 (𝛿), 𝛿)-differential privacy for the training dataset 𝐷, and produces a privatized transcript H = (𝑟˜1, 𝑐˜1, . . . , 𝑟˜𝑄 , 𝑐˜𝑄 ). All subsequent operations in Algorithm 1, including thresholding, probabilistic sampling, detokenization, student training, and synthetic data generation, depend solely on H . Since differential privacy is preserved under arbitrary post-processing [22], these steps incur no additional privacy cost. Therefore, the overall mechanism that maps the private dataset 𝐷 to the released synthetic dataset 𝐷˜ satisfies (𝜀 (𝛿), 𝛿)-differential privacy, completing the proof. □

## Bound sentences
