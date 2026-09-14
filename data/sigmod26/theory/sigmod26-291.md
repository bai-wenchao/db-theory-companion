# sigmod26-291 — Continuous Subgraph Matching via Cost-Model-based Dynamic Vertex Dominance Embeddings

from=tex flag=True score=17 stmts=9 proofs=4 chars=133803
kinds: {"definition": 5, "lemma": 4}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 13, "big_o": 15, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 3, "sketch": 0, "cost_model": 7, "cardinality": 0, "learned": 0}

## Statements
**Definition .** (Continuous Subgraph Matching, CSM) Given a dynamic graph $G_D$, a set, $Q$, of registered query graph patterns $q$, and a current timestamp $t$, a continuous subgraph matching (CSM) query maintains a subgraph matching answer set $A(q,t)$ for each query graph pattern $q Q$, such that any subgraph $g A(q,t)$ in $G_D$ is isomorphic to the query graph $q$ (denoted as $g q$). Alternatively, for each $q Q$, the CSM problem incrementally computes an update, $ A(q,t)$, to the answer set $A(q,t-1)$, upon the change $ G_t$ to $G_ t-1 $. $ $

**Definition .** (Dynamic Graph, $G_D$) A dynamic graph , $G_D$, consists of an initial graph $G_0$ (as given by Definition~ [ref] ) and a sequence of graph update operations $ G =\ G_1, G_2, , G_t, \ $ on $G$. Here, $ G_t$ is a graph update operator, in the form of $(e+, t)$ or $(e-, t)$, which indicates either an insertion ($+$) or a deletion ($-$) of an edge $e$ at timestamp $t$, respectively. $ $

**Lemma .** (The Dominance Property of the Optimized Vertex Dominance Embeddings) Given a unit star subgraph $g_ v_i $ centered at vertex $v_i$ and any of its star substructures $s_ v_i $ (i.e., $s_ v_i g_ v_i $), their optimized vertex dominance embeddings (via base vector $z_i$) satisfy the condition that: $o'(s_ v_i ) o'(g_ v_i )$ (including $o'(s_ v_i )=o'(g_ v_i )$) in the embedding space.

**Definition .** (Graph Isomorphism) Given two graphs $G_1$ and $G_2$, graph $G_1$ is isomorphic to graph $G_2$ (denoted as $G_1 G_2$), if there exists a bijection mapping function $M: V(G_1) V(G_2)$, such that: i) $ v_i V(G_1)$, we have $L(v_i)=L(M(v_i))$, and; ii) $ e_ i,j E(G_1)$, edge $e_ M(v_i),M(v_j) = (M(v_i), M(v_j)) E(G_2)$ holds. $ $

**Lemma .** (The Dominance Property of Vertex Embeddings) Given a unit star subgraph $g_ v_i $ centered at vertex $v_i$ and any of its star substructures $s_ v_i $ (i.e., $s_ v_i g_ v_i $), their vertex embeddings satisfy the dominance condition that: $o(s_ v_i ) o(g_ v_i )$ (including $o(s_ v_i )=o(g_ v_i )$) in the embedding space.

**Definition .** (Static Graph, $G$) A static graph , $G$, is denoted as a triple $(V(G), E(G), L(G))$, where $V(G)$ is a set of vertices $v_i$, $E(G)$ is a set of edges $e_ i,j =(v_i,v_j)$ between vertices $v_i$ and $v_j$, and $L(G)$ is a label function from each vertex $v_i V(G)$ to a label $l(v_i)$. $ $

**Lemma \bf (MBR Range Pruning).** Given a query embedding $o'(q_i)$ of the query vertex $q_i$ and a vertex $v_i$ in a cell of DAS$^3$ synopsis $Syn_j$ (for $deg(q_i) (δ_ j-1 , δ_j]$), vertex $v_i$ can be safely pruned, if it holds that $o'(q_i) v_i.MBR_ deg(q_i) $.

**Lemma \bf (Embedding Dominance Pruning).** Given a query embedding vector $o'(q_i)$ of the query vertex $q_i$, any cell $C$ or vertex $v_i$ can be safely pruned, if $o'(q_i)$ does not dominate any portion of cell $C$ or embedding upper bound vector $v_i.UB_δ$.

**Definition .** (Subgraph Matching) Given graphs $G$ and $g$, a subgraph matching problem identifies subgraphs $g'$ of $G$ (i.e., $g' G$) such that $g$ and $g'$ are isomorphic. $ $

## Proofs
**Proof.** For a given unit star subgraph $g_ v_i $ centered at vertex $v_i$ and any of its star substructures $s_ v_i $ (i.e., $s_ v_i g_ v_i $), since they share the same center vertex $v_i$ (i.e., with the same label $l(v_i)$), they must have the same SPUR vector $x_i$. Moreover, since $s_ v_i g_ v_i $ holds, we also have $ N _ v_i (s_ v_i ) N _ v_i (g_ v_i )$, where $ N _ v_i (s_ v_i )$ (or $ N _ v_i (g_ v_i )$) is a set of $v_i$'s 1-hop neighbors in subgraph $s_ v_i $ (or $g_ v_i $). Thus, for SPAN vectors $y_i(s_ v_i )$ and $y_i(g_ v_i )$ of $s_ v_i $ and $g_ v_i $, respectively, it must hold that: $y_i(s_ v_i )[k] ≤ y_i(g_ v_i )[k]$ for all dimensions $k$ (since we have $y_i(s_ v_i )[k] =Σ_ v_j N _ v_i (s_ v_i ) x_j[k] ≤ Σ_ v_j N _ v_i (g_ v_i ) x_j[k] = y_i(g_ v_i )[k]$). In other words, their SPAN vectors satisfy the condition that $y_i(s_ v_i ) y_i(g_ v_i )$. Therefore, for $s_ v_i g_ v_i $, their vertex dominance embeddings satisfy the condition that: $o(s_ v_i ) = (x_i || y_i(s_ v_i )) (x_i || y_i(g_ v_i )) = o(g_ v_i )$ (including $o(s_ v_i )=o(g_ v_i )$) in the embedding space, which completes the proof.

**Proof.** Given a unit star subgraph $g_ v_i $ centered at vertex $v_i$ and any of its star substructures $s_ v_i $ (i.e., $s_ v_i g_ v_i $), since they have the same center vertex $v_i$ (with the same vertex label), their base vectors have the same values, i.e., $z_i(s_ v_i )=z_i(g_ v_i )$, or equivalently $β z_i(s_ v_i )=β z_i(g_ v_i )$ (for $β >0$). Due to the property of vertex dominance embeddings (as given in Lemma [ref] ), we have $o(s_ v_i ) o(g_ v_i )$, or equivalently $α o(s_ v_i ) α o(g_ v_i )$ (for $α>0$). Therefore, we can derive that $α o(s_ v_i ) + β z_i(s_ v_i ) α o(g_ v_i ) + β z_i(g_ v_i )$, or equivalently $o'(s_ v_i ) o'(g_ v_i )$ (including $o'(s_ v_i )=o'(g_ v_i )$), which completes the proof.

**Proof.** If a query vertex $q_i$ in query graph $q$ matches with a data vertex $v_i$ in a subgraph of the data graph, then their vertex dominance embeddings must hold that $o'(q_i) o'(v_i)$. Therefore, if $o'(q_i)$ does not dominate the cell $C$, then $o'(q_i)$ cannot dominate any vertex $o'(v_i)$ inside cell $C$, and all vertices in cell $C$ (or cell $C$) can be safely pruned. Moreover, if $o'(q_i)$ does not dominate embedding upper bound vector $v_i.UB_δ$, i.e., $v_i.UB_δ DR(o'(q_i))$, then $o'(q_i)$ does not dominate any star substructure $s_ v_i $ with center vertex $v_i$ and the corresponding degree group. In other words, $q_i$ does not match $v_i$. Thus, vertex $v_i$ can be safely pruned.

**Proof.** The MBR $v_i.MBR_ deg(q_i) $ minimally bounds vertex embeddings for all possible star substructures $s_ v_i $ with center vertex $v_i$ and degree $deg(q_i)$. Thus, if query vertex $q_i V(q)$ and its 1-hop neighbors match with some star substructures with the same degree $deg(q_i)$, then its query embedding vector $o'(q_i)$ must fall into this MBR $v_i.MBR_ deg(q_i) $. Therefore, if this condition does not hold, i.e., $o'(q_i) v_i.MBR_ deg(q_i) $, then $q_i$ does not match with $v_i$, and $v_i$ can be safely pruned, which completes the proof.

## Bound sentences
- Each vertex $v_i C.list$ contains the following aggregates: ; an embedding upper bound vector, $v_i.UB_ δ $, for all star substructures $s_ v_i $ with center vertex degrees $δ (δ_ j-1 , δ_j]$, and; ; a list of MBRs, $v_i.MBR_δ$ (for $δ (δ_ j-1 , δ_j]$), that minimally bound all embedding vectors $o' …
- Let $v_i.UB_ δ $ be the maximum corner point of the MBR $v_i.MBR_ δ $ (by taking the upper bound of the MBR on each dimension).
- Then, for vertex $v_i$, we insert vertex $v_i$ into the vertex list, $C.list$, of a cell $C I _j$, into which corner point $v_i.UB_ ub\_δ $ falls, where degree upper bound $ub\_δ = min\ deg(v_i), δ_j\ $.
- In DAS$^3$, each vertex $v_i$ is associated with an embedding upper bound vector $v_i.UB_ δ $ and a list of MBRs, $v_i.MBR_δ$.
- Specifically, in $Syn_2$, we store data vertices $v_1$ and $v_2$ in the cell $C$, which are associated with embedding upper bound vectors, $v_1.UB_3$ and $v_2.UB_2$, and MBR lists, $\ v_1.MBR_2$, $v_1.MBR_3\ $ and $\ v_2.MBR_2\ $, respectively.
- Here, each MBR $v_i.MBR_δ$ (e.g., $v_1.MBR_2$ in Figure [ref] ) minimally bounds embedding vectors $o'(v_i)$ of star substructures with degree $δ$ (i.e., $s_ v_1 ^4$, $s_ v_1 ^5$, and $s_ v_1 ^6$ with degree 2), and each embedding upper bound vector $v_i.UB_ ub\_δ $ (e.g., $v_1.UB_3$) is the maximum …
- (Embedding Dominance Pruning) Given a query embedding vector $o'(q_i)$ of the query vertex $q_i$, any cell $C$ or vertex $v_i$ can be safely pruned, if $o'(q_i)$ does not dominate any portion of cell $C$ or embedding upper bound vector $v_i.UB_δ$.
- Moreover, if $o'(q_i)$ does not dominate embedding upper bound vector $v_i.UB_δ$, i.e., $v_i.UB_δ DR(o'(q_i))$, then $o'(q_i)$ does not dominate any star substructure $s_ v_i $ with center vertex $v_i$ and the corresponding degree group.
- As mentioned above, by checking the dominance condition between embedding upper bound vector $q_1.UB_2$ and the cells' keys $C.key$, we can obtain candidate cells.
- Specifically, to implement embedding dominance and MBR range pruning strategies, we compare embedding upper bound vectors $q_1.UB_2$ and $v_i.UB_ δ $ (e.g., $v_1.UB_3$ and $v_2.UB_2$), and MBRs with same degree $q_1.MBR_2$ and $v_i.MBR_2$ (e.g., $v_1.MBR_2$ and $v_2.MBR_2$), respectively.
