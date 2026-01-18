import matplotlib.pyplot as plt
import math

time_steps = list(range(50))
coherence = [math.exp(-0.08 * t) for t in time_steps]

plt.plot(time_steps, coherence)
plt.xlabel("Time")
plt.ylabel("State Coherence")
plt.title("Decoherence Over Time")
plt.grid(True)
plt.show()
