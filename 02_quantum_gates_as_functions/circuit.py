from gates import Qubit, X_gate, H_gate, Z_gate

# Create a qubit
q = Qubit()
print("Initial:", q)

# Apply Hadamard gate
q = H_gate(q)
print("After H gate:", q)

# Apply X gate
q = X_gate(q)
print("After X gate:", q)

# Apply Z gate
q = Z_gate(q)
print("After Z gate:", q)
