import pandas as pd

# Employee Dataset
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales", "IT", "Finance"],
    "Salary": [70000, 50000, 85000, 60000, 55000, 65000, 90000, 75000],
    "Experience": [5, 2, 8, 4, 3, 6, 10, 7],
    "Performance": [88, 75, 95, 82, 78, 90, 98, 85]
}

df = pd.DataFrame(data)

print(df)

# Add Bonus (10% of Salary)
df["Bonus"] = df["Salary"] * 0.10

# Total Compensation
df["Total Salary"] = df["Salary"] + df["Bonus"]

# Experienced Employees
experienced = df[df["Experience"] >= 5]

print("\nEmployees with Experience >= 5 Years ")
print(experienced)

# Sort by Performance
sorted_df = df.sort_values(by="Performance", ascending=False)

print("\n Top Performers ")
print(sorted_df[["Employee", "Performance"]])

# Department Statistics
department_summary = df.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Performance": "mean",
    "Experience": "mean"
})

print("\nDepartment Summary")
print(department_summary)

# Highest Paid Employee
highest_paid = df.loc[df["Salary"].idxmax()]

print("\n Highest Paid Employee ")
print(highest_paid)
