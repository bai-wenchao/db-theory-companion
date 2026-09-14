# sigmod26-061 — CoTra: Towards Efficient and Scalable Distributed Vector Search with RDMA

from=tex flag=False score=1 stmts=1 proofs=0 chars=80061
kinds: {"definition": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 3, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition .** Given a vector dataset $ X = \ x_1, x_2, …, x_N\ R ^d$ with size $N$, a query vector $q R ^d$, and the number of required vectors $k$, return a set of vectors $ S X $ that satisfy \[ x_i-q x_j-q , x_i S ,x_j X - S \ and \ | S | = k. \]

## Proofs
## Bound sentences
- In particular, the exchanged messages include ; new candidates that are inserted into the candidate queue since the last synchronization. ; the current distance upper bound for a node to be added to the candidate queue.
- Using the synchronization messages, each primary machine updates its local candidate queue and distance upper bound (by taking the minimum of all bounds), and checks if the candidates to be traversed locally have been visited by the other machines.
- The distance upper bound is used to reject candidates that cannot be added to candidate queue. [display] Optimizations and Implementations RDMA-friendly Graph Layout To reduce communication costs, we tailor a graph storage format for vector search and RDMA.
