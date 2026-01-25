import matplotlib.pyplot as plt

states = ["A", "B", "C", "D"]
prob = [0.25, 0.25, 0.25, 0.25]
target = 2  # index of correct answer

history = []

for _ in range(5):
    for i in range(len(prob)):
        prob[i] += 0.1 if i == target else -0.03
    total = sum(prob)
    prob = [p / total for p in prob]
    history.append(prob.copy())

for i in range(len(states)):
    plt.plot([h[i] for h in history], label=states[i])

plt.xlabel("Iteration")
plt.ylabel("Probability")
plt.title("Probability Amplification (Quantum Intuition)")
plt.legend()
plt.show()
