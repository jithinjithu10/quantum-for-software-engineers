## What Problem Are We Solving?

How does a quantum program written by a developer
actually run on real quantum hardware?

## Big Picture

Quantum computing is delivered through a layered software stack,
similar to modern cloud and systems software.

Each layer abstracts complexity from the layer above it.

## Layers of the Quantum Software Stack

From bottom to top:

1. Quantum hardware
2. Control electronics and firmware
3. Hardware abstraction layer
4. Compilers and transpilers
5. Runtime and execution engines
6. SDKs and programming frameworks
7. User applications and workflows

## Why This Matters

Understanding the stack helps software engineers:
- debug unexpected behavior
- reason about performance and errors
- choose the right tools
- design realistic workflows

## Key Takeaway

Quantum programming is systems engineering,
not just writing circuits.
## Visual Intuition

```mermaid
flowchart TD
    App["User Application"]
    SDK["Quantum SDK"]
    Compiler["Compiler / Transpiler"]
    Runtime["Runtime & Scheduler"]
    HAL["Hardware Abstraction Layer"]
    Control["Control Electronics"]
    Hardware["Quantum Hardware"]

    App --> SDK
    SDK --> Compiler
    Compiler --> Runtime
    Runtime --> HAL
    HAL --> Control
    Control --> Hardware
