class Qubit:
    def __init__(self):
        self.state = [1, 0]  # |0>

    def __str__(self):
        return f"State: {self.state}"


def X_gate(qubit):
    # NOT gate
    qubit.state = [qubit.state[1], qubit.state[0]]
    return qubit


def H_gate(qubit):
    # Hadamard-like behavior (conceptual)
    qubit.state = [0.5, 0.5]
    return qubit


def Z_gate(qubit):
    # Phase flip (conceptual)
    qubit.state = [qubit.state[0], -qubit.state[1]]
    return qubit
