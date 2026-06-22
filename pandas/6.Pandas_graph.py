import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Year":[2020,2021,2022,2023,2024,2025,2026],
    "Sales":[250,300,400,500,400,1000,700],
    "Profit":[70,90,120,160,250,150,300]
})

print(data)
#line plot
data.plot(x="Year",y="Sales",kind="line", marker="o" , title="Sales over years")
plt.show()

#bar chart
data.plot(x="Year",y="Profit",kind="bar", title="profit over years")
plt.show()

#Multiple col in one graph
data.plot(x="Year",y=["Sales","Profit"],kind="line", marker="o" , title="Sales vs profit")
plt.show()

#histogram
data["Sales"].plot(kind = 'hist',bins=5,title="Sales distribution")
plt.show()

#scatter plot
data.plot(x="Sales",y="Profit",kind="scatter",title="Sales vs profit")
plt.show()

#box plot
data[["Sales","Profit"]].plot(kind = "box", title="Sales and profit spread")
plt.show()

#horizontal bar
data.plot(x="Year", y="Profit",kind="barh", title="Profit over years")
plt.show()

#area plot
data.plot(x="Year", y="Profit",kind="area", alpha=0.4, title="Profit over years")
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [15, 25, 35],
    "C": [22, 28, 40]
})

sns.heatmap(df, annot=True)
plt.title("Pandas DataFrame Heatmap")
plt.show()
