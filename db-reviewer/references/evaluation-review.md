# Evaluation Review

## Focus

Review whether the evidence is strong enough to support the database claim. Benchmark quality is a
first-class part of database work, not an afterthought.

## Checklist

1. Workload realism
   - Does the workload resemble the target use case in read/write mix, skew, and scale?
   - Are concurrency, burstiness, and maintenance tasks represented?
2. Metric selection
   - Are throughput, latency percentiles, freshness, recovery time, or cost reported where relevant?
   - Are averages hiding tail behavior or instability?
3. Baseline fairness
   - Are baselines tuned comparably and given equal hardware, caching, and indexing treatment?
   - Are default settings being compared against heavily tuned proposed methods?
4. Experimental hygiene
   - Are warm-cache and cold-cache conditions separated?
   - Are repeated runs and variance reported?
   - Are data loading, compaction, and checkpoint costs excluded without justification?
5. Ablations and diagnostics
   - Can the claimed gain be attributed to the proposed component rather than unrelated tuning?
   - Are failure cases, skew sensitivity, and scale limits reported?
6. Reproducibility
   - Are schema, queries, dataset versions, and environment settings documented?
   - Could another team reproduce the setup without hidden tribal knowledge?

## High-Risk Smells

- Claims based only on microbenchmarks or toy datasets
- Missing tail latency, error rate, or recovery behavior
- No evidence under skew, high cardinality, or concurrency
- Proposed system gets custom tuning while baselines stay untuned

## Suggested Checks

- Request the exact schema, query text, and hardware profile.
- Ask for cold-start runs, concurrency sweeps, and sensitivity to data scale.
- Tie every top-line claim to at least one direct measurement.
