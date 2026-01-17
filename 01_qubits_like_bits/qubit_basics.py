import random

class Qubit:
    def __init__(self):
        self.state = "superposition"

    def measure(self):
        result = random.choice([0, 1])
        self.state = result
        return result

q = Qubit()

print("Qubit state before measurement:", q.state)

outcomes = []
for _ in range(10):
    outcomes.append(q.measure())

print("Measurement results:", outcomes)
