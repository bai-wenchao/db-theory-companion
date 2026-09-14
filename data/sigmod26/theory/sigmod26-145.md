# sigmod26-145 — LeaseGuard: Raft Leases Done Right

from=tex flag=False score=2 stmts=2 proofs=0 chars=121889
kinds: {"theorem": 2}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 2, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Theorem Read At Highest commitIndex.** For the set of nodes $ L $ whose state is ``leader'' at some moment, let $i_ max $ be the greatest commitIndex over $ L $. Any read $r$ observes the effects of all commands $c_i$ associated with all entries $e_i$ that were ever committed by any leader, for all $i ≤ i_ max $, for the value of $i_ max $ at some moment between $r$'s invocation and acknowledgment.

**Theorem Read-Your-Writes.** If a leader $L_1$ in term $t_1$ commits and applies write $w$, represented by log entry $e_1$ with index $i_1$, a later read $r$ must observe $w$'s effect.

## Proofs
## Bound sentences
