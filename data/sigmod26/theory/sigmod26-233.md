# sigmod26-233 — Succinct Structure Representations for Efficient Query Optimization

from=tex flag=True score=41 stmts=23 proofs=8 chars=221762
kinds: {"proposition": 1, "definition": 2, "theorem": 11, "lemma": 8, "corollary": 1}
counts: {"np_hard": 1, "lower_bound": 0, "upper_bound": 2, "big_o": 19, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 5, "sketch": 2, "cost_model": 8, "cardinality": 21, "learned": 0}

## Statements
**Definition .** Given a conjunctive query $Q$ and the associated hyergraph $H$, its meta-decomposition $M = (V(M), r(M), E(M), λ, , )$ is a labeled tree, where [leftmargin=*] ; $V(M)$ is the set of vertices, $r(M) V(M)$ is the root, and $E(M)$ is the set of edges, ; $λ : V(M) 2^ E(H) $ maps each vertex of $M$ to a set of hyperedges of $H$ (possibly empty), and ; $ : V(M) 2^ V(H) $ and $ : V(M) 2^ V(H) $ each maps each vertex of $M$ to a set of vertices of $H$, such that it satisfies [ref] , [ref] , and [label=(C ),ref=(C ),leftmargin=*] enumi 3 ; [ (C$_3'$) [H3'] ] For all $p V(M)$, $ (p) V(λ(p))$ if $λ(p) ≠ $. ; [ref] Interface condition. For every non-root $p V(M)$, let $q$ be $p$'s parent node. $ (p)$ satisfies ; $ (p) = (p) (V(M) V(M_p)) (q)$, where $M_p$ is the subtree of $M$ rooted at $p$; and ; $ (p) (s) for all s V(M) V(M_q)$ if $ (p) ≠ (q)$. For the root node $r(M)$, we set $ (r(M)) = $. ; [ref] Minor nodes and uniqueness condition. For every maximal subset of nodes $S = \ p_1, , p_n \ V(M) $ $(n ≥ 2)$ such that $ (p_1) = = (p_n) = $ for some value of $ $, there exists one unique node $ m V(M) $ with $ λ(m) = $ and $ (m) = $.

**Lemma .** Given a meta-decomposition $M$ of an acyclic hypergraph $H$, for all $v V(M)$, [leftmargin=*] ; if $λ(v) = $ and $ (v) = (v)$, then, for each join tree $T$ of $H$, there exists some $S = \ p V(M) λ(p) ≠ , (v) (p) \ $ such that the set $V_v^P = \ p V(M_ v ) λ(p) ≠ \ S$ induces a connected subtree $T_v$ of $T$; ; if $λ(v) ≠ $ or $ (v) ≠ (v)$, then, for each join tree $T$ of $H$, the set $V_v^P = \ p V(M_v) λ(p) ≠ \ $, i.e., physical nodes on the subtree $M_v$ rooted at $v$, induces a connected subtree $T_v$ of $T$.

**Definition .** We say a query plan $ P $ is induced by a join tree $T$~if [leftmargin=*] ; for each node $p V(T)$, there exists $q V( P )$ with $Q(p) = Q(q)$, i.e., the induced query of node $p$ in the join tree is exactly the induced query of node $q$ in the query plan; and ; for each non-leaf node $q V( P )$ with two children $u$ and $v$, there exists some $s E(H_u)$ and $t E(H_v)$ such that $I(u) s$, $I(v) t$, and there exists an edge between $s$ and $t$ in $E(T)$.

**Lemma .** Given a meta-decomposition $M$ of hypergraph $H$, for all $v V(M)$, let $V_v^P = \ p V(M_v) λ(p) ≠ \ $. Then, [leftmargin=*] ; if $λ(v) = $ and $ (v) = (v)$, then alg:enum enumerates all join trees of the hypergraph $H_v$ with $E(H_v) = λ(V_v^P) \ (v) \ $ and $V(H_v) = E(H_v)$; ; if $λ(v) ≠ $ or $ (v) ≠ (v)$, then alg:enum enumerates all join trees of the hypergrpah $H_v$ with $E(H_v) = λ(V_v^P)$ and $V(H_v) = E(H_v)$.

**Theorem .** Consider star queries We note that, in some literature, e.g.,~ [cite] , such queries are called `` clique '' queries, because their query graphs are cliques. of the form \[ Q_ star R_1[ x _1] … R_n[ x _n], \] where for any $i, j [n]$, $ x _i x _j = x $, for some attribute $x$. There are $n^ n-1 $ possible join trees for such a star query with $n$ relations.

**Lemma .** For all width-1 query plans $ P $ induced by a join tree $T$, for all non-leaf nodes $t V(T)$ with distinct children $c_1$ and $c_2$, if $p_1, p_2 V( P )$ are the nodes on $ P $ such that $Q(p_1) = Q(c_1)$ and $Q(p_2) = Q(c_2)$, then there exists no $q P $ such that $Q(q) = Q(p_1) Q(p_2) = Q(c_1) Q(c_2)$.

**Theorem .** Given a Boolean conjunctive query $Q$ and a query plan $ P $ for the query, the maximum intermediate result size, i.e., $max_ p V(H_p) | _ I(p) Q(p)|,$ is upper-bounded by $O(N^ w( P ) )$ in the worst case, where $N$ is the maximum cardinality of any base relation.

**Proposition .** Given an acyclic hypergraph $H$, if there exists a set of distinct ears $S = \ e_1, , e_n \ E(H)$ $(n ≥ 2)$ such that $o(e_1, H) = = o(e_n, H) = o$, then, the hypergraph $H'$, with $E(H') = (E(H) S) \ o \ $ and $V(H') = E(H')$, is acyclic.

**Lemma .** For each edge $(q, p) E(M)$, where $ (p) = \ e_p \ $ and $ (q) = \ e_q \ $, we have either ; $e_p$ is removed as ear by the algorithm before $e_q$ is, or ; $λ(q) = $ and $ (q) = (q)$ Additionally, $ (p) = (p) (q)$.

**Theorem .** In the meta-decomposition $M$ of an acyclic hypergraph $H$ as constructed by alg:meta , the number of vertices $|V(M)|$ and the number of edges $|E(M)|$ are $O(|E(H)|)$.

**Lemma .** Given a meta-decomposition $M$, if some non-root node $p V(M)$ has $λ(p) = $ and $ (p) = (p)$, then its parent $q$ has either $λ(q) ≠ $ or $ (q) ≠ (q)$.

**Theorem .** A relation-dominated conjunctive query can be evaluated in $O(|db|)$ time using a width-1 query plan, where $|db|$ represents the size of the database.

**Lemma .** Given an acyclic hypergraph $H$, if there exist two ears $e_1, e_2 E(H)$ such that $o(e_1, H) = o(e_2, H)$, then $o(e_1, H) = o(e_2, H) = e_1 e_2$.

**Theorem .** Given a query plan $ P $ for a query $Q$, the width $w( P ) = 1$ if and only if there exists a join tree $T$ of $Q$ that induces $ P $.

**Theorem Correctness.** Given a meta-decomposition $M$ of an acyclic hypergraph $H$, all trees $T$ output by alg:enum are valid join trees of $H$.

**Theorem Completeness.** Given a meta-decomposition $M$ of an acyclic hypergraph $H$, alg:enum enumerates all possible join trees of $H$.

**Theorem .** Given a join tree $T$, the optimal width-1 query plan induced by $T$ can be found in time $O(f(T)2^ f(T) |Q|)$.

**Theorem .** Given an acyclic query with an acyclic hypergraph $H$, alg:meta returns a valid meta-decomposition of $H$.

**Corollary .** $p$ is a descendant of $q$ on $M$ if and only if $e_p$ is removed as ear by the algorithm before $e_q$ is.

**Lemma .** For all $p V(M)$ with $λ(p) = $ and $ (p) = (p)$, all children $c$ of $p$ satisfy $ (c) = (p)$.

**Lemma .** For any non-root node $p$ on a meta-decomposition $M$ with parent $q$, $ (p) = (p) (q)$.

**Theorem .** A conjunctive query $Q$ has width-1 query plans if and only if $Q$ is acyclic.

**Theorem .** alg:meta terminates in time $O(|E(H)|^3)$.

## Proofs
**Proof.** Suppose there is such a $q$, then by def:w1plan-induced-by-jt , there would have been an edge between $c_1$ and $c_2$ on $T$, contradicting with the assumption that $c_1$ and $c_2$ are distinct children of some node $t$.

**Proof.** ($ $): $o(e_1, H) = e_1 ( (E(H) \ e_1 \ )) e_1$, and, similarly, $o(e_2, H) e_2$. So it follows that $o(e_1, H) = o(e_2, H) e_1 e_2$. ($ $): Since $e_1 E(H) \ e_2 \ $, we have $o(e_1, H) = o(e_2, H) = e_2 ( (E(H) \ e_2 \ )) e_1 e_2$.

**Proof.** We first have $ (p) (p)$ by definition on Lines~ [ref] , [ref] , and [ref] . Since the algorithm adds the edge $(q, p)$, by Lines~ [ref] and [ref] , we have $ (p) (q)$. Therefore, $ (p) (p) (q)$. We then consider the relative order in which $e_p$ and $e_q$ are removed from $E(H')$ in the algorithm. (1) If $e_p$ is removed before $e_q$ is, then at the time $e_p$ is removed, $e_q E(H')$, and therefore $ (p) (q) = e_p e_q e_p ( (E(H') \ e_p \ )) = (p)$. Since also $ (p) (p) (q)$, we have $ (p) = (p) (q)$. (2) If $e_p$ is removed after $e_q$ is, then, symmetric to case (1), we have $ (p) (q) (q)$. Then, since we have shown that $ (p) (p) (q)$, we have $ (p) (p) (q) (q)$. By alg-line:minor-origin-edge-cond and alg-line:phys-find-parent , this is only possible if $λ(q) = $ and $ (p) = (q)$. Since $ (p) (p)$ and $ (p) = (q)$, it is true that $ (p) = (p) (q)$.

**Proof.** ($ $) : Since $q V(M) V(M_p)$, $ (p) (q) (p) (V(M) V(M_p)) = (p)$. ($ $) : For any $v (p) = (p) (V(M) V(M_p))$, i.e., any $v (p) (s)$ for some $s V(M) V(M_p)$, the parent $q$ of $p$ lies on the path on $M$ between $p$ and $s$. Then, by the connectedness condition [ref] for $M$, $v (q)$.

**Proof.** Suppose by way of contradiction that there exists such a $p V(T)$ with child $c$ such that $ (c) ≠ (p)$. By lem:kappa , we have $ (c) = (c) (p) (p)$. Since $ (p) = (p) ≠ $, $p$ is not the root of $M$ and thus has a parent $q$. Again by lem:kappa , we have $ (p) = (p) (q) (q)$. But then, $ (c) (p) = (p) (q)$, contradicting [ref] (b) since $ (c) ≠ (p)$ but $q V(T) V(T_p)$.

**Proof.** Suppose by way of contradiction that, on a meta-decomposition $M$, there is $p V(M)$ such that $λ(p) = $ and $ (p) = (p)$, and its parent $q$ has $λ(q) = $ and $ (q) = (q)$. Then, $ (p) (q) = (q)$. Since $ (q) = (q) ≠ $, $q$ has a parent as well. Let the parent of $q$ be $s$. Then, $ (q) = (q) (s) (s)$. So, $ (p) (q) (s)$. By [ref] , $ (p) ≠ (q) = (q)$, contradicting [ref] (b).

**Proof.** We prove by structural induction on $M$. In the base case, for leaf nodes $v V(M)$, there is only one node on the subtree $M_v$, so the statement is vacuously true. For non-leaf nodes $v V(M)$, we assume as induction hypothesis that the statement is true for all children $c$ of $v$. Let $c$ and $d$ be the children of $v$ such that $p V(M_c)$ and $q V(M_d)$. We now consider two cases of $v$. (1) If $λ(v) = $ and $ (v) = (v)$, then, for any $s$ on the path between $p$ and $q$ on $T$ such that $s M_v$, we have $ (p) (q) (s)$ by the connectedness condition on $T$. By (the contrapositive of) lem:no-consec-special-minor , $λ(c) ≠ $ or $ (c) ≠ (c)$, so by the inductive hypothesis, $V_c^P$ induces a connected subtree $T_c$ of $T$. Similarly, $V_d^P$ induces a connected subtree $T_d$ of $T$. If $c = d$, then $p$ and $q$ are in the same subtree rooted at the same child of $v$, and the statement would hold. If $c ≠ d$, on the path from $p$ to $q$ on $T$, let the last node on $T_c$ be $x$ and the first node on $T_d$ be $y$. $s$ is between $x$ and $y$. Then, the path from $c$ and $d$ has to go through $x$ and $y$, and hence also $s$. Therefore, $ (c) (d) (s)$. By lem:minor-all-origin , in this case, $ (v) = (c) = (d) = (c) (d) (s)$. (2) If $λ(v) ≠ $ or $ (v) ≠ (v)$, we would like to show that for any $s$ on the path between $p$ and $q$ on $T$, $s V(M_v)$. Suppose by way of contradiction that this is not the case, i.e., there exists some $s$ on the path between $p$ and $q$ on $T$, but $s V(M) V(M_v)$. By the connectedness condition on $T$, we have $ (p) (q) (s)$. Furthermore, on $M$, $ (p) (s) (v)$ and $ (q) (s) (v)$, so $ (p) (q) = (p) (q) (s) (v)$. Let the parent of $p$ on $M$ be $t$. Then, $ (t) (s) (v)$. Then, $ (p) = (p) (s) = (p) (t) (s) = ( (p) (s)) ( (t) (s)) (v) (v) = (v)$. But, by [ref] , this means either $t = v$ or $t$ is a minor node with $ (t) = (t)$. In either case, we have $ (t) (q) (v)$, because (i) if $t = v$, $ (t) (q) = (v) (q) (v)$, and (ii) if $t$ is a minor node with $ (t) = (t)$, then $ (t) (q) = (t) (q) = (p) (q) (p) (q) (v)$. Also, we have $ (t) = (p) (t) (q)$, because either $t$ is on the path between $p$ and $q$, or $p$ is on the path between $t$ and $q$. Let the parent of $v$ be $u$. Then, we have $ (t) = (t) (q) = (t) (q) = ( (t) (q)) ( (p) (q)) ( (t) (q)) ( (p) (q)) (v) (s) (u)$. But, since it cannot be that $ (v) = (v)$ in this case, this violates [ref] , contradiction.

**Proof.** We will show that each join tree $T$ of $H$ can be enumerated by the algorithm based on the meta-decomposition $M$ of $H$. We prove by structural induction on vertices $v V(M)$. If $v$ is a leaf node, there is only one node in the subtree $M_v$, so this statement is vacuously true. If $v$ is a non-leaf node, consider the following cases. (1) If $λ(v) = $ and $ (v) = (v)$, by lem:no-consec-special-minor , all children $c$ of $v$ have either $λ(c) ≠ $ or $ (c) ≠ (c)$, so, by the induction hypothesis, alg:enum enumerates all join trees of hypergraph $H_c$ with $E(H_c) = _ p V_c^P λ(p)$ and $V(H_c) = _ e E(H_c) e$. Also, note that it is possible to obtain a meta-decomposition $M_v'$ of the hypergraph $H_v$ from $M_v$ by simply replacing $v$ by a physical node $v'$ with $λ(v') = \ (v) \ $, $ (v') = (v)$, and $ (v') = $. By lem:subtree-in-jt , for each child $c$ of $v$, on any join tree $T_c$ of hypergraph $H_c$, $V_c^P$ induces a connected subtree $T_c$ of $T$. Furthermore, $T_c$ is a join tree of the meta-decomposition $M_c$, and can hence be enumerated on alg-line:enum-subtrees . So it remains to show that the algorithm enumerates all possible ways to combine these subtrees along with $v$. For each possible join tree $T_v$ of $H_v$, without loss of generality, assume that $T_v$ is rooted at $v'$. $T_v$ can be constructed from the algorithm as follows. We first construct a tree $T_P$, by a top-down traversal of $T_v$, where, for each node $p$, if (i) $ (v) (p)$, (ii) $p M_c$, i.e., in the subtree $M_c$ rooted at some child $c$ of $v$, and (iii) its parent $q$ is in a different subtree $M_d$ rooted at some child $d ≠ c$ of $v$, then we add an edge from $d$ to $c$. If $p = v$, and its parent $q V(M_d)$ for some child $d$ of $v$, we add an edge from $d$ to $v$. If $p V(M_c)$ for some child $c$ of $v$, and its parent $q = v$, we add an edge from $v$ to $c$. Note that, for all pairs of $c$ and $d$ where we add edges, $ (c) = (d) = (v)$. Now, this tree $T_P$ is a spanning tree of the clique with vertices $C \ v \ $, where $C$ is the set of all children of $v$, so it can be enumerated by the sequence on alg-line:enum-minor-dummy . For each child $c$ of $v$, by lem:subtree-in-jt , $V_c^P$ induces a connected subtree $T_c$ of $T_v$. We traverse the vertices $c V(T_P)$ in bottom-up order. For each $c$ and each child $d$ of $c$ on $T_P$, let $r_d$ be the root of the connected subtrees $T_d$ of $T_v$ induced by $V_d^P$, and $u$ be the parent of $r_d$ on $T_v$. The algorit …

## Bound sentences
- In fact, finding the optimal join order of a query is well-known to be NP-hard in general~ [cite] .
- The width of a query plan indicates an upper bound on the minimal intermediate results over all nodes $p$ during evaluation.
- In the worst-case scenario, where all relations in $S$ share no common attributes and their join is a Cartesian product, the size of this join is $O(N^ |S| )$, which gives an upper bound of $O(N^ w( P ) )$.
