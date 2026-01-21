import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=1, shots=1000)

@qml.qnode(dev)
def circuit():
    qml.Hadamard(0)
    return qml.sample(qml.PauliZ(0))

samples = circuit()
unique, counts = np.unique(samples, return_counts=True)

print(dict(zip(unique, counts)))
