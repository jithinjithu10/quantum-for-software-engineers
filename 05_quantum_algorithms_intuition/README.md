## What Problem Are We Solving?

Why do quantum algorithms outperform classical ones
for specific problem types?

## Visual Intuition

```mermaid
flowchart LR
    Problem["Problem Space"]
    Uniform["Uniform Probability"]
    Transform["Quantum Transformation"]
    Amplify["Correct Answers Amplified"]
    Measure["Measurement"]

    Problem --> Uniform
    Uniform --> Transform
    Transform --> Amplify
    Amplify --> Measure

## Classical Intuition

Classical algorithms search or compute step by step.
Each attempt is independent.

## Quantum Idea

Quantum algorithms modify probability distributions
so that correct answers become more likely when measured.

## What This Module Covers

- Search problems (Grover-style intuition)
- Period finding (Shor-style intuition)
- Probability amplification
- Why quantum speedup is problem-specific

## Key Takeaway

Quantum algorithms work by amplifying the probability
of correct outcomes, not by brute-force computation.
