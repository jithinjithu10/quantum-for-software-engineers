import random
import matplotlib.pyplot as plt

def run_experiment(shots):
    results = {0: 0, 1: 0}
    for _ in range(shots):
        outcome = random.choice([0, 1])
        results[outcome] += 1
    return results

shot_sizes = [10, 50, 100, 500, 1000]
probabilities = []

for shots in shot_sizes:
    results = run_experiment(shots)
    prob_1 = results[1] / shots
    probabilities.append(prob_1)

plt.plot(shot_sizes, probabilities, marker="o")
plt.xlabel("Number of Shots")
plt.ylabel("Probability of measuring 1")
plt.title("Measurement Distribution Convergence")
plt.grid(True)
plt.show()
