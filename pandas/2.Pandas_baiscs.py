import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["Mumbai", "Delhi", "Pune", "Bangalore"]
}
df = pd.DataFrame(data)

print(df[df["Age"] > 25])

print(df[(df["Age"] > 25) & (df["City"] == "Delhi")])

print(df.query("Age > 20 and City == 'Pune'"))

print("Add or update any column")
df["NewAge"] = df["Age"]+ 5
print(df)

print("Multi conditions")
df["Senior"] = df["Age"].apply(lambda x:"Yes" if x>30 else "No")
print(df)

print("Rename a column name")
df.rename(columns={"City" : "Location"}, inplace=True)
print(df)
