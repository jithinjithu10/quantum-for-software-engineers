import random

score = 0.5

for step in range(15):
    measurement = random.uniform(0, 1)
    score = 0.7 * score + 0.3 * measurement
    print(f"Step {step+1}: score={round(score, 3)}")
