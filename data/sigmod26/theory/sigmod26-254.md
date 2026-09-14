# sigmod26-254 — Weighted Set Multi-Cover on Bounded Universe and Applications in Package Recommendation

from=tex flag=True score=24 stmts=14 proofs=4 chars=198664
kinds: {"definition": 3, "theorem": 4, "lemma": 7}
counts: {"np_hard": 1, "lower_bound": 0, "upper_bound": 0, "big_o": 122, "omega": 0, "theta": 0, "approx_ratio": 102, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 2, "learned": 0}

## Statements
**Lemma .** Given a parameter $ >0$, any continuous, convex and non-decreasing function $ (·): [α, β] [γ, δ]$, where $0<α≤ β$ and $0<γ≤ δ$, can be approximated by a continuous, convex non-decreasing piecewise linear function $ (·): [α, β] [γ, δ]$ having $O(log( δ γ )log^ -1 (1+ ))$ pieces, such that for every $α ≤ x ≤ β$, it holds that $ (x) ≤ (x) ≤ (1 + ε) (x)$. Moreover, the function $ (·)$ can be constructed in $O(log( δ γ ) ^ -1 (1+ )· T_ ^>· T_ ^=)$ time, where $T_ ^=$ is the time needed to calculate $ (x)$, for any $α x ≤ β$, and $T_ ^>$ is the time needed to compute the smallest value $x'≥ x $ such that $ (x')≤ (1+ ) ( x )$, for any values $ x , x'$ satisfying $α≤ x ≤ x'≤β$.

**Definition Weighted Set Multi-Cover problem with Bounded Universe --- \prob.** Let $ $ be a universe of $ =O(1)$ items, where each item $g $ is associated with non-negative demand $ _g$, and let $ $ be a family of $n$ sets where each set $t $ is defined as a subset of $ $, i.e., $t $, and it is associated with a non-negative weight $w_t$. The goal is to select a family of sets $ $ (each set in $ $ may be selected at most once in $ $) with minimum total weight such that every item $g $ is covered at least $ _g$ times. Formally, that is: minimize: & Σ_ t w_t \\ subject to: & |\ t g t\ |≥ _g, g \\ & .

**Definition Fair Minimum-Weight Cover problem --- \prob.** Given a set of weighted tuples $ $, a set of groups of interest $ $, and demands $ $, the objective is to select a result set $ $ such that the total sum of the weights of the selected tuples is minimized, subject to satisfying the demand constraints $ $. Formally, that is: minimize: & Σ_ t_i w_i \\ subject to: & |\ t_i g_j G_i\ |≥ _j, g_j \\ & .

**Definition \topkprob problem.** Given a dataset $ $ and an integer $k$, the objective is to select a result set $ $ consisting of $k$ tuples such that the total sum of the weights $w$ is maximized, subject to satisfying the demand constraints $ $ defined over a constant number of groups $ $. Formally, that is:

**Theorem .** Given an instance $( , )$ of the \ problem with $| |=n$ and $| |=O(1)$, and an arbitrary constant $ >0$, there exists a $(2+ )$-approximation algorithm for the \ problem that runs in $O(nlog n+ L (log(W)))$ time, where $W= Σ_ t w_t min_ t w_t $.

**Lemma .** (i) $ opt ≤ opt $. (ii) For every $H $, the function $ f _H(·)$ is a non-decreasing piecewise linear and convex function. (iii) Problem~ [ref] is equivalent to LP~ [ref] .

**Theorem .** Given an instance $( , )$ of the \ problem with $| |=n$ and $| |=O(1)$, there exists a $2$-approximation algorithm for the \ problem that runs in $O( L (n))$ time.

**Lemma .** For any arbitrary constant $ >0$, the algorithm runs in $O(nlog n + L (log (W)))$ time, where $W= Σ_ t w_t min_ t w_t $.

**Theorem .** If the optimal solution (OPT) selects $k$ sets, the naive greedy algorithm uses at most $| | · k$ sets.

**Theorem .** There exists an exact algorithm for the \ problem that runs in $O(n^ | |+1 )$ time.

**Lemma .** For all items $g $, it holds that $Σ_ H , g H e'_H ≥ Q_g$.

**Lemma .** For all $H $, it holds that $0 ≤ e'_H - x _H ≤ r$.

**Lemma .** Algorithm~ [ref] runs in $O( L (n))$ time.

**Lemma .** $Σ_ H f_H( x _H)≤ 2·(1+ )· $.

## Proofs
**Proof.** For (i), notice that $ f _H(x)=f_H(x)$ when $x Z $, while the function $f_H(x)$ is not defined for $x Z $. Furthermore, the constraints of IP~ [ref] and its relaxed Problem~ [ref] are the same. For every $H $, let $x_H^*$ be the value of the variable $x_H$ in the optimum solution optimum of IP~ [ref] . By definition, $ opt ≤ Σ_ H f _H(x_H^*)=Σ_ H f_H(x_H^*)= opt $. We show (ii). The function $ f _H$ is continuous since $ _ x z^- f _H(x)= _ x z^+ f _H(x)= f _H(z)$, for every $z Z $. The function $ f _H$ is piecewise linear because for every interval $z≤ x<z+1$ for a $z Z $, the function is defined as a linear function with respect to $x$. Finally, we show that $ f _H$ is convex showing that the slopes of the linear functions are non-decreasing. We fix $H $. For every $i \ 1,…, |B(H)|\ $, let $α_i$ be the slope of $ f _H$ in the $i$-th interval $z≤ x<z+1$, i.e., $i-1≤ x<i$. By definition $α_i=f_H(i)-f_H(i-1)$. Recall the definition of $f_H(i)$: It is the sum of weights of the $i$ sets in $B(H)$ with the smallest weights. Hence $α_i$ is defined as the $i$-th smallest weight among the weights of the sets in $B(H)$, i.e., $a_i=w_ H,i $ for every $i [|B[H]|]$. Thus, $α_1≤ α_2≤ …≤ α_ |B(H)| $, proving that the function $ h _H$ is convex. Since $ f _H$ is piecewise linear, convex and every slope $α_i≥ 0$, it also follows that it is non-decreasing. An example of a function $ f _H$ is shown in Figure~ [ref] . For iii), we show that LP~ [ref] and Problem~ [ref] are equivalent. For each $H $, let $ x _H$ be the value of variable $x_H$ on an optimum solution of Problem~ [ref] , and let $ Y =Σ_ H f _H( x _H)$ be the value of the objective function. We show that there exists a feasible solution in LP~ [ref] with an objective value equal to $ Y $. For every $H $, let $ (H)= x _H $. For every $i \ 1,2,…, (H)\ $ we set $ x _ H,i =1$, for every $i \ (H)+2,…, |B(H)|\ $ we set $ x _ H,i =0$, while for $i= (H)+1$ we set $ x _ H, (H)+1 = x _H- (H)$. Notice that, by definition, for every $H $, $ x _H=Σ_ i [|B(H)|] x _ H,i $. Hence, all constraints in LP~ [ref] hold. Furthermore, for any $H $, we have $ f _H( x _H)=(f_H( (H)+1)-f_H( (H)))· ( x _H- (H))+f_H( (H))=w_ H, (H)+1 · x _ H, (H)+1 +Σ_ i [ (H)] w_ H,i =Σ_ i [|B(H)|] w_ H,i · x _ H,i $. Thus, $Σ_ H Σ_ i [|B(H)|] w_ H,i · x _ H,i = Σ_ H f _H( x _H)= Y $. Next, we show the other direction: For each $H $ and $i [|B(H)|]$, let $ x _ H,i $ be the value of variable $x_ H,i $ an optimum solution of LP~ [ref] , and let $ Y =Σ_ H Σ_  …

**Proof.** Recall that by definition, $e_H = max\ x _H, _H\ $ and $e'_H = min\ e_H, x _H + r\ $. Thus, we have $e'_H = min\ max\ x _H, _H\ , x _H + r\ $. Hence, we have $e'_H ≥ x _H$ and $e'_H ≤ x _H + r$, for all $H $. The lemma follows.

**Proof.** By definition, both the fractional vector $ x _ H $ and the optimal solution vector $ _ H $ satisfy all the demands. More formally, for any $g $ we have $Σ_ H , g H x _H ≥ Q_g$, and Σ_ H , g H _H ≥ Q_g . Recall that $r = Σ_ H ( x _H - x _H) $, and since $ x _ H $ covers all the demands, for any $g $ we have $r + Σ_ H , g H x _H ≥ Q_g$. Intuitively, if we take $ x _H$ sets from $B(H)$ for all $H $, then for any item $g $, we need at most $r$ additional sets to satisfy its demand. By definition, $e'_H = min\ max\ x _H, _H\ , x _H + r)\ $. Thus, for all $H $, we have e'_H ≥ x _H. Moreover, by definition, we have H : e'_H = x _H + r, & if _H > x _H + r, \\[4pt] e'_H ≥ _H, & if _H ≤ x _H + r. Let $g $, be any arbitrary item. There are 2 different cases. (i) For all sets $H $, such that $g H$, it holds that $ _H ≤ x _H + r$. In this case, for all $H $ such that $g H$, we have that $e'_H ≥ _H$, by the second condition of ( [ref] ). Therefore, we get Σ_ H , g H e'_H ≥ Σ_ H , g H _H ≥ Q_g, as desired in this case. The last inequality holds by ( [ref] ). (ii) There exists a set $H' $, such that $g H'$ and $ _ H' ≥ x _ H' + r$. In this case, by the first condition of ( [ref] ), we have $e'_ H' = x _ H' + r$. Moreover, for all $H $, it holds that $e'_H ≥ x _H$, by ( [ref] ). Thus, we get $Σ_ H , g H e'_H ≥ r + Σ_ H , g H x _H ≥ Q_g$, as desired. Thus, the lemma follows in both cases.

**Proof.** The LP~ [ref] has $O(n)$ variables and constraints (Lemma~ [ref] ), so its optimum solution is computed in $O( L (n))$ time. Then we bound the time for the rounding procedure. For all $H $, we have $ x _H - x _H < 1$, and hence $r = Σ_ H ( x _H - x _H) ≤ 2^ $. Since there are $2^ $ different buckets and from each bucket we consider at most $r$ sets (with the smallest weight), the rounding step takes $O(r^ 2^ ) = O((2^ )^ (2^ ) ) = O(1)$ time. Although one might argue that $O(r^ 2^ )$ represents a large constant that could slow down the rounding procedure in practice, in Section~ [ref] we show that $r$ is typically quite small in practice. Overall, the algorithm runs in $O( L (n))$ time.

## Bound sentences
- Bredereck et al.~ [cite] , showed that the weighted set multi-cover problem is fixed parameter tractable, when parameterized by the size of the universe, implying that \ is not NP-hard.
- The classical greedy algorithm achieves an $O(log )$-approximation~ [cite] , which is asymptotically optimal~ [cite] .
