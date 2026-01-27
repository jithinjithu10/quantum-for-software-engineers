import cirq
import numpy as np

q = cirq.LineQubit(0)
sim = cirq.Simulator()

for angle in np.linspace(0, 3.14, 5):
    circuit = cirq.Circuit(
        cirq.ry(angle)(q),
        cirq.measure(q)
    )
    result = sim.run(circuit, repetitions=500)
    print("angle:", round(angle, 2), "→", result.histogram(key='0'))
