# sigmod26-381 — VecFlow: A High-Performance Vector Data Management System for Filtered-Search on GPUs

from=tex flag=True score=4 stmts=2 proofs=1 chars=153381
kinds: {"definition": 2}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 1, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 2, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition \textbf{Filtered Nearest Neighbor Search (Filtered-NNS).** Given a finite data point set $X$ of $N$ points in a vector space $ R ^D$, each data point (a.k.a. vector) $x X$ has an associated set of labels $L_x L $, where $ L $ is a finite set of labels. The goal of filtered-NNS is to answer a given query point $q R ^D$ with labels $L_q L $ by finding the closest point $x X$ with $L_q$, i.e., points in $X$ that have the label $L_q$ associated with them.

**Definition \textbf{Filtered Approximated Nearest Neighbor Search} (Filtered-ANNS).** The goal of $ε$-filtered-NNS is to design an algorithm that answers a given query point $q R ^D$ with labels $L_q L $ by maximizing the recall of finding the top-k closest points $A_ topk X$ with $L_q$ while minimizing the search time spent to return $A_ topk $.

## Proofs
**Proof.** 

## Bound sentences
