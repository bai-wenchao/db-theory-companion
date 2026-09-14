# sigmod26-358 — Retrieve-and-Verify: A Table Context Selection Framework for Accurate Column Annotations

from=tex flag=True score=3 stmts=3 proofs=0 chars=136380
kinds: {"definition": 3}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 1, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 1, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition Column Property Annotation (CPA).** Given a table $T$ with $n$ columns, and a target column pair $ = (c_i, c_j)$, where $1 ≤ i,j ≤ n$, and a set of possible relation types $ R $, the task of CPA is to develop a model $ M $ that can predict a relation type $ M ( , T) R $ to represent the relationship between the two columns.

**Definition Column Type Annotation (CTA).** Given a table $T$ with $n$ columns, and a target column $ = c_i$, where $1 ≤ i ≤ n$, and a set of possible semantic types $ T $, the task of CTA is to develop a model $ M $ that can predict a type label $ M ( , T) T $ so that each cell in $ $ has the same semantic type.

**Definition Column Context Verification.** Given a table $T$ with a target $ $ and its column context $ $, let $ S = \ \ $. Column context verification aims to identify the subset $ S $ that maximizes the quality score, i.e., = S argmax \ ( , ), where $ $ evaluates the effectiveness of $ $ for annotating $ $.

## Proofs
## Bound sentences
