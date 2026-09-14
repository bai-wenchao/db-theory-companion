# sigmod26-263 — A General Framework for Per-record Differential Privacy

from=tex flag=True score=30 stmts=18 proofs=5 chars=171168
kinds: {"definition": 7, "theorem": 6, "lemma": 5}
counts: {"np_hard": 0, "lower_bound": 2, "upper_bound": 3, "big_o": 55, "omega": 3, "theta": 0, "approx_ratio": 1, "whp": 0, "regret": 0, "dp": 2, "invariant": 0, "convergence": 0, "competitive": 0, "worst_case": 2, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Theorem .** For any given privacy budget function $ E (·)$ and $β (0,1)$, as well as any DP mechanism $ M $ for query $Q$, Algorithm~ [ref] returns $ Q (D)$, such that with probability at least $1 - β$, we have | Q (D) - Q(D) | ≤ |Q(D) - Q(D')| _ I + Err _ M (D',\, _ min (D)/4,\, β/2 ) _ II , where $D'$ is obtained by removing $O ( 1 _ min (D) log log ( / ) β )$ records from $D$ and $ Err _ M (·,\, ·,\, ·)$ denotes the error introduced by the DP mechanism $ M $, which depends on the input dataset, privacy budget, and failure rate.

**Theorem .** The sum estimation algorithm described in Section~ [ref] satisfies $ E $-PrDP and it returns $ Q _ sum (D) $, such that with at least $1 - β$ probability, we have & | Q _ sum (D) - Q _ sum (D)| \\ &≤ Σ_ i=1 ^ -1 |Q_ sum (D X _i) | + Σ_ i= ^ log ( / ) | Q_ sum (D X _i) - Q_ sum (D X _i) | \\ &≤ Σ_ i=k ^ -1 2 · max_ r X _i ( v_ Bal E (r) ) ln ( log ( / ) β ) + \\ &Σ_ i= ^ log ( / ) max_ r X _i ( v_ Bal E (r) ) ln ( log ( / ) β ). where $k$ is the index of the first non-empty privacy-specified domain.

**Theorem .** For any privacy budget function $ E (·)$, $β (0,1)$, and any LDP protocol $ M $, Algorithm~ [ref] returns an estimate $ Q (D)$ such that, with probability at least $1 - β$, | Q (D) - Q(D)| ≤ |Q(D) - Q(D')| _ (I) + Err _ M (D',\, _ min (D)/4,\, β/2 ) _ (II) , where $D'$ is obtained by removing $O ( √ n _ min (D) log log ( / ) β )$ records from $D$, and $ Err _ M (·,\, ·,\, ·)$ denotes the error introduced by the LDP protocol, which depends on the dataset, privacy budget, and failure rate.

**Definition .** (Down-neighborhood Optimality) ~ [cite] . Let $ M $ be the class of all $ $-DP mechanisms. Given any query $Q$, the $ $-down neighborhood lower bound on dataset $D$ is defined as & L (D, ) := \\ & _ M' M _ D' D, \\ d(D,\, D') ≤ \ : [ | M' (D') - Q(D')| ≤ ] ≥ 2 3 \ , and a mechanism $ M $ is $( , c)$-down neighborhood optimal if, for any dataset $D$, [ | M (D) - Q(D)| ≤ c · L (D, \, ) ] ≥ 2 3 , where $c$ is a constant quantifying the level of optimality.

**Definition .** (Per-record Local Differential Privacy) . Given a record-dependent privacy budget function $ E : [U]^ d [ , \, ]$, a mechanism $ M $ is $ E $-per-record local DP, or simply $ E $-PrLDP, if for arbitrary input record $r [U]^ d $ and for all possible outputs $y$, the following holds: e^ - E (r) [ M ( ) y] ≤ [ M (r) y] ≤ e^ E (r) [ M ( ) y].

**Definition .** (Per-record Privacy (PrDP)) . Given a record-dependent privacy budget function $ E :[U]^d [ ,\, ]$, a mechanism $ M $ is $ E $-per-record differentially private, or simply $ E $-PrDP, if for any pair of neighboring datasets $D ~_r D'$ and for all possible outputs $y$, the following holds: [ M (D) = y] ≤ e^ E (r) · [ M (D') = y].

**Theorem .** For any given privacy budget function $ E (·)$ and $β (0,1)$, the combination of Algorithm~ [ref] and Algorithm ~ [ref] returns $ _ $ and $ Q _ count (D)$, such that with probability at least $1 - β$, we have $ _ ≥ 1 2 _ min (D)$, and | Q _ count (D)-Q_ count (D) | = O ( √ n _ min (D) log ( log ( / ) β ) ).

**Lemma .** (PrDP Parallel Composition) . Let $ R _1, , R _k$ be a set of disjoint subdomains. Let $\ M _1, , M _k\ $ be a series of $ E _i$-PrDP mechanisms. Then their parallel composition M (D) := ( M _1(D R _1), , M _k(D R _k) ) satisfies $ E '$-PrDP, where $ E '(r) = max\ E _i(r)\ _ i=1 ^k$ for all $r [U]^d$.

**Theorem .** For any given privacy budget function $ E (·)$ and $β (0,1)$, Algorithm~ [ref] returns $ _ $ and $ Q _ count (D)$, such that with probability at least $1 - β$, we have $ _ ≥ 1 2 _ min (D)$, and \[ | Q _ count (D)-Q_ count (D) | = O ( 1 _ min (D) log ( log ( / ) β ) ).\]

**Lemma .** (PrDP Sequential Composition) . Let $\ M _1,\, …,\, M _k\ $ be a series of $ E _i$-PrDP mechanisms. Then $ M _ [k] $, defined as M _ [k] (D) := ( M _1(D),\, M _2(D),\, …,\, M _k(D)), satisfies $ E '$-PrDP, where $ E '(r) = Σ_ i=1 ^ k E _i(r)$ for all $r [U]^d$.

**Definition .** (Record-Dependent Privacy Budget Function) . A record-dependent privacy budget function, or simply a privacy budget function, is a mapping $ E : [U]^d [ , ]$, where $ , R _ + $ are predefined lower and upper bounds on the privacy budgets, respectively.

**Definition .** ($ $-Local Differential Privacy) . For a given $ > 0$, $ M $ is $ $-local differential privacy ($ $-LDP) if for any pair $r,\, r' [U]^ d $ and for all possible outputs $y$, the following holds: [ M (r) = y] ≤ e^ · [ M (r') = y].

**Definition .** (Privacy-Specified Domain) . For a given $ E : [U]^ d R _+$ and a privacy budget range $[ _ a , \, _ b ]$, the privacy-specified domain is defined as X _ [ _ a , \, _ b ] = \ r [U]^d E (r) [ _ a , \, _ b ]\ .

**Lemma .** (Laplace Mechanism) . Given a query $Q : [U]^ n× d R $, the Laplace mechanism M (D) = Q(D) + satisfies $ $-DP, where $ $ is drawn from a Laplace distribution with scale $ GS _Q/ $, i.e., $ ~ Lap ( GS _Q/ )$.

**Definition .** (Differential Privacy). For $ > 0$, a mechanism $ M $ is $ $-DP if for any pair of neighboring datasets $D ~_r D'$ and any possible output $y$, the following holds: [ M (D) = y] ≤ e^ · [ M (D') = y].

**Theorem \cite{fang2022shifted.** For any query $Q$, dataset $D$, $ ≤ ln 2$ and $ ≥ 1$, we have L (D, ) ≥ Q^ ( -1) (D) 2 , where Q^ ( -1) (D) = max_ D' D,\, d(D, D') ≤ |Q(D') - Q(D) | is the $( -1)$-downward query difference .

**Lemma .** (Laplace Tail Bound) . Let $ ~ Lap (1)$ be a random variable drawn from the unit Laplace distribution. For any $β (0, 1)$, the tail probability of $ $ satisfies (| | ≥ ln 1 β ) ≤ β.

**Lemma .** (Post-Processing) . If a mechanism $ M $ is considered $ E $-PrDP, then for any mechanism $ M '$, $ M '( M (D))$ is still $ E $-PrDP.

## Proofs
**Proof.** The privacy and error-bound proofs can be derived similarly to those for Theorem~ [ref] , with the error bound now modified due to the new threshold.

**Proof.** We analyze the error introduced by the algorithm, which consists of two components. The first component arises from omitting the results of the first $ -1$ privacy-specified domains. According to Lemma~ [ref] and the union bound over $ log ( / ) $ domains, with probability at least $1 - β$, we have | Q _ count (D X _i) - Q_ count (D X _i)| &≤ T_i \\ &= 1 2^ i-1 · ln ( log ( / ) β ), which holds for all domains. This means Algorithm [ref] will not stop at empty domains with $Q_ count (D X _i) = 0$, to be more specific, we have _ ≥ 1 2 _ min (D). ( [ref] ) also indicates that for each domain with $i < $, the number of elements within those domains is very limited even if they are discarded Q_ count (D X _i) ≤ 2 · 1 2^ i-1 · ln ( log ( / ) β ), That is, for domains preceding $ $, they are either empty—if they are before the domain containing $ _ min (D)$—or very ``light'' if they coincide with or follow the domain containing $ _ min (D)$: Σ_ i=1 ^ -1 Q_ count (D X _i) &= O ( 1 _ min (D) log ( log ( / ) β ) ) \\ &= O ( 1 _ min (D) ). This part achieves sub-goal (a). The second component comes from the intrinsic error of the Laplace mechanism. According to ( [ref] ), the cumulative error over the retained domains is bounded by &Σ_ i= ^ log ( / ) | Q _ count (D X _i) - Q_ count (D X _i)| \\ ≤ & Σ_ i= ^ log ( / ) 1 2^ i-1 · ln ( log ( / ) β ) \\ ≤ & O ( 1 _ log ( log ( / ) β ) ) \\ ≤ & O ( 1 _ min (D) log ( log ( / ) β ) ) \\ = & O ( 1 _ min (D) ). From the second to the third line, we observe that the series follows an exponential pattern. Therefore, the summation is on the order of its first term. This bound satisfies sub-goal (b) discussed earlier. By combining ( [ref] ) and ( [ref] ), we obtain the desired error bound stated in Theorem~ [ref] .

**Proof.** Firstly, according to Theorem~ [ref] , we know that | D D_ | &≤ O ( 1 1 2 _ min (D) log 2 log ( / ) β ) \\ &= O ( 1 _ min (D) log log ( / ) β ). Thus, $D_ $ itself satisfies the requirement for $D'$. As for the error of the selected mechanism $ M $ over the remaining records $D'$, its magnitude is primarily determined by $ _ min (D)$. According to Theorem~ [ref] , we have $ _ ≥ 1 2 _ min (D)$. Therefore, part II holds. Combining these two parts, we derive the stated error bound in Theorem~ [ref] . Finally, the probability that the bound holds with at least $1 - β$ follows from the union bound over the two consecutive algorithms, each of which guarantees utility with probability at least $1 - β 2 $.

**Proof.** Algorithm~ [ref] satisfies PrLDP by Lemma~ [ref] . For utility, the analysis follows similarly to the proof of Theorem~ [ref] , where the $√ n $ factor arises from aggregating $n$ noisy responses—standard in LDP settings. More precisely, for $n$ independent and identically distributed Laplace noises, the variance of their sum increases by a factor of $n$, resulting in a larger error magnitude proportional to $√ n $.

**Proof.** For privacy, the result follows from the sequential composition of the two components in the framework. For utility, the argument mirrors that of Theorem~ [ref] , with the $√ n $ term carried over from Theorem~ [ref] . In particular, at most $ O (√ n / _ min (D))$ users return $ $, and the remaining users contribute through a $ _ 2 $-LDP mechanism.

## Bound sentences
- However, as a global lower bound on privacy budgets, $ $ is typically set to a conservatively small value.
- Optimality of DP Errors The Laplace mechanism is known to achieve worst-case optimal error ~ [cite] .
- Given any query $Q$, the $ $-down neighborhood lower bound on dataset $D$ is defined as [display] and a mechanism $ M $ is $( , c)$-down neighborhood optimal if, for any dataset $D$, [display] where $c$ is a constant quantifying the level of optimality.
- For the example of estimating a bank's total deposits, a possible privacy budget function is defined as [display] where $α$ is a constant factor and $ $ is a predefined upper bound on the privacy budget.
- Such a technique is widely used in standard DP sum estimation to reduce error dependence from a predefined domain upper bound $U$ to $ Max (D)$.
