# sigmod26-355 — Reliable and Private Utility Signaling for Data Markets

from=tex flag=True score=25 stmts=12 proofs=6 chars=130566
kinds: {"definition": 5, "theorem": 5, "lemma": 2}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 1, "big_o": 11, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 2, "regret": 0, "dp": 1, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 1, "learned": 0}

## Statements
**Definition .** (Collision-Resistance) Let $ H : \ 0,1\ ^* \ 0,1\ ^n $ be a function that maps an input of arbitrary length to a fixed-length output of $n$-bits. The function $ H $ is said to be collision-resistant if for any probabilistic polynomial-time (PPT) adversary $ A $, the probability of finding a collision is negligible. Formally: $$ [ x_1 ≠ x_2 H(x_1) = H(x_2) \;|\; (x_1, x_2) A (1^λ) ] ≤ negl (λ), $$ where $ λ $ is the security parameter. $ negl (λ) $ denotes a negligible function, a function that decreases faster than the inverse of any polynomial. $ A (1^λ) $ denotes the adversary $ A $ running in probabilistic polynomial time with access to the security parameter $ 1^λ $.

**Definition .** (Utility Signaling) Given a selling dataset $ D $ from a data seller $m$, a test dataset $ T $ from a data buyer used to benchmark utility, and a utility evaluation function $f$, a utility signaling mechanism $ M $ is formally characterized as M : f( D , T ), where $ $ is the utility of $ D $ evaluated on $ T $ according to $f$. $ M $ determines whether $ $ is disclosed to the buyer, the seller, or both.

**Definition .** [cite] $F$ is hazard rate dominated by $F_0$ if \[ 1 - F(p) f(p) < 1 - F_0(p) f_0(p) , p supp (F) supp (F_0), \] where $ supp (F)$ denotes the support of distribution $F$.

**Theorem .** Given total number of data blocks be $k$, number of falsified blocks be $t$, number of challenged blocks be $c$, $ HashVeri _ AP $ achieves $( t k ,1-( k-t k )^c)$-AoI.

**Theorem .** If $u(b) < u_0(b)$, then $$ P _ buyer, DT _ M ^ true (p^*) > P _ buyer, DT _ - ^ true (p^*_0)$$ under the assumption of Lemma [ref] .

**Lemma .** Assume $1 - F_0$ and $1 - F$ are log-concave, and $F$ is hazard rate dominated by $F_0$, if $u(b) < u_0(b)$, then $p^* < p^*_0$.

**Definition .** Given secret-shared input dataset $ D $ and $ T $, the MPC-based utility calculation protocol is defined as: _ f ( D , T )

**Definition .** ($(α,β)$-AoI) Given seller falsifies $α$ ratio data blocks, the $ HashVeri $ output $False$ with at least $β$ probability.

**Theorem .** If $p$ is fixed and $ $ is given to the buyer, then $$ P _ buyer, DT _ M ' ^ true P _ buyer, DT _ - ' ^ true .$$

**Theorem .** If $u(b) > u_0(b)$, then $$ P _ seller, DT _ M ^ true (p^*) > P _ seller, DT _ - ^ true (p_0^*).$$

**Lemma .** The seller's payoff maximization problem [ref] has a unique solution if $1 - F_0$ is log-concave.

**Theorem .** $ P _ seller, DT _ M ^b ^ true 0, P _ buyer, DT _ M ^b ^ true 0$.

## Proofs
**Proof.** The first order condition of problem [ref] is 1 - F_0(p) - pf_0(p) = 0. So if $p - 1 - F_0(p) f_0(p) $ is monotonically increasing, problem [ref] has a unique solution, which equals to d (p - 1 - F_0(p) f_0(p) ) d p = 2f^2_0(p) + f'_0(p)(1 - F_0(p)) f^2_0(p) ≥ 0. If $1 - F_0$ is log-concave, which means $log(1 - F_0)$ is concave, which implies that d ^2 log (1 - F_0(p)) d p^2 = - f^2_0(p) + f'_0(p)(1 - F_0(p)) (1 - F_0(p))^2 ≤ 0. It's obvious that [ref] implies [ref] , so the seller's payoff maximization problem [ref] has a unique solution if $1 - F_0$ is log-concave.

**Proof.** If $u(b) > u_0(b)$, then the probability that $u(b) < p$ is smaller than the probability that $u_0(b) < p$, $ p, F(p) < F_0(p)$, so $ P _ seller, DT _ M (p_0^*) > P _ seller, DT _ - (p_0^*)$. Furthermore, by the optimality definition of $p^*$, we can derive that $ P _ seller, DT _ M (p^*) ≥ P _ seller, DT _ M (p_0^*) > P _ seller, DT _ - (p_0^*)$.

**Proof.** Under the log-concave property of $1 - F_0$ and $1 - F$, the pricing solutions $p_0^*$ and $p^*$ emerge as unique payoff maximizers for optimization problems [ref] and [ref] respectively, thus satisfying first order conditions \[p_0^* = 1 - F_0(p_0^*) f_0(p_0^*) , p^* = 1 - F(p^*) f(p^*) .\] Given $F$ is hazard rate dominated by $F_0$, $ 1 - F(p_0^*) f(p_0^*) < 1 - F_0(p_0^*) f_0(p_0^*) = p_0^*$, $p_0^* - 1 - F(p_0^*) f(p_0^*) > 0$. The log-concavity of $1 - F$ ensures the mapping $ (p) := p - 1 - F(p) f(p) $ maintains strict monotonicity. Combining this with $ (p^*) = 0$, we establish that $p^* < p_0^*$.

**Proof.** Under the assumption of Lemma [ref] , the relationship $p^* < p^*_0$ holds. We systematically examine four mutually exclusive and collectively exhaustive scenarios: ; $u_0(b) ≥ p_0^*, u(b) ≥ p^*$: In this case, both mechanisms induce data purchase, but $ DT_ M $ achieves strictly higher buyer utility through price reduction, $ P _ buyer, DT _ M (p^*) > \\ P _ buyer, DT _ - (p^*_0)$; ; $u_0(b) < p_0^*, u(b) < p^*$: In this case, transaction failure occurs under both mechanisms, yielding identical zero utilities; ; $u_0(b) ≥ p_0^*, u(b) < p^*$: In this case, because $u(b) < p^* < p^*_0$, $ DT_ M $ prevents loss-making transactions that would occur in the basic case $ DT_ - $, thereby improving utility: $ P _ buyer, DT _ M (p^*) > P _ buyer, DT _ - (p^*_0)$; ; $u_0(b) < p_0^*, u(b) ≥ p^*$: In this case, the buyer would not buy data in basic case $ DT_ - $ with utility $0$, but would buy data in $ DT_ M $ with non-negative utility, so we have $ P _ buyer, DT _ M (p^*) ≥ P _ buyer, DT _ - (p^*_0)$. The above four cases are collectively exhaustive, given that case 1 occurs with positive measure, we can derive that $ P _ buyer, DT _ M (p^*) > P _ buyer, DT _ - (p^*_0)$.

**Proof.** Note that the price in $ DT _ M '$ would remain the same as $ DT _ - '$ since the seller's information remains unchanged. Given $p$, we examine two mutually exclusive and collectively exhaustive scenarios: ; When $u_0(b) ≥ p$ ( $ P _ buyer, DT _ - ' ≥ 0$), the buyer decides to purchase in the basic case. Since $u( ,b)$ is non-decreasing and $p$ is positive, there exists $ ^*$ such that $u( ^*,b) < p $, which leads to $ P _ buyer, DT _ - ' ^ true ( ^*) < 0$. Since the buyer with a signal $ ^*$ will refuse to purchase and her true payoff will be zero, it holds that $ P _ buyer, DT _ M ' ^ true ( ^*)> P _ buyer, DT _ - ' ^ true ( ^*) $. For other cases where $u( ,b) p $, the buyer's decision remains the same, so is their true payoff. ; When $u_0(b) < p$ ( $ P _ buyer, DT _ - ' < 0$), the buyer refuses to purchase in the basic case. Thus, $ P _ buyer, DT _ - ' ^ true = 0$. Similar as situation (1), there exists $ ^*$ such that $u( ^*,b) p $, which leads to $ P _ buyer, DT _ M ' ^ true ( ^*) > P _ buyer, DT '_ - ^ true ( ^*) = 0$. For other cases where $u( ,b) < p $, the buyer's decision remains the same, so is their true payoff. The above two cases are collectively exhaustive, we can derive that $ P _ buyer, DT '_ M ^ true > P _ buyer, DT '_ - ^ true $.

**Proof.** We compute $P(X)$, the probability that at least one of the blocks selected by $I$ corresponds to a block falsified by the seller. P_X &= P\ X ≥ 1\ = 1 - P\ X = 0\ \\ &= 1 - k-t k · k-1-t k-1 · k-2-t k-2 … k-c+1-t k-c+1 . Since $ k-i-t k-i ≥ k-i-1-t k-i-1 $, it follows that: 1 - ( k-t k )^c &≤ P_X ≤ 1 - ( k-c+1-t k-c+1 )^c. This implies that if the seller falsifies $t$ blocks of data, the buyer has a probability of at least $1 - ( k-t k )^c$ to detect this misbehavior after challenging $c$ blocks.

## Bound sentences
- Malicious checking To ensure a malicious security guarantee, many techniques can be used to enhance LSS with checking procedures ( based on Information-theoretic MACs [cite] ).
- We observe that FullPto exhibits a linear growth in runtime, establishing the performance upper bound as expected.
- ACM-Reference-Format sample [display] Frequently Used Notations We summarize the frequently used notations in Tab. [ref] . -0in [display] MAC Checking To check for malicious deviations, we describe a MAC checking mechanism that enhance secret sharing with information-theoretic MACs, as used in SPDZ- …
