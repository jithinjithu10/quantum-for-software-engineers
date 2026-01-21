import cirq

qubit = cirq.LineQubit(0)
circuit = cirq.Circuit(
    cirq.H(qubit),
    cirq.measure(qubit)
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)

print(result.histogram(key='0'))
