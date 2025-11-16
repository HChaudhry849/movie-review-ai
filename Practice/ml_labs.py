import numpy as np

# Inputs and initial values
w = np.array([1.0, 2.5, -3.3, 4.0, 5.5, 1.20, 3.30, 5.1, 2.4, 1.1])
x = np.array([10, 20, 30, 45, 56, 67, 88, 99, 100, 25])
b = 4
y = 12345  # example true target

# Learning rate (you pick this)
lr = 0.00001  # small step size

# Forward pass
y_pred = np.dot(w, x) + b
error = y - y_pred

# Gradient descent step
w = w + 2 * lr * error * x
b = b + 2 * lr * error

# New prediction after update
new_pred = np.dot(w, x) + b

print("Old prediction:", y_pred)
print("New prediction:", new_pred)
