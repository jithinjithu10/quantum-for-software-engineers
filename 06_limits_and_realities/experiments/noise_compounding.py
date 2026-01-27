noise = 0.03
steps = 30

remaining_fidelity = 1.0
for _ in range(steps):
    remaining_fidelity *= (1 - noise)

print("Remaining fidelity:", round(remaining_fidelity, 3))
