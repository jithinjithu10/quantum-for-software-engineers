physical_qubits = [50, 100, 500, 1000]
ratio = 100  # physical per logical (rough intuition)

for p in physical_qubits:
    logical = p // ratio
    print(f"{p} physical qubits → ~{logical} logical qubits")
