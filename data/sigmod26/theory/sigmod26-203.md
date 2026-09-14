# sigmod26-203 — RadixGraph: A Fast, Space-Optimized Data Structure for Dynamic Graph Storage

from=tex flag=True score=8 stmts=4 proofs=2 chars=132754
kinds: {"theorem": 3, "lemma": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 77, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 6, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Theorem .** Under a single-threaded execution model, the amortized time complexity of edge insertion, update and deletion is $O(1)$.

**Lemma .** (Proof in Appendix A) There exists an optimal solution $(s_0^*,s_1^*,…,s_ l-1 ^*)$, such that $s_ l-1 ^*=x$.

**Theorem .** The time complexity of computing $g(l-1,x)$ is $O(nlx^2)$ and the space complexity is $O(lx)$.

**Theorem .** (Proof in Appendix A) The optimal value of $f$ is equal to $g(l-1,x)$.

## Proofs
**Proof.** To compute $g(l-1,x)$, we need to compute $g(i,j)$ for all $0≤ i<l-1,0≤ j≤ x$, which contains $O(lx)$ subproblems. To compute each $g(i,j)$, we need to enumerate $k$ for all $0≤ k≤ j$ (i.e., $O(x)$ subproblems) to find the optimal transition. Each transition requires $O(n)$ multiplications and divisions. Therefore, the total time complexity is $O(nlx^2)$. For the space complexity, we need to store $g(i,j)$ for all $O(lx)$ subproblems and the previous optimal subproblem $g(i-1,k)$ contributing to $g(i,j)$, such that we can find a path for optimal transition to $g(l-1,x)$ which recovers the optimal $a_i$.

**Proof.** [Proof Sketch] We prove the theorem by discussing the two cases of edge operations: (1) when the log segment is not full, appending an edge log to the segment clearly costs $O(1)$ time; (2) when a compaction is required, the compaction process costs $O(d)$, and is amortized to $O(1)$ for each edge operation. The complete proof can be found in Appendix B.

## Bound sentences
