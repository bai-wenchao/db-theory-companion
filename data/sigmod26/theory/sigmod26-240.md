# sigmod26-240 — Through the Lens of Hubness: A Revisit on Graph-Based Approximate Nearest Neighbor Search: [Experiments & Analysis]

flag=True score=6 stmts=1 proofs=2 chars=88537
kinds: {"lemma": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 0, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 2, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Lemma 1.** . This variance introduces a systematic bias into the transition probabilities at each step, heavily favoring transitions toward high-centrality hubs. This functional bias partitions the graph into a strongly attractive core (hubs) and a weakly connected periphery (where 𝑉gate resides). For a search of finite length, the probability of navigating into the low-density gateway set before being absorbed by a hub’s basin of attraction vanishes as skewness intensifies. This dynamic renders the anti-hub topologically unreachable via greedy traversal. (See Appendix A.21 for the formal derivation.) □ 4 Revisiting Graph-based Algorithms through the Lens of Hubness Building on Section 3, we revisit mainstream graph-based ANNS algorithms through the lens of hubness. We argue that their effectiveness depends largely on how they (often implicitly) counteract hubness-induced distortions during index construction. As summarized in Figure 4, we organize existing methods by increasing mitigation complexity and analyze how their designs shape two core stages: candidate acquisition (neighbor discovery) and neighbor selection (edge pruning). This perspective yields a unified framework that traces the progression from topological diversification, to parameterized pruning, and finally to data-driven adaptivity. 4.1 Topological Diversification HNSW (Hierarchical Navigable Small World graph) [40] and NSG (Navigating Spreading-out Graph) [17] constitute the foundational tier of our hubness mitigation …

## Proofs
**Proof.** The event 𝑥 𝑝𝑡 +1 = 𝑥ℎ occurs when 𝛿 (𝑞, 𝑥ℎ ) is smaller than 𝛿 (𝑞, 𝑥 𝑣 ) for all other candidates 𝑥 𝑣 ∈ 𝑁 (𝑥 𝑝𝑡 ) \{𝑥ℎ }. Due to its high spatial centrality, 𝛿 (𝑞, 𝑥ℎ ) is drawn from a distribution with a smaller mean than those of less-central neighbors. As 𝑑 increases, Lemma 1 amplifies this mean separation, while distance concentration shrinks the variance, so 𝑥ℎ becomes the argmin with probability approaching one. Finally, the hub’s high in-degree increases the likelihood that 𝑥ℎ appears in 𝑁 (𝑥 𝑝𝑡 ), making capture prevalent. A formal proof is provided in Appendix A.11 . □

**Proof.** We model the greedy search as a stochastic process on the graph 𝐺. The premise of high in-degree skewness (𝑆 𝑁𝑘 ) implies a high variance in spatial centrality across vertices (per

## Bound sentences
