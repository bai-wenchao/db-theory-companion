# sigmod26-315 — Focus! Fast On-disk Concurrency-control Using Sketches

flag=True score=5 stmts=1 proofs=1 chars=95274
kinds: {"lemma": 1}
counts: {"np_hard": 0, "lower_bound": 2, "upper_bound": 4, "big_o": 1, "omega": 0, "theta": 4, "approx_ratio": 9, "whp": 1, "regret": 0, "dp": 0, "invariant": 1, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 56, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Lemma 3.** Each timestamp increases monotonically in physical time in TicToc with approximate timestamp storage. Furthermore, every write to a key 𝑘 causes 𝑘’s write timestamp to increase.

## Proofs
**Proof.** We establish the second fact first. Consider a committing transaction that writes to 𝑘. TicToc guarantees that, when the transaction performs put (𝑘.𝑤𝑡𝑠, 𝜏) during its commit phase, 𝜏 is larger than the read timestamp returned by a previous get (𝑘.𝑟𝑡𝑠) performed by the same transaction. By Property 2, 𝑘.𝑤𝑡𝑠 ≤ 𝑘.𝑟𝑡𝑠 at the time of the get and, since the transaction references 𝑘 for the entire duration between the get and put, the approximate timestamp storage cannot spontaneously increase 𝑘.𝑤𝑡𝑠 during that interval. Furthermore, the transaction holds a lock on 𝑘 the entire time between the get and the put, so no other transaction could have performed a put on 𝑘.𝑤𝑡𝑠. Hence 𝑘.𝑤𝑡𝑠 cannot change between the transaction’s get and its put, ensuring that the put increases 𝑘.𝑤𝑡𝑠. The above argument also shows that, when a transaction performs put (𝑘.𝑟𝑡𝑠, 𝜏) in its commit phase, it does not decrease 𝑘.𝑟𝑡𝑠. A transaction that reads 𝑘 may also update 𝑘.𝑟𝑡𝑠 during its validation phase, but this trivially does not decrease 𝑘.𝑟𝑡𝑠 because the transaction does put (𝑘.𝑟𝑡𝑠, max(𝜏,get (𝑘.𝑟𝑡𝑠))) in an atomic section. Thus put operations can never decrease a key’s timestamps. The only other way a timestamp can change is through approximation, which is guaranteed not to decrease a timestamp (Property 1). Thus timestamps increase monotonically over physical time. □

## Bound sentences
