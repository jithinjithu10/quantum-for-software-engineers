from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(1, 1)

for _ in range(20):  # deep circuit
    qc.h(0)

qc.measure(0, 0)

backend = Aer.get_backend("qasm_simulator")
job = execute(qc, backend, shots=1000)
print(job.result().get_counts())
