import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David","Adesh"],
    "Age": [24, 30, 22, 35, None],
    "City": ["Mumbai", "Delhi", "Pune", "Bangalore","Chennai"]
}

df = pd.DataFrame(data)
print(df)

df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)

print("Sorting")
print(df.sort_values("Age",ascending=False))
print(df.sort_values(["Name","Age"],ascending=[False,False]))


import pandas as pd

data = {
    "Employee": ["Amit", "Priya", "Raj", "Sneha", "Ankit", "Ritu", "Arjun", "Neha", "Vikas", "Meera", 
                 "Suresh", "Pooja", "Nikhil", "Divya", "Manoj", "Kiran", "Sunita", "Rahul", "Isha", "Deepak"],
    "City": ["Mumbai", "Delhi", "Pune", "Bangalore", "Delhi", "Mumbai", "Pune", "Bangalore", "Delhi", "Mumbai",
             "Pune", "Delhi", "Mumbai", "Bangalore", "Delhi", "Pune", "Mumbai", "Bangalore", "Delhi", "Pune"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR", "IT", "Finance", "HR", "IT",
                   "Finance", "HR", "IT", "Finance", "HR", "IT", "Finance", "IT", "Finance", "HR"],
    "Salary": [50000, 65000, 48000, 72000, 55000, 51000, 80000, 60000, 47000, 70000,
               52000, 68000, 75000, 58000, 54000, 81000, 62000, 79000, 56000, 53000],
    "Age": [29, 32, 26, 35, 28, 31, 30, 27, 25, 34,
            29, 33, 36, 28, 40, 26, 32, 31, 27, 30]
}

df = pd.DataFrame(data)
# print(df)


print(df.groupby("City")["Salary"].sum())
#we can perform various operations

print(df.groupby("Department")["Salary"].agg(["min","max","mean"]))

print("Multiple agg")
print(df.groupby(["City","Department"]).agg({
    "Salary":["min","max","sum"],
    "Age":["min","max"]
}))


print("Counting")
print(df["City"].value_counts())

print("Sorting groupby")
print(df.groupby("City")['Salary'].sum().sort_values(ascending=False))

# df["Age"].unique()         # unique values
# df["Age"].nunique()        # count unique
# df["City"].value_counts()  # frequency count

# df.sample(2)               # random rows
# df.drop_duplicates()       # remove duplicates