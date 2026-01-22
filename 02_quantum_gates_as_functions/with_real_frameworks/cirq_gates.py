import cirq

q = cirq.LineQubit(0)
circuit = cirq.Circuit(
    cirq.H(q),
    cirq.X(q),
    cirq.measure(q)
)

sim = cirq.Simulator()
result = sim.run(circuit, repetitions=1000)
print(result.histogram(key='0'))
