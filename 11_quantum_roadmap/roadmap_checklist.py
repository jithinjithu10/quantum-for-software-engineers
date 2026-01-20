roadmap = {
    "Classical Foundations": [
        "Python proficiency",
        "Probability basics",
        "Algorithmic thinking"
    ],
    "Quantum Fundamentals": [
        "Qubit behavior",
        "Gate transformations",
        "Measurement interpretation"
    ],
    "Quantum Tools": [
        "Qiskit usage",
        "Running simulators",
        "Reading circuit outputs"
    ],
    "Hybrid Thinking": [
        "Classical control loops",
        "Parameterized circuits",
        "Iterative execution"
    ]
}

print("Quantum Computing Roadmap Checklist\n")

for stage, skills in roadmap.items():
    print(stage)
    for skill in skills:
        print("  [ ]", skill)
    print()
