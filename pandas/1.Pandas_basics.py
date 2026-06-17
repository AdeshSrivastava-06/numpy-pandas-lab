import pandas as pd

"""df=pd.read_csv("file_name",encoding="latin1" or "utf-8")
gcsfs library can be used for reading the file on google drive"""

data = {
    "Name":["Adesh","Daksh","Bhavesh","Arpit"],
    "Age" :[19,18,10,99],
    "City" :["Mumbai","Delhi","Dholakpur","Bihar"],
    "Marks":[99,89,100,89]
}
info = pd.DataFrame(data)
print(info)

print(info.head(1))

print(info.tail(1))

print("Information")
print(info.info())

print("Description")
print(info.describe())

print("Deleting")
# coloumn deletion
info.drop("Age", axis =1 ,inplace=True)
print(info)
# row deletion
info.drop(2 , axis=0,inplace=True)
print(info)


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["Mumbai", "Delhi", "Pune", "Bangalore"]
}
df = pd.DataFrame(data)

print(df["Name"])

print("Multiple")
print(df[["Name","City"]])

print("first row")
print(df.iloc[0])

print("1 rows")
print(df.iloc[0:1:])

print(df.iloc[1:3])

print("rows 1 -3 only name and age")
print(df.loc[1:3 ,[ "Name","Age"]])

print("Row 1 column city")
print(df.loc[2,"City"])

print("Fast access single cell")
print(df.at[2,"Age"])

print("Fast acces by position")
print(df.iat[3,2])