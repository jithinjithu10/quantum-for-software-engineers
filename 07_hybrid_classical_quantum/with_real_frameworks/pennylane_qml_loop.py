import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1, shots=500)

@qml.qnode(dev)
def circuit(theta):
    qml.RY(theta, 0)
    return qml.sample(qml.PauliZ(0))

theta = 0.2

for _ in range(10):
    samples = circuit(theta)
    loss = np.mean(samples)
    theta -= 0.1 * loss
    print("theta:", round(theta, 3))
