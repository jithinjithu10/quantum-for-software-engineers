import random

max_depth = 10
current_depth = 0
error_probability = 0.0

while current_depth < max_depth:
    current_depth += 1
    error_probability += random.uniform(0.05, 0.12)

    print(
        f"Depth {current_depth}: "
        f"Estimated error probability = {round(error_probability, 2)}"
    )

    if error_probability >= 1.0:
        print("Computation becomes unreliable.")
        break
