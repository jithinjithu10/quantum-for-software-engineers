import random

# Classical correlation
classical = [(0, 0), (1, 1)]

print("Classical correlation samples:")
for _ in range(5):
    print(random.choice(classical))

print("\nQuantum entanglement samples:")
for _ in range(5):
    shared = random.choice([0, 1])
    print(shared, shared)
