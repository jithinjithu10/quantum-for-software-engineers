from qiskit import QuantumCircuit, Aer, execute
import random

theta = 0.4

for _ in range(8):
    qc = QuantumCircuit(1, 1)
    qc.ry(theta, 0)
    qc.measure(0, 0)

    backend = Aer.get_backend("qasm_simulator")
    result = execute(qc, backend, shots=1000).result()
    counts = result.get_counts()

    energy = counts.get("0", 0) / 1000
    theta -= 0.1 * (energy - 0.5)

    print("theta:", round(theta, 3))
