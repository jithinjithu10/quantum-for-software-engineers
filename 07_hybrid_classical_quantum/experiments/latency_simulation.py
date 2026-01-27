import time

steps = [
    "Prepare parameters",
    "Send job to quantum device",
    "Queue & schedule",
    "Execute circuit",
    "Receive results",
    "Post-process"
]

for step in steps:
    print(step)
    time.sleep(0.4)
