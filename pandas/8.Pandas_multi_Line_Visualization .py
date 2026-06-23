import pandas as pd
import matplotlib.pyplot as plt


"""line plot isnthe most used when we wnat ot see the trends and the data is big"""
def buildData():
    data = pd.DataFrame({
        "Year": list(range(2015, 2026)),
        "Sales": [250, 300, 400, 500, 450, 550, 600, 700, 800, 750, 900],
        "Profit": [70, 90, 120, 160, 150, 180, 200, 250, 270, 240, 300],
        "Expenses": [180, 210, 280, 340, 300, 370, 400, 450, 530, 510, 600],
        "Region": ["North","South","East","West","North","South","East","West","North","South","East"]
    })
    return data

data=buildData()
print(data)

#multi-line chart
data.plot(
    x="Year",
    y=["Sales","Profit","Expenses"],
    kind="line",
    marker="o",
    title="Sales, Profit & Expenses Over Years"
)
plt.ylabel("Amount (in thousands)")
plt.show()

#styled multi-line graph
data.plot(
    x="Year",y=["Sales","Profit","Expenses"],
    kind="line", marker="D",
    linestyle="--",
    color=["blue","yellow","red"],
    title="company metrices over years"
)
plt.ylabel("Amount(in thousands)")
plt.grid(True)
plt.show()
