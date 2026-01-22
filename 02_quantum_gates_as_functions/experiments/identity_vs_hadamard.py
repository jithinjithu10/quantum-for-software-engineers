import random

def identity():
    return random.choice([0, 1])

def hadamard():
    return random.choice([0, 1])

print("Identity output:", identity())
print("Hadamard output:", hadamard())
