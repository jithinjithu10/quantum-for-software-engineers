logical_qubits = 10
overhead = [50, 100, 500]

for o in overhead:
    print(
        f"{logical_qubits} logical qubits "
        f"→ {logical_qubits * o} physical qubits"
    )
