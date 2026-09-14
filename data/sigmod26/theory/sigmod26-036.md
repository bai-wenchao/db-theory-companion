# sigmod26-036 — Beyond Relational: Semantic-Aware Multi-Modal Analytics with LLM-Native Query Optimization

from=tex flag=True score=5 stmts=2 proofs=1 chars=133546
kinds: {"hypothesi": 2}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 5, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 1, "cost_model": 0, "cardinality": 4, "learned": 0}

## Statements
**Hypothesi Operator Independence.** Suppose that a model $m_a$ is more intelligent and costly than a model $m_b$. Then, choosing $m_a$ over $m_b$ as the execution engine for an operator in a plan improves the overall result quality (but at higher cost), regardless of the models allocated to other operators in the plan.

**Hypothesi Model Capability Hypothesis.** Given the ground-truth result $y$ to a query $x$, if a model $m$ returns a correct answer $y$ to $x$, $m(x)=y$, any model $m^ + $ that is more powerful than $m$ also returns the right answer $y$, $m^ + (x)=y$.

## Proofs
**Proof.** 

## Bound sentences
