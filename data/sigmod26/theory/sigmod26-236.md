# sigmod26-236 — Task Cascades for Efficient Unstructured Data Processing

from=tex flag=True score=7 stmts=3 proofs=1 chars=142145
kinds: {"theorem": 2, "lemma": 1}
counts: {"np_hard": 1, "lower_bound": 0, "upper_bound": 2, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 3, "whp": 1, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 3, "cardinality": 0, "learned": 0}

## Statements
**Lemma Corollary to \Cref{thm:guarantees} by \cite{waudby2024estimating.** Consider the $i$-th cascade threshold set $ t _i$ and the corresponding Bernoulli random variables $X^i$ with $|X^i|=k$. If $ Acc _D( t _i)<T$ and for a confidence parameter $α [0, 1]$, P ( E ( t , D_V)=True)≤ α, where E ( t _i, D_V)= I [ j [k]\, s.t. \, K (T, X^i[:j])≥ 1 α ]. $ K (T, X)$ for a set of $i$ random variables $X=\ X_1, ..., X_i\ $ is defined as K (T, X)= _ j=1 ^ i (1+min(λ_j, 3 4T )×(X_j-T)), -13pt λ_i=√ 2log(2/δ) ilog(i+1) σ ^2_ i-1 ,\; σ _i^2= 1/4+Σ_ j=1 ^i(X_j- μ _j)^2 i+1 , \; μ _i = 1/2+Σ_ j=1 ^iX_j i+1 .

**Theorem .** For any adjustment strategy $ε$ and appropriate estimator $ E $, alg:threshold_adjustment returns a cascade $ ^*$ with $ ( Acc ( ^*) < α) ≤ δ$.

**Theorem .** Constructing an optimal task cascade is NP-Hard .

## Proofs
**Proof.** (Sketch) Given an instance of MSSC , $(U, S)$, where $U$ denotes the items, and $S$ denotes the sets, we generate an instance of cascade assembly as follows. For each item $u U$, we create a document $d_u$. For each set $S_i S $, we create a candidate task $T_i = (m, o_i, 1)$, where $m$ is a single proxy model, and $o_i$ is an operation that predicts True with confidence $1$ on $d_u$ iff $u S_i$ and returns a random answer with confidence $0$ otherwise. Therefore, every task in our cascade will have thresholds set to 1. We design the cost model so that accessing cached document tokens costs 0; each document is cached after the first task that processes it. Thus, the total cost for processing document tokens is constant across all cascades and can be ignored. We set each operation $o_i$ to have cost 1, so running any task $T_i$ on any $d_u$ incurs cost 1. We set the accuracy target $α=1$ and assign the oracle infinite cost, so every document must exit the cascade via some task. Under this cost model, processing any $d_u$ through a cascade $(T_ i_1 ,T_ i_2 , )$ incurs a cost equal to the index of the first $T_ i_j $ with confidence 1 on $d_u$. Hence the cascade cost equals the MSSC objective.

## Bound sentences
- Problem Statement Given a document collection $D$, an original operation $o_ orig $, a set of classes $C$, an oracle model $m_ oracle $, available proxy models $M$, and an accuracy target $α$, we seek to construct a minimal-cost task cascade $ = (T_1, T_2, , T_k)$ as follows: -5pt [display] where $  …
- We first show that a substantially simplified version of cascade assembly is NP-hard ( ssec:hardness ), motivating our greedy approach.
- NP-Hardness of Optimal Task Cascade Constructing an optimal task cascade $ $ on $D_ dev $, given task configurations $ T = \ (m_i, o_i, f_i)\ $ is NP-Hard .
- Our reduction is from the NP-Hard Min-Sum-Set-Cover problem~ [cite] ( MSSC ), a variant of the more standard Set-Cover problem.
- Oracle Only runs the oracle model (GPT-4o) on every document, giving an ideal but costly upper bound.
- We show that optimally ordering tasks is NP-Hard through a reduction from Minimum-Sum-Set-Cover , and inspired by approximation algorithms for this problem, we develop a greedy algorithm that sequentially adds the task that most reduces total inference cost while satisfying accuracy constraints. ; C …
- Overall, our contributions include: [nosep, leftmargin=*, wide=0pt] ; We introduce the concept of task cascades for LLM-based document processing, generalizing model cascades by allowing each stage to specify a model, operation (original or surrogate), and document fraction. ; We show that the probl …
