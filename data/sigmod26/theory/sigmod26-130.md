# sigmod26-130 — HONEYBEE: Efficient Role-based Access Control for Vector Databases via Dynamic Partitioning

from=tex flag=True score=3 stmts=1 proofs=0 chars=138233
kinds: {"definition": 1}
counts: {"np_hard": 3, "lower_bound": 1, "upper_bound": 1, "big_o": 8, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 2, "sketch": 0, "cost_model": 0, "cardinality": 1, "learned": 0}

## Statements
**Definition .** $γ = U,R,D, _ UA , _ PA $ defines a basic RBAC system, where ; $U$, $R$ and $D$ are the sets of users, roles, and documents in the systems, respectively. ; $ _ UA : U 2^R$ defines the many-to-many relationship between users and roles. ; $ _ PA : R 2^D$ defines the many-to-many relationship between roles and documents. In this system, a user $u_i$'s authorized permissions are determined by the union of permissions acquired through their assigned roles: $auth(u_i) = _ r _ UA (u_i) _ PA (r)$.

## Proofs
## Bound sentences
- This optimization problem belongs to the class of Mixed-Integer Nonlinear Programming (MINLP), which is NP-hard due to its combinatorial nature and nonlinear constraints.
- Parameters include: tree height ($h$), lower-bound ($b_0$) and upper-bound ($b_1$) for children per internal node. ; Tree and role construction : Generate tree \( T \) with height \( h \), constructing role hierarchy recursively from root, assigning random children in range \( [b_0, b_1] \) until ro …
- This problem is a Mixed-Integer Nonlinear Program (MINLP), which is NP-hard due to its combinatorial search space and nonlinear constraints.
- Since solving this problem is NP-hard, further introduces a greedy algorithm that generates a spectrum of partitioning strategies under different memory constraints, ranging from post-filtering to dedicated indices per role.
