import random

depths = [5, 10, 20, 40]
base_error = 0.02

for d in depths:
    error = 1 - (1 - base_error) ** d
    print(f"Circuit depth {d}: failure probability ≈ {error:.2f}")
