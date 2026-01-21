import random

shots = [10, 100, 1000]

def measure():
    return random.choice([0, 1])

for s in shots:
    results = [measure() for _ in range(s)]
    print(f"\nShots = {s}")
    print("0:", results.count(0))
    print("1:", results.count(1))
