import random

shots = 20

def measure_qubit():
    # Simulated superposition measurement
    return random.choice([0, 1])

results = []

for _ in range(shots):
    results.append(measure_qubit())

print("Measurement results:")
print(results)

print("\nCounts:")
print("0:", results.count(0))
print("1:", results.count(1))
