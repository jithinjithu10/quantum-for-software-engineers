import random
import matplotlib.pyplot as plt

shots = 1000

def measure(prob_0, prob_1):
    return random.choices([0, 1], weights=[prob_0, prob_1])[0]

def run_experiment(prob_0, prob_1):
    results = {0: 0, 1: 0}
    for _ in range(shots):
        outcome = measure(prob_0, prob_1)
        results[outcome] += 1
    return results

# Gate behaviors (conceptual)
gates = {
    "H Gate (Superposition)": (0.5, 0.5),
    "X Gate (Flip)": (0.0, 1.0),
    "No Gate (|0>)": (1.0, 0.0)
}

plt.figure()

for gate, probs in gates.items():
    results = run_experiment(*probs)
    plt.bar(
        [f"{gate} → 0", f"{gate} → 1"],
        [results[0], results[1]]
    )

plt.ylabel("Measurement Count")
plt.title("Effect of Quantum Gates on Measurement Distribution")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
