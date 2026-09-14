# sigmod26-192 — Practical Parameterized Query Optimization via Efficient Plan Reuse and List-wise Ranking

flag=False score=3 stmts=2 proofs=0 chars=93655
kinds: {"observation": 2}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 4, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 3, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 4, "cardinality": 44, "learned": 4}

## Statements
**Observation 1.** Two close queries in the query space of the same query template have the same (near-)optimal execution plan with a high probability.

**Observation 2.** There exist some sensitive regions where a small change in the predicates’ values leads to different plans. These observations are well supported by prior studies [19, 45]. For example, Reddy and Haritsa [45] visualize the mapping from queries to execution plans and show that large contiguous regions are often covered by the same plan. However, they also identify optimizer instability near plan boundaries, where even minor changes in selectivity can trigger abrupt plan changes. Motivated by these insights, we propose selecting 𝑘 nearest neighbors of query 𝑞 and using their (near-)optimal plans as the plan candidates. Observation 1 supports using nearest neighbors to Proc. ACM Manag. Data, Vol. 4, No. 1 (SIGMOD), Article 93. Publication date: February 2026. Practical Parameterized Query Optimization via Efficient Plan Reuse and List-wise Ranking 93:5 PCG: Plan Candidates Generation Plan Candidate Pool Generation Plan Candidates Selection (Section 3.1) (Section 3.2) PR: Plan Ranking with the lowest rank (Section 4) Fig. 1. PLARQ overview. include high-quality plans, while Observation 2 motivates choosing multiple neighbors (via 𝑘) to reduce the risk of including only suboptimal plans from unstable regions. Table 2. Profiling PR stage of Bao and Lero on CEB and Stack. #Plans Opt. Time Model Time Exe. Time Bao Lero Bao Lero Bao Lero Bao CEB-1 CEB-2 CEB-3 CEB-4 CEB-5 5 5 5 5 5 40 45 25 65 75 23.2 195.8 29.4 371.2 11.9 67.2 339.5 6088.9 1802.9 34696.4 5.7 5.8 4.7 6.8 7.9 60.4 75.9  …

## Proofs
## Bound sentences
- All pools were built sequentially – processing templates and their queries one by one – so the results represent an upper bound.
- (3) While a larger 𝑘 improves the upper bound (i.e., reducing the Best time), the total running time of plans selected by PLARQ tends to increase.
