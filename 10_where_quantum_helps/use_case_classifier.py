def quantum_applicability(problem):
    quantum_friendly = [
        "optimization",
        "simulation",
        "sampling",
        "search",
        "graph"
    ]

    for keyword in quantum_friendly:
        if keyword in problem.lower():
            return "Quantum methods may provide advantage"

    return "Classical computing is more suitable"


problems = [
    "optimization of delivery routes",
    "database query system",
    "quantum chemistry simulation",
    "web application backend",
    "graph-based pattern search"
]

for p in problems:
    print(f"{p}: {quantum_applicability(p)}")
