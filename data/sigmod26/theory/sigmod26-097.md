# sigmod26-097 — ESTune: Bayesian Uncertainty-Guided Early Stopping for Database Configuration Tuning

flag=False score=4 stmts=2 proofs=0 chars=97534
kinds: {"definition": 2}
counts: {"np_hard": 1, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 1, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 8, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Definition 2.1.** Database Performance is defined as the overall performance of the database when the entire workload is executed to completion. The primary objective of database knob tuning is to enhance database performance.

**Definition 2.2.** Database Segment Performance refers to the performance observed during short intervals of workload execution, such as the average throughput calculated every 5 seconds during a 200-second workload execution, or the total runtime measured for a group of 5 queries in a sequence of 200. Consider a scenario involving 𝑛 database knobs to be tuned, denoted as 𝑘𝑛𝑜𝑏 1, 𝑘𝑛𝑜𝑏 2, . . . , 𝑘𝑛𝑜𝑏𝑛 . Each knob 𝑘𝑛𝑜𝑏𝑖 is associated with a value domain Θ𝑖 , which may be continuous, discrete, or categorical depending on the knob type. The configuration space is thus defined as Θ = Θ1 × Θ2 × . . . × Θ𝑛 . Let 𝑦 denote a performance metric of interest (e.g., throughput or total runtime), quantified by an objective function 𝑓 : Θ → R that maps each configuration 𝑥 ∈ Θ to its corresponding performance value. Given a specified metric, the goal of knob tuning is to identify the optimal configuration 𝑥 ∗ that maximizes or minimizes 𝑓 (𝑥), formally: 𝑥 ∗ = arg max 𝑓 (𝑥). 𝑥 ∈Θ (1) Each iteration in iterative tuning methods typically follows a structured process. Formally, in the 𝑖-th iteration, the method 𝑀𝑒𝑡ℎ determines the next configuration 𝑥𝑖+1 based on the current configuration 𝑥𝑖 , its corresponding performance metric 𝑦𝑖 , and the historical dataset 𝐷𝑖 −1 , which comprises configuration–performance tuples from all previous iterations: 𝑥𝑖+1 = 𝑀𝑒𝑡ℎ (𝐷𝑖 −1 ∪ {(𝑥𝑖 , 𝑦𝑖 )}) , s.t. 𝑦𝑖 = 𝑓𝑤 (𝑥𝑖 ), (2) where 𝑦𝑖 = 𝑓𝑤 (𝑥𝑖 ) denotes the database performance 𝑦𝑖 obtained by fully executing the entire workload 𝑤 u …

## Proofs
## Bound sentences
- Identifying the optimal configuration within the configuration knob space has been proven to be an NP-hard problem [33].
