# Methodology Checks

## Core Review Path

1. Compare the theoretical assumptions with the actual experimental setup.
2. Check whether key ablations are missing or underpowered.
3. Compare motivation, method, and experiments side by side.
4. Separate "the method helps" from "the paper proves why it helps."

## High-Value Checks

### Reverse-read the ablation table

- When the paper's own ablation shows that a proposed component contributes very little, treat that
  as evidence against strong innovation claims.
- If the gain is tiny and no standard deviation is reported, the result may not support the claim at
  all.

### Baseline completeness

- Inspect which baselines are missing in each result table.
- If the abstract or conclusion makes ranking claims from incomplete comparisons, call that out
  directly.

### Extra information fairness

- If the proposed method uses external data, LLM embeddings, stronger retrieval, or other side
  information, check whether the comparison isolates that source of advantage.

### Capacity fairness

- Compare embedding dimension, hidden dimension, and parameter count across methods.
- If capacity differs, say clearly that the current evidence does not isolate architectural benefit.

### Synthetic experiments

- For synthetic or simulated settings, scalability and realism are core issues.
- Random simulation is not the same as the structural bias of a real deployment setting.

### Efficiency claims

- Check whether efficiency metrics cover the entire pipeline rather than only a favorable subpart.
- Ask for wall-clock time when the paper only reports proxy metrics such as FLOPs from one module.

## Classical-Method Framing Checks

### Platt scaling and similar calibration claims

- Classical Platt scaling assumes a held-out calibration set and a post-hoc fit on fixed model
  outputs.
- If the paper trains the affine-plus-sigmoid parameters end to end with the rest of the model,
  that may still work in practice, but it is not the same theoretical object.
- Critique the framing gap separately from the empirical usefulness.
- Good follow-up asks for calibration evidence, such as reliability diagrams, or for a more honest
  description of the component as a learnable gating function.

### Probabilistic independence assumptions

- When a paper models correlated events as independent Bernoulli variables, check whether the data
  structure makes that approximation implausible.
- For graph, relational, or multi-hop settings, correlated edges can systematically bias confidence
  estimates.
- Ask for empirical evidence that the approximation is adequate on the target datasets.

### First-order approximation reliability

- Approximations such as `E[Phi(a)] ~= Phi(E[a])` become less trustworthy when the activation
  variance is large or the nonlinearity is curved in the operating regime.
- If the paper performs best exactly where the approximation should be weakest, ask the authors to
  explain that tension.

## Theory Versus Evidence

- Distinguish an existence result from a learning-dynamics result.
- Check whether notation, set relations, and assumptions match the paper's own definitions.
- Do not let indirect evidence from model A stand in for a claim about model B unless the necessary
  assumptions are shared and stated.

## Question Design

- Prefer questions that demand explanation of current results over questions that merely request a
  whole new experiment.
- When parameter counts differ, ask whether a parameter-matched variant exists rather than asking
  for an unrelated new baseline.
- State how the answer would change the review. If the answer is decisive for acceptance, say so.
