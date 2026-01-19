import random

iterations = 10

def quantum_step(parameter):
    # Simulated quantum outcome depending on parameter
    if random.random() < parameter:
        return 1
    return 0

parameter = 0.3

print("Initial parameter:", parameter)

for i in range(iterations):
    outcome = quantum_step(parameter)

    # Classical feedback update
    if outcome == 1:
        parameter += 0.05
    else:
        parameter -= 0.02

    parameter = min(max(parameter, 0.0), 1.0)

    print(f"Iteration {i+1}: outcome={outcome}, parameter={round(parameter, 3)}")
