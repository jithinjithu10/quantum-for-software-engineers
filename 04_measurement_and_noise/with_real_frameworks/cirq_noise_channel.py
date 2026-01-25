import cirq

q = cirq.LineQubit(0)
noise = cirq.depolarize(0.1)

circuit = cirq.Circuit(
    cirq.H(q),
    noise.on(q),
    cirq.measure(q)
)

sim = cirq.Simulator()
result = sim.run(circuit, repetitions=1000)
print(result.histogram(key='0'))
