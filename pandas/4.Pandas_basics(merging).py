import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice","Bob","Charlie","David"],
    "Age": [24, 30, 22, 35]
})

salary = pd.DataFrame({
    "Name": ["Alice","Bob","Charlie","David"],
    "Salary": [50000,60000,45000,70000]
})

merge = pd.merge(df,salary,on="Name")
print(merge)

# concat

df1 = pd.DataFrame({"A":[1,2], "B":[3,4]})
print(df1)
df2 = pd.DataFrame({"B":[5,6], "C":[7,8]})
print(df2)
#row wise
row = pd.concat([df1,df2])
print(row)
# col wise
col = pd.concat([df1,df2],axis=1)
print(col)
