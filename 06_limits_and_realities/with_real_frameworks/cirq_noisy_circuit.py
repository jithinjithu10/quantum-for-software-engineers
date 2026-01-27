import cirq

q = cirq.LineQubit(0)
noise = cirq.depolarize(0.05)

circuit = cirq.Circuit()

for _ in range(15):
    circuit.append(cirq.H(q))
    circuit.append(noise.on(q))

circuit.append(cirq.measure(q))

sim = cirq.Simulator()
result = sim.run(circuit, repetitions=1000)
print(result.histogram(key='0'))
