# sigmod26-377 — Triangle Counting in Hypergraph Streams: A Complete and Practical Approach

from=tex flag=True score=31 stmts=14 proofs=8 chars=201670
kinds: {"definition": 3, "theorem": 9, "lemma": 2}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 1, "big_o": 14, "omega": 0, "theta": 0, "approx_ratio": 2, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 3, "competitive": 0, "worst_case": 2, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Theorem .** The variance of the hyper-vertex triangle count estimate in Algorithm~ [ref] is bounded as follows: \[ Var [ c _ _ inr ] = 0 ; \] \[ Var [ c _ _ hyb ] ≤ (2 c_ _ hyb ^2 - c_ _ hyb ) _1 - c_ _ hyb ^2; \] \[ Var [ c _ _ otr ] ≤ ( 2 c_ _ otr ^2 - c_ _ otr ) _2 - c_ _ otr ^2. \] where \[ _1 = max_ x [1, ] m[x](m[x]-1) |G_s[x]|(|G_s[x]|-1) , \] \[ _2 = max_ x [1, ] m[x](m[x]-1)(m[x]-2) |G_s[x]|(|G_s[x]|-1)(|G_s[x]|-2) \]

**Theorem .** Algorithm~ [ref] provides an unbiased estimate of hyper-vertex triangle count. Specifically, $ E [ c _ _ inr ] = c_ _ inr $, $ E [ c _ _ hyb ] = c_ _ hyb $, $ E [ c _ _ otr ] = c_ _ otr $, where $ c _ _ inr , c _ _ hyb , c _ _ otr $ are the triangle count estimate produced by at any time \( t \) and $ c_ _ inr , c_ _ hyb , $ $c_ _ otr $ is the true count.

**Theorem .** The Algorithm~ [ref] provides an unbiased estimate of three triangle count. Specifically, $ E [ c _ _ inr ] = c_ _ inr $, $ E [ c _ _ hyb ] = c_ _ hyb $, $ E [ c _ _ otr ] = c_ _ otr $, $ E $ where $ c _ _ inr , c _ _ hyb , c _ _ otr $ are the triangle count estimate produced by at any time \( t \) and $ c_ _ inr , c_ _ hyb , c_ _ otr $ is the true count.

**Theorem .** The variance of hyper-vertex triangle count estimates in Algorithm~ [ref] is bounded as follows: \[ Var [ c _ _ inr ] = 0 ; \] \[ Var [ c _ _ hyb ] ≤ (2 c_ _ hyb ^2 - c_ _ hyb ) m(m-1) |G_s|(|G_s|-1) - c_ _ hyb ^2; \] \[ Var [ c _ _ otr ] ≤ (2 c_ _ otr ^2 - c_ _ otr ) m(m-1)(m-2) |G_s|(|G_s|-1)(|G_s|-2) - c_ _ otr ^2. \]

**Theorem .** Algorithm~ [ref] takes $O(Σ_ j=1 ^ (m[j]^ (t) + (|G_s[j]^ (t) |_ max $ $+ |G_s[j]^ (t) |_ max · ln m[j]^ (t) +1 |G_s[j]^ (t) | )· M^2))$ time to process $t$ elements in the input hypergraph stream, where $|G_s[j]^ (t) |_ max $ is the maximum number of hyperedges ever held in the sample subset $j$.

**Theorem .** Algorithm~ [ref] takes $O(m^ (t) + (|G_s^ (t) |_ max + |G_s^ (t) |_ max · ln m^ (t) +1 |G_s^ (t) | )· M^2)$ time to process $t$ elements in the input hypergraph stream, where $|G_s^ (t) |_ max $ is the maximum number of hyperedges ever held in the sample space throughout the algorithm.

**Lemma .** In each sampled subset $G_s[i] G_s$, the probability that each hyperedge is sampled is equal and depends only on the state of the subset itself, i.e., $ (e_i is sampled ) = |G_s[i]| m[i] $ ($1 i $) where $e_i$ represents the hyperedge assigned to the sampled subset $G_s[i]$.

**Lemma .** In Algorithm~ [ref] , each hyperedge in the hypergraph stream has an equal probability of being sampled up to any time $t$, given by $ |G_s^ (t) | m^ (t) $, where $|G_s^ (t) |$ and $m^ (t) $ denote the number of sampled and observed hyperedges up to time $t$, respectively.

**Definition Hyper-vertex Triangle.** Given a hypergraph $H=(V,E)$, and three vertices $v_i, v_j, v_k V$ with $E_ v_i E_ v_j ≠ , E_ v_i E_ v_k ≠ $, and $E_ v_j E_ v_k ≠ $, a hyper-vertex triangle $ _ \ v_i, v_j, v_k\ ^ v $ is a subgraph formed by the three vertices \( v_i, v_j, v_k \) in $H$.

**Definition Hyper-edge Triangle.** Given a hypergraph \( H = (V, E) \) and three hyperedges \( e_i, e_j, e_k E \) with \( e_i e_j ≠ \), \( e_i e_k ≠ \), and \( e_j e_k ≠ \), a hyper-edge triangle $ _ \ e_i, e_j, e_k\ ^ e $ is a subgraph composed of \( e_i, e_j \) and \( e_k \) in \( H \).

**Theorem .** By applying to estimate hyper-edge triangle counts, we have: $ E [ c _ ] = c_ ;~~~ Var [ c _ ] ≤ ( 2 c_ ^2 - c_ ) - c_ ^2 $, where $ = max_ x [1, ] m[x](m[x]-1)(m[x]-2) |G_s[x]|(|G_s[x]|-1)(|G_s[x]|-2) $ and $ \ CCC,$ $ TCC, TTC, TTT\ $.

**Definition Hypergraph Stream.** A hypergraph stream $ $ is a sequence of edges: \[ = ( e^ (1) ,\ e^ (2) ,\ ,\ e^ (t) ,\ ) \] where each $e^ (i) $ represents a hyperedge that contains vertices $v_1^ (i) , v_2^ (i) … v_ |e^ (i) | ^ (i) $, arriving at time $i$.

**Theorem .** By applying to estimate hyper-edge triangle counts, we have: -0.2em \[ E [ c _ ] = c_ ;~~~ Var [ c _ ] ≤ (2 c_ ^2 - c_ ) m(m-1)(m-2) |G_s|(|G_s|-1)(|G_s|-2) - c_ ^2 \] -0.2em where $ \ CCC, TCC, TTC, TTT\ $

**Theorem .** Algorithm~ [ref] has a space complexity of $O(M)$, where $M$ is the maximum memory size.

## Proofs
**Proof.** When the sample set is not yet full or only a single hyperedge is replaced, the probability that each hyperedge is sampled can be directly established as $ |G_s^ (t) | m^ (t) $ by the classical theory of reservoir sampling. If multiple replacements are needed to meet the memory constraint, the process is repeated. Assuming $k$ hyperedges are removed, the final probability remains: \[ (e_s remains ) = |G_s^ (t-1) | m^ (t) · |G_s^ (t-1) | - 1 |G_s^ (t-1) | … |G_s^ (t-1) | - k |G_s^ (t-1) | - k + 1 = |G_s^ (t) | m^ (t) \]

**Proof.** proof/Unbiasedness1.3 Variance We now analyze the variance of hyper-vertex triangle count estimates provided by . The variance of hyper-vertex triangle count estimates in Algorithm~ [ref] is bounded as follows: \[ Var [ c _ _ inr ] = 0 ; \] \[ Var [ c _ _ hyb ] ≤ (2 c_ _ hyb ^2 - c_ _ hyb ) m(m-1) |G_s|(|G_s|-1) - c_ _ hyb ^2; \] \[ Var [ c _ _ otr ] ≤ (2 c_ _ otr ^2 - c_ _ otr ) m(m-1)(m-2) |G_s|(|G_s|-1)(|G_s|-2) - c_ _ otr ^2. \] proof/variance1.2

**Proof.** Whenever a new hyperedge $e$ arrives, computing its internal triangle count takes $O(1)$ time (line 5). Next, we determine whether $e$ should be inserted into the sample set $G_s$ and carry out the corresponding insertion or replacement operation at an additional cost of $O(1)$ (lines 6-8). Thus, processing all incoming hyperedges at the end of $t$ totals $O(m^ (t) )$ time. Each time a hyperedge $e$ is successfully inserted into $G_s$, we update the triangle count by checking the intersections between \(e\) and every existing hyperedge in \(G_s\). Iterating over all hyperedges \(e_i\) in \(G_s\) takes \(O(M)\) time, since \(M\) bounds the total number of vertices in the sample. For every \(e_i\) intersecting \(e\), we further check whether there exists some \(e_j G_s\) with \(e_i e_j ≠ \) to form outer triangles or hyper-edge triangles. Consequently, each update requires \(O(M^2)\) time. When the sample set is not yet full, each edge is accepted with probability 1. Otherwise, it is accepted with probability $ |G_s^ (t) | m^ (t) +1 $. Consequently, the total number of inserting edges is $|G_s^ (t) | + Σ_ i=|G_s^ (t) | ^ m^ (t) |G_s^ (t) | i+1 ≈ |G_s^ (t) | + |G_s^ (t) | · ln m^ (t) +1 |G_s^ (t) | $ based on the approximation formula for harmonic numbers. Since the number of hyperedges in the sample space changes dynamically over time, we take its maximum value $|G_s^ (t) |_ max $. Overall, the time cost of Algorithm~ [ref] is $O(m^ (t) + (|G_s^ (t) |_ max + |G_s^ (t) |_ max · ln m^ (t) +1 |G_s^ (t) | )· M^2)$.

**Proof.** Algorithm~ [ref] maintains a sample set $G_s$ containing hyperedges whose total size is dynamically controlled to strictly remains within the memory limit $M$. When inserting a new hyperedge causes the total size to exceed $M$, existing hyperedges are removed until the constraint is satisfied (Algorithm~ [ref] , lines 18--20). In addition, our algorithm also uses a small amount of auxiliary space for temporary computations (such as storing intersection results in UpdateTriangles and variables like $θ$, $γ$). However, these auxiliary data structures are at most proportional to the size of a single hyperedge or its intersections, and in practice are much smaller than $M$. Thus, the space complexity is $ O (M)$.

**Proof.** When a hyperedge $e$ arrives, it is assigned to a subset using a weighted discrete distribution~$WeightedDiscrete()$. This assignment is independent for each hyperedge. According to Lemma~ [ref] , each hyperedge $e$ has an equal probability of being sampled up to any time $t$, given by $ |G_s[i]^ (t) | m[i]^ (t) $.

**Proof.** proof/Unbiasedness2.1

**Proof.** When processing each incoming hyperedge $e$, the algorithm first checks and possibly creates new subsets or decides which subset the hyperedge should be assigned to. These steps (lines 2-11) require constant time $O(1)$. Since sampling and counting within each sampled subset are performed independently, according to Theorem~ [ref] , the time complexity for subset $j$ is \[ m[j]^ (t) + (|G_s[j]^ (t) |_ max + |G_s[j]^ (t) |_ max · ln m[j]^ (t) +1 |G_s[j]^ (t) | )· M^2) \] Therefore, the total time complexity is \[ O(Σ_ j=1 ^ (m[j]^ (t) + (|G_s[j]^ (t) |_ max + |G_s[j]^ (t) |_ max · ln m[j]^ (t) +1 |G_s[j]^ (t) | )· M^2)) \] where $ $ denotes the number of sample subsets actually used.

**Proof.** Algorithm~ [ref] partitions the total memory $M$ into up to $N$ sample subsets. Each subset only stores hyperedges up to the limit imposed by its current memory allocation \( M'[i] \), and the sum \( Σ_ j=1 ^ N M'[j] = Σ_ j=1 ^ M'[j] ≤ M \) always holds. Thus, the total space used by Algorithm~ [ref] is bounded by $O(M)$.

## Bound sentences
- To avoid the increased costs from over-fragmentation, we set an upper bound $N$ on the number of sample subsets.
