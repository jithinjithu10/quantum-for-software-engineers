import random

def entangled_pair():
    return random.choice([(0, 0), (1, 1)])

# First measurement
a, b = entangled_pair()

# After measurement, values become independent
a2 = random.choice([0, 1])
b2 = random.choice([0, 1])

print("Before measurement:", a, b)
print("After measurement:", a2, b2)
