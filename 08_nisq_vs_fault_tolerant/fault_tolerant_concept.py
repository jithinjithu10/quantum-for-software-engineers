import matplotlib.pyplot as plt

steps = list(range(1, 21))
physical_error = [0.1 * (1 / step) for step in steps]
logical_error = [e * 0.1 for e in physical_error]

plt.plot(steps, physical_error, label="Physical Qubit Error")
plt.plot(steps, logical_error, label="Logical Qubit Error (Corrected)")
plt.xlabel("Error Correction Layers")
plt.ylabel("Error Probability")
plt.title("Fault-Tolerant Error Suppression (Conceptual)")
plt.legend()
plt.grid(True)
plt.show()
