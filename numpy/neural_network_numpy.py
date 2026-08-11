import numpy as np

np.random.seed(42)

# Training data

# [Hours studied, Attendance]
X = np.array([
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90],
    [9, 95]
], dtype=float)

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

# Normalize features
X = (X - X.mean(axis=0)) / X.std(axis=0)


# Initialize neural network

input_size = 2
hidden_size = 4
output_size = 2

W1 = np.random.randn(input_size, hidden_size) * 0.1
b1 = np.zeros((1, hidden_size))

W2 = np.random.randn(hidden_size, output_size) * 0.1
b2 = np.zeros((1, output_size))


# Activation functions
def relu(x):
    return np.maximum(0, x)


def softmax(x):
    exp_values = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_values / np.sum(exp_values, axis=1, keepdims=True)


# Forward Pass
hidden = relu(np.dot(X, W1) + b1)

output = softmax(np.dot(hidden, W2) + b2)

predictions = np.argmax(output, axis=1)


# Results

print("Predicted Classes:")
print(predictions)

print("\nActual Classes:")
print(y)


# Accuracy

accuracy = np.mean(predictions == y)

print("\nAccuracy:", round(accuracy * 100, 2), "%")


# Prediction probabilities

print("\nPrediction Probabilities:")
print(np.round(output, 3))


# Test a new student

new_student = np.array([[6.5, 82]])

new_student = (
    new_student - X.mean(axis=0)
) / X.std(axis=0)

hidden_new = relu(
    np.dot(new_student, W1) + b1
)

output_new = softmax(
    np.dot(hidden_new, W2) + b2
)

prediction = np.argmax(output_new)

print("\nNew Student Prediction:")

if prediction == 1:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("Probability:", np.round(output_new, 3))
