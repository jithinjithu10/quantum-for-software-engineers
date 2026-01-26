base_error = 0.01

for qubits in [1, 2, 5, 10]:
    system_error = 1 - (1 - base_error) ** qubits
    print(f"{qubits} qubits → error ≈ {system_error:.2f}")
