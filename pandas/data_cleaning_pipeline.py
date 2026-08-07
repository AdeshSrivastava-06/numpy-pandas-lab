import pandas as pd
import numpy as np

# Sample messy dataset
data = {
    "Name": [" Alice ", "Bob", "Charlie", None, "Eva", "Bob"],
    "Age": [25, np.nan, 30, 28, -5, np.nan],
    "Email": [
        "alice@gmail.com",
        "bob@gmail.com",
        None,
        "david@gmail.com",
        "eva@gmail.com",
        "bob@gmail.com"
    ],
    "Salary": [50000, 60000, np.nan, 70000, 65000, 60000]
}

df = pd.DataFrame(data)

print("Original Dataset\n")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove leading/trailing spaces from string columns
df["Name"] = df["Name"].str.strip()

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Replace invalid ages (negative values) with NaN
df.loc[df["Age"] < 0, "Age"] = np.nan

# Fill missing ages with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing salaries with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing emails
df["Email"] = df["Email"].fillna("Not Available")

# Convert Age to integer
df["Age"] = df["Age"].astype(int)

# Standardize email text
df["Email"] = df["Email"].str.lower()

# Create Salary Category
df["Salary_Category"] = pd.cut(
    df["Salary"],
    bins=[0, 55000, 70000, 100000],
    labels=["Low", "Medium", "High"]
)

print("\nCleaned Dataset\n")
print(df)

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# Save cleaned data
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nCleaned data saved successfully!")
