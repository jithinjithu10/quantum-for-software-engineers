import random

class EntangledPair:
    def __init__(self):
        self.state = random.choice([0, 1])

    def measure_qubit_a(self):
        return self.state

    def measure_qubit_b(self):
        return self.state


pair = EntangledPair()

a_results = []
b_results = []

for _ in range(10):
    a_results.append(pair.measure_qubit_a())
    b_results.append(pair.measure_qubit_b())

print("Qubit A measurements:", a_results)
print("Qubit B measurements:", b_results)
print("Do results always match?", a_results == b_results)
