from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

backend = Aer.get_backend("qasm_simulator")
job = execute(qc, backend, shots=1000)
print(job.result().get_counts())
