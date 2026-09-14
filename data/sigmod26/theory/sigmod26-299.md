# sigmod26-299 — DiskJoin: Large-scale Vector Similarity Join with SSD

from=tex flag=True score=7 stmts=3 proofs=1 chars=138698
kinds: {"definition": 2, "theorem": 1}
counts: {"np_hard": 7, "lower_bound": 0, "upper_bound": 0, "big_o": 7, "omega": 0, "theta": 0, "approx_ratio": 5, "whp": 0, "regret": 0, "dp": 0, "invariant": 1, "convergence": 0, "competitive": 0, "worst_case": 2, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition MECC: Minimum Edge Cover with Cache.** Assume a given undirected graph $G=(V,E)$ and an initially-empty cache with capacity $C$. The cache supports two operations: $ load (v)$, which loads node $v$ to the cache, and $ evict (v)$, which evicts node $v$ from the cache following a given policy $P$ when the cache is full and needs to load a node. An edge of $(u,v) G$ is said to be covered if both $u$ and $v$ are present in the cache at the same time. The Minimum Edge Cover with Cache problem seeks to find the sequence of load operations with the minimum length that covers all edges of $G$.

**Definition Similarity self-join (SSJ) for vector dataset.** Given a vector dataset $ X =\ x_1, x_2,…, x_N\ $, where each $x_n X $ ($1 \! \! n \! \! N$) is a $d$-dimensional vector, and a threshold $ε>0$, find all vector pairs $(x_n, x_ n' )$ with $ x_n- x_ n' ε$ and $1 n≠ n' N$.

**Theorem .** The MECC problem is NP-hard.

## Proofs
**Proof.** We show that the decision version of MECC can be reduced from independent set (IS), which, given a graph $G=(V,E)$ and an integer $T$, asks whether there exists a set $V' V$ such that $|V'|= T$ and $ u,v V'$ such that $(u,v) E$. Given an instance of IS with connected graph $G(V,E)$ and integer $T$, we construct an instance of MECC with the same graph $G(V,E)$ and a cache of size $C=|V|-T+1$ with last-in-first-out (LIFO) as the eviction policy $P$. We first show that if $G$ has an independent set of size $T$, the solution of MECC is a load sequence of length $|V|$. Let $V_T V$ be an independent set of size $T$ in $G$. We create a load sequence of length $|V|$ that loads the nodes $V V_T$ first into the cache, followed by the nodes in $V_T$. When executing this load sequence, nodes $V V_T$ will take up $|V|-T$ slots in the cache, leaving one free slot. Each subsequent node in $V_T$, is loaded into that slot, and, after being processed, gets evicted (based on LIFO) to load the next node. Since the nodes in $V_T$ form an independent set, there are no edges between them. All edges in $E$ are either among nodes in $V V_T$, which are together in the cache, and thus are covered, or between a node in $u V_T$ and nodes in $V V_T$, which are covered when $u$ is loaded. Thus, this sequence covered all edges in $G$. [!t] [width=0.47 ] figs/Problem-Model.pdf -3mm An example of the minimum edge covering with cache (MECC) problem, the graph is in the left plot, the cache size is 2, and $L(·)$ and $E(·)$ mean load and evict a node, respectively. The dotted lines show the edges covered in each step. [!t] [width= ] figs/belady.pdf -6mm An example for Belady's algorithm. The edge processing order is in (b), the cache size is 3, LRU loads 8 buckets while Belady's algorithm loads 7 buckets. Conversely, we also show that if the MECC instance can be solved with exactly $|V|$ node loads (so every node is loaded once) and a cache size of $|V|-T+1$ using LIFO, the set of evicted nodes form an independent set of size $T$. This is because any two evicted nodes are never present in the cache at the same time, and if any edges existed between them they would not have been covered. Since IS is NP-hard, and IS reduces to MECC in polynomial time, it follows that MECC is also NP-hard.

## Bound sentences
- Identifying the optimal bucket ordering is NP-hard (Section~ [ref] ).
- We define the problem of identifying the bucket load sequence to process all edges with minimum cache misses and show that it is NP-hard (Section~ [ref] ).
- We start by defining the problem of covering all graph edges with minimum cache misses, and show that it is NP-hard.
- Since IS is NP-hard, and IS reduces to MECC in polynomial time, it follows that MECC is also NP-hard.
- As MECC is NP-hard, we solve it approximately by decomposing it into two sub-problems. ; Given a processing order of the edges, we examine the cache eviction policy that minimizes the number of bucket loads.
