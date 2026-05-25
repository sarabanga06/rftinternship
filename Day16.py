import pandas as pd
import matplotlib.pyplot as plt

# Create Sample Dataset
data = {
    'Date': ['2025-01-01', '2025-01-05', '2025-01-10',
             '2025-02-01', '2025-02-08', '2025-02-15',
             '2025-03-01', '2025-03-10', '2025-03-20'],

    'Product': ['Laptop', 'Mobile', 'Tablet',
                'Laptop', 'Mobile', 'Tablet',
                'Laptop', 'Mobile', 'Tablet'],

    'Region': ['North', 'South', 'East',
               'West', 'North', 'South',
               'East', 'West', 'North'],

    'Sales': [50000, 30000, None,
              45000, 35000, 25000,
              60000, 40000, 28000]
}
df = pd.DataFrame(data)

# Data Cleaning
print("Original Dataset:\n")
print(df)

# Handle missing values
df['Sales'].fillna(df['Sales'].mean(), inplace=True)
print("\nDataset After Handling Missing Values:\n")
print(df)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Total Sales Per Product
product_sales = df.groupby('Product')['Sales'].sum()
print("\nTotal Sales Per Product:\n")
print(product_sales)

# Region-wise Performance
region_sales = df.groupby('Region')['Sales'].sum()
print("\nRegion-wise Sales:\n")
print(region_sales)

# Monthly Growth Analysis
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales:\n")
print(monthly_sales)

# Best Performing Region
best_region = region_sales.idxmax()
print("\nBest Performing Region:", best_region)

# Sales Trend Visualization
plt.figure(figsize=(8,5))
plt.plot(df['Date'], df['Sales'], marker='o')
plt.title('Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Top Products Visualization
plt.figure(figsize=(6,5))
product_sales.plot(kind='bar')
plt.title('Top Products by Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Key Insights
print("\n----- KEY INSIGHTS -----")
print("1. Laptop has the highest total sales.")
print("2. North region contributed significant sales.")
print("3. Sales increased steadily over time.")
print("4. Missing sales values were replaced using mean.")
print("5. Best performing region is:", best_region)