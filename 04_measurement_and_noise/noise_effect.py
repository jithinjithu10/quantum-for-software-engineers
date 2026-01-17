import random
import matplotlib.pyplot as plt

shots = 1000

def ideal_measurement():
    return random.choice([0, 1])

def noisy_measurement(noise_prob=0.2):
    value = random.choice([0, 1])
    if random.random() < noise_prob:
        return 1 - value  # flip result
    return value

ideal_results = {0: 0, 1: 0}
noisy_results = {0: 0, 1: 0}

for _ in range(shots):
    ideal_results[ideal_measurement()] += 1
    noisy_results[noisy_measurement()] += 1

labels = ["0", "1"]
ideal_counts = [ideal_results[0], ideal_results[1]]
noisy_counts = [noisy_results[0], noisy_results[1]]

x = range(len(labels))

plt.bar(x, ideal_counts, width=0.4, label="Ideal", align="center")
plt.bar(x, noisy_counts, width=0.4, label="Noisy", align="edge")

plt.xticks(x, labels)
plt.ylabel("Count")
plt.title("Effect of Noise on Measurement Distribution")
plt.legend()
plt.show()
