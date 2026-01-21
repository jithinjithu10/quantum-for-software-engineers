import random

def biased_measurement(prob_one=0.7):
    return 1 if random.random() < prob_one else 0

results = [biased_measurement() for _ in range(1000)]

print("0:", results.count(0))
print("1:", results.count(1))
