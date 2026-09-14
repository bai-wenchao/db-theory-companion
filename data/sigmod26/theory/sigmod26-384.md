# sigmod26-384 — WaveStitch: Flexible and Fast Conditional Time Series Generation With Diffusion Models

from=tex flag=True score=3 stmts=1 proofs=1 chars=297595
kinds: {"proposition": 1}
counts: {"np_hard": 0, "lower_bound": 0, "upper_bound": 2, "big_o": 5, "omega": 0, "theta": 0, "approx_ratio": 0, "whp": 0, "regret": 0, "dp": 0, "invariant": 0, "convergence": 3, "competitive": 0, "worst_case": 4, "sketch": 0, "cost_model": 0, "cardinality": 0, "learned": 0}

## Statements
**Proposition .** With sets \( X _ real \), \( X _ self ^δ \), \( X _ stitch ^δ \), and \( X _ cond ^δ\) defined as above, we have the following chain of inclusions: \[ X _ real X _ cond ^0 X _ cond ^δ X _ self ^δ. \]

## Proofs
**Proof.** By definition, the conditional loss is the sum of the self-guidance loss and the stitch loss, with all losses being non-negative (see eq.~ [ref] ). Therefore, for any \( x X _ cond ^δ \), we have: \[ L _ cond (x) ≤ δ L _ self (x) ≤ δ and L _ stitch (x) ≤ δ. \] This implies that for all $ x X _ cond ^δ $: \[ x X _ self ^δ X _ stitch ^δ X _ cond ^δ X _ self ^δ. I \] Next, since the zero conditional loss is a special case of loss less than or equal to \(δ\), we have: \[ X _ cond ^ 0 X _ cond ^ δ . II \] Finally, according to the earlier definition, any \( x X _ real \) must have zero self-guidance loss and zero stitch loss. Hence, for all $ x X _ real $, we have: \[ x X _ self ^0 X _ stitch ^0 = X _ cond ^0 X _ real X _ cond ^0. III \] Combining (I), (II), and (III), we then obtain the chain of inclusions: \[ X _ real X _ cond ^0 X _ cond ^δ X _ self ^δ. \]

## Bound sentences
- This analysis suggests an ideal speedup factor of approximately $b$ over the autoregressive approach, representing an upper bound on performance under minimal communication overhead and optimal hardware utilization.
