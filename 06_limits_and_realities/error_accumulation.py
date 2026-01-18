import random
import matplotlib.pyplot as plt

steps = 30
error_rate = 0.03

error_probability = []
current_error = 0.0

for step in range(steps):
    if random.random() < error_rate:
        current_error += random.uniform(0.02, 0.05)

    current_error = min(current_error, 1.0)
    error_probability.append(current_error)

plt.plot(range(1, steps + 1), error_probability, marker="o")
plt.xlabel("Computation Step")
plt.ylabel("Accumulated Error Probability")
plt.title("Error Accumulation in Quantum Computation")
plt.grid(True)
plt.show()
