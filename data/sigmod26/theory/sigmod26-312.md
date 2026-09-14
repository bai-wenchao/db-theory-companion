# sigmod26-312 — Fast Indexing for Temporal Information Retrieval

flag=True score=2 stmts=1 proofs=0 chars=105693
kinds: {"definition": 1}
counts: {"np_hard": 0, "lower_bound": 2, "upper_bound": 3, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 2, "sketch": 0, "cost_model": 4, "cardinality": 7, "learned": 1}

## Statements
**Definition 2.** 1 (Time-travel IR query). Let [𝑞.𝑡𝑠𝑡 , 𝑞.𝑡𝑒𝑛𝑑 ] be a query time interval and 𝑞.𝑑 be a set of query elements, a time-travel IR query returns all objects in O whose interval overlaps with [𝑞.𝑡𝑠𝑡 , 𝑞.𝑡𝑒𝑛𝑑 ] and their description contains all elements in 𝑞.𝑑; formally, every object 𝑜 with: 𝑂𝑣𝑒𝑟𝑙𝑎𝑝 ( [𝑜.𝑡𝑠𝑡 , 𝑜.𝑡𝑒𝑛𝑑 ], [𝑞.𝑡𝑠𝑡 , 𝑞.𝑡𝑒𝑛𝑑 ]) = 𝑇 𝑅𝑈 𝐸, and 𝑜.𝑑 ⊇ 𝑞.𝑑 Note that if O contains e.g., document versions in an archive, our goal is to find the versions, not the distinct documents, that contain the query elements (terms); a similar assumption was made in [4]. Example 2.2. Figure 1 introduces our running example of 8 objects {𝑜 1, . . . , 𝑜 8 }. The descriptive elements for the objects are drawn from the D = {a,b,c} dictionary. Consider the time-travel IR query 𝑞 with its time interval corresponding to the red shaded area and 𝑞.𝑑 = {a,c}. The answer to 𝑞 consists of objects 𝑜 2 , 𝑜 4 and 𝑜 7 whose time intervals overlap with the shared area and their descriptions contain both user-given elements. 2.2 Temporal IR indexing As explained in the introduction, state-of-the-art temporal IR indexing builds on top of the inverted index. Therefore, we start our discussion with the base temporal inverted index which we denote by 3 For now, we only assume set semantics for 𝑜.𝑑; bag semantics and language models, where 𝑜.𝑑 can contain an element 𝑒 multiple times are left for future work. Proc. ACM Manag. Data, Vol. 3, No. 4 (SIGMOD), Article 246. Publication date: September 2025. Fast Indexin …

## Proofs
## Bound sentences
- Given a user-defined upper bound on the tolerable index-size increase (due to replicating object entries) compared to the original temporal inverted index, the goal is to determine the best slicing that satisfies the above constraint while minimizing the expected query processing cost.
