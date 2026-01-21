import random

def run():
    return random.choice([0, 1])

print("Running the same experiment 5 times:\n")
for i in range(5):
    print(f"Run {i+1}: {run()}")
