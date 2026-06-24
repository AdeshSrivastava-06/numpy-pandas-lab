import pandas as pd

# Orders dataset
orders = pd.DataFrame({
    'order_id': [1,2,3,4,5,6,7],
    'customer_id': [101,102,103,101,104,102,105],
    'product': ['Laptop','Phone','Laptop','Tablet','Phone','Phone','Laptop'],
    'amount': [70000, 20000, 75000, 15000, 22000, 25000, 72000],
    'order_date': pd.to_datetime(['2024-01-12','2024-01-14','2024-02-02',
                                   '2024-02-20','2024-03-05','2024-03-07','2024-03-08'])
})

# Customers dataset
customers = pd.DataFrame({
    'customer_id': [101,102,103,104,105],
    'name': ['Amit','Riya','John','Sneha','David'],
    'region': ['North','West','East','South','West']
})
#inner join
df = pd.merge(orders, customers, on='customer_id', how='inner')
print(df)

#agg(gropu by)
sales_by_region = df.groupby('region')['amount'].sum().reset_index()
print(sales_by_region)

#subquery customers who spent more than ₹70,000 in total
high_spenders = df.groupby('name')['amount'].sum().reset_index()
high_spenders = high_spenders[high_spenders['amount'] > 70000]
print(high_spenders)



