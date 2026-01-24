import random

def measure():
    return random.choice([0, 1])

print("Single run result:", measure())

shots = 1000
results = [measure() for _ in range(shots)]

print("\nAfter", shots, "shots:")
print("0:", results.count(0))
print("1:", results.count(1))
