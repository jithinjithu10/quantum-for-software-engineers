import random

shots = 1000

def ideal():
    return random.choice([0, 1])

def noisy(noise=0.2):
    value = random.choice([0, 1])
    if random.random() < noise:
        return 1 - value
    return value

ideal_results = [ideal() for _ in range(shots)]
noisy_results = [noisy() for _ in range(shots)]

print("Ideal distribution:", ideal_results.count(0), ideal_results.count(1))
print("Noisy distribution:", noisy_results.count(0), noisy_results.count(1))
