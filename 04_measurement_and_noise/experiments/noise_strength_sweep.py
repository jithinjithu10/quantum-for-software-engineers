import random

def noisy_measurement(noise):
    v = random.choice([0, 1])
    return 1 - v if random.random() < noise else v

for noise in [0.0, 0.1, 0.2, 0.3, 0.4]:
    results = [noisy_measurement(noise) for _ in range(500)]
    print(f"Noise={noise}: 1-prob={results.count(1)/500:.2f}")
