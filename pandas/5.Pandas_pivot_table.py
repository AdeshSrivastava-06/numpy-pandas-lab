import pandas as pd

data = {
    "City": ["Mumbai","Delhi","Delhi","Pune","Mumbai","Pune","Delhi"],
    "Department": ["HR","IT","Finance","IT","HR","Finance","IT"],
    "Age": [29, 32, 28, 26, 35, 30, 27],
    "Salary": [50000, 60000, 55000, 48000, 70000, 51000, 62000]
}
df = pd.DataFrame(data)

pivot_age = df.pivot_table(values="Age", index="City",aggfunc="mean")
print(pivot_age)

pivot_salary = df.pivot_table(values="Salary",index="City", columns="Department",aggfunc="mean")
print(pivot_salary)

stack = df.stack()
print(stack)

stacked= pivot_age.stack()
print(stacked)

unstacked = pivot_age.unstack()
print(unstacked)
