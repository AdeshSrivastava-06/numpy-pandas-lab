import numpy as np
import matplotlib.pyplot as plt

# function we want to minimize: f(x) = x^2 + 4x + 4  -> minimum at x = -2
def f(x):
    return x**2 + 4*x + 4

# derivative (slope) of f, tells us which direction to move
def f_prime(x):
    return 2*x + 4

def gradient_descent(start_x, lr=0.1, epochs=50):
    x = start_x
    history = [x]

    for i in range(epochs):
        grad = f_prime(x)
        x = x - lr * grad
        history.append(x)
        print(f"epoch {i+1}: x = {x:.4f}, f(x) = {f(x):.4f}, gradient = {grad:.4f}")

    return x, history

# run it
final_x, history = gradient_descent(start_x=10, lr=0.1, epochs=50)

print(f"\nstarted at x=10, ended at x={final_x:.4f}")
print(f"true minimum is at x=-2")

# plot the function and the path gradient descent took
x_vals = np.linspace(-12, 12, 200)
y_vals = f(x_vals)

history = np.array(history)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="f(x) = x² + 4x + 4")
plt.scatter(history, f(history), color="red", s=20, label="descent path")
plt.plot(history, f(history), color="red", alpha=0.4)
plt.scatter([-2], [f(-2)], color="green", s=100, marker="*", label="true minimum")
plt.title("Gradient Descent Finding the Minimum")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.savefig("gradient_descent_path.png", dpi=150)
plt.show()

# bonus: try different learning rates and compare convergence speed
learning_rates = [0.01, 0.1, 0.5, 0.95]
plt.figure(figsize=(8, 5))

for lr in learning_rates:
    _, h = gradient_descent(start_x=10, lr=lr, epochs=30)
    plt.plot(f(np.array(h)), label=f"lr={lr}")

plt.title("Effect of Learning Rate on Convergence")
plt.xlabel("epoch")
plt.ylabel("f(x)")
plt.legend()
plt.savefig("learning_rate_comparison.png", dpi=150)
plt.show()
