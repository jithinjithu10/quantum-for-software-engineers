## What Problem Are We Solving?

Why do quantum programs give different outputs each time,
and why does real quantum hardware behave worse than simulators?

## Classical Intuition

Classical programs are deterministic.
The same input always produces the same output.

## Quantum Reality 

Quantum programs produce probability distributions.
Measurement samples from those distributions.

Noise changes the distribution itself.

## What This Module Demonstrates

- Measurement variability
- Repeated execution (shots)
- Ideal vs noisy behavior
- Why averaging matters

## Key Takeaway

Quantum programs must be analyzed statistically,
not by single execution results.

flowchart TD

%% ===============================
%% MEASUREMENT AS SAMPLING
%% ===============================
subgraph A["Measurement as Sampling"]
    Qubit["Qubit State\n(Superposition)"]
    Measure["Measurement"]
    Result["Random Output\n0 or 1"]

    Qubit --> Measure
    Measure --> Result
end

%% ===============================
%% REPEATED EXECUTION (SHOTS)
%% ===============================
subgraph B["Why Repetition (Shots) Is Required"]
    Program["Quantum Program"]
    Run1["Run 1\n0"]
    Run2["Run 2\n1"]
    Run3["Run 3\n0"]
    Stats["Aggregate Statistics"]

    Program --> Run1
    Program --> Run2
    Program --> Run3

    Run1 --> Stats
    Run2 --> Stats
    Run3 --> Stats
end

%% ===============================
%% IDEAL VS NOISY EXECUTION
%% ===============================
subgraph C["Ideal vs Noisy Execution"]
    Circuit["Quantum Circuit"]
    Ideal["Ideal Measurement\n(Expected Distribution)"]
    Noise["Noise\n(Hardware, Environment)"]
    Noisy["Noisy Measurement\n(Distorted Distribution)"]

    Circuit --> Ideal
    Circuit --> Noise
    Noise --> Noisy
end

%% ===============================
%% STATISTICAL CONVERGENCE
%% ===============================
subgraph D["Statistical Convergence"]
    Few["Few Shots\nUnstable Results"]
    More["More Shots\nMore Stable"]
    True["True Distribution"]

    Few --> More
    More --> True
end
