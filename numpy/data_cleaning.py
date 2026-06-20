import numpy as np
import pandas as pd

df=pd.read_csv("WineQT.csv")
print(df.head())

#checking the missing values
print("Missing values in each column")
print(df.isnull().sum())

df["Salary(INR)"].fillna(df["Salary(INR)"].mean(),inplace=True)

df["peformance_rating"].fillna(df["performance_rating"].median(),inplace=True)

#replacing infinite values with mean

df.replace([np.inf,-np.inf],np.nan,inplace=True)
df.fillna(df.mean(),inplace=True)

df.drop_duplicates(inplace=True)

#replacing negative salary with avg salary
df["Salary(INR)"] = np.where(df["Salary(INR)"]<0,df["Salary(INR)"].mean(),df["Salary(INR)"])

salary_mean=df['Salary(INR)'].mean()
salary_std=df['Salary(INR)'].std()
lower_bound = salary_mean - (3*salary_std)
upper_bound = salary_mean + (3*salary_std)

#remove rows where slary is too high or too low
df=df[(df['Salary(INR)'] >= lower_bound) & (df["Salary(INR)"] <= upper_bound)]

df.to_csv("Cleaned_file.csv",index=False)



"""Winsorization means:
 You do NOT delete outliers
 Instead, you cap them at some percentile value.
Example (95% Winsorization):
Any value above 95th percentile → replaced with 95th percentile
Any value below 5th percentile → replaced with 5th percentile
So the extreme values become less extreme, but you keep all rows."""
# winsorize the Salary column


lower_percentile = df["Salary(INR)"].quantile(0.05)   # 5th percentile
upper_percentile = df["Salary(INR)"].quantile(0.95)   # 95th percentile

df["Salary(INR)"] = df["Salary(INR)"].clip(lower=lower_percentile,
                                           upper=upper_percentile)


from scipy.stats.mstats import winsorize

df["Salary(INR)_wins"] = winsorize(df["Salary(INR)"], limits=[0.05, 0.05])
