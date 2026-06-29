import plotly.express as px
import pandas as pd

data = {
    "Region": ["Asia", "Asia", "Asia", "Europe", "Europe", "America", "America"],
    "Product": ["Electronics", "Clothing", "Furniture",
                "Electronics", "Furniture",
                "Clothing", "Electronics"],
    "Sales": [120000, 80000, 60000, 90000, 70000, 50000, 110000],
    "Profit": [20000, 12000, 8000, 15000, 9000, 6000, 18000]
}

df=pd.DataFrame(data)

#treemap
fig_treemap = px.treemap(df,path=["Region","Product"], values="Sales",color="Profit",
color_continuous_scale="viridis",
title="Treemap - company sales by region and product")
fig_treemap.show()

#sunburst
fig_sunburst = px.sunburst(df,path=["Region","Product"], values="Sales",color="Profit",
color_continuous_scale="Blues",
title="Sunburst - company sales by region and product")
fig_sunburst.show()

