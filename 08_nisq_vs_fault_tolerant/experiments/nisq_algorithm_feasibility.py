algorithms = {
    "Grover (small)": True,
    "VQE": True,
    "QAOA": True,
    "Shor (useful size)": False,
    "Large quantum simulation": False
}

for algo, feasible in algorithms.items():
    print(f"{algo}: {'NISQ-feasible' if feasible else 'Needs fault tolerance'}")
