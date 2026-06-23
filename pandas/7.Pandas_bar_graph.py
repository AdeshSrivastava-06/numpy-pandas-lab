import pandas as pd
import matplotlib.pyplot as plt

def buildData():
    data = pd.DataFrame({
        "Year": list(range(2015, 2026)),
        "Sales": [250, 300, 400, 500, 450, 550, 600, 700, 800, 750, 900],
        "Profit": [70, 90, 120, 160, 150, 180, 200, 250, 270, 240, 300],
        "Expenses": [180, 210, 280, 340, 300, 370, 400, 450, 530, 510, 600],
        "Region": ["North","South","East","West","North","South","East","West","North","South","East"]
    })
    return data
# Basic stacked bar graph
data=buildData()
print(data)

data.plot(
    x="Year", y=["Sales","Profit","Expenses"],
    kind="bar", stacked=True,
    title="stacked sales,Profit and expenses"
)
plt.ylabel("Amount(in thousands)")
plt.show()

#stacked bar graph with customization
data.plot(
    x="Year",
    y=["Sales","Profit","Expenses"],
    kind="bar",
    stacked=True,
    color=["skyblue","orange","green"],
    title="Company Performance: Stacked Bar"
)
plt.ylabel("Amount(in thounsands)")
plt.xlabel("Year")
plt.legend(loc="upper left")
plt.grid(axis="y", linestyle="--",alpha =0.9)
plt.show()
