import random
import matplotlib.pyplot as plt

shots = 500

results = {
    "00": 0,
    "11": 0
}

for _ in range(shots):
    shared_state = random.choice([0, 1])
    if shared_state == 0:
        results["00"] += 1
    else:
        results["11"] += 1

states = list(results.keys())
counts = list(results.values())

plt.bar(states, counts)
plt.xlabel("Joint Measurement Outcome")
plt.ylabel("Count")
plt.title("Entangled Qubit Measurement Distribution")
plt.show()
