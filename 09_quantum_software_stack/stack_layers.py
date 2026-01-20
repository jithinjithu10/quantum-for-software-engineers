stack = [
    "Quantum Hardware",
    "Control Electronics",
    "Hardware Abstraction Layer",
    "Compiler / Transpiler",
    "Runtime / Scheduler",
    "Quantum SDK",
    "User Application"
]

print("Quantum Software Stack (Bottom → Top):\n")

for layer in stack:
    print("->", layer)

print("\nEach layer abstracts complexity from the one below it.")
