import time

layers = [
    "User Application",
    "Quantum SDK",
    "Compiler / Transpiler",
    "Runtime / Scheduler",
    "Hardware Abstraction Layer",
    "Control Electronics",
    "Quantum Hardware"
]

print("Submitting quantum job...\n")

for layer in layers:
    print(f"Processing at: {layer}")
    time.sleep(0.3)

print("\nQuantum job executed. Results returned to user.")
