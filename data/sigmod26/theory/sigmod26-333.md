# sigmod26-333 — Marlin: Efficient Coordination for Autoscaling Cloud DBMS

from=tex flag=True score=14 stmts=2 proofs=6 chars=351075
kinds: {"theorem": 1, "hypothesi": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 20, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Theorem .** System Table Consistency. is always consistent across all compute nodes in the cluster. The contents of a local may diverge slightly from the ground truth, but the local must have identical content as the ground truth regarding granules mapped the current node.

**Hypothesi .** After data loading, the system is in a consistent initial state where is correctly partitioned by the primary key and the two consistency guarantees on system tables are satisfied.

## Proofs
**Proof.** We prove the theorem by induction. Initially, the theorem holds as per hyp:initial . We will show that the theorem continues to hold after the execution of transactions. Consistency for . User transactions and MigrationTxn do not modify and do not affect its consistency. AddNodeTxn commits its commits to in all compute nodes through the distributed atomic commit protocol. Therefore, all nodes will see a consistent view of after the transaction. For DeleteNodeTxn , if it is triggered to delete an alive node, the theorem holds for the same reason as AddNodeTxn . If it is triggered to delete a failed node, the coordinator will commit to the of the failed node on behalf and other nodes. Therefore, every active node in (and the failed node's log as well) will see a consistent view of . Consistency for . The theorem holds for user transactions, AddNodeTxn , and DeleteNodeTxn since they do not modify . For a committed MigrationTxn , the coordinator writes the ownership change to , which holds the ground truth. As the transaction is committed on both the source and destination nodes, their local will reflect these updates. Therefore, the local of the source and the destination nodes have identical content as the ground truth regarding the migrating granule. Since the modification does not involve any granule owned by other nodes, the theorem holds for every node.

**Proof.** [ Proof ] All transactions end with , which involves the TryLog compare-and-swap operation that we assume is supported atomically by the storage service. For any log, the input to the compare-and-swap is a tracked LSN that is only updated by the last TryLog operation itself. This implies that, throughout the lifetime of any committed reconfiguration transaction (or more generally, throughout the time span starting from the last completion of any transaction up to the completion of the committed one), no other transactions touching the same log could have been committed. By contradiction, all transactions involving the log are serialized in the same order as the completed TryLog s.

**Proof.** [ Proof ] We enumerate over reconfiguration transaction types that involve the . ; [ AddNodeTxn ] Exactly one node is added and associated with a new, unique GTable. ; [ DeleteNodeTxn ] Exactly one node is removed along with its GTable/GLog partition. ; [ Other transactions ] Never update membership.

**Proof.** [ Proof ] We enumerate over reconfiguration transaction types that involve GTable update(s). ; [ MigrationTxn ] At commit, we have $dst.GTable[G].NodeID == dst$, meaning that $dst$ is an owner of $G$. ; [ RecoveryMigrTxn ] At commit, $dst$ is an owner of $G$ following the same reasoning as above. ; [ Other transactions ] Never update GTables.

**Proof.** [ Proof ] We enumerate over reconfiguration transaction types that involve GTable update(s). ; [ MigrationTxn ] We use induction. At a base state without any migrations, this invariant obviously holds. Now, assume it holds at the start of a successful MigrationTxn . Because $src.GTable[G].NodeID == src$ is required in order for the transaction to commit, $src$ is an owner of $G$ at the start. Therefore, $src$ is the only owner at the start. After the transaction, $src$ is no longer an owner (GTable entry changed) while $dst$ is an owner (as previously shown). Therefore, $dst$ is the only owner at the end. ; [ RecoveryMigrTxn ] We use induction similarly. Base state obviously holds, and that every transaction exactly swaps the owner of $G$ from $src$ to $dst$. Therefore, $dst$ is the only owner at the end. ; [ Other transactions ] Never update GTables.

**Proof.** [ Proof ] Let $N$ be the only owner of $G$ according to definition D1; the existence and uniqueness of $N$ is guaranteed by I4. $N$ is the only node that can ever execute and successfully commit a user request on $G$, because the additional guard at the start of a user transaction requires exactly D1 to enter the commit path.

## Bound sentences
