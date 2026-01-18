import matplotlib.pyplot as plt

# Simulated periodic signal
x = list(range(32))
period = 4
signal = [1 if i % period == 0 else 0 for i in x]

plt.stem(x, signal, use_line_collection=True)
plt.xlabel("Input")
plt.ylabel("Signal")
plt.title("Periodicity Detection (Shor-Style Intuition)")
plt.show()
