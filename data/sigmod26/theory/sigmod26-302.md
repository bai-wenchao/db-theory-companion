# sigmod26-302 — Dynamically Detect and Fix Hardness for Efficient Approximate Nearest Neighbor Search

from=tex flag=True score=10 stmts=9 proofs=0 chars=99717
kinds: {"definition": 3, "theorem": 5, "corollary": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 3, "big_o": 7, "omega": 0, "theta": 0, "approx_ratio": 2, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 1, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition .** (Escape Hardness (EH)). Given a directed graph index $G = (V, E)$ and a query $q$, let $P(u,v,G)$ denotes the set of all paths from vertex $u$ to vertex $v$ in graph $G$ and $F_ u,q $ denote the point $u$ is the $F_ u,q $-th NN of $q$, the Escape Hardness of query $q$ from vertex $u$ to vertex $v$ is defined as: $$ EH(u,v,q,G) = p P(u,v,G) min x p max F_ x,q $$ and we define the Escape Hardness Matrix $ H \ 1,2,...,|X|\ ^ N_q × N_q $ where $ H _ i,j = EH(N_ i,q , N_ j,q , q, G)$ and $N_q$ represents the number of nearest neighbors considered for query $q$.

**Definition .** ($S$-Neighboring Graph with query $q$ ($NG_ S,q $)). Consider a directed graph index $G = (V, E)$ and a query $q$, and define $V_ S,q = \ N_ 1,q ,N_ 2,q ,...,N_ S,q \ $. Then $NG_ S,q = (V_ S,q , E_ S,q )$ is the subgraph induced in $G$ by $V_ S,q $, where $E_ S,q $ is the edge set of the subgraph.

**Definition .** ($K_h$-reachable). Given a directed graph index $G = (V, E)$ and a query $q$, if point $u$ and $v$ satisfy $EH(u,v,q,G) K_h$, we consider $u$ to be $K_h$-reachable to $v$. Then we define the $K_h$-reachable Matrix $ T \ 0,1\ ^ N_q × N_q $ as: $ T _ i,j = 1 & H _ i,j K_h \\ 0 & H _ i,j > K_h \\ $

**Theorem .** Let $T$ denote the set of historical queries. Without pruning the edges, our method ensures that when $q T$ and $k N_q$, the accuracy of GreedySearch($G$, $q$, $k$, centroid, $K_h$) is 100\% (Algorithm [ref] ).

**Theorem .** For a directed graph index $G = (V, E)$ and a query $q$. If $N_ i,q $ can reach $N_ j,q $ in $NG_ S,q $ ($1 i,j S$). The Algorithm [ref] will always visit $N_ j,q $ when query $=q$, $ep = N_ i,q $ and $L S $.

**Theorem .** If points $N_ i,q $ and $N_ j,q $ satisfy the condition that $N_ i,q $ cannot reach $N_ j,q $ in $NG_ S-1,q $ but can reach $N_ j,q $ in $NG_ S,q $, then $EH(N_ i,q ,N_ j,q ,q,G) = S$ and $ H _ i,j =S$.

**Theorem .** Given a base data set $X$ and the DG constructed from the points in $X$. If any edge of DG is removed, there exists a query $q$ such that $NG_ 2,q $ contains only two isolated nodes.

**Corollary .** For a directed graph index $G = (V, E)$ and a query $q$. the Algorithm [ref] will always visit $N_ j,q $ when query $=q$, $ep = N_ i,q $ and $L EH(N_ i,q ,N_ j,q ,q,G) $.

**Theorem .** Given a query $q$, Algorithm [ref] will add at most $2(N_q-1)$ extra directed edges.

## Proofs
## Bound sentences
- EH establishes an upper bound on the search list size required to successfully reach a point from another point around the query.
- However, it is generally difficult to determine the exact $L$ needed to ensure a certain point is visited, so EH provides an upper bound on $L$.
- (2) Steiner Hardness focuses on estimating the computational cost required to achieve a target accuracy (e.g., recall@100 = 0.9), whereas EH aims to provide theoretical support for graph construction by measuring the upper bound of the search list size required for greedy search to reach a target fr …
