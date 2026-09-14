# sigmod26-352 — Query-Aware Path Inference from Spatial Videos

flag=False score=2 stmts=1 proofs=0 chars=93085
kinds: {"definition": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 2, "learned": 0}

## Statements
**Definition 1.** Path Inference Query Given a video database D and an input query image with object 𝑂𝑞 , the task of visual path inference query is to identify the trajectory sequence in the form of (𝐶 1, 𝐹𝑡,1 ) → (𝐶 2, 𝐹𝑡,2 ) → . . . such that: • The 𝑖-th trajectory node (𝐶𝑖 , 𝐹𝑡,𝑖 ) denotes a traversal at camera 𝐶𝑖 at timestamp 𝐹𝑡,𝑖 ; • Each (𝐶𝑖 , 𝐹𝑡,𝑖 ) corresponds to a frame 𝐹𝑖 containing object 𝑂𝑞 ; • The timestamps are strictly increasing: 𝐹𝑡,𝑖 < 𝐹𝑡,𝑗 for all 𝑖 < 𝑗. • The sequence is the most probable trajectory of 𝑂𝑞 in D. We employ a sequence of camera IDs instead of road segment IDs to approximately represent the trajectory of the query object. This is because our path inference query operates on a spatial video database, without any prior knowledge of the GPS traces of vehicles. Consequently, the groundtruth travel path between two adjacent cameras, 𝐶𝑖 and 𝐶𝑖+1 , remains unknown. The exact time window in which the query object 𝑂𝑞 appears in camera 𝐶𝑖 is also ignored in the output because it is challenging to estimate when only a portion of the raw frames is semantically parsed. Instead, we use a representative timestamp in the time window as an approximation. If the occurrence time window is required for downstream applications, we can post-process the output by further applying object tracking models [43] on the neighboring raw frames of 𝐹𝑖 under 𝐶𝑖 to derive such information. 3 Related Work In this section, we first review trajectory recovery from camera network, which is most rel …

## Proofs
## Bound sentences
