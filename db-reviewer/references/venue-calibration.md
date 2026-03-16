# Venue Calibration

## Default Rule

Do not assume ICML-specific expectations unless the user explicitly asks for them. Treat the review
as venue-aware and calibrate the emphasis based on the paper type and likely submission venue.

## SIGMOD / VLDB / ICDE

For classic database or data-management venues, emphasize:

- workload realism rather than toy evidence
- end-to-end system value, not only a local microbenchmark win
- correctness, robustness, and operational cost under realistic deployment conditions
- fairness of baseline tuning, hardware budget, and parameter budget
- whether the proposed gain survives concurrency, skew, scale, and maintenance overhead

Common pressure points:

- real-world relevance of the workload
- whether the contribution is algorithmic, systems, or mostly engineering
- whether the evaluation covers throughput, latency, storage, update cost, and operational burden
- reproducibility of the pipeline and benchmark setup

## NeurIPS / ICLR Database Or Data-Centric Track

For database-related papers in ML venues, still care about systems rigor, but also emphasize:

- whether the method framing matches what is empirically validated
- whether external data, pretrained models, or stronger embeddings are isolated fairly
- whether the theory story overreaches beyond what the experiments support
- whether the contribution matters beyond one benchmark slice

Common pressure points:

- framing gap between theory and implementation
- under-controlled comparisons against stronger pretrained or larger-capacity baselines
- broad claims from narrow datasets or synthetic setups
- unclear distinction between modeling gain and data or scale advantage

## Cross-Venue Review Heuristics

- If the paper claims systems impact, ask whether the evidence is deployment-like.
- If the paper claims theoretical grounding, check whether the assumptions survive contact with the
  actual implementation.
- If the paper claims novelty from one component, use the paper's own ablations to test that claim.
- If the paper mixes database systems and machine learning, do not let one side excuse weak
  evidence on the other.
