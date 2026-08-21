import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load the CSV Dataset
# -------------------------------
df = pd.read_csv("sales_data.csv")

print("Original Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())


# -------------------------------
# 2. Data Cleaning
# -------------------------------

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing values
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
df["Customer"] = df["Customer"].fillna("Unknown")
df["Product"] = df["Product"].fillna("Unknown")
df["Category"] = df["Category"].fillna("Other")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

print("\nCleaned Dataset:")
print(df.head())


# -------------------------------
# 3. Total Sales & Average Revenue
# -------------------------------

total_sales = df["Sales"].sum()
average_revenue = df["Sales"].mean()

print("\n--- SALES SUMMARY ---")
print("Total Sales:", total_sales)
print("Average Revenue:", round(average_revenue, 2))


# -------------------------------
# 4. Top 5 Customers
# -------------------------------

top_customers = (
    df.groupby("Customer")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n--- TOP 5 CUSTOMERS ---")
print(top_customers)


# -------------------------------
# 5. Sales Trend Line Chart
# -------------------------------

sales_trend = df.groupby("Date")["Sales"].sum().reset_index()

plt.figure(figsize=(10, 5))
plt.plot(sales_trend["Date"], sales_trend["Sales"], marker="o")
plt.title("Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -------------------------------
# 6. Top Products Bar Chart
# -------------------------------

top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(8, 5))
sns.barplot(
    x=top_products.values,
    y=top_products.index
)
plt.title("Top 5 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.show()


# -------------------------------
# 7. Category Distribution Pie Chart
# -------------------------------

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales Distribution by Category")
plt.show()


# -------------------------------
# 8. Five Business Insights
# -------------------------------

print("\n--- BUSINESS INSIGHTS ---")

print(f"1. The company generated total sales of ₹{total_sales:,.2f}.")

print(
    f"2. The average revenue per transaction was "
    f"₹{average_revenue:,.2f}."
)

print(
    f"3. The top customer was {top_customers.index[0]}, "
    f"contributing ₹{top_customers.iloc[0]:,.2f} in sales."
)

print(
    f"4. The best-selling product was {top_products.index[0]}, "
    f"generating ₹{top_products.iloc[0]:,.2f} in sales."
)

largest_category = category_sales.idxmax()
largest_category_sales = category_sales.max()

print(
    f"5. The {largest_category} category generated the highest sales "
    f"of ₹{largest_category_sales:,.2f}, making it an important "
    f"area for business growth."
)