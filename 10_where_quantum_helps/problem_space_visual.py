import matplotlib.pyplot as plt

labels = ["Classical Only", "Hybrid Zone", "Quantum Advantage"]
sizes = [65, 25, 10]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Where Quantum Computing Provides Value")
plt.show()
