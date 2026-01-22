state = "0"

def X(state):
    return "1" if state == "0" else "0"

def H(state):
    return "0/1"  # symbolic superposition

print("Initial:", state)
state = H(state)
print("After H:", state)
state = X(state)
print("After X:", state)
