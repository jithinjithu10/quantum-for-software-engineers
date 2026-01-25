import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1, shots=1000)

@qml.qnode(dev)
def circuit(theta):
    qml.RY(theta, 0)
    return qml.sample(qml.PauliZ(0))

theta = 0.5
samples = circuit(theta)
print("Mean result:", np.mean(samples))
