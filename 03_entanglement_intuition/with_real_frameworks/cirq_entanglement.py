import cirq

q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(
    cirq.H(q0),
    cirq.CNOT(q0, q1),
    cirq.measure(q0, q1)
)

sim = cirq.Simulator()
result = sim.run(circuit, repetitions=1000)
print(result.histogram(key='0,1'))
