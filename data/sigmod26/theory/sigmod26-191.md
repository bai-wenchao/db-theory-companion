# sigmod26-191 — Poisson Sampling over Acyclic Joins

from=tex flag=True score=10 stmts=4 proofs=3 chars=199180
kinds: {"proposition": 2, "definition": 1, "theorem": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 1, "theta": 1, "approx_ratio": 0, "whp": 0, "regret": 2, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 1, "sketch": 0, "cost_model": 1, "cardinality": 4, "learned": 0}

## Statements
**Definition .** Assume that $R $ is a flat relation, let $ $ and let $t$ be a $ $-tuple. The degree of $t$ in $R$ is the number of times that $t$ occurs in $ _y(R)$. In other words, it is the cardinality of $σ_ = t (R)$. The degree of $ $ in $R$, denoted $ _ (R)$ is the maximum degree of any $y$-tuple in $R$. The degree of a join query $ Q = R_1( _1) R_k( _k)$ in a database $ $ is defined as \[ _ Q ( ) max \ _ _i _j (R_i) i = j, _i _j = \ \]

**Theorem .** Poisson sampling over acyclic joins, as well as over free-connex projections of such joins, can be solved in time $ ( + k log )$ in data complexity, where $ $ is the size of the input database, and $k$ the size of the resulting sample.

**Proposition .** For every acyclic join query $ Q $ and any attribute $y$ of $ Q $ we can compute an equivalent two-phase expression $ (E)$ such that $y$ is a flat attribute in the output scheme of $E$.

**Proposition .** Using nested semijoins it is possible to construct in $ ( )$ time a that can be used as a random-access index for an acyclic join query $ Q $, with access time $ (log + _ Q ( ))$.

## Proofs
**Proof.** First, compute a join tree $J$ of Q . Pick any node in $J$ that mentions $y$, and reroot $J$ into a join tree $J'$ that has this node as the root. Then the above-mentioned procedure applied to $J'$ yields the desired expression.

**Proof.** Since $ Q $ is acyclic, we can compute $ Q ( )$ by means of expression $ (E)$, where $E$ consists of nested semijoins only. By our earlier reasoning we can build a for $N = E( )$ in time linear in $ $. We can then compute the prefix vector also in linear time. This + prefix vector allows random access into $ (N)$ with access time $ (log N + h × _Q( ))$. The result follows by observing that necessarily $ N = ( )$ and that $h$ is constant in data complexity.

**Proof.** Let $Q = β_y (R_1( _1) R_m( _m) )$ be an acyclic Poisson sampling query. By Proposition~ [ref] we can compute a expression $ (E)$ equivalent to $ Q $, such that $y$ is a flat attribute of $E$. Given $E$, we can compute in $ ( )$ time a $ $ of the nested relation $N E( )$, which supports single-tuple random access into $ (N) = Q ( )$ in $ (log )$ time. Given $ $ we can use $ $ to compute a probe sequence $ $ of length $k$ in $ ( N + k) = ( + k)$ time, and use this to produce the resulting sample in $ (k log )$ time by probing the index. Summing up the complexity of each individual step yields the claimed complexity. For Poisson sampling queries of the form $β_y(δ _A( Q ))$ with $ _A( Q )$ free-connex acyclic we reason as follows. Carmeli et al.~ [cite] observe that for every free-connex acyclic conjunctive query $δ _A( Q )$ and database $D$, one can compute in linear time a full acyclic join query $Q'$ and a database $D'$ such that $δ _A( Q )(D) = Q'(D')$. In other words, processing $β(δ _A( Q ))$ on $D$ is equivalent to processing $β(Q')$ on $D'$ and our techniques apply to the latter. Since there is only a linear time overhead to obtain the latter from the former, our complexity results transfer to sampling over free-connex queries where the projection is set-based. For bag-based projection, our complexity results trivially hold because $β_y( _A( Q )) = _A(β_y( Q ))$.

## Bound sentences
