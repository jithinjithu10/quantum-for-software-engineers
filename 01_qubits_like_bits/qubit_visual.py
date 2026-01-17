import random
import matplotlib.pyplot as plt

# Number of measurements
shots = 1000

results = {
    0: 0,
    1: 0
}

# Simulate measuring a qubit in superposition
for _ in range(shots):
    measurement = random.choice([0, 1])
    results[measurement] += 1

print("Measurement Results after", shots, "shots")
print("0:", results[0])
print("1:", results[1])

# Plot the results
states = list(results.keys())
counts = list(results.values())

plt.bar(states, counts)
plt.xlabel("Measured State")
plt.ylabel("Count")
plt.title("Qubit Measurement Distribution")
plt.show()

