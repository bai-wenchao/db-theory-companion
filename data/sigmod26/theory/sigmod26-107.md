# sigmod26-107 — FGIM: a Fast Graph-based Indexes Merging Framework for Approximate Nearest Neighbor Search

from=tex flag=True score=10 stmts=7 proofs=1 chars=104655
kinds: {"definition": 7}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 21, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 1, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition Merging Graph-based Indexes for ANNS.** Given $h$ datasets $\ X _i R ^d\ _ i=1 ^h$, we have their $h$ pre-built graph-based indexes $\ G_i=(V_i,E_i)\ _ i=1 ^h$ using the same distance metric $δ$. Let $B( X _i)$ denote the index construction cost of dataset $ X _i$, and $M(·)$ the cost of merging multiple indexes. The merge process is formulated as a multi-objective optimization problem: $$ max \ \, B\! ( X ) - M(G_1, ,G_h),\; Q( G ),\; R( G ) \, \ , $$ where $ X = _ i=1 ^h X _i$, the merged index is $ G =(V,E)$ with $V= _ i=1 ^h V_i$, $Q( G )$ is the query-per-second throughput of $ G $, and $R( G )$ is the recall rate of $ G $.

**Definition $k$-NNS.** Given a finite dataset $ X $ and a query vector $ x _q R ^d$, and a parameter $k n$, $k$-NNS retrieve the set $ R $ consisting of the $k$ vectors from $ X $ that have the minimum distance to $ x _q$ based on $ δ $. For $ x _r R $ and $ x _s X R$, we have $δ( x _q, x _r) δ( x _q, x _s)$. $ R $ can be formally described as follows: -2ex R = _ R = k, R X Σ_ x R δ(q, x)

**Definition Cross Candidate Neighbors.** Given a vertex $u$ in $G_i$ in a set of graph-based indexes $\ G_1, G_2, …, G_h\ $ with enterpoints $\ ep_1, ep_2, …, ep_h\ $, and a search pool size $L$ (i.e., the beam width used in beam search), the cross candidate neighbors can be obtained by querying the other indexes $\ G_1, G_2, …, G_h\ G_i$: C_ i ^ - (u) = _ j i KNNSearch ( x _u, G_j, L, L, ep_j)

**Definition Proximity Graph.** The PG of $ X $ is a graph $G = (V, E)$ with the vertex set $V$ and edge set $E$. Each vertex $v_i V$ corresponds to a vector $ x _i X $. Each edge $e_ ij E$ represents the proximity between vertices $v_i$ and $v_j$, which is determined by a specified distance metric (e.g., $ _2$). The neighbors of a vertex $v$ in $V$ are denoted as $N_G(v)$.

**Definition Local Candidate Neighbors.** Given a vertex $u$ in $G_i$ in a set of graph-based indexes $\ G_1, G_2, …, G_h\ $, the local candidate neighbors can be obtained from the original graph $G_i$: C_ i ^ + (u) = \ v V_i (u, v) E_i\ where $V_i$ and $E_i$ are the vertex set and edge set of $G_i$, respectively.

**Definition $k$-ANNS.** Given a finite dataset $ X $ and a query vector $ x _q R ^d$, ANNS constructs an Index $I$ on $ X $. It then retrieves a subset $C$ of $ X $ by $I$, and evaluates $δ( x _i, x _q)$ to obtain the approximate $k$ nearest neighbors $ R $ of $q$, where $ x _i C$.

**Definition .** ($k$-Nearest Neighbor Graph). $k$-NNG $G = (V, E)$ connects each vertex $v_i V$ to its $k$ nearest neighbors in dataset $ X $, where $|N_G(v_i)| = k$.

## Proofs
**Proof.** 

## Bound sentences
