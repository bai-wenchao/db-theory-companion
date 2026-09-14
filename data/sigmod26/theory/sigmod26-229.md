# sigmod26-229 — Stress-Testing Causal Claims via Cardinality Repairs

from=tex flag=True score=15 stmts=8 proofs=3 chars=267264
kinds: {"proposition": 3, "definition": 3, "theorem": 1, "lemma": 1}
counts: {"np_hard": 2, "lower_bound": 0, "upper_bound": 7, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 5, "sketch": 0, "cost_model": 1, "cardinality": 12, "learned": 0}

## Statements
**Definition Tuple Influence.** The influence of a tuple $t $ on the ATE of $T$ on $O$ is defined as: \[ influence (t) = ATE_ (T, O) - ATE_ \ t\ (T, O) \] where $T$ and $O$ denote the treatment and outcome variables, respectively, and $ATE_ (T, O)$ represents the ATE of $T$ on $O$ computed over the dataset $ $, while adjusting for confounding variables (omitted from the notation for clarity).

**Lemma .** Consider a database $ $ and its identifier augmentation $ _2$. For every set of tuples $I \ 1,…, n\ $, there exists a pattern $ _I$ such that $ ( _I)=I$.

**Definition DB Causality \cite{meliou2010causality.** Let $t ^n$ be an endogenous tuple, and $r$ a possible answer to query $q$.

**Proposition .** Problem [ref] and Problem [ref] are NP-complete for AVG and ATE.

**Definition \brit{TODO: Give a name.** Let $t _d^n$ be an endogenous tuple, $T $ is and $t_i (T)$ is

**Theorem .** The pattern-deletion problem is NP-complete for AVG and ATE.

**Proposition .** The \ problem is NP-complete.

**Proposition .** Problem [ref] is NP-complete.

## Proofs
**Proof.** [Proof of Lemma [ref] ]

**Proof.** [Proof of Proposition [ref] ] We show a reduction from SUBSET-SUM to the decision version of . Recall that in SUBSET-SUM we are given a set of numbers $S = \ x_1, …, x_n\ $ and a target $k$, and the problem is to decide whether there exists a subset $S' S$ such that $Σ_ x S' x = k$. Recall that in \ we are given a database instance $ $ over a schema $ $, a binary treatment variable $T $, an outcome variable $O $, a desired value $ATE_d$ and $ε>0$. In the decision version of this problem we are also given an additional bound $n$, and we need to decide whether there is a subset of tuples $ $ s.t. $| | n$ and it holds that $ATE_ (T,O) [ATE_d - ε, ATE_d + ε]$. We turn to describe the reduction. See xmp:reduction subset sum for an example. Given a SUBSET-SUM instance $(S, k)$, we define an instance of \ as follows: The schema $ $ is defined as $ = \ T,O\ $ (i.e., there are no confounding variables). For each element $x S$, we add to $ $ two corresponding tuples $t_x^1$ and $t_x^2$ with the following values: ; $t_x^1[T] = 1, t_x^1[O] = x$ ; $t_x^2[T] = 0, t_x^2[O] = 0$ In addition, we add to $ $ the tuple $t$ where $t[T] = 1$ and $t[O] = - k$. We set the target ATE to $ATE_d=0$ and set $ε = 0$, i.e., we must reach exactly the target ATE of $0$. Finally, we bound on the allowed number of tuples to delete to be at most $|S|$. Clearly the reduction can be implemented in polynomial time. We turn to show correctness. ($ $) Assume the SUBSET-SUM instance has a solution $S' S$. We remove from $ _d$ all tuples $t_x^1$ for $x S'$ (intuitively, we retain only the $t_x^1$ tuples that are in $S'$). Note that since $|S'| |S|$, we are within the allowed number of deleted tuples. We claim that the ATE after this removal is $0$. Indeed, we have $AVG(O|T= 0) = 0$ (since all the tuples with $T=0$ have $O=0$), and since $Σ_ x S' x=k$, then $AVG(O|T=1)=(-k+Σ_ x S' x)/(|S'|+1)=(-k+k)/(|S'|+1)=0$ (accounting for the remaining tuples with $T=1$). It follows that the resulting ATE is $0$. ($ $) Assume that the instance of our problem is solvable, with a deleted set of tuples $ $. Intuitively, we do not care about deleted tuples where $t[T] = 0$, as these tuples also have $t[O]=0$ and do no affect the ATE. Denote by $ '$ the set of deleted tuples with $t[T]=1$. Since the new ATE is $0$, and since the contribution of $t[T]=0$ tuples is $0$, it follows that after deleting the $ '$, the average of the tuples with $t[T]=1$ is $0$, and therefore also the sum. Since $S$ contains only non-nega …

**Proof.** Define the pattern $ _I= _ i I S_i=0$. We claim that $ ( _I)=I$. Indeed, for $i I$ we have that $t_i(S_j)=0$ for all $j≠ i$, and in particular for all $j I$. Therefore $i ( _I)$. Conversely, let $i ( _I)$, then $t_i(S_j)=0$ for all $j I$. Since $t_i(S_i)=1$, it follows that $i I$.

## Bound sentences
- Given a desired causal estimate $ATE_d$ and a threshold $ε > 0$, find a minimal size subpopulation defined by a pattern $ $ such that: $$ATE_ ( ) (T,O) [ATE_d -ε, ATE_d + ε]$$ In order to analyze the complexity of the problems, we implicitly refer to their decision-problem versions, where an upper b …
- To nevertheless assess how closely \ approximates the optimal solution, we designed controlled experiments using synthetic data where an upper bound on the number of deletions is known, thus bounding the search space OPT.
- We then injected 20\% noisy records into the data, making the number of noisy tuples an upper bound on the solution size.
- Both algorithms produced solutions smaller than the upper bound for up to 1.3k noisy tuples.
- Proof of prop:problem_is_np_hard_pattern We now turn to prove prop:problem_is_np_hard_pattern , showing that prob:patterns is NP-hard.
- We can assume without loss of generality that there are no confounding variables, as the problem remains NP-hard in this case, as we show in the proof of prop:problem_is_np_hard (this assumption only simplifies the writing, but has no meaningful impact on the construction).
- To nonetheless evaluate how close \ comes to the optimal solution in large scale data, we designed experiments using synthetic data where an upper bound on the number of tuples to remove is known.
- In this setup, the number of inserted noisy tuples serves as an upper bound on the number of deletions required to reach the target ATE.
- Up to 1300 noisy tuples, all algorithms found solutions smaller than the upper bound, indicating high accuracy.
