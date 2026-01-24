import pennylane as qml

dev_analytic = qml.device("default.qubit", wires=1)
dev_shots = qml.device("default.qubit", wires=1, shots=1000)

@qml.qnode(dev_analytic)
def analytic():
    qml.Hadamard(0)
    return qml.expval(qml.PauliZ(0))

@qml.qnode(dev_shots)
def sampled():
    qml.Hadamard(0)
    return qml.sample(qml.PauliZ(0))

print("Analytic result:", analytic())
print("Sampled result (mean):", sum(sampled()) / 1000)
