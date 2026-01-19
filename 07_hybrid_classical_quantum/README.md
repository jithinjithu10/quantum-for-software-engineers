## What Problem Are We Solving?

How are quantum computers actually used in real systems today?

## Common Misconception

Quantum programs run entirely on quantum hardware.

This is false.

## Reality

Quantum computation is always embedded inside
a larger classical control system.

Classical computers:
- prepare inputs
- control execution
- collect measurement results
- perform post-processing

Quantum hardware acts as a probabilistic accelerator.

## What This Module Covers

- Classical control loops
- Hybrid execution pipelines
- Iterative quantum algorithms
- Why hybrid models dominate current usage

## Key Takeaway

Real-world quantum computing is hybrid by design.

## Visual Intuition

```mermaid
flowchart LR
    Classical["Classical Computer"]
    Quantum["Quantum Processor"]
    Measure["Measurement Results"]
    Update["Classical Update"]

    Classical -->|Prepare & Control| Quantum
    Quantum -->|Probabilistic Output| Measure
    Measure --> Update
    Update --> Classical

