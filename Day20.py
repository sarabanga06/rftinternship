import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create Sample Sales Dataset
np.random.seed(42)

data = {
    "Product": np.random.choice(["Laptop", "Mobile", "Tablet", "Headphones"], 100),
    "Region": np.random.choice(["North", "South", "East", "West"], 100),
    "Sales": np.random.randint(5000, 50000, 100),
    "Profit": np.random.randint(1000, 15000, 100)
}

df = pd.DataFrame(data)

# DATA CLEANING
print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ANALYSIS
print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

print("\nSales by Product:")
print(df.groupby("Product")["Sales"].sum())

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

# VISUALIZATION

# Sales by Product
plt.figure(figsize=(8,5))
sns.barplot(x=df.groupby("Product")["Sales"].sum().index,
            y=df.groupby("Product")["Sales"].sum().values)
plt.title("Total Sales by Product")
plt.show()

# Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(x=df.groupby("Region")["Sales"].sum().index,
            y=df.groupby("Region")["Sales"].sum().values)
plt.title("Total Sales by Region")
plt.show()

# Profit Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Profit"], bins=10)
plt.title("Profit Distribution")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[["Sales","Profit"]].corr(),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()