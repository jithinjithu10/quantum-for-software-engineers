import random

success = 0
runs = 100

for _ in range(runs):
    if random.random() < 0.3:
        success += 1

print("Success rate:", success / runs)
