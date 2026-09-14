# sigmod26-235 — TaCo: Data-adaptive and Query-aware Subspace Collision for High-dimensional Approximate Nearest Neighbor Search

from=tex flag=True score=23 stmts=11 proofs=5 chars=118775
kinds: {"definition": 7, "theorem": 2, "lemma": 2}
counts: {"np_hard": 0, "lower_bound": 1, "upper_bound": 1, "big_o": 6, "omega": 0, "theta": 0, "approx_ratio": 2, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 1, "learned": 0}

## Statements
**Lemma Local Distance Preservation for Algorithm~\ref{eigensystem_allocation.** Let $ D=\ o_i\ _ i=1 ^n R ^d$ be a dataset, and let $B R ^ d × (N_s · s) $ denote the transformation returned by Algorithm~ [ref] , i.e., $B= B_1 & B_2 & … & B_ N_s $, with $B_j R ^ d × s $ and $N_s · s ≤ d$. For any point $o_i D $ and its neighbor $o_j$, assume that the local difference vector satisfies \|(I_d - B B^ )(o_i - o_j)\|^2 \, \|o_i - o_j\|^2, for some $ (0,1)$. Then, the distance after transformation satisfies The assumption of the form in [ref] has been established for random data points drawn from the so-called spiked random matrix model, see~ [cite] . (1- )\,\|o_i - o_j\|^2 \|B^ (o_i - o_j)\|^2 \|o_i - o_j\|^2.

**Definition Query Discriminability.** Given a query $q$ and the number of subspaces $N_s$. As a consequence of the uniformity of the subspaces after the subspace-oriented data transformation in Theorem~ [ref] , we denote $p^*$ the collision probability such that subspace collision happens for a true nearest neighbor $o^* R ^*= \ o^*_1,…,o^*_k\ $, and $p$ the probability that subspace collision happens for a non-neighbor $o R ^*$, with $p^* > p$. The Discriminability Gap of $q$ is defined as $ (q) = p^* - p > 0$.

**Definition Subspace Collision.** Given a dataset $ D$ of $n$ data points in $d$-dimensional space, a query $q R ^d$, and a collision ratio $α (0, 1 )$. We randomly select $s$ dimensions from all $d$ dimensions as a subspace $ R ^s$ ($s<d$). The dataset $ D$, the data point $o$, and the query point $q$ in this subspace are denoted as $ D^ $, $o^ $, and $q^ $. If a point $o D$ satisfies: $o^ $ is one of the $(α · n)$-NNs of $q^ $ in $ D^ $, we say that $o$ collides with $q$ in the subspace $ R ^s$.

**Definition SC-score.** Given a dataset $ D$ of $n$ data points in $d$-dimensional space, a query $q R ^d$, $N_s$ $s$-dimensional subspaces, a collision ratio $α (0, 1 )$. Probe collisions of $q$ in $N_s$ subspaces with the collision ratio $α$. For a data point $o D$, its SC-score is the number of subspaces where it collides with $q$. Therefore, SC-score is an integer in $ [0, N_s ]$.

**Lemma SC-score Separation.** For a given query $q$ and its discriminability gap $ (q)$ as in Definition~ [ref] , denote $o^*$ a true nearest neighbor of $q$ and $o R ^*$ a non-neighbor. Then, the optimal Type-I and Type-II errors both decay at least at the rate $exp ( - N_s ^2(q) 8p(1-p) )$. That is, both errors decay exponentially fast to zero as $N_s$ or $ (q)$ becomes large.

**Definition $k$-Approximate Nearest Neighbor Search, $k$-ANNS.** Given a dataset $ D$ of $n$ data points in $d$-dimensional Euclidean space $ R ^d$, a query $q R ^d$, an approximation ratio $c > 1$, and an integer $k$. Let $o^*_i$ be the $i$-th exact nearest neighbor of $q$ in $ D$. A $k$-ANNS returns $k$ points $o_1,o_2,…,o_k$. For each $o_i D$ satisfying $ \|q,o_i \| ≤ c · \|q,o^*_i \|$, where $i [1,k]$.

**Definition Subspace Sampling.** Given a dataset $ D$ of $n$ data points in $d$-dimensional space, we adopt a multi-round sampling strategy to obtain $N_s$ subspaces. In round $i$, a number of $s= d N_s $ dimensions are uniformly sampled without replacement to form a subspace $S_i$, $i=1,2,…,N_s-1$. For the last subspace $S_ N_s $, it simply pick up all remaining dimensions.

**Theorem Relative Neighborhood Ordering Preservation for Algorithm~\ref{data_transformation.** Under the notations and conditions of Lemma~ [ref] , consider two points $o_j, o_z D $ such that \|o_i - o_j\|^2 < (1- )\,\|o_i - o_z\|^2. Then, their relative ordering with respect to $o_i$ is preserved after the transformation through $B$, in the sense that \|B^ (o_i - o_j)\| < \|B^ (o_i - o_z)\|.

**Definition $k$-Nearest Neighbor Search, $k$-NNS.** Given a dataset $ D$ of $n$ data points in $d$-dimensional Euclidean space $ R ^d$, a query $q R ^d$, and an integer $k$. Let $o^*_i$ be the $i$-th exact nearest neighbor of $q$ in $ D$, and $ B=\ o^*_1,o^*_2,…,o^*_k\ $. A $k$-NNS returns $k$ points $ R=\ o_1,o_2,…,o_k\ $, satisfying $ R= B$.

**Definition Nearest Neighbor Search, NNS.** Given a dataset $ D$ of $n$ data points in $d$-dimensional Euclidean space $ R ^d$ and a query $q R ^d$. An NNS returns a point $o^* D$ which has the minimum Euclidean distance to $q$ among all points in $ D$, i.e., for each $o D$ satisfying $ \|q,o^* \| ≤ \|q,o \|$.

**Theorem Performance Guarantee for Algorithm~\ref{eigensystem_allocation.** Assume that the data sample covariance $ Σ$ has distinct eigenvalues that are all greater than or equal to one. Then, the Eigensystem Allocation method in Algorithm~ [ref] solves the optimization problem in Equation~ [ref] .

## Proofs
**Proof.** [Proof of Theorem~ [ref] ] To show that Eigensystem Allocation in Algorithm~ [ref] solves the optimization problem in [ref] , we first focus on the inner maximization problem: Denote $λ_1 > … > λ_d$ and $μ_1 ≥ … ≥ μ_s$ the eigenvalues of $ Σ$ and $B_j^ Σ B_j$, respectively (in descending order), we have, by the Poincaré separation theorem (also known as general Cauchy interlacing theorem) that λ_i ≥ μ_i ≥ λ_ d - s + i , i = 1, …, s, that is, each eigenvalue $μ_i$ of $B_j^ Σ B_j$ lies between two eigenvalues of $ Σ$. Since the logarithm function is monotonically increasing, maximizing the (log-)determinant in [ref] is equivalent to maximizing the product of eigenvalues. We formally have, by [ref] , that max_ B_j^ B_j = I_s (B_j^ Σ B_j) = Π_ i=1 ^s λ_i, and the maximum is achieved by taking $B_j$ to be the associated eigenvectors, i.e., $B_j = [ _1, …, _s]$. Further note that the greedy procedure in Algorithm~ [ref] finds the optimal ``balanced'' partition $B_1, …, B_ N_s $ that solves the outer minimization problem of [ref] . This concludes the proof.

**Proof.** [Proof of Lemma~ [ref] ] Recall from Algorithm~ [ref] that $B R ^ d × (N_s · s) $ contains eigenvectors of $ Σ$ as its columns, so that $B B^ $ is an orthogonal projection matrix. As a consequence, $o_i - o_j R ^d$ can be decomposed as the sum of the projection $B B^ (o_i - o_j)$ and the corresponding residue $(I_d - B B^ )(o_i - o_j)$, with \|o_i - o_j\|^2 = \|B^ (o_i - o_j)\|^2 + \|(I_d - B B^ )(o_i - o_j)\|^2. Rearranging~ [ref] gives \|B^ (o_i - o_j)\|^2 = \|o_i - o_j\|^2 - \|(I_d - B B^ )(o_i - o_j)\|^2. By~~ [ref] , the second term on the right-hand side is bounded by $ \|o_i - o_j\|^2$, which yields the lower bound in [ref] . The upper bound follows directly from the non-expansiveness of orthogonal projection.

**Proof.** [Proof of Theorem~ [ref] ] It follows from Lemma~ [ref] that \[ \|B^ (o_i - o_j)\|^2 \|o_i - o_j\|^2 and \|B^ (o_i - o_z)\|^2 (1- )\,\|o_i - o_z\|^2. \] Combining these two inequalities with [ref] yields \[ \|B^ (o_i - o_j)\|^2 < \|B^ (o_i - o_z)\|^2. \] This concludes the proof of Theorem~ [ref] .

**Proof.** [Proof of Lemma~ [ref] ]

**Proof.** [Proof of Lemma~ [ref] ] As a consequence of Theorem~ [ref] , we have that $SC(o)$ the SC-score of $o$ follows a binomial distribution with parameters $N_s$ and $p$, and $SC(o^*)$ the SC-score of $o^*$ follows a binomial distribution with parameters $N_s$ and $p^*$. The associated Bernoulli KL divergence writes, for small $ (q)$ as D(p||p^*) = ^2(q) 2p(1-p) + O( ^3(q)). Using the Bayes optimal decision rule (that balances the two log-likelihoods) and applying the (relative entropy) Chernoff bound, we conclude the proof of Lemma~ [ref] .

## Bound sentences
- In this paper, we address these limitations from two aspects: first, we design a subspace-oriented data transformation mechanism by averaging the entropies computed over each subspace of the transformed data, which ensures balanced subspace partitioning (in an information theoretical sense) and enab …
- A $k$-NNS returns $k$ points $ R=\ o_1,o_2,…,o_k\ $, satisfying $ R= B$. [$k$-Approximate Nearest Neighbor Search, $k$-ANNS] Given a dataset $ D$ of $n$ data points in $d$-dimensional Euclidean space $ R ^d$, a query $q R ^d$, an approximation ratio $c > 1$, and an integer $k$.
- In practice, many $k$-ANNS implementations do not explicitly rely on an approximation ratio $c$ during query processing; instead, they constrain the quality of the results through evaluation metrics~ [cite] .
- As a consequence, $o_i - o_j R ^d$ can be decomposed as the sum of the projection $B B^ (o_i - o_j)$ and the corresponding residue $(I_d - B B^ )(o_i - o_j)$, with [display] Rearranging~ [ref] gives [display] By~~ [ref] , the second term on the right-hand side is bounded by $ \|o_i - o_j\|^2$, which …
- The upper bound follows directly from the non-expansiveness of orthogonal projection.
