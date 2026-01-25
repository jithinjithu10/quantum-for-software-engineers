from qiskit import Aer
from qiskit.circuit.library import GroverOperator
from qiskit.algorithms import Grover
from qiskit.utils import QuantumInstance

oracle = GroverOperator.from_boolean_expression("a & b")
backend = Aer.get_backend("qasm_simulator")

grover = Grover(quantum_instance=QuantumInstance(backend, shots=1024))
result = grover.amplify(oracle)

print(result.top_measurement)
