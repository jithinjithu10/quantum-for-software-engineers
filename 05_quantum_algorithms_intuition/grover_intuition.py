import random
import matplotlib.pyplot as plt

items = ["A", "B", "C", "D"]
target = "C"
iterations = 4

# Start with uniform probability
probabilities = {item: 1 / len(items) for item in items}

history = []

for _ in range(iterations):
    for item in items:
        if item == target:
            probabilities[item] += 0.15
        else:
            probabilities[item] -= 0.05

    # Normalize probabilities
    total = sum(probabilities.values())
    for item in items:
        probabilities[item] /= total

    history.append(probabilities.copy())

# Plot probability amplification
for item in items:
    plt.plot(
        range(1, iterations + 1),
        [h[item] for h in history],
        label=item
    )

plt.xlabel("Iteration")
plt.ylabel("Probability")
plt.title("Grover-Style Probability Amplification")
plt.legend()
plt.show()
