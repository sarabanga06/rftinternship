import pandas as pd

# Given data
data = {
    "PRODUCT": ["A", "B", "A", "C"],
    "QUANTITY": [2, 1, 3, 5],
    "PRICE": [100, 200, 100, 50]
}

# Framing the data
df = pd.DataFrame(data)
print(df)

#Adding new column
df["TOTAL"] = df["QUANTITY"] * df["PRICE"]

print("Sales Data: \n")
print(df)

#Total sales per product
sales_product = df.groupby("PRODUCT")["TOTAL"].sum()

print("Total Sales Per Product: \n")
print(sales_product)

#Total revenue
grand_total = df["TOTAL"].sum()
print("\n Grand Total :", grand_total)

#Top selling product
top_product = sales_product.idxmax()
print("\n Top selling Product : ", top_product)

#Sort by Revenue
sorteddf = df.sort_values(by = "TOTAL", ascending = False)
print("\nData Sorted by Revenue : \n")
print(sorteddf)