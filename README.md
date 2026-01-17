# quantum-for-software-engineers

Learn quantum computing the way software engineers think.

> A code-first, intuition-driven collection of resources, tools, and platforms for understanding quantum computing without heavy physics or math.

## What You Will Learn (Conceptually)

- Qubits as stateful computational objects
- Quantum gates as transformations
- Circuits as execution pipelines
- Measurement as probabilistic output
- Entanglement as shared system state
- How quantum computers differ from classical computers *in practice*
- Where quantum computing is useful today (and where it is not)

---
---
## Visual Overview

### Classical vs Quantum
![Bit vs Qubit](diagrams/bit_vs_qubit.jpg)

### Quantum Gates
![Quantum Gates](diagrams/quantum_gates.png)

---

## Core Quantum Software Frameworks

### Qiskit (IBM)
- https://qiskit.org
- https://github.com/Qiskit/qiskit
- https://learning.quantum.ibm.com

Primary use:
- circuit design
- simulation
- real quantum hardware access

Key components:
- `qiskit.circuit`
- `qiskit.quantum_info`
- `qiskit_aer`
- `qiskit_ibm_runtime`

---

### PennyLane (Xanadu)
- https://pennylane.ai
- https://github.com/PennyLaneAI/pennylane

Primary use:
- hybrid quantum–classical computing
- quantum machine learning
- differentiable quantum circuits

Integrates with:
- PyTorch
- TensorFlow
- JAX

---

### Cirq (Google)
- https://quantumai.google/cirq
- https://github.com/quantumlib/Cirq

Primary use:
- NISQ-era algorithms
- hardware-aware circuit design
- research-focused workflows

---

### Braket SDK (AWS)
- https://github.com/aws/amazon-braket-sdk-python
- https://aws.amazon.com/braket/

Primary use:
- cloud-native quantum workflows
- access to multiple quantum hardware providers
- scalable experimentation

---

### Q# (Microsoft)
- https://learn.microsoft.com/azure/quantum/
- https://github.com/microsoft/qsharp

Primary use:
- algorithm design
- quantum program composition
- tight integration with classical control logic

---

## Quantum Simulation Tools

Used when real quantum hardware is unavailable or impractical.

- Qiskit Aer  
  https://qiskit.org/ecosystem/aer/

- Cirq Simulator  
  https://quantumai.google/cirq/simulators

- QuTiP  
  https://qutip.org

- ProjectQ  
  https://projectq.ch

---

## Cloud Quantum Platforms (Hands-On)

### IBM Quantum
- https://quantum.ibm.com
- Free tier available
- Real superconducting quantum processors

---

### Amazon Braket
- https://aws.amazon.com/braket/
- Access to IonQ, Rigetti, QuEra
- Pay-as-you-go model

---

### Azure Quantum
- https://azure.microsoft.com/products/quantum
- Multi-vendor quantum access
- Strong tooling and documentation

---
## Quantum Computer Types

| Type | Qubit Technology | Key Characteristics | Used By / Examples | Typical Use Cases |
|-----|------------------|---------------------|--------------------|-------------------|
| Superconducting | Josephson junctions | Fast gates, cryogenic, scalable | IBM, Google, Rigetti | General-purpose QC, research |
| Trapped Ion | Electromagnetically trapped ions | High fidelity, long coherence | IonQ, Quantinuum | Algorithms, precision tasks |
| Photonic | Single photons | Room temperature, optical | Xanadu, PsiQuantum | Quantum networking, ML |
| Neutral Atom | Atoms in optical tweezers | Highly scalable, flexible | QuEra, Pasqal | Simulation, optimization |
| Quantum Annealing | Superconducting flux qubits | Optimization-specific, not gate-based | D-Wave | Combinatorial optimization |
| Spin Qubits | Electron / nuclear spin | CMOS-compatible, compact | Intel, research labs | Future scalable systems |
| Topological (Research) | Anyons (theoretical) | Error-resistant by design | Microsoft (research) | Fault-tolerant QC |

--

## Quantum Hardware Providers

- IBM Quantum  
  https://quantum.ibm.com

- Google Quantum AI  
  https://quantumai.google

- IonQ  
  https://ionq.com

- Rigetti  
  https://www.rigetti.com

- Quantinuum  
  https://www.quantinuum.com

- Xanadu  
  https://www.xanadu.ai

- D-Wave  
  https://www.dwavesys.com

---
## Learning Resources

| Level | Resource | Type | Link | Notes |
|------|----------|------|------|------|
| Beginner | IBM Quantum Learning | Interactive | https://learning.quantum.ibm.com | Best hands-on start |
| Beginner | Qiskit Textbook | Book / Labs | https://qiskit.org/learn | Code-first explanations |
| Beginner | Microsoft Quantum Katas | Exercises | https://github.com/microsoft/QuantumKatas | Practice-oriented |
| Beginner | Quantum Country | Essays | https://quantum.country | Intuition-focused |
| Intermediate | PennyLane Demos | Tutorials | https://pennylane.ai/qml/demonstrations.html | Quantum ML |
| Intermediate | Cirq Tutorials | Docs | https://quantumai.google/cirq/tutorials | Hardware-aware |
| Intermediate | IBM Quantum Lab | Cloud Lab | https://quantum.ibm.com/lab | Real hardware |
| Intermediate | AWS Braket Notebooks | Notebooks | https://github.com/aws/amazon-braket-examples | Multi-hardware |
| Advanced | MIT OpenCourseWare (QC) | Course | https://ocw.mit.edu | Academic depth |
| Advanced | Stanford Quantum Courses | Lectures | https://quantum.stanford.edu/education | Theory + systems |
| Advanced | Xanadu Quantum Codebook | Book | https://codebook.xanadu.ai | Photonic focus |

---
## Academic References

| Title | Authors / Institution | Type | Link | Focus |
|-----|----------------------|------|------|------|
| Quantum Computation and Quantum Information | Nielsen & Chuang | Book | https://doi.org/10.1017/CBO9780511976667 | Standard reference |
| The Quantum Algorithm Zoo | NIST | Survey | https://quantumalgorithmzoo.org | Algorithm catalog |
| Lecture Notes on Quantum Computation | John Preskill (Caltech) | Notes | http://theory.caltech.edu/~preskill/ph219 | Theory |
| Quantum Computing for Computer Scientists | Yanofsky & Mannucci | Book | https://www.cambridge.org/9780521876582 | CS-focused |
| Fault-Tolerant Quantum Computation | Gottesman | Paper | https://arxiv.org/abs/quant-ph/9705052 | Error correction |
| Shor’s Algorithm | Peter Shor | Paper | https://arxiv.org/abs/quant-ph/9508027 | Factoring |
| Grover’s Algorithm | Lov Grover | Paper | https://arxiv.org/abs/quant-ph/9605043 | Search |
| Quantum Error Correction | Daniel Gottesman | Survey | https://arxiv.org/abs/0904.2557 | Reliability |
| No-Cloning Theorem | Wootters & Zurek | Paper | https://doi.org/10.1038/299802a0 | Information theory |
| Quantum Supremacy Using Superconducting Qubits | Google AI | Paper | https://www.nature.com/articles/s41586-019-1666-5 | Hardware milestone |
| Topological Quantum Computation | Alexei Kitaev | Paper | https://arxiv.org/abs/quant-ph/9707021 | Fault tolerance |

---

## Quantum Computing + Software Engineering

### Mental Model Mapping

| Software Engineering | Quantum Computing |
|----------------------|-------------------|
| Variable             | Qubit             |
| Function             | Quantum Gate      |
| Pipeline             | Quantum Circuit   |
| Randomized algorithm | Measurement       |
| Shared memory        | Entanglement      |

---

## Programming Languages Used in Quantum

- Python (dominant)
- Q#
- C++ (hardware control layers)
- Rust (emerging ecosystems)

---

## Industry & Ecosystem

Quantum computing is relevant to:
- optimization
- communication and networking
- chemistry & materials
- machine learning research
- simulation of physical systems
- information theory

Major contributors:
- IBM
- Google
- Microsoft
- Amazon
- Intel
- Startups and research labs worldwide

---

## How to Use This Repository

- Pick a framework
- Run examples
- Observe probabilistic behavior
- Compare simulators vs real hardware
- Build intuition through experimentation

---

## Philosophy

> Quantum computing is not magic.
> It is computation under different rules of information, state, and probability.

---

If this repository helps you explore quantum computing as a software engineer,
consider starring it and sharing it with others.

- Curious Developers

##  Contributing
Pull requests are welcome.

⭐ If this repository helps you, please consider starring it.
