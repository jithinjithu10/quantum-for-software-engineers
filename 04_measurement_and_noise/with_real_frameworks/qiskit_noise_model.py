from qiskit import QuantumCircuit, Aer, execute
from qiskit_aer.noise import NoiseModel, depolarizing_error

noise_model = NoiseModel()
noise_model.add_all_qubit_quantum_error(
    depolarizing_error(0.1, 1), ["h", "x"]
)

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

backend = Aer.get_backend("qasm_simulator")
job = execute(qc, backend, shots=1000, noise_model=noise_model)
print(job.result().get_counts())
