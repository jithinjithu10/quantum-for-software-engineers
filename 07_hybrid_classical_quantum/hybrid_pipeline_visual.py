import random
import matplotlib.pyplot as plt

iterations = 25
parameter = 0.2
history = []

def quantum_step(p):
    return 1 if random.random() < p else 0

for _ in range(iterations):
    result = quantum_step(parameter)
    if result == 1:
        parameter += 0.04
    else:
        parameter -= 0.01
    parameter = min(max(parameter, 0.0), 1.0)
    history.append(parameter)

plt.plot(range(1, iterations + 1), history, marker="o")
plt.xlabel("Iteration")
plt.ylabel("Classical Parameter Value")
plt.title("Hybrid Classical–Quantum Optimization Loop")
plt.grid(True)
plt.show()
