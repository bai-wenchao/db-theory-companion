# sigmod26-310 — Estimating Biclique Counts with Accuracy Guarantees

flag=True score=16 stmts=5 proofs=4 chars=88271
kinds: {"lemma": 2, "theorem": 3}
counts: {"np_hard": 1, "lower_bound": 5, "upper_bound": 1, "big_o": 0, "omega": 0, "theta": 0, "approx_ratio": 12, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 1, "competitive": 0, "worst_case": 0, "sketch": 0, "cost_model": 0, "cardinality": 2, "learned": 0}

## Statements
**Lemma 1.** Every (𝑝, 𝑞)-biclique in 𝐺 with 𝑝 ≤ 𝑞 contains exactly one ℎ-zstar for ℎ = 𝑝.

**Lemma 2.** Let Δ(𝐺) be the set of all ℎ-zstars in 𝐺 for ℎ = 𝑝, and 𝑍 be a random ℎ-zstar uniformly sampled from Δ(𝐺). The probability that 𝑍 forms a (𝑝, 𝑞)-biclique in 𝐺 is 𝑐𝑛𝑡𝑝,𝑞 (𝐺) Pr(𝑍 forms a (𝑝, 𝑞)-biclique in 𝐺) = |Δ(𝐺)|

**Theorem 2.** Let T be a set of zstars uniformly sampled from Δ(𝐺). Then, Í |Δ(𝐺)| 𝑍 ∈ T 𝑋 (𝑍 ) c 𝑝,𝑞 (𝐺) = 𝑐𝑛𝑡 |T | is an unbiased estimator for the count of (𝑝, 𝑞)-bicliques in 𝐺. Proc. ACM Manag. Data, Vol. 3, No. 6 (SIGMOD), Article 326. Publication date: December 2025. Estimating Biclique Counts with Accuracy Guarantees 326:9

**Theorem 3.** The time complexity of Algorithm 3 is 𝑂 (|𝐸| + 𝑝 · 𝑑 max ).

**Theorem 4.** With probability at least 1 − 𝛿, the biclique count estimated by Algorithm 4 has a relative error at most 𝜖. 3.3 Balancing the Running Time of the Two Stages Recall that, our framework in Algorithm 4 for estimating the (𝑝, 𝑞)-biclique count consists of two stages: Stage-I constructs the sample space S𝑝,𝑞 (𝐺), represented by a BC-Shadow S𝑝,𝑞 (𝐺), while Stage-II samples zstars from S𝑝,𝑞 (𝐺) and estimates 𝑐𝑛𝑡𝑝,𝑞 (𝐺) based on the stopping rule theorem (Theorem 1). Different sample spaces S𝑝,𝑞 (𝐺) yield different biclique densities 𝜇 S𝑝,𝑞 (𝐺 ) , which in turn affect the running time of Stage-II of the algorithm. In this subsection, we explore methods for constructing S𝑝,𝑞 (𝐺) that aim to optimize the overall performance of the algorithm by balancing the computational workload between Stage-I and Stage-II. Proc. ACM Manag. Data, Vol. 3, No. 6 (SIGMOD), Article 326. Publication date: December 2025. 326:14 Rashmika Gamage and Lijun Chang 3.3.1 Balancing Strategy. As shown in Algorithm 4, our sample space construction algorithm first initializes the BC-Shadow as {(∅, ∅, 𝑈 , 𝑉 )} and then iteratively refines it. If we spend minimal time refining the sampling space (e.g., stop Stage-I immediately after the initialization), then Stage-I will be very efficient. However, the sample space remains large and contains many elements that do not form bicliques, resulting in a low 𝜇 S𝑝,𝑞 (𝐺 ) and causing Stage-II to require a large number of samples to achieve the desired estimation accuracy. Con …

## Proofs
**Proof.** Let’s consider an arbitrary (𝑝, 𝑞)-biclique; without loss of generality, assume it is ({𝑢 1, 𝑢 2 , . . . , 𝑢𝑝 }, {𝑣 1, 𝑣 2, . . . , 𝑣𝑞 }). Then, these vertices form a unique zstar (𝑢 1, 𝑣 1, 𝑢 2, 𝑣 2, . . . , 𝑢𝑝 , 𝑣 𝑝 , 𝑣 𝑝+1, . . . , 𝑣𝑞 ), while any other ordering of these vertices is not a zstar. □

**Proof.** As each (𝑝, 𝑞)-biclique in 𝐺 corresponds to exactly one ℎ-zstar for ℎ = 𝑝 and each ℎ-zstar is contained in at most one (𝑝, 𝑞)-biclique, the total number of ℎ-zstars of Δ(𝐺) that form (𝑝, 𝑞)bicliques is equal to 𝑐𝑛𝑡𝑝,𝑞 (𝐺). Then, the lemma follows from the fact that 𝑍 is sampled uniformly at random from Δ(𝐺). □

**Proof.** For a random zstar 𝑍 sampled from Δ(𝐺), we have E[𝑋 (𝑍 )] = Pr(𝑍 forms a (𝑝, 𝑞)-biclique in 𝐺) = 𝑐𝑛𝑡𝑝,𝑞 (𝐺)/|Δ(𝐺)| By the linearity of expectation, we get: " #   |Δ(𝐺)| ∑︁ |Δ(𝐺)| ∑︁ c 𝑝,𝑞 (𝐺) = E E 𝑐𝑛𝑡 𝑋 (𝑍 ) = E[𝑋 (𝑍 )] = 𝑐𝑛𝑡𝑝,𝑞 (𝐺), |T | 𝑍 ∈ T |T | 𝑍 ∈ T c 𝑝,𝑞 (𝐺) is an unbiased estimator for the number of (𝑝, 𝑞)-bicliques in 𝐺. proving that 𝑐𝑛𝑡 □

**Proof.** Setting the initial distribution over the edges of 𝐺 in Line 1 requires 𝑂 (|𝐸|) time. The recursive construction of the zstar runs for 2𝑝 − 3 iterations, where each iteration processes up to 𝑑 max neighbors. These recursion steps take 𝑂 (𝑝 · 𝑑 max ) time in total. Since selecting the remaining 𝑞 − 𝑝 + 1 vertices does not dominate the time complexity, the overall time complexity is 𝑂 (|𝐸| + 𝑝 · 𝑑 max ). □

## Bound sentences
