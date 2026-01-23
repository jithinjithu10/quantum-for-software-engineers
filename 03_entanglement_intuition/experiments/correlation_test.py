import random

shots = 1000
results = {"00": 0, "11": 0}

for _ in range(shots):
    shared = random.choice([0, 1])
    if shared == 0:
        results["00"] += 1
    else:
        results["11"] += 1

print("Entangled outcomes:")
print(results)
