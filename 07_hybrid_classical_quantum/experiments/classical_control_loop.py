import random

parameter = 0.3

def quantum_step(p):
    return 1 if random.random() < p else 0

for i in range(10):
    result = quantum_step(parameter)

    if result == 1:
        parameter += 0.05
    else:
        parameter -= 0.02

    parameter = min(max(parameter, 0.0), 1.0)

    print(f"Iter {i+1}: result={result}, parameter={round(parameter, 3)}")
