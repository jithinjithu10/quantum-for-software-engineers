import random

value = 0.2

for i in range(12):
    noise = random.uniform(-0.1, 0.1)
    value += 0.05 + noise
    print(f"Iter {i+1}: value={round(value, 3)}")
