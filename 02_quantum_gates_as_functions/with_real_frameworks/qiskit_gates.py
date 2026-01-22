from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.x(0)
qc.measure(0, 0)

backend = Aer.get_backend("qasm_simulator")
job = execute(qc, backend, shots=1000)
print(job.result().get_counts())
