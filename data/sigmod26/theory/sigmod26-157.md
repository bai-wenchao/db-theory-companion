# sigmod26-157 — Mathematical Foundations of Poisoning Attacks on Linear Regression over Cumulative Distribution Functions

flag=True score=27 stmts=8 proofs=9 chars=92101
kinds: {"theorem": 6, "lemma": 1, "observation": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 53, "big_o": 70, "omega": 0, "theta": 0, "approx_ratio": 2, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 10, "sketch": 5, "cost_model": 0, "cardinality": 3, "learned": 44}

## Statements
**Theorem 1.** Observation 1 always holds. In other words, the optimal single-point attack P ∗ satisfies: P ∗ ⊂ {𝑘 + 1 | 𝑘 ∈ K} ∪ {𝑘 − 1 | 𝑘 ∈ K}. (7) To prove Theorem 1, we first establish the following key lemma. Proc. ACM Manag. Data, Vol. 4, No. 3 (SIGMOD), Article 208. Publication date: June 2026. 208:8 Atsuki Sato, Martin Aumüller, and Yusuke Matsui

**Lemma 1.** Let X be the set of keys stored in the index, with 𝑚 = |X| ≥ 3, and let 𝑥 1 ≤ 𝑥 2 ≤ · · · ≤ 𝑥𝑚 denote the elements of X in increasing order. Then, for each 𝑖 ∈ {2, 3, . . . , 𝑚 − 1},  sign 𝑑𝐸𝑑𝑥( X) is non-decreasing over the interval 𝑥𝑖 ∈ (𝑥𝑖 −1, 𝑥𝑖+1 ), and there exists at most one 𝑖 = 0. Here, the function sign(𝑥) is defined as −1 if value of 𝑥𝑖 in this interval for which 𝑑𝐸𝑑𝑥( X) 𝑖 𝑥 < 0, 0 if 𝑥 = 0, and 1 if 𝑥 > 0.

**Observation 2.** The iterative greedy approach (Algorithm 2) does not guarantee an optimal multi-point poisoning attack. Figure 3 provides an illustrative example where the greedy approach does not lead to the optimal solution. As shown in the previous section, for the single-point attack case, the optimal solution can be found by exhaustively evaluating all integers adjacent to the legitimate keys (Figure 3a). The greedy poisoning method of [28] performs a two-point attack by adding one additional optimal poison key on top of this (Figure 3b). However, the true optimal two-point attack involves adding poison keys as shown in Figure 3c. Thus, the greedy poisoning method does not always yield the optimal solution. This finding is valuable for preventing confusion among future researchers, as [28] reports the following: “Even though we do not provide a proof of optimality for the multiple-point poisoning, we experimentally observed that our approach matched the performance of the brute-force attack in every tested dataset.” Next, we establish the following theorem, which characterizes the structure of the optimal solution for multi-point attacks. This result can be seen as an extension of Theorem 1.

**Theorem 2.** The optimal multi-point attack consists only of poison keys that are either adjacent to legitimate keys directly or connected transitively to legitimate keys via chains of neighboring poison keys. Formally, the optimal multi-point attack P ∗ satisfies: ∀𝑝 ∈ P ∗, ∃𝑘 ∈ K, {min(𝑝, 𝑘) + 1, . . . , max(𝑝, 𝑘) − 1} ⊂ P ∗ . (9) Proc. ACM Manag. Data, Vol. 4, No. 3 (SIGMOD), Article 208. Publication date: June 2026. 208:10 Atsuki Sato, Martin Aumüller, and Yusuke Matsui

**Theorem 3.** The optimal solution P ∗ to the Relaxed Poisoning Problem is a multiset over K, i.e., Supp(P ∗ ) ⊂ K, where Supp denotes the support of the multiset.

**Theorem 4.** The optimal solution 𝒅 ∗ to the Relaxed Poisoning Problem satisfies ∗ 𝑖=1 𝑑𝑖 = 𝜆. Í𝑛

**Theorem 5.** For fixed 𝒅, min𝑏 L (K ⊎ Q K (𝒅); 𝑤, 𝑏) is a convex quadratic function of 𝑤.

**Theorem 6.** For fixed 𝑤 > 0, the choice of 𝒅 (subject to 𝑛𝑖=1 𝑑𝑖 = 𝜆) that maximizes min𝑏 L (K ⊎ Q K (𝒅); 𝑤, 𝑏) is characterized as follows: • If 𝑤 (𝑘𝑛 − 𝑘 1 ) < 𝑛 + 𝜆, all poison points are concentrated on a single key; that is, ∃𝑖 ∈ {1, 2, . . . , 𝑛} such that 𝑑𝑖 = 𝜆. • Otherwise, all poison points are concentrated at the endpoints 𝑘 1 and 𝑘𝑛 ; that is, 𝑑 1 +𝑑𝑛 = 𝜆.

## Proofs
**Proof.** Lemma 1 implies that either 𝐸 (K ∪ {𝑝 ∗ − 1}) or 𝐸 (K ∪ {𝑝 ∗ + 1}) is greater than 𝐸 (K ∪ {𝑝 ∗ }). 𝑝 that maximizes the loss in each interval lies at either endpoint of the interval. Specifically, the optimal single-point attack in this case is P = {12}, which aligns with Observation 1. Based on this observation, [28] proposed the following single-point attack algorithm: exhaustively evaluating 𝐸 (K ∪ {𝑝}) for every candidate poison point 𝑝 (i.e., integers adjacent to legitimate keys). The algorithm is summarized in Algorithm 1. By employing differential calculation, this evaluation can be performed in time O (𝑛). However, [28] did not prove the optimality of this algorithm. Multi-point poisoning attack. For multi-point attacks, [28] iteratively applies the above singlepoint attack 𝜆 times, see Algorithm 2. The time complexity of this multi-point poisoning algorithm is O ((𝑛 + 𝜆)𝜆). Empirically, they report that this greedy approach results in an optimal attack, again missing a formal proof. 4 Optimality of Single-Point Poisoning Attack We theoretically guarantee the optimality of the single-point attack proposed in [28] by proving the following theorem.

**Proof.** Computing sign (𝑑𝐸 (X)/𝑑𝑥𝑖 ) shows that it equals the sign of the covariance between 𝒙 ′ and 𝒓 ′ , where 𝒙 ′ and 𝒓 ′ denote the vectors obtained from 𝒙 and 𝒓, respectively, by removing their 𝑖-th elements (i.e., 𝑥𝑖 and 𝑖). Since both 𝒙 ′ and 𝒓 ′ are monotonically increasing, the sign of covariance is positive. □

**Proof.** To facilitate comprehension of the proof structure, an illustrative figure is presented in Figure 2. Assume, for the sake of contradiction, that there exists an optimal single-point attack P ∗ = {𝑝 ∗ } such that 𝑝 ∗ ∉ {𝑘 + 1 | 𝑘 ∈ K} ∪ {𝑘 − 1 | 𝑘 ∈ K}. Let 𝑖 ∈ {2, 3, . . . , 𝑛} be the unique index satisfying 𝑘𝑖 −1 < 𝑝 ∗ < 𝑘𝑖 . Under our assumption, the integers adjacent to 𝑝 ∗ are not legitimate keys, meaning 𝑘𝑖 −1 < 𝑝 ∗ − 1 and 𝑝 ∗ + 1 < 𝑘𝑖 (see Figure 2). Since 𝑝 ∗ is assumed to be an optimal single poison point, we have: 𝐸 (K ∪ {𝑝 ∗ −1}) ≤ 𝐸 (K ∪ {𝑝 ∗ }) ∧ 𝐸 (K ∪ {𝑝 ∗ }) ≥ 𝐸 (K ∪ {𝑝 ∗ +1}).  According to Lemma 1, the function sign 𝑑𝐸 ( K∪{𝑝 } ) 𝑑𝑝  (8) is non-decreasing over the interval 𝑝 ∈ 𝑑𝐸 ( K∪{𝑝 } ) (𝑘𝑖 −1, 𝑘𝑖 ), and there exists at most one point 𝑝 in this interval where = 0. Therefore, 𝑑𝑝 the behavior of 𝐸 (K ∪ {𝑝}) over 𝑝 ∈ (𝑘𝑖 −1, 𝑘𝑖 ) must fall into one of the following three cases: (i) strictly increasing, (ii) strictly decreasing, or (iii) strictly decreasing over (𝑘𝑖 −1, 𝑝 ′ ) and strictly increasing over (𝑝 ′, 𝑘𝑖 ) for some 𝑝 ′ ∈ (𝑘𝑖 −1, 𝑘𝑖 ). In all cases, either 𝐸 (K ∪ {𝑝 ∗ − 1}) > 𝐸 (K ∪ {𝑝 ∗ }) or 𝐸 (K ∪ {𝑝 ∗ }) < 𝐸 (K ∪ {𝑝 ∗ + 1}). This contradicts the assumption that 𝑝 ∗ is optimal. □

**Proof.** Lemma 2 implies that 𝐸 (K ∪ P− ) or 𝐸 (K ∪ P+ ) is greater than 𝐸 (K ∪ P ∗ ). 5.1 Structure of Optimal Multi-Point Attacks

**Proof.** To facilitate comprehension of the proof structure, an illustrative figure is presented in Figure 4. First, we prove an extension of Lemma 1, denoted Lemma 2 (in Appendix B of the full version [46]), which implies that if there exists an isolated block of consecutive poison keys (an Isolated Poison Block), then moving that block either left or right can strictly increase the loss. Applying the same argument as in Theorem 1, but with an Isolated Poison Block instead of a single poison key, yields Theorem 2. □

**Proof.** The proof is analogous to that of Theorem 2: if there exists poison points outside of K, we can increase the loss by shifting them to the keys within K. □

**Proof.** We first prove Lemma 3 (in Appendix C of the full version [46]), which states that in the relaxed setting, there exists some 𝑖 ∈ {1, 2, . . . , 𝑛} such that adding a poison at 𝑥𝑖 increases the loss. This implies that using the full poisoning budget is optimal. □

**Proof.** For fixed 𝑤, the optimal 𝑏 ∗ can be solved in closed form, and substituting it shows the loss is a quadratic function in 𝑤 with positive quadratic coefficient. □

**Proof.** When 𝑤 (𝑘𝑛 − 𝑘 1 ) < 𝑛 + 𝜆, for any 1 ≤ 𝑖 < 𝑗 ≤ 𝑛 with 𝑑𝑖 , 𝑑 𝑗 ≥ 1, moving a poison from 𝑖 to 𝑗, or from 𝑗 to 𝑖, always increases the loss. When 𝑤 (𝑘𝑛 − 𝑘 1 ) ≥ 𝑛 + 𝜆, for any 2 ≤ 𝑖 ≤ 𝑛 − 1 with 𝑑𝑖 ≥ 1, moving a poison from 𝑖 to 1, or from 𝑖 to 𝑛, always increases the loss. □

## Bound sentences
