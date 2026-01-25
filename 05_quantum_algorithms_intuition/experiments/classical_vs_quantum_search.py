import random

items = list(range(100))
target = 73

def classical_search():
    for i in items:
        if i == target:
            return True

def quantum_like_search():
    return random.random() < 0.25  # amplified success

print("Classical search:", classical_search())
print("Quantum-style search success:", quantum_like_search())
