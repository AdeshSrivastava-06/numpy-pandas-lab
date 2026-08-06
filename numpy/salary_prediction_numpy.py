import numpy as np

# Years of experience and corresponding salaries
experience = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
salary = np.array([30000, 35000, 45000, 50000,
                   60000, 68000, 75000, 82000], dtype=float)

# Linear Regression using NumPy
m, b = np.polyfit(experience, salary, 1)

# Predict salary
new_employee = 5.5
predicted_salary = m * new_employee + b

print(f"Slope: {m:.2f}")
print(f"Intercept: {b:.2f}")
print(f"Predicted Salary for {new_employee} years experience: ₹{predicted_salary:.2f}")

# Calculate R² Score
predicted = m * experience + b

ss_total = np.sum((salary - salary.mean()) ** 2)
ss_residual = np.sum((salary - predicted) ** 2)

r2 = 1 - (ss_residual / ss_total)

print(f"Model Accuracy (R²): {r2:.3f}")
